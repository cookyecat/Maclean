"""Segment-aware production ownership. No synthetic fact inputs accepted."""
import fnmatch
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
    def owners(self, path, kind):
        p = canonical(path)
        found = []
        for r in self.catalog['rules']:
            for s in r['selectors']:
                root = self.roots.get(s['root'])
                if not root: continue
                for anchor in (p,*p.parents):
                    if not anchor.is_relative_to(root): continue
                    if s['kind'] not in ('any', kind if anchor==p else 'directory'): continue
                    if any(segment_match(anchor.relative_to(root), x) for x in s['patterns']):
                        found.append(((r['status']=='protected',r['priority'],len(anchor.parts)),r,str(anchor)))
        return sorted(found,key=lambda v:v[0],reverse=True)
    def owner(self,path,kind):
        matches = self.owners(path,kind)
        if not matches: return None
        if len({r['id'] for score,r,_ in matches if score==matches[0][0]}) != 1: return None
        return matches[0][1:]
