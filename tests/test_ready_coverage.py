import plistlib
from test_core import Fixture
from maclean_core.fs import BudgetExceeded

class ReadyCoverageTests(Fixture):
    def test_standard_container_group_ai_logs(self):
        paths=['Library/Containers/com.fixture/Data/Library/Caches/a','Library/Containers/com.fixture/Data/Library/Logs/a','Library/Group Containers/com.fixture/Library/Caches/a','Library/Group Containers/com.fixture/Library/Logs/a','.codex/log/codex-tui.log','.claude/debug/session.txt','.npm/_logs/debug.log']
        files=[self.file(p) for p in paths];s=self.scan();selected=self.selected(s)
        for f in files:self.assertIn(str(f),selected)
        self.execute(s)
        for f in files:self.assertFalse(f.exists())
    def test_registered_editor(self):
        self.file('Applications/Visual Studio Code.app/Contents/Info.plist',plistlib.dumps({'CFBundleIdentifier':'com.microsoft.VSCode'}))
        (self.home/'Library/Application Support/Code/User').mkdir(parents=True)
        files=[self.file('Library/Application Support/Code/'+name+'/a') for name in ['CachedData','CachedExtensionVSIXs','logs']]
        s=self.scan()
        for f in files:self.assertIn(str(f),self.selected(s))
    def test_browser_valid_full_profile_and_invalid_profile(self):
        files=[]
        for profile in ['Default','Profile 12','Profile 12oops']:
            for cache in ['Code Cache','GPUCache']:
                files.append(self.file('Library/Application Support/Google/Chrome/'+profile+'/'+cache+'/a'))
        s=self.scan()
        self.assertTrue(all(str(f) in self.selected(s) for f in files[:4]));self.assertTrue(all(str(f) not in self.selected(s) for f in files[4:]))
    def test_cargo_incremental_not_target(self):
        self.file('project/Cargo.toml');a=self.file('project/target/debug/incremental/a');b=self.file('project/target/debug/deployed')
        s=self.scan(project=str(self.home/'project'));self.execute(s);self.assertFalse(a.exists());self.assertTrue(b.exists())
    def test_scan_cancel_saves_partial(self):
        self.file('Library/Caches/A/a');s=self.scan(cancel=lambda:True);self.assertFalse(s['complete']);self.assertTrue(any(c['status']=='cancelled' for c in s['coverage']))
    def test_unknown_inspect_metadata_only(self):
        f=self.file('Documents/unique');s=self.scan(paths=[str(f)]);self.assertEqual(s['inspections'][0]['reason'],'no_rule');self.assertFalse(self.selected(s))

    def test_container_metadata_file_does_not_abort_discovery(self):
        self.file('Library/Containers/.DS_Store')
        f=self.file('Library/Containers/com.fixture/Data/Library/Caches/a')
        s=self.scan();self.assertIn(str(f),self.selected(s));self.assertTrue(s['complete'])
    def test_registered_app_and_browser_root(self):
        files=[]
        for base in ['Library/Application Support/Slack','Library/Application Support/Google/Chrome']:
            for leaf in ['Code Cache','GPUCache']:files.append(self.file(base+'/'+leaf+'/cache'))
        s=self.scan()
        for f in files:self.assertIn(str(f),self.selected(s))
