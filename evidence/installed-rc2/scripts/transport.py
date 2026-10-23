#!/usr/bin/env python3
"""Byte-preserving release verifier/installer shared with existing connectors."""
import argparse
import base64
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import tempfile
import zipfile


def verify_archive(data,expected_sha,expected_version):
    if len(data)>100*1024*1024 or hashlib.sha256(data).hexdigest()!=expected_sha:raise ValueError('archive integrity mismatch')
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        entries=z.infolist();seen=set();total=0
        for e in entries:
            p=PurePosixPath(e.filename)
            if p.is_absolute() or '..' in p.parts or '\\' in e.filename or not p.parts or p.parts[0]!='macos-disk-auditor' or e.filename in seen:raise ValueError('unsafe or duplicate ZIP path')
            if stat.S_ISLNK(e.external_attr>>16):raise ValueError('ZIP symlink forbidden')
            seen.add(e.filename);total+=e.file_size
            if total>200*1024*1024:raise ValueError('archive expanded size limit')
        manifest=json.loads(z.read('macos-disk-auditor/MANIFEST.json'))
        if manifest['version']!=expected_version:raise ValueError('version mismatch; no fallback')
        expected={'macos-disk-auditor/'+k for k in manifest['files']}|{'macos-disk-auditor/MANIFEST.json'}
        if {e.filename for e in entries if not e.is_dir()}!=expected:raise ValueError('manifest coverage mismatch')
        for path,want in manifest['files'].items():
            if hashlib.sha256(z.read('macos-disk-auditor/'+path)).hexdigest()!=want:raise ValueError('file integrity mismatch')
        return manifest


def install(data,expected_sha,expected_version,destination):
    manifest=verify_archive(data,expected_sha,expected_version)
    dest=Path(destination).absolute()
    if dest.exists() or dest.is_symlink():raise ValueError('destination exists; choose a new version directory')
    dest.parent.mkdir(parents=True,exist_ok=True)
    # The destination parent is selected by the user; never merge with an existing installation.
    with tempfile.TemporaryDirectory(prefix='.maclean-install-',dir=dest.parent) as tmp:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for rel in manifest['files']:
                p=Path(tmp)/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read('macos-disk-auditor/'+rel));p.chmod(0o600)
            (Path(tmp)/'MANIFEST.json').write_bytes(z.read('macos-disk-auditor/MANIFEST.json'))
        os.rename(tmp,dest)
    return {'installed':str(dest),'version':expected_version,'sha256':expected_sha}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--archive',required=True);p.add_argument('--base64',action='store_true');p.add_argument('--sha256',required=True);p.add_argument('--version',required=True);p.add_argument('--destination');a=p.parse_args()
    raw=Path(a.archive).read_bytes();data=base64.b64decode(raw,validate=True) if a.base64 else raw
    result=install(data,a.sha256,a.version,a.destination) if a.destination else verify_archive(data,a.sha256,a.version)
    print(json.dumps(result,ensure_ascii=False,indent=2))
