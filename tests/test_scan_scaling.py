import os
from unittest.mock import patch
from test_core import Fixture
from maclean_core.fs import Budget, BudgetExceeded, Unsafe, inventory, snapshot
from maclean_core.probes import probe
from maclean_core.scanner import Scanner


class ScanScalingTests(Fixture):
    def test_metadata_count_and_identity_match(self):
        for n in range(120):self.file('Library/Caches/App/'+str(n),b'x')
        target=self.home/'Library/Caches/App';budget=Budget(121,10)
        records=list(inventory(target,budget))
        self.assertEqual(budget.used,121)
        for r in records:self.assertEqual(r,snapshot(r['path']))

    def test_ai_filter_before_recursive_measurement(self):
        for n in range(100):self.file('Library/Caches/Other/'+str(n))
        wanted=self.file('Library/Caches/Codex/a')
        visited=[]
        def tracked(path,*args):
            visited.append(str(path));yield from inventory(path,*args)
        with patch('maclean_core.scanner.inventory',tracked):s=self.scan(category='ai',entries=10)
        self.assertNotIn(str(self.home/'Library/Caches/Other'),visited)
        self.assertIn(str(wanted),self.selected(s));self.assertTrue(s['complete'])

    def test_big_target_does_not_starve_later_rule(self):
        for n in range(30):self.file('Library/Caches/A/'+str(n))
        wanted=self.file('.codex/log/codex-tui.log')
        s=self.scan(entries=10)
        self.assertFalse(s['complete']);self.assertTrue(s['discovery_complete'])
        self.assertIn(str(wanted),self.selected(s))
        self.assertEqual(s['errors'][0]['limit_reason'],'entry_limit')

    def test_target_probe_once_for_many_files(self):
        for n in range(2000):self.file('Library/Application Support/Cursor/Cache/'+str(n),b'x')
        for name in ['GPUCache','Code Cache']:(self.home/'Library/Application Support/Cursor'/name).mkdir()
        with patch('maclean_core.scanner.probe',wraps=probe) as observed:s=self.scan(category='ai')
        cache=str(self.home/'Library/Application Support/Cursor/Cache')
        checks=[c for c in observed.call_args_list if c.args[0]=='chromium_layout' and c.args[2]==cache]
        self.assertEqual(len(checks),1)
        self.assertEqual(len(self.selected(s)),2000)

    def test_entry_limit_and_time_limit_are_distinct(self):
        with self.assertRaisesRegex(BudgetExceeded,'entry_limit'):Budget(0,10).tick()
        with self.assertRaisesRegex(BudgetExceeded,'time_limit'):Budget(10,-1).tick()

    def test_inventory_symlink_never_descended(self):
        outside=self.file('Documents/unique')
        cache=self.file('Library/Caches/App/a').parent
        (cache/'link').symlink_to(outside.parent)
        rows=list(inventory(cache,Budget(10,10)))
        self.assertEqual(len(rows),3)
        self.assertEqual(next(r for r in rows if r['path'].endswith('/link'))['kind'],'special')

    def test_directory_replaced_before_open(self):
        a=self.file('Library/Caches/App/a');target=a.parent
        rows=inventory(target,Budget(10,10))
        next(rows)
        target.rename(target.with_name('previous'))
        target.symlink_to(self.home/'Documents')
        with self.assertRaises(OSError):list(rows)

    def test_total_time_expiry_still_discovers_targets(self):
        self.file('Library/Caches/A/a');self.file('.codex/log/codex-tui.log')
        scanner=Scanner(fixture_home=str(self.home))
        scanner.total_budget.deadline=0
        s=scanner.scan()
        self.assertTrue(s['discovery_complete']);self.assertFalse(s['measurement_complete'])
        self.assertTrue(any(e['path'].endswith('/.codex/log/codex-tui.log') for e in s['errors']))
        self.assertTrue(all(e['limit_reason']=='time_limit' for e in s['errors']))

    def test_directory_replaced_by_another_directory(self):
        target=self.file('Library/Caches/App/a').parent
        rows=inventory(target,Budget(10,10));next(rows)
        target.rename(target.with_name('previous'));target.mkdir()
        (target/'unique').write_bytes(b'new')
        with self.assertRaisesRegex(Unsafe,'directory_identity_changed'):list(rows)
        self.assertEqual((target/'unique').read_bytes(),b'new')

    def test_protected_directory_not_enumerated(self):
        for n in range(30):self.file('Library/Caches/CloudKit/'+str(n))
        wanted=self.file('Library/Caches/App/a')
        s=self.scan(entries=3)
        self.assertTrue(s['complete']);self.assertIn(str(wanted),self.selected(s))
        self.assertFalse(any('/CloudKit/' in f for f in self.selected(s)))
