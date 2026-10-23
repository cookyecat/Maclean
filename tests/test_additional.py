import json
import os
from pathlib import Path
from unittest.mock import patch
from test_core import Fixture
from maclean_core.scanner import scan_projects
from maclean_core.workflow import apply, validate_approval, _seal_approval
from maclean_core.fs import Unsafe, read_limited

class AdditionalTests(Fixture):
    def test_nested_project_discovery(self):
        self.file('mono/pkg/pyproject.toml');self.file('mono/pkg/mod.py');f=self.file('mono/pkg/__pycache__/mod.cpython-314.pyc')
        s=scan_projects(project=str(self.home/'mono'),fixture_home=str(self.home));self.assertIn(str(f),self.selected(s));self.execute(s);self.assertFalse(f.exists())
    def test_permission_incomplete(self):
        f=self.file('Library/Caches/A/a');f.parent.chmod(0)
        try:
            s=self.scan();self.assertFalse(s['complete']);self.assertFalse(any(t['selected'] for t in s['targets']))
        finally:f.parent.chmod(0o700)
    def test_protected_runtime_current_and_staging(self):
        a=self.file('.cache/codex-runtimes/codex-primary-runtime/bin/node');b=self.file('.cache/codex-runtimes/codex-runtime-install-x/payload/node');c=self.file('Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-agent-worker/agent-cli/.local/share/cursor-agent/versions/123/bin')
        s=self.scan();self.assertFalse(self.selected(s));self.execute(s);self.assertTrue(all(x.exists() for x in [a,b,c]))
    def test_ruff_unknown_subtree(self):
        self.file('project/pyproject.toml');self.file('project/.ruff_cache/CACHEDIR.TAG',b'Signature: 8a477f597d28d172789f06886806bc55\ntext')
        a=self.file('project/.ruff_cache/0.15.0/hash');b=self.file('project/.ruff_cache/paid-model/result');s=self.scan(project=str(self.home/'project'))
        self.assertIn(str(a),self.selected(s));self.assertNotIn(str(b),self.selected(s));self.execute(s);self.assertTrue(b.exists())
    def test_forged_channel_is_not_approval(self):
        self.file('Library/Caches/A/a');i,p,a=self.planning()
        with self.assertRaises(Unsafe):validate_approval(i,p,{k:v for k,v in a.items() if k!='proof'}|{'channel':'macOS_native_dialog'})
    def test_expired_authentic_approval(self):
        self.file('Library/Caches/A/a');i,p,a=self.planning();fields={k:v for k,v in a.items() if k!='proof'};fields['expires']=0
        with self.assertRaises(Unsafe):validate_approval(i,p,_seal_approval(fields))
    def test_plan_cannot_select_research(self):
        f=self.file('.codex/models_cache.json');s=self.scan();from maclean_core.workflow import plan
        p=plan(s,[t['id'] for t in s['targets']]);self.assertEqual(p['actions'],[])
    def test_interrupted_journal_is_not_replayed(self):
        f=self.file('Library/Caches/A/a');i,p,a=self.planning();(self.store.path/(i+'.journal')).write_text(json.dumps({'status':'started','path':str(f)})+'\n')
        r=apply(self.store,i,a)[1];self.assertEqual(r['results'][0]['status'],'pending');self.assertTrue(f.exists())
    def test_project_open_file_pending_only_target(self):
        self.file('project/pyproject.toml');self.file('project/a.py');f=self.file('project/__pycache__/a.cpython-314.pyc');other=self.file('Library/Caches/A/a')
        with f.open('rb'):
            s=self.scan(project=str(self.home/'project'));r=self.execute(s)
        self.assertTrue(f.exists());self.assertFalse(other.exists());self.assertIn('pending',{x['status'] for x in r['results']})
    def test_native_user_keep_blocks_whole_domain(self):
        self.file('.cache/uv/CACHEDIR.TAG',b'Signature: 8a477f597d28d172789f06886806bc55');f=self.file('.cache/uv/wheels-v5/file')
        s=self.scan(keep=[str(f)]);self.assertFalse(any(t['selected'] for t in s['targets']))
