import fcntl
import json
import os
from pathlib import Path
import subprocess
import time
from unittest.mock import patch
from test_core import Fixture
from maclean_core.native import prepare, execute
from maclean_core.runtime import prepare as runtime_prepare, execute as runtime_execute
from maclean_core.workflow import apply

TAG=b'Signature: 8a477f597d28d172789f06886806bc55'

class ProtocolTests(Fixture):
    def test_uv_actual_clean(self):
        self.file('.cache/uv/CACHEDIR.TAG',TAG);f=self.file('.cache/uv/wheels-v5/fixture')
        s=self.scan();ts=[t for t in s['targets'] if t['rule']=='uv-native-cache'];self.assertTrue(ts[0]['selected'],ts)
        r=self.execute(s);self.assertFalse(f.exists());self.assertEqual(r['results'][0]['status'],'completed')
    def test_uv_external_lock(self):
        self.file('.cache/uv/CACHEDIR.TAG',TAG);f=self.file('.cache/uv/wheels-v5/fixture');lock=self.file('.cache/uv/.lock',b'')
        s=self.scan();native=next(t['native'] for t in s['targets'] if t['rule']=='uv-native-cache')
        with lock.open('rb') as h:
            fcntl.flock(h,fcntl.LOCK_SH|fcntl.LOCK_NB)
            r=execute(native,timeout=.25)
        self.assertEqual(r['status'],'pending',r);self.assertTrue(f.exists())
    def test_uv_unknown_child_blocks_domain(self):
        self.file('.cache/uv/CACHEDIR.TAG',TAG);a=self.file('.cache/uv/unique-user-document')
        s=self.scan();self.assertNotIn(str(a),self.selected(s))
    def test_native_cancel(self):
        self.file('.cache/uv/CACHEDIR.TAG',TAG);self.file('.cache/uv/wheels-v5/f');s=self.scan()
        i,p,a=self.planning(s);r=apply(self.store,i,a,cancel=lambda:True)[1]
        self.assertEqual(r['results'][0]['status'],'skipped')
    def test_npm_actual_clean(self):
        # Only an isolated content-addressed cache; no installs or network.
        f=self.file('.npm/_cacache/content-v2/sha512/aa/bb/data')
        s=self.scan();self.assertTrue(any(t['selected'] and t['rule']=='npm-content-cache' for t in s['targets']))
        r=self.execute(s);self.assertFalse(f.exists());self.assertTrue(any(x['status']=='completed' for x in r['results']),r)
    def test_npx_actual_remove(self):
        f=self.file('.npm/_npx/abcdef/node_modules/fixture/package.json',b'{"name":"fixture","version":"1.0.0"}')
        s=self.scan();i,p,a=self.planning(s);r=apply(self.store,i,a)[1]
        self.assertFalse(f.exists(),r)
    def test_playwright_copy_and_external_link(self):
        self.file('Library/Caches/ms-playwright/chromium-123/INSTALLATION_COMPLETE',b'')
        f=self.file('Library/Caches/ms-playwright/chromium-123/chrome')
        s=self.scan();self.assertIn(str(f),self.selected(s));self.execute(s);self.assertFalse(f.parent.exists())
        self.file('Library/Caches/ms-playwright/chromium-124/INSTALLATION_COMPLETE',b'')
        f=self.file('Library/Caches/ms-playwright/chromium-124/chrome');(f.parent/'bad').symlink_to(self.home)
        self.assertNotIn(str(f),self.selected(self.scan()))
    def test_runtime_open_reference(self):
        self.file('Library/Caches/ms-playwright/chromium-123/INSTALLATION_COMPLETE',b'');f=self.file('Library/Caches/ms-playwright/chromium-123/chrome')
        s=self.scan()
        with f.open('rb'):
            r=self.execute(s)
        self.assertTrue(f.exists());self.assertEqual(r['results'][0]['status'],'pending')
    def puppeteer(self):
        base='.cache/puppeteer/chrome/mac_arm-123'
        exe=self.file(base+'/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');exe.chmod(0o700)
        meta=self.file('.cache/puppeteer/chrome/.metadata',json.dumps({'aliases':{'stable':'123','old':'122'},'executablePaths':{'mac_arm-123':str(exe)}}).encode())
        return exe,meta
    def test_puppeteer_metadata_transaction(self):
        f,m=self.puppeteer();s=self.scan();self.assertIn(str(f),self.selected(s));r=self.execute(s)
        self.assertFalse(f.exists(),r);data=json.loads(m.read_text());self.assertEqual(data['aliases'],{'old':'122'});self.assertEqual(data['executablePaths'],{})
    def test_puppeteer_metadata_concurrent(self):
        f,m=self.puppeteer();i,p,a=self.planning();m.write_text('{}');r=apply(self.store,i,a)[1]
        self.assertTrue(f.exists());self.assertEqual(r['results'][0]['status'],'pending')
    def test_partial_failure_does_not_stop_batch(self):
        a=self.file('Library/Caches/A/a');b=self.file('Library/Caches/B/b');i,p,ap=self.planning()
        from maclean_core.workflow import unlink_record
        def fail_one(record):
            if record['path']==str(a): raise PermissionError('fixture failure')
            return unlink_record(record)
        with patch('maclean_core.workflow.unlink_record',side_effect=fail_one):r=apply(self.store,i,ap)[1]
        self.assertTrue(a.exists());self.assertFalse(b.exists());self.assertEqual({x['status'] for x in r['results']},{'failed','completed'})

