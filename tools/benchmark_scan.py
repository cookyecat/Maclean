#!/usr/bin/env python3
"""Compare scanners on a disposable small-file tree; never removes user caches."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--old-package',required=True);p.add_argument('--files',type=int,default=60000);p.add_argument('--output',required=True);a=p.parse_args()
script='''import json,sys,time
sys.path.insert(0,sys.argv[1]+'/scripts')
from maclean_core.scanner import Scanner
start=time.monotonic();s=Scanner(fixture_home=sys.argv[2]).scan()
print(json.dumps({'elapsed_seconds':time.monotonic()-start,'complete':s['complete'],'selected_files':sum(len(t['files']) for t in s['targets'] if t['selected']),'selected_bytes':sum(t['eligible_logical_bytes'] for t in s['targets'] if t['selected']),'errors':s['errors'],'entries':s['entries']}))
'''
with tempfile.TemporaryDirectory(prefix='maclean-small-files-') as temp:
    home=Path(temp).resolve();cache=home/'Library/Caches/SmallFiles';cache.mkdir(parents=True)
    for i in range(a.files):(cache/str(i)).write_bytes(b'x'*32)
    later=home/'.codex/log';later.mkdir(parents=True);(later/'codex-tui.log').write_bytes(b'later')
    results={'fixture_files':a.files+1,'fixture_bytes':a.files*32+5,'python':sys.version,'runs':{}}
    for label,package in [('rc1',a.old_package),('rc2',str(ROOT/'macos-disk-auditor'))]:
        r=subprocess.run([sys.executable,'-c',script,package,str(home)],text=True,capture_output=True,timeout=240)
        if r.returncode:raise RuntimeError(r.stderr)
        results['runs'][label]=json.loads(r.stdout)
    Path(a.output).write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
