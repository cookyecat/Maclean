"""Whole-copy runtime protocols and restricted retirement probes."""
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import subprocess
import tempfile
from .fs import Budget, BudgetExceeded, Unsafe, identity, names, parent_fd, read_limited, same, snapshot, within, unlink_record, read_prefix
from .probes import directory, regular, run


def puppeteer(path):
    p=Path(path);match=re.fullmatch(r'(mac|mac_arm)-([A-Za-z0-9._-]+)',p.name)
    if not match or p.parent.name not in {'chrome','chrome-headless-shell','firefox'}: return None
    arch='arm64' if match[1]=='mac_arm' else 'x64'
    candidates={'chrome':[f'chrome-mac-{arch}/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'],
                'chrome-headless-shell':[f'chrome-headless-shell-mac-{arch}/chrome-headless-shell'],
                'firefox':['Firefox.app/Contents/MacOS/firefox','Firefox Nightly.app/Contents/MacOS/firefox']}[p.parent.name]
    if not any(regular(p/c) and os.access(p/c,os.X_OK) for c in candidates): return None
    meta=p.parent/'.metadata'
    result={'metadata':None,'metadata_after':None,'build_id':match[2]}
    if meta.exists() or meta.is_symlink():
        raw=read_limited(meta);obj=json.loads(raw)
        if not isinstance(obj,dict) or set(obj)-{'aliases','executablePaths'}: return None
        for k in ['aliases','executablePaths']:
            if not isinstance(obj.get(k,{}),dict) or any(not isinstance(x,str) or not isinstance(v,str) for x,v in obj.get(k,{}).items()): return None
        for key,value in obj.get('executablePaths',{}).items():
            if not re.fullmatch(r'mac(_arm)?-[A-Za-z0-9._-]+',key): return None
            q=Path(value)
            if not q.is_absolute(): q=p.parent/key/q
            if not within(q,p.parent/key) or '..' in q.parts: return None
        after={k:dict(v) for k,v in obj.items()}
        after['aliases']={k:v for k,v in after.get('aliases',{}).items() if v!=match[2]}
        if 'executablePaths' in after: after['executablePaths'].pop(p.name,None)
        result.update(metadata=snapshot(meta),metadata_sha256=hashlib.sha256(raw).hexdigest(),metadata_before=obj,metadata_after=after)
    return result


def claude(path,roots,shared_budget=None):
    p=Path(path);base=Path(roots['CLAUDE_VERSIONS']);launcher=Path(roots['HOME'])/'.local/bin/claude'
    if not re.fullmatch(r'\d+\.\d+\.\d+',p.name): return None
    try:
        if not launcher.is_symlink(): return None
        current=Path(os.path.abspath(launcher.parent/os.readlink(launcher)))
        if current.parent!=base or not regular(current): return None
        candidates=[n for n in names(base,Budget(50000,10,parent=shared_budget)) if re.fullmatch(r'\d+\.\d+\.\d+',n) and regular(base/n)]
        if len(candidates)>128:return None
        versions=[]
        budget=Budget(128,30,parent=shared_budget)
        for n in candidates:
            budget.tick();binary=base/n
            if read_prefix(binary,4) not in {b'\xcf\xfa\xed\xfe',b'\xfe\xed\xfa\xcf',b'\xca\xfe\xba\xbe',b'\xbe\xba\xfe\xca'}:continue
            verified=run(['/usr/bin/codesign','--verify','--strict',str(binary)])
            detail=run(['/usr/bin/codesign','-d','--verbose=4',str(binary)]).stderr.decode()
            if verified.returncode==0 and 'Authority=Developer ID Application: Anthropic PBC (' in detail:versions.append(n)
        if current.name not in versions or p.name not in versions:return None
        keep=set(sorted(versions,key=lambda s:tuple(map(int,s.split('.'))),reverse=True)[:2])|{current.name}
        if p.name in keep:return None
        info=run(['/usr/sbin/diskutil','info','-plist',str(base)])
        obj=plistlib.loads(info.stdout)
        if not str(obj.get('DeviceNode','')).startswith('/dev/disk') or obj.get('FilesystemType') not in {'apfs','hfs'}:return None
        return {'launcher':snapshot(launcher),'current':snapshot(current),'keep':sorted(keep)}
    except BudgetExceeded:raise
    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired): return None


