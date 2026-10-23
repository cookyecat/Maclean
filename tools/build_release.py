#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import sys
import zipfile
ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'macos-disk-auditor'
sys.path.insert(0,str(PACKAGE/'scripts'))
from maclean_core import VERSION

def build():
    paths=sorted(p for p in PACKAGE.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts and p.suffix!='.pyc')
    manifest={'version':VERSION,'files':{str(p.relative_to(PACKAGE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (PACKAGE/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    dest=ROOT/'dist'/('maclean-'+VERSION+'.zip');dest.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for p in paths+[PACKAGE/'MANIFEST.json']:
            info=zipfile.ZipInfo('macos-disk-auditor/'+str(p.relative_to(PACKAGE)),date_time=(2026,10,19,0,0,0));info.external_attr=0o100600<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
    checksum=hashlib.sha256(dest.read_bytes()).hexdigest()
    dest.with_suffix('.zip.sha256').write_text(checksum+'  '+dest.name+'\n')
    print(json.dumps({'archive':str(dest),'sha256':checksum,'files':len(paths)+1}))
if __name__=='__main__':build()
