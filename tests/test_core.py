import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'macos-disk-auditor/scripts'))
from maclean_core.fs import Unsafe, snapshot, digest, read_limited
from maclean_core.rules import RuleBook, CATALOG
from maclean_core.scanner import Scanner
from maclean_core.workflow import Store, plan, apply, validate_approval, _seal_approval
from maclean_core.report import render
from maclean_core.probes import probe, bind
from maclean_core.native import prepare, execute

class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='maclean-test-')
        self.root=Path(self.tmp.name).resolve();self.home=self.root/'home';self.home.mkdir()
        self.store=Store(self.root/'state')
    def tearDown(self): self.tmp.cleanup()
    def file(self,path,content=b'x'*4096):
        p=self.home/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content);return p
    def scan(self,**kw): return Scanner(fixture_home=str(self.home),**kw).scan()
    def planning(self,s=None):
        s=s or self.scan();p=plan(s,[t['id'] for t in s['targets'] if t['selected']]);i=self.store.put(p);p=self.store.get(i)
        return i,p,_seal_approval({'digest':i,'confirmed_at':time.time(),'expires':time.time()+100,'channel':'fixture_test'})
    def execute(self,s=None,**kw):
        i,p,a=self.planning(s);return apply(self.store,i,a,**kw)[1]
    def selected(self,s): return {f['path'] for t in s['targets'] if t['selected'] for f in t['files']}

