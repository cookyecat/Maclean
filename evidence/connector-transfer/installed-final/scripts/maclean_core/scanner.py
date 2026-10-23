"""Bounded directed discovery and per-file ownership/inventory."""
import fnmatch
import os
from pathlib import Path
import time
from .fs import Budget, BudgetExceeded, Unsafe, canonical, digest, names, snapshot, within, unique_bytes
from .rules import RuleBook, CATALOG
from .probes import bind, probe
from .native import prepare
from .runtime import prepare as prepare_runtime, in_use

EXCLUDED={'.git','node_modules','.venv','venv','.env'}
SUPPORTED={'online_inventory','project_cache'}
STANDARD={'macos-user-cache','macos-user-log','sandbox-cache','sandbox-log','group-cache','group-log'}
AI_DOMAINS={'Codex','Claude','ChatGPT','Cursor','Windsurf','LM Studio','com.openai.codex','com.openai.chat','com.anthropic.claudefordesktop','com.todesktop.230313mzl4w4u92'}

def category_for(rule,anchor):
    if rule['id'] in STANDARD and set(Path(anchor).parts)&AI_DOMAINS:return 'ai'
    return rule['category']

class Scanner:
    def __init__(self, project=None, overrides=None, fixture_home=None, entries=50000, seconds=180, keep=(), paths=(), category=None, cancel=lambda:False):
        self.roots,self.bindings=bind(project,overrides,fixture_home)
        self.book=RuleBook(self.roots)
        self.budget=Budget(entries,seconds,cancel)
        self.keep=[canonical(x) for x in keep]
        self.paths=[canonical(x) for x in paths]
        self.category=category
        self.coverage=[]; self.targets={}; self.errors=[]; self.seen=set(); self.measured=set()
        self.list_cache={}
        self.native_cache={}
    def children(self,p):
        key=str(p)
        if key not in self.list_cache: self.list_cache[key]=list(names(p,self.budget))
        return self.list_cache[key]
    def expand(self,root,pattern):
        parts=[] if pattern=='.' else pattern.split('/')
        def walk(p, rest, depth=0):
            self.budget.tick()
            if not self.allowed(p):return
            if rest and snapshot(p)['kind']!='directory':return
            if not rest:
                try: snapshot(p); yield p
                except FileNotFoundError: pass
                return
            part=rest[0]
            if part=='**':
                yield from walk(p,rest[1:],depth)
                if depth<6:
                    for n in self.children(p):
                        q=p/n
                        if n not in EXCLUDED and snapshot(q)['kind']=='directory': yield from walk(q,rest,depth+1)
                return
            if any(c in part for c in '*?['):
                for n in self.children(p):
                    if fnmatch.fnmatchcase(n,part): yield from walk(p/n,rest[1:],depth)
            else:
                try: yield from walk(p/part,rest[1:],depth)
                except FileNotFoundError: pass
        yield from walk(Path(root),parts)
    def allowed(self,p):
        return not self.paths or any(within(p,x) or within(x,p) for x in self.paths)
    def target(self,rule,anchor):
        key=digest([rule['id'],anchor])[:20]
        if key not in self.targets:
            self.targets[key]={'id':key,'path':anchor,'rule':rule['id'],'rule_version':rule['version'],
                'category':category_for(rule,anchor),'purpose':rule['purpose'],'impact':rule['impact'],
                'recovery':rule['recovery'],'sources':rule['evidence_sources'],
                'inference_cost_effect':rule['inference_cost_effect'],'gap':rule['gap'],
                'protocol':rule['execution_protocol'],'disposition':rule['disposition'],
                'execution_route':'online' if rule['execution_protocol'] in SUPPORTED else 'unsupported',
                'files':[],'retained':[],'logical_bytes':0,'allocated_bytes':0,'complete':True,
                'selected':False,'issues':[]}
        return self.targets[key]
    def leaf(self,p,record):
        owned=self.book.owner(p,record['kind'])
        if not owned: return
        rule,anchor=owned
        if self.category and category_for(rule,anchor)!=self.category: return
        t=self.target(rule,anchor)
        if record['kind']!='file':
            if record['kind']=='special':
                reason='special_or_symlink'
                if rule['execution_protocol'].startswith('native_') and Path(p).is_symlink():
                    destination=Path(os.path.abspath(Path(p).parent/os.readlink(p)))
                    if within(destination,anchor):reason='internal_native_link'
                t['issues'].append({'path':str(p),'reason':reason})
            return
        inode=tuple(record['identity'][:2])
        if inode not in self.measured:
            t['logical_bytes']+=record['logical_bytes']; t['allocated_bytes']+=record['allocated_bytes']; self.measured.add(inode)
        reasons=[]
        if any(within(p,x) for x in self.keep): reasons.append('user_keep')
        if self.paths and not any(within(p,x) for x in self.paths): reasons.append('outside_selected_path')
        if rule['status']!='ready': reasons.append(rule['status'])
        else:
            reasons += [f for f in rule['identity_checks'] if not probe(f,p,anchor,self.roots)]
            if rule['execution_protocol'] not in SUPPORTED:
                protocol=rule['execution_protocol']
                if protocol not in self.native_cache: self.native_cache[protocol]=prepare(protocol,self.roots,self.budget)
                native=self.native_cache[protocol]
                if native:
                    reasons=[x for x in reasons if x not in {'native_supported'}]
                    t['native']=native; t['execution_route']='coordinated'
                else:
                    rk=(protocol,anchor)
                    if rk not in self.native_cache: self.native_cache[rk]=prepare_runtime(protocol,anchor,self.roots,self.budget)
                    runtime=self.native_cache[rk]
                    if runtime:
                        reasons=[x for x in reasons if x not in {'puppeteer_layout','claude_launcher','claude_obsolete','local_volume'}]
                        t['runtime']=runtime; t['execution_route']='coordinated'
                    else: reasons.append('adapter_not_verified')
        if reasons:
            t['retained'].append({'path':str(p),'reason':reasons})
            for reason in reasons:
                if {'reason':reason} not in t['issues']:t['issues'].append({'reason':reason})
            if rule['status']=='ready': t['disposition']='investigate'
        else:
            t['files'].append(record)
    def measure(self,p):
        local=Budget(50000,30)
        def visit(q):
            if not self.allowed(q) or str(q) in self.seen: return
            local.tick(); self.budget.tick(); self.seen.add(str(q))
            r=snapshot(q)
            owner=self.book.owner(q,r['kind'])
            if owner:
                t=self.target(*owner)
                if owner[0]['status']=='protected' and r['kind']=='directory':
                    t['measurement']='not_measured_protected';return
            if r['kind']=='directory':
                for n in self.children(q): visit(q/n)
            else: self.leaf(q,r)
        try: visit(p)
        except (OSError,Unsafe,BudgetExceeded) as e:
            reason=('cancelled' if str(e)=='cancelled' else 'budget_exceeded') if isinstance(e,BudgetExceeded) else 'access_denied' if isinstance(e,PermissionError) else 'layout_unverified'
            self.errors.append({'path':str(p),'status':reason,'error':str(e),'continue_path':str(p)})
            for t in self.targets.values():
                if within(t['path'],p) or within(p,t['path']): t['complete']=False
    def scan(self):
        for rule in CATALOG['rules']:
            if self.category and rule['category']!=self.category and not(self.category=='ai' and rule['id'] in STANDARD): continue
            for s in rule['selectors']:
                root=self.roots.get(s['root'])
                cov={'rule':rule['id'],'root':s['root'],'path':root,'status':'absent','matches':0}
                self.coverage.append(cov)
                if not root:
                    cov['status']='not_requested' if s['root'] in {'PROJECT','NEXT_DIST','CARGO_BUILD','PYTEST_CACHE','RUFF_CACHE'} and not self.roots.get('PROJECT') else 'root_unresolved'
                    continue
                try:
                    for pattern in s['patterns']:
                        for p in self.expand(root,pattern):
                            if not self.allowed(p): continue
                            cov['status']='matched'; cov['matches']+=1
                            before=len(self.errors)
                            self.measure(p)
                            if len(self.errors)>before: cov['status']=self.errors[-1]['status']
                except FileNotFoundError: pass
                except (OSError,Unsafe,BudgetExceeded) as e:
                    cov['status']=('cancelled' if str(e)=='cancelled' else 'budget_exceeded') if isinstance(e,BudgetExceeded) else 'access_denied' if isinstance(e,PermissionError) else 'layout_unverified'
                    cov['error']=str(e); cov['continue_path']=root
        targets=list(self.targets.values())
        for t in targets:
            t['eligible_logical_bytes']=unique_bytes(t['files'])
            # Valid independent leaves remain selectable even if siblings need investigation.
            t['selected']=bool(t['files'] and t['eligible_logical_bytes'] and t['complete'])
            if t.get('native') and (t['retained'] or any(i['reason']!='internal_native_link' for i in t['issues']) or any(within(x, t['native']['domain']['path']) for x in self.keep)):
                t['selected']=False; t['issues'].append({'reason':'native_domain_has_exclusions'})
            if t.get('runtime') and (t['retained'] or any(within(x,t['path']) for x in self.keep)):
                t['selected']=False
            if t.get('native') or t.get('runtime'):
                domain=t.get('native',{}).get('domain',{}).get('path',t['path'])
                if any(other is not t and within(other['path'],domain) and other['disposition']=='retain' for other in targets):
                    t['selected']=False; t['issues'].append({'reason':'protected_child_in_atomic_domain'})
            if t['selected']:
                t['disposition']='disposable'
                if t['protocol']=='project_cache' and in_use(t['path'],snapshot(t['path'])['kind']=='directory'):
                    t['execution_route']='after_task'
        inspections=[]
        for selected in self.paths:
            try:
                meta=snapshot(selected);matches=self.book.owners(selected,meta['kind'])
                inspections.append({'path':str(selected),'metadata':meta,'matching_rules':[r['id'] for _,r,_ in matches],'reason':'matched' if matches else 'no_rule'})
            except (OSError,Unsafe) as e:inspections.append({'path':str(selected),'reason':'unavailable','error':str(e)})
        return {'inspections':inspections,'kind':'scan','schema_version':1,'created':time.time(),'roots':self.roots,'bindings':self.bindings,
                'catalog_version':CATALOG['catalog_version'],'catalog_digest':digest(CATALOG),
                'targets':targets,'coverage':self.coverage,'errors':self.errors,'entries':self.budget.used,
                'complete':not self.errors and not any(x['status'] in {'budget_exceeded','cancelled','access_denied','layout_unverified','root_unresolved'} for x in self.coverage),
                'options':{'project':self.roots.get('PROJECT'),'keep':[str(x) for x in self.keep],'paths':[str(x) for x in self.paths]},
                'fixture':self.bindings['HOME']['source']=='fixture'}