class ClaudeContractTests(Fixture):
    """Lifecycle filesystem tests with explicitly simulated vendor/volume probes."""
    def test_current_latest_two_and_invalid_signature(self):
        import plistlib
        from maclean_core.runtime import claude
        versions=['1.0.0','1.9.0','1.10.0','2.0.0','99.0.0']
        for v in versions:self.file('.local/share/claude/versions/'+v,b'\xcf\xfa\xed\xfe'+b'fixture simulated binary')
        launcher=self.home/'.local/bin/claude';launcher.parent.mkdir(parents=True);launcher.symlink_to(self.home/'.local/share/claude/versions/1.0.0')
        roots={'HOME':str(self.home),'CLAUDE_VERSIONS':str(self.home/'.local/share/claude/versions')}
        def fake_run(argv,*args):
            if 'codesign' in argv[0]:
                return subprocess.CompletedProcess(argv,1 if argv[-1].endswith('99.0.0') else 0,b'',b'Authority=Developer ID Application: Anthropic PBC (TEST_ONLY)')
            return subprocess.CompletedProcess(argv,0,plistlib.dumps({'DeviceNode':'/dev/disk3s1','FilesystemType':'apfs'}),b'')
        with patch('maclean_core.runtime.run',side_effect=fake_run):
            for v in ['1.0.0','1.10.0','2.0.0','99.0.0']:self.assertIsNone(claude(self.home/'.local/share/claude/versions'/v,roots))
            self.assertIsNotNone(claude(self.home/'.local/share/claude/versions/1.9.0',roots))
    def test_custom_launcher_is_not_retired(self):
        from maclean_core.runtime import claude
        f=self.file('.local/share/claude/versions/1.0.0');self.file('.local/bin/claude',b'#!/bin/sh')
        self.assertIsNone(claude(f,{'HOME':str(self.home),'CLAUDE_VERSIONS':str(f.parent)}))

class NativeSymlinkTests(Fixture):
    def test_native_internal_symlink_uses_native_protocol(self):
        self.file('.cache/uv/CACHEDIR.TAG',TAG);f=self.file('.cache/uv/wheels-v5/data');(f.parent/'link').symlink_to('data')
        s=self.scan();self.assertTrue(any(t['selected'] and t.get('native') for t in s['targets']));self.execute(s);self.assertFalse(f.exists())
    def test_native_external_symlink_blocks_domain(self):
        self.file('.cache/uv/CACHEDIR.TAG',TAG);f=self.file('.cache/uv/wheels-v5/data');outside=self.file('unique');(f.parent/'link').symlink_to(outside)
        s=self.scan();self.assertFalse(any(t['selected'] for t in s['targets']));self.assertTrue(outside.exists())
