"""Sealed local records, human approval, deterministic execution receipts."""
import fcntl
import hashlib
import hmac
import json
import os
from pathlib import Path
import platform
import pwd
import secrets
import shutil
import subprocess
import sys
import time
from . import VERSION
from .fs import Unsafe, digest, read_limited, same, snapshot, unlink_record, unique_bytes, residual_bytes
from .rules import CATALOG
from .probes import probe
from .native import execute as execute_native
from .runtime import execute as execute_runtime, in_use

_APPROVAL_SECRET=secrets.token_bytes(32)

def _seal_approval(fields):
    return fields|{'proof':hmac.new(_APPROVAL_SECRET,digest(fields).encode(),hashlib.sha256).hexdigest()}

class Store:
    def __init__(self, path=None):
        self.path=Path(path or Path(pwd.getpwuid(os.getuid()).pw_dir)/'Library/Logs/MacLean')
        self.path.mkdir(parents=True,exist_ok=True,mode=0o700)
        if snapshot(self.path)['kind']!='directory' or self.path.is_symlink() or self.path.stat().st_uid!=os.getuid(): raise Unsafe('unsafe state directory')
        os.chmod(self.path,0o700)
        key=self.path/'seal.key'
        try:
            fd=os.open(key,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
            with os.fdopen(fd,'wb') as f: f.write(secrets.token_bytes(32)); f.flush(); os.fsync(f.fileno())
        except FileExistsError: pass
        self.key=read_limited(key,32)
    def put(self,value):
        payload={**value,'software_version':VERSION}
        ident=digest(payload)
        blob={'payload':payload,'mac':hmac.new(self.key,ident.encode(),hashlib.sha256).hexdigest()}
        p=self.path/(ident+'.json')
        try:
            fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
            with os.fdopen(fd,'w') as f: json.dump(blob,f,ensure_ascii=True); f.flush(); os.fsync(f.fileno())
        except FileExistsError: pass
        return ident
    def get(self,ident):
        if len(ident)!=64 or any(c not in '0123456789abcdef' for c in ident): raise Unsafe('invalid record id')
        blob=json.loads(read_limited(self.path/(ident+'.json'),512*1024*1024))
        if digest(blob['payload'])!=ident or not hmac.compare_digest(blob['mac'],hmac.new(self.key,ident.encode(),hashlib.sha256).hexdigest()): raise Unsafe('record integrity failed')
        return blob['payload']

def plan(scan,ids):
    if scan['catalog_digest']!=digest(CATALOG): raise Unsafe('catalog changed; rescan')
    known={t['id']:t for t in scan['targets']}
    if set(ids)-known.keys(): raise Unsafe('unknown target selection')
    actions=[]; pending=[]; seen=set()
    for ident in dict.fromkeys(ids):
        t=known[ident]
        if not t['selected']: pending.append({'id':ident,'reason':'not_eligible'}); continue
        files=[]
        for old in t['files']:
            try:
                new=snapshot(old['path'])
                if new['identity'][:3]!=old['identity'][:3] or new['ancestors']!=old['ancestors']:
                    pending.append({'path':old['path'],'reason':'identity_changed'}); continue
                if old['path'] not in seen: files.append(new); seen.add(old['path'])
            except (OSError,Unsafe): pending.append({'path':old['path'],'reason':'unavailable'})
        if files and sum(f['logical_bytes'] for f in files):
            actions.append({k:t[k] for k in ['id','path','rule','rule_version','protocol','purpose','impact','recovery']}|{'files':files, 'native':t.get('native'), 'runtime':t.get('runtime'), 'project_roots':t.get('project_roots',scan['roots'])})
    now=time.time()
    return {'kind':'plan','schema_version':1,'created':now,'expires':now+1800,'catalog_digest':digest(CATALOG),
            'roots':scan['roots'],'fixture':scan.get('fixture',False),'actions':actions,'pending':pending,
            'logical_bytes':unique_bytes([f for a in actions for f in a['files']]),'allocated_bytes':unique_bytes([f for a in actions for f in a['files']],'allocated_bytes')}

def approve_native(plan_id,plan):
    if platform.system()!='Darwin' or os.getuid()==0: raise Unsafe('macOS user session required')
    # Arguments are data to a fixed AppleScript; never source interpolation.
    text=f"MacLean {VERSION}\n计划 SHA-256: {plan_id}\n{len(plan['actions'])} 项，{plan['logical_bytes']} 字节。\n删除封存的缓存文件；日志历史不可恢复。\n"+'\n'.join(a['purpose']+' | '+repr(a['path'])+' | '+a['protocol']+'\n'+a['impact']+('\n原生完整影响域：'+repr(a['native']['domain']['path'])+'；'+a['native']['effect'] if a.get('native') else '') for a in plan['actions'])
    script='on run argv\n display dialog (item 1 of argv) with title "MacLean 批量删除批准" buttons {"取消", "批准删除"} default button "取消" cancel button "取消" with icon caution\n return "confirmed"\nend run'
    try:
        r=subprocess.run(['/usr/bin/osascript','-e',script,text],capture_output=True,timeout=1800)
    except (OSError,subprocess.TimeoutExpired): r=None
    if r is None or (r.returncode and b'User canceled' not in r.stderr):
        if not sys.stdin.isatty():return None
        with open('/dev/tty','r+') as tty:
            tty.write(text+'\n真人确认：输入完整计划 SHA-256，其他输入取消：\n');tty.flush()
            if tty.readline().strip()!=plan_id:return None
        return _seal_approval({'digest':plan_id,'confirmed_at':time.time(),'expires':min(plan['expires'],time.time()+1800),'channel':'human_terminal'})
    if r.returncode or r.stdout.strip()!=b'confirmed': return None
    return _seal_approval({'digest':plan_id,'confirmed_at':time.time(),'expires':min(plan['expires'],time.time()+1800),'channel':'macOS_native_dialog'})

def validate_approval(plan_id,p,approval):
    if digest(p)!=plan_id: raise Unsafe('plan digest mismatch')
    if not isinstance(approval,dict): raise Unsafe('missing approval')
    fields={k:v for k,v in approval.items() if k!='proof'}
    expected=hmac.new(_APPROVAL_SECRET,digest(fields).encode(),hashlib.sha256).hexdigest()
    if not hmac.compare_digest(approval.get('proof',''),expected): raise Unsafe('unverifiable human approval')
    if not approval or approval.get('digest')!=plan_id or approval.get('channel') not in {'macOS_native_dialog','human_terminal','fixture_test'}: raise Unsafe('no bound approval')
    if approval.get('channel')=='fixture_test' and not p.get('fixture'): raise Unsafe('fixture approval for real home forbidden')
    now=time.time()
    if not approval.get('confirmed_at',0)<=now<min(p['expires'],approval.get('expires',0)): raise Unsafe('approval expired')
    if p['catalog_digest']!=digest(CATALOG): raise Unsafe('rules changed')

def apply(store,plan_id,approval,cancel=lambda:False):
    p=store.get(plan_id)
    validate_approval(plan_id,p,approval)
    if p['kind']!='plan': raise Unsafe('not a plan')
    lockfd=os.open(store.path/(plan_id+'.lock'),os.O_CREAT|os.O_RDWR|os.O_NOFOLLOW,0o600)
    try:
        fcntl.flock(lockfd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        journal=store.path/(plan_id+'.journal')
        done={}; uncertain=set()
        if journal.exists():
            for line in read_limited(journal,512*1024*1024).splitlines():
                event=json.loads(line)
                if event['status']=='started': uncertain.add(event['path'])
                else: done[event['path']]=event; uncertain.discard(event['path'])
        def record(e):
            fd=os.open(journal,os.O_APPEND|os.O_WRONLY|os.O_CREAT|os.O_NOFOLLOW,0o600)
            with os.fdopen(fd,'w') as f: f.write(json.dumps(e,ensure_ascii=True)+'\n'); f.flush(); os.fsync(f.fileno())
        results=[]; volumes={}
        for a in p['actions']:
            project_busy=False
            if a['protocol']=='project_cache':
                try:
                    kind=snapshot(a['path'])['kind']
                    project_busy=kind=='special' or in_use(a['path'],kind=='directory')
                except (OSError,Unsafe):project_busy=True
            if a.get('native') or a.get('runtime'):
                path=a['path']
                if path in done: results.append(done[path]); continue
                e={'target_id':a['id'],'path':path,'logical_bytes':0,'allocated_bytes':0}
                if path in uncertain: e.update(status='pending',reason='interrupted_native_requires_rescan')
                elif cancel(): e.update(status='skipped',reason='cancelled')
                elif project_busy: e.update(status='pending',reason='project_target_in_use')
                elif time.time()>=approval['expires']: e.update(status='skipped',reason='approval_expired')
                else:
                    domain=(a.get('native') or {}).get('domain',(a.get('runtime') or {}).get('target',{}))
                    dev=str(domain['identity'][0]);volume_path=str(Path(domain['path']).parent)
                    if dev not in volumes:volumes[dev]={'path':volume_path,'free_before':shutil.disk_usage(volume_path).free}
                    record(e|{'status':'started'})
                    try:e.update(execute_native(a['native'],cancel) if a.get('native') else execute_runtime(a['runtime'],a['project_roots'],cancel))
                    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as ex:e.update(status='failed',reason=str(ex),requires_rescan=True)
                    e['target_logical_bytes']=sum(f['logical_bytes'] for f in a['files'])
                    e['inventory_missing_logical_bytes']=sum(f['logical_bytes'] for f in a['files'] if not Path(f['path']).exists())
                record(e); results.append(e); continue
            for f in a['files']:
                path=f['path']
                if path in done:
                    results.append(done[path]); continue
                e={'target_id':a['id'],'path':path,'logical_bytes':0,'allocated_bytes':0}
                if path in uncertain:
                    e.update(status='pending',reason='interrupted_action_requires_rescan')
                elif cancel(): e.update(status='skipped',reason='cancelled')
                elif project_busy: e.update(status='pending',reason='project_target_in_use')
                elif time.time()>=approval['expires']: e.update(status='skipped',reason='approval_expired')
                elif not same(f): e.update(status='skipped',reason='identity_changed')
                else:
                    rule=next(r for r in CATALOG['rules'] if r['id']==a['rule'])
                    missing=[x for x in rule['identity_checks'] if not probe(x,path,a['path'],a['project_roots'])]
                    if missing: e.update(status='pending',reason='probe_changed:'+','.join(missing))
                    else:
                        try:
                            dev=str(f['identity'][0])
                            if dev not in volumes: volumes[dev]={'path':str(Path(path).parent),'free_before':shutil.disk_usage(Path(path).parent).free}
                            record(e|{'status':'started'})
                            unlink_record(f)
                            e.update(status='completed',logical_bytes=f['logical_bytes'],allocated_bytes=f['allocated_bytes'])
                        except Unsafe as ex: e.update(status='skipped',reason=str(ex))
                        except OSError as ex: e.update(status='failed',reason=str(ex))
                record(e); results.append(e)
        for v in volumes.values():
            v['free_after']=shutil.disk_usage(v['path']).free
            v['free_delta']=v['free_after']-v['free_before']
        receipt={'kind':'receipt','schema_version':1,'plan':plan_id,'created':time.time(),'approval':approval,
                 'results':results,'target_processed_logical_bytes':sum(x.get('logical_bytes',0) for x in results if x['status']=='completed'),'residual_inventory_logical_bytes':residual_bytes([f for a in p['actions'] for f in a['files']]),'volumes':volumes,'space_note':'卷空闲变化含并发写入、开放句柄和快照影响，不等于删除量。'}
        return store.put(receipt),receipt
    finally: os.close(lockfd)