def prepare(protocol,path,roots,shared_budget=None):
    p=Path(path)
    extra={}
    try:
        if protocol=='puppeteer_runtime':
            extra=puppeteer(p)
            if extra is None:return None
        elif protocol=='claude_retirement':
            extra=claude(p,roots,shared_budget)
            if extra is None:return None
        elif protocol=='download_runtime':
            if not re.fullmatch(r'(chromium|chromium_headless_shell|firefox|webkit|ffmpeg)-[0-9]+',p.name) or not regular(p/'INSTALLATION_COMPLETE'):return None
        else:return None
        records=[];budget=Budget(50000,30,parent=shared_budget)
        def visit(q):
            budget.tick();r=snapshot(q)
            if r['kind']=='special':
                if not q.is_symlink(): raise Unsafe('special_runtime_object')
                value=os.readlink(q);dest=Path(os.path.abspath(q.parent/value))
                if not within(dest,p):raise Unsafe('external_runtime_symlink')
                r['link']=value
            records.append(r)
            if r['kind']=='directory':
                for n in names(q,budget):visit(q/n)
        visit(p)
        return {'protocol':protocol,'target':snapshot(p),'inventory':records,**extra}
    except BudgetExceeded:raise
    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired):return None


def in_use(path,directory_target=True):
    try:
        argv=['/usr/sbin/lsof','-nP','-F','p']+(['+D',path] if directory_target else ['--',path])
        r=run(argv,30)
        if r.returncode==1 and not r.stdout and not r.stderr:return False
        return True # Open references, errors and unavailable visibility wait; never global process names.
    except (OSError,subprocess.TimeoutExpired):return True


def execute(runtime,roots,cancel=lambda:False):
    target=runtime['target'];path=target['path']
    if cancel():return {'status':'skipped','reason':'cancelled'}
    if not all(same(r) for r in runtime['inventory']):return {'status':'pending','reason':'runtime_inventory_changed'}
    if runtime['protocol']=='claude_retirement' and not claude(path,roots):return {'status':'pending','reason':'retirement_relationship_changed'}
    if in_use(path,target['kind']=='directory'):return {'status':'pending','reason':'target_reference_or_probe_unavailable'}
    repaired=False
    try:
        meta=runtime.get('metadata')
        if meta:
            if not same(meta) or hashlib.sha256(read_limited(meta['path'])).hexdigest()!=runtime['metadata_sha256']:
                return {'status':'pending','reason':'metadata_changed'}
            with parent_fd(meta['path'],meta['ancestors']) as (fd,name,_):
                temporary='.maclean-'+os.urandom(12).hex()
                child=os.open(temporary,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600,dir_fd=fd)
                try:
                    with os.fdopen(child,'w') as f:json.dump(runtime['metadata_after'],f);f.flush();os.fsync(f.fileno())
                    if not same(meta):raise Unsafe('metadata_changed')
                    os.replace(temporary,name,src_dir_fd=fd,dst_dir_fd=fd);repaired=True
                finally:
                    try:os.unlink(temporary,dir_fd=fd)
                    except FileNotFoundError:pass
        completed=0
        for r in reversed(runtime['inventory']):
            if cancel():return {'status':'pending','reason':'cancelled_partial','removed_files':completed,'repair':'reinstall selected runtime','metadata_updated':repaired}
            if r['kind']=='file':unlink_record(r);completed+=1
            else:
                with parent_fd(r['path'],r['ancestors']) as (fd,name,_):
                    st=os.stat(name,dir_fd=fd,follow_symlinks=False)
                    if identity(st)!=r['identity'][:3]:raise Unsafe('runtime_identity_changed')
                    if r['kind']=='directory':os.rmdir(name,dir_fd=fd)
                    elif os.readlink(name,dir_fd=fd)==r['link']:os.unlink(name,dir_fd=fd)
                    else:raise Unsafe('runtime_link_changed')
        return {'status':'completed','removed_files':completed,'metadata_updated':repaired}
    except (OSError,Unsafe) as e:
        return {'status':'failed','reason':str(e),'metadata_updated':repaired,'repair':'使用原生安装器重新下载该版本；元数据前态保存在批准计划中。'}