class CoreTests(Fixture):
    def test_online_cache_and_open_log(self):
        a=self.file('Library/Caches/App/now');b=self.file('Library/Logs/App/current.log')
        with b.open('rb') as opened:
            r=self.execute();self.assertFalse(a.exists());self.assertFalse(b.exists());self.assertTrue(opened.read())
        self.assertTrue(all(x['status']=='completed' for x in r['results']))
        self.assertIn('free_delta',next(iter(r['volumes'].values())))
    def test_protected_parent_no_bypass(self):
        safe=self.file('Library/Caches/App/cache');protected=self.file('Library/Caches/CloudKit/test')
        self.execute();self.assertFalse(safe.exists());self.assertTrue(protected.exists())
    def test_special_objects_do_not_block(self):
        a=self.file('Library/Caches/App/file');os.mkfifo(a.parent/'fifo');(a.parent/'link').symlink_to(self.home)
        self.execute();self.assertFalse(a.exists());self.assertTrue((a.parent/'fifo').exists());self.assertTrue((a.parent/'link').is_symlink())
    def test_file_and_ancestor_replacement(self):
        a=self.file('Library/Caches/A/a');b=self.file('Library/Caches/B/b');i,p,ap=self.planning()
        a.unlink();a.write_bytes(b'new');parent=b.parent;parent.rename(parent.with_name('old'));parent.symlink_to(parent.with_name('old'))
        r=apply(self.store,i,ap)[1];self.assertTrue(a.exists());self.assertTrue(b.exists());self.assertTrue(all(x['status']=='skipped' for x in r['results']))
    def test_no_new_files_or_modified_files(self):
        a=self.file('Library/Caches/A/a');i,p,ap=self.planning();b=self.file('Library/Caches/A/new');a.write_bytes(b'changed')
        apply(self.store,i,ap);self.assertTrue(a.exists());self.assertTrue(b.exists())
    def test_changed_before_plan_remeasures(self):
        a=self.file('Library/Caches/A/a');s=self.scan();a.write_bytes(b'new size');i,p,ap=self.planning(s)
        self.assertEqual(p['logical_bytes'],8);apply(self.store,i,ap);self.assertFalse(a.exists())
    def test_zero_hidden_and_no_plan(self):
        self.file('Library/Caches/A/empty',b'');s=self.scan();self.assertFalse(any(t['selected'] for t in s['targets']));self.assertFalse(self.planning(s)[1]['actions'])
    def test_budget_partial(self):
        for n in range(20): self.file('Library/Caches/A/'+str(n))
        s=self.scan(entries=5);self.assertFalse(s['complete']);self.assertTrue(any(c['status']=='budget_exceeded' for c in s['coverage']))
    def test_failed_specialized_no_fallback(self):
        a=self.file('Library/Caches/ms-playwright/chromium-123/a');s=self.scan();self.assertNotIn(str(a),self.selected(s));self.execute(s);self.assertTrue(a.exists())
    def test_cache_layout_evidence(self):
        a=self.file('Library/Application Support/Cursor/Cache/a');s=self.scan();self.assertNotIn(str(a),self.selected(s))
        (a.parent.parent/'GPUCache').mkdir();(a.parent.parent/'Code Cache').mkdir();s=self.scan();self.assertIn(str(a),self.selected(s))
    def test_hardlink_dedup(self):
        a=self.file('Library/Caches/A/a');os.link(a,a.with_name('b'));s=self.scan()
        self.assertEqual(sum(t['logical_bytes'] for t in s['targets']),4096)
        i,p,ap=self.planning(s);self.assertEqual(p['logical_bytes'],4096)
        r=apply(self.store,i,ap)[1];self.assertEqual(r['residual_inventory_logical_bytes'],4096)
    def test_boundary_keep_and_scope(self):
        a=self.file('Library/Caches/A/a');b=self.file('Library/Caches-Old/B/b');s=self.scan(keep=[str(a)])
        self.assertNotIn(str(a),self.selected(s));self.assertNotIn(str(b),self.selected(s))
    def test_cancellation_and_retry(self):
        a=self.file('Library/Caches/A/a');i,p,ap=self.planning();r=apply(self.store,i,ap,cancel=lambda:True)[1]
        self.assertEqual(r['results'][0]['status'],'skipped');self.assertTrue(a.exists())
        # A cancelled plan does not silently restart on retry; a new plan is required.
        apply(self.store,i,ap);self.assertTrue(a.exists())
    def test_completed_retry(self):
        a=self.file('Library/Caches/A/a');i,p,ap=self.planning();apply(self.store,i,ap)
        a.write_bytes(b'new');r=apply(self.store,i,ap)[1];self.assertTrue(a.exists());self.assertEqual(r['results'][0]['status'],'completed')
    def test_seal_and_expiry(self):
        self.file('Library/Caches/A/a');i,p,ap=self.planning()
        with self.assertRaises(Unsafe): validate_approval(i,p,ap|{'expires':0})
        with self.assertRaises(Unsafe): validate_approval(i,p,{'approved':True})
        f=self.store.path/(i+'.json');b=json.loads(f.read_text());b['payload']['logical_bytes']=1;f.write_text(json.dumps(b))
        with self.assertRaises(Unsafe): self.store.get(i)
    def test_report_injection(self):
        self.file('Library/Caches/<script>alert(1)</script>/a');s=self.scan();out=self.root/'report';render(s,out)
        h=(out/'report.html').read_text();self.assertNotIn('<script>alert(1)</script>',h);self.assertIn('&lt;script&gt;',h)
    def test_project_dirty_independent(self):
        project=self.home/'project';project.mkdir();self.file('project/pyproject.toml',b'[project]');self.file('project/module.py',b'private source')
        a=self.file('project/__pycache__/module.cpython-314.pyc');orphan=self.file('project/__pycache__/missing.cpython-314.pyc')
        subprocess.run(['git','init','-q',str(project)],check=True)
        s=self.scan(project=str(project));self.assertIn(str(a),self.selected(s));self.assertNotIn(str(orphan),self.selected(s))
        self.execute(s);self.assertTrue(orphan.exists());self.assertFalse(a.exists())
    def test_tracked_cache_retained(self):
        project=self.home/'project';a=self.file('project/__pycache__/module.cpython-314.pyc');self.file('project/module.py');self.file('project/pyproject.toml')
        subprocess.run(['git','init','-q',str(project)],check=True);subprocess.run(['git','-C',str(project),'add','-f',str(a)],check=True)
        self.assertNotIn(str(a),self.selected(self.scan(project=str(project))))
    def test_next_paid_cache(self):
        project=self.home/'project';self.file('project/package.json',b'{"dependencies":{"next":"1"}}')
        a=self.file('project/.next/cache/webpack/a');b=self.file('project/.next/cache/fetch-cache/api')
        self.execute(self.scan(project=str(project)));self.assertFalse(a.exists());self.assertTrue(b.exists())
    def test_pytest_unknown_keys(self):
        project=self.home/'project';self.file('project/pyproject.toml');self.file('project/.pytest_cache/CACHEDIR.TAG',b'Signature: 8a477f597d28d172789f06886806bc55')
        a=self.file('project/.pytest_cache/v/cache/nodeids');b=self.file('project/.pytest_cache/v/paid/model')
        self.execute(self.scan(project=str(project)));self.assertFalse(a.exists());self.assertTrue(b.exists())
    def test_manifest_symlink_size(self):
        a=self.file('manifest',b'x'*100)
        with self.assertRaises(Unsafe): read_limited(a,10)
        l=self.home/'link';l.symlink_to(a)
        with self.assertRaises(OSError): read_limited(l)
    def test_roots_fixed(self):
        with self.assertRaises(Unsafe): bind(overrides={'HOME':'/x'})
        with self.assertRaises(Unsafe): RuleBook({'HOME':str(self.home)}).owner(str(self.home)+'/../evil','file')

class CatalogContracts(unittest.TestCase):
    def test_all_125_production_ownership(self):
        cases=json.loads((ROOT/'tests/catalog_cases.json').read_text())
        spec=importlib.util.spec_from_file_location('reference',ROOT/'tests/reference_catalog.py');ref=importlib.util.module_from_spec(spec);spec.loader.exec_module(ref)
        count=0
        for c in cases['cases']:
            roots=cases['roots']|c.get('root_overrides',{})
            if not ref.canonical_syntax(c['path']):
                with self.assertRaises(ValueError): RuleBook(roots).owner(c['path'],c.get('kind','directory'))
                count+=1;continue
            expected=ref.owners(CATALOG,roots,c['path'],c.get('kind','directory'))
            actual=RuleBook(roots).owners(c['path'],c.get('kind','directory'))
            self.assertEqual({(r['id'],a) for _,r,a in actual},{(r['id'],a) for _,r,a in expected},c['id']);count+=1
        self.assertEqual(count,125)

if __name__=='__main__': unittest.main()
