"""Segment-aware production ownership. No synthetic fact inputs accepted."""
import fnmatch
from functools import lru_cache
import json
from pathlib import Path, PurePosixPath
from .fs import canonical

PACKAGE = Path(__file__).resolve().parents[2]
CATALOG = json.loads((PACKAGE/'rules/catalog.json').read_text())

def segment_match(relative, pattern, depth=6):
    a = () if str(relative)=='.' else relative.parts
    b = () if pattern=='.' else tuple(pattern.split('/'))
    if b and b[0]=='**':
        n = len(a)-len(b)+1
        return 0 <= n <= depth and all(fnmatch.fnmatchcase(x,y) for x,y in zip(a[n:],b[1:]))
    return len(a)==len(b) and all(fnmatch.fnmatchcase(x,y) for x,y in zip(a,b))

class RuleBook:
    def __init__(self, roots, catalog=None):
        self.catalog = catalog or CATALOG
        self.roots = {k:str(canonical(v)) for k,v in roots.items() if v}
    @lru_cache(maxsize=8192)
    def _directory_matches(self, path):
        p = Path(path)
        inherited = self._directory_matches(str(p.parent)) if p.parent != p else ()
        return inherited + tuple(self._direct(p, 'directory'))
    def _direct(self, p, kind):
        for r in self.catalog['rules']:
            for s in r['selectors']:
                root = self.roots.get(s['root'])
                if not root or s['kind'] not in ('any', kind): continue
                value = str(p)
                if value != root and not value.startswith(root.rstrip('/') + '/'): continue
                rel = PurePosixPath(value[len(root):].lstrip('/') or '.')
                if any(segment_match(rel, pattern) for pattern in s['patterns']):
                    yield ((r['status']=='protected', r['priority'], len(p.parts)), r, value)
    def owners(self, path, kind):
        p = canonical(path)
        inherited = self._directory_matches(str(p.parent)) if p.parent != p else ()
        return sorted((*inherited, *self._direct(p, kind)), key=lambda v:v[0], reverse=True)
    def owner(self,path,kind):
        matches = self.owners(path,kind)
        if not matches: return None
        if len({r['id'] for score,r,_ in matches if score==matches[0][0]}) != 1: return None
        return matches[0][1:]
