#!/usr/bin/env python3
"""MacLean CLI. All hosts call this same entry point."""
import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import sys
from maclean_core import VERSION
from maclean_core.fs import Unsafe, digest
from maclean_core.rules import CATALOG, PACKAGE
from maclean_core.scanner import Scanner, scan_projects
from maclean_core.workflow import Store, plan, approve_native, apply
from maclean_core.report import render


def main():
    p=argparse.ArgumentParser(description='MacLean deterministic cache maintenance')
    p.add_argument('--state-dir');sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('capabilities')
    r=sub.add_parser('rules');r.add_argument('operation',choices=['list'])
    for name in ['scan','inspect']:
        s=sub.add_parser(name);s.add_argument('--project');s.add_argument('--root-map',action='append',default=[])
        s.add_argument('--path',action='append',default=[]);s.add_argument('--keep',action='append',default=[])
        s.add_argument('--category',choices=['app','ai','development']);s.add_argument('--entries',type=int,default=250000,help='maximum metadata visits per target (default: 250000)')
        s.add_argument('--target-seconds',type=float,default=120,help='seconds per target (default: 120)')
        s.add_argument('--seconds',type=float,default=600,help='total scan time limit (default: 600)')
    s=sub.add_parser('plan');s.add_argument('--scan',required=True);s.add_argument('--selection',required=True)
    s=sub.add_parser('apply');s.add_argument('--plan',required=True)
    s=sub.add_parser('report');s.add_argument('--record',required=True);s.add_argument('--output',required=True);s.add_argument('--share',action='store_true')
    a=p.parse_args()
    manifest=PACKAGE/'MANIFEST.json'
    package_digest=digest(json.loads(manifest.read_text())) if manifest.exists() else 'development-unsealed'
    if manifest.exists():
        import hashlib
        for rel,want in json.loads(manifest.read_text())['files'].items():
            file=PACKAGE/rel
            if file.is_symlink() or hashlib.sha256(file.read_bytes()).hexdigest()!=want: raise Unsafe('package integrity failed: '+rel)
    base={'schema_version':1,'software_version':VERSION,'catalog_version':CATALOG['catalog_version'],'package_digest':package_digest}
    if a.command=='capabilities':
        return base|{'platform':platform.platform(),'python':platform.python_version(),'mac_access':platform.system()=='Darwin' and os.getuid()!=0,'python_supported':sys.version_info>=(3,10),
            'approval_channels':['macOS_native_dialog'] if platform.system()=='Darwin' and os.path.exists('/usr/bin/osascript') else [],
            'host_event_approval':'not_configured','tools':{t:shutil.which(t) for t in ['uv','npm','git','lsof']},'root_binding':'pwd.getpwuid(os.getuid())'}
    if a.command=='rules': return base|{'rules':CATALOG['rules']}
    if sys.version_info<(3,10):raise Unsafe('Python >=3.10 required; configured interpreter is '+platform.python_version())
    if platform.system()!='Darwin' or os.getuid()==0: raise Unsafe('requires non-root macOS execution; cloud scan forbidden')
    store=Store(a.state_dir)
    if a.command in ['scan','inspect']:
        if not 1<=a.entries<=1000000: raise Unsafe('entries out of bounds: 1..1000000')
        if not 0<a.target_seconds<=3600 or not 0<a.seconds<=7200:raise Unsafe('time limits out of bounds')
        cancelled=[False];signal.signal(signal.SIGINT,lambda *_:cancelled.__setitem__(0,True));signal.signal(signal.SIGTERM,lambda *_:cancelled.__setitem__(0,True))
        data=scan_projects(cancel=lambda:cancelled[0],project=a.project,overrides=dict(x.split('=',1) for x in a.root_map),paths=a.path,keep=a.keep+[str(store.path)],category=a.category,entries=a.entries,target_seconds=a.target_seconds,seconds=a.seconds)
        ident=store.put(data)
        return base|{'scan_id':ident,'record':str(store.path/(ident+'.json')),'targets':len(data['targets']),'selected':sum(t['selected'] for t in data['targets']),'complete':data['complete'],'discovery_complete':data['discovery_complete'],'measurement_complete':data['measurement_complete'],'limits':data['limits'],'entries':data['entries'],'incomplete_targets':[{'path':e['path'],'reason':e.get('limit_reason') or e['status']} for e in data['errors']]}
    if a.command=='plan':
        ids=json.loads(Path(a.selection).read_text());
        if not isinstance(ids,list) or any(not isinstance(x,str) for x in ids): raise Unsafe('selection must be target ID array')
        data=plan(store.get(a.scan),ids);ident=store.put(data)
        return base|{'plan_id':ident,'actions':len(data['actions']),'logical_bytes':data['logical_bytes'],'record':str(store.path/(ident+'.json'))}
    if a.command=='report': return base|render(store.get(a.record),a.output,a.share)
    if a.command=='apply':
        data=store.get(a.plan)
        approval=approve_native(a.plan,data)
        if not approval: return base|{'status':'preview','reason':'human_approval_unavailable_or_cancelled'}
        cancelled=[False];signal.signal(signal.SIGINT,lambda *_:cancelled.__setitem__(0,True));signal.signal(signal.SIGTERM,lambda *_:cancelled.__setitem__(0,True))
        ident,receipt=apply(store,a.plan,approval,lambda:cancelled[0])
        return base|{'receipt_id':ident,'statuses':{s:sum(x['status']==s for x in receipt['results']) for s in ['completed','pending','failed','skipped']}}

if __name__=='__main__':
    try: print(json.dumps(main(),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError) as e:
        print(json.dumps({'schema_version':1,'error':str(e)},ensure_ascii=False));sys.exit(2)
