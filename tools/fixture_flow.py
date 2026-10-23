#!/usr/bin/env python3
"""Destructive acceptance only in a newly allocated disposable fixture."""
import argparse
import os
import json
from pathlib import Path
import sys
import tempfile
import time
ROOT=Path(__file__).resolve().parents[1]
PACKAGE=Path(os.environ.get('MACLEAN_FIXTURE_PACKAGE',str(ROOT/'macos-disk-auditor')))
sys.path.insert(0,str(PACKAGE/'scripts'))
from maclean_core.scanner import Scanner
from maclean_core.workflow import Store,plan,apply,approve_native,_seal_approval
from maclean_core.report import render

p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--human',action='store_true');a=p.parse_args()
out=Path(a.output).absolute();out.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='maclean-acceptance-') as temp:
    root=Path(temp).resolve();home=root/'home';cache=home/'Library/Caches/Fixture';cache.mkdir(parents=True)
    (cache/'generated-cache.bin').write_bytes(b'fixture'*4096)
    store=Store(root/'state');scan=Scanner(fixture_home=str(home)).scan();scan_id=store.put(scan)
    render(scan,out/'scan')
    selected=[t['id'] for t in scan['targets'] if t['selected']]
    p=plan(scan,selected);pid=store.put(p);p=store.get(pid)
    (out/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2));render(p,out/'plan')
    print(json.dumps({'fixture':str(root),'plan_id':pid,'logical_bytes':p['logical_bytes'],'approval':'human_native' if a.human else 'simulated_fixture_only'}),flush=True)
    ap=approve_native(pid,p) if a.human else _seal_approval({'digest':pid,'confirmed_at':time.time(),'expires':time.time()+60,'channel':'fixture_test'})
    if ap:
        rid,receipt=apply(store,pid,ap);render(receipt,out/'receipt');(out/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
        result={'package':str(PACKAGE),'status':'passed','approval':'human_native' if a.human else 'simulated_fixture_only','scan_id':scan_id,'receipt_id':rid,'deleted':not (cache/'generated-cache.bin').exists()}
    else:result={'status':'not_verified','reason':'no_human_confirmation'}
    (out/'result.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