def scan_projects(project=None, **options):
    """Find manifest roots only inside an explicitly selected tree, sharing one budget."""
    primary=Scanner(project=project,**options)
    if not project:return primary.scan()
    projects=[str(canonical(project))];discovery_errors=[]
    def discover(p,depth):
        try:
            entries=primary.children(p)
            if p!=Path(project) and set(entries)&{'package.json','Cargo.toml','pyproject.toml','setup.cfg','setup.py','requirements.txt'}:
                projects.append(str(p))
            if depth>=6:return
            for n in entries:
                if n in EXCLUDED or n in {'.next','target','dist','build','.pytest_cache','.ruff_cache','__pycache__'}:continue
                q=p/n
                primary.budget.tick()
                if snapshot(q)['kind']=='directory':discover(q,depth+1)
        except (OSError,Unsafe,BudgetExceeded) as e:
            discovery_errors.append({'path':str(p),'status':('cancelled' if str(e)=='cancelled' else 'budget_exceeded') if isinstance(e,BudgetExceeded) else 'access_denied','continue_path':str(p)})
    discover(Path(project),0)
    result=primary.scan();seen={t['id'] for t in result['targets']}
    for selected in projects[1:]:
        if primary.budget.used>primary.budget.limit or time.monotonic()>primary.budget.deadline:
            discovery_errors.append({'path':selected,'status':'budget_exceeded','continue_path':selected});break
        opts=dict(options);opts['category']='development'
        child=Scanner(project=selected,**opts);child.budget=primary.budget
        child_result=child.scan()
        for t in child_result['targets']:
            if t['id'] not in seen:
                t['project_roots']=child.roots;result['targets'].append(t);seen.add(t['id'])
            elif t['selected']:
                for n,old in enumerate(result['targets']):
                    if old['id']==t['id'] and not old['selected']:
                        t['project_roots']=child.roots;result['targets'][n]=t;break
        result['coverage']+=child_result['coverage'];result['errors']+=child_result['errors']
        result['complete']=result['complete'] and child_result['complete']
    # Parent and child project roots can discover the same bytecode leaf: keep one action.
    paths=set();inodes=set()
    for t in result['targets']:
        unique=[]
        for f in t['files']:
            if f['path'] not in paths:unique.append(f);paths.add(f['path'])
        t['files']=unique;t['eligible_logical_bytes']=unique_bytes(unique)
        if not unique:t['selected']=False
    result['errors']+=discovery_errors;result['complete']=result['complete'] and not discovery_errors
    result['project_discovery']={'projects':projects,'max_depth':6,'entries':primary.budget.used}
    return result
