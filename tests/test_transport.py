import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('transport',ROOT/'macos-disk-auditor/scripts/transport.py');transport=importlib.util.module_from_spec(spec);spec.loader.exec_module(transport)

class TransportTests(unittest.TestCase):
    def archive(self,extra=None,version='1'):
        b=io.BytesIO();content=b'fixed release bytes';m={'version':version,'files':{'SKILL.md':hashlib.sha256(content).hexdigest()}}
        with zipfile.ZipFile(b,'w') as z:
            z.writestr('macos-disk-auditor/SKILL.md',content);z.writestr('macos-disk-auditor/MANIFEST.json',json.dumps(m))
            if extra:z.writestr(extra,b'escape')
        return b.getvalue()
    def test_install_exact_bytes(self):
        data=self.archive()
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'new';transport.install(data,hashlib.sha256(data).hexdigest(),'1',target)
            self.assertEqual((target/'SKILL.md').read_bytes(),b'fixed release bytes')
            with self.assertRaises(ValueError):transport.install(data,hashlib.sha256(data).hexdigest(),'1',target)
    def test_interruption_and_wrong_hash(self):
        data=self.archive()
        for bad in [data[:30],data+b'changed']:
            with self.assertRaises(ValueError):transport.verify_archive(bad,hashlib.sha256(data).hexdigest(),'1')
    def test_wrong_version(self):
        data=self.archive()
        with self.assertRaises(ValueError):transport.verify_archive(data,hashlib.sha256(data).hexdigest(),'2')
    def test_path_traversal_and_unlisted_file(self):
        for name in ['macos-disk-auditor/../../outside','/tmp/outside','macos-disk-auditor/extra']:
            data=self.archive(name)
            with self.assertRaises(ValueError):transport.verify_archive(data,hashlib.sha256(data).hexdigest(),'1')
