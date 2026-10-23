#!/usr/bin/env python3
"""Build a reproducible source delivery using an explicit inclusion list."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '3.0.0-rc.2'

def build():
    roots = ['macos-disk-auditor', 'tests', 'tools', 'docs',
             'README.zh-CN.md', 'QUICKSTART.zh-CN.md', '第一部分MacLean SKILL 开发基准.md', '第二部分完整资料包']
    evidence = ['ACCEPTANCE.json', 'ACCEPTANCE-rc2.json', 'baseline.json', 'tests.log', 'tests-rc2.log', 'scan-benchmark-rc2.json',
                'cold-install.json', 'connector-final-verification.json',
                'rc2-cold-install.json', 'rc2-upgrade.json', 'rc2-live-summary.json',
                'native-wait-limit.json', 'skill-validation.txt',
                'report-320-light-dark.png', 'research-sources.json',
                'codex-arg0.txt', 'codex-retirement.txt', 'cursor-installer.txt',
                'puppeteer-cache.txt', 'live-readonly-summary.json']
    roots += ['evidence/' + p for p in evidence]
    roots += ['evidence/' + p for p in ['human-local-flow', 'human-connector-flow',
                                      'final-connector-fixture', 'rc2-connector-fixture']]
    paths = set()
    for name in roots:
        root = ROOT / name
        for p in ([root] if root.is_file() else root.rglob('*')):
            if p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts and p.suffix != '.pyc' and p.name not in {'.DS_Store', 'seal.key'}:
                paths.add(p)
    target = ROOT / 'dist' / ('maclean-' + VERSION + '-source.zip')
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in sorted(paths):
            info = zipfile.ZipInfo('MacLean-' + VERSION + '-source/' + str(p.relative_to(ROOT)), (2026, 10, 19, 0, 0, 0))
            info.external_attr = 0o100600 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, p.read_bytes())
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    target.with_suffix('.zip.sha256').write_text(digest + '  ' + target.name + '\n')
    print(json.dumps({'archive': str(target), 'sha256': digest, 'files': len(paths)}))

if __name__ == '__main__':
    build()
