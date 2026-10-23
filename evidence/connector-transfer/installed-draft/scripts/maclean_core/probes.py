"""Restricted metadata, manifest and installed-tool probes."""
import importlib.util
import json
import os
from pathlib import Path
import pwd
import plistlib
import re
import shutil
import subprocess
import tempfile
from .fs import Unsafe, canonical, snapshot, read_limited, read_prefix, within

ENV_KEYS = {'CODEX_HOME':'CODEX_HOME','CLAUDE_HOME':'CLAUDE_CONFIG_DIR',
            'PLAYWRIGHT_CACHE':'PLAYWRIGHT_BROWSERS_PATH','PUPPETEER_CACHE':'PUPPETEER_CACHE_DIR'}
DEFAULTS = {'SUPPORT':'Library/Application Support','CODEX_HOME':'.codex','CLAUDE_HOME':'.claude',
'CLAUDE_VERSIONS':'.local/share/claude/versions','NPM_CACHE':'.npm','UV_CACHE':'.cache/uv',
'PLAYWRIGHT_CACHE':'Library/Caches/ms-playwright','PUPPETEER_CACHE':'.cache/puppeteer'}
PROJECT_DEFAULTS = {'NEXT_DIST':'.next','CARGO_BUILD':'target','PYTEST_CACHE':'.pytest_cache','RUFF_CACHE':'.ruff_cache'}

def run(argv, seconds=5):
    with tempfile.TemporaryDirectory(prefix='maclean-probe-') as cwd:
        env = {'PATH':'/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin','HOME':pwd.getpwuid(os.getuid()).pw_dir,
               'LANG':'C','UV_LOCK_TIMEOUT':'30','npm_config_update_notifier':'false'}
        return subprocess.run(argv,cwd=cwd,env=env,capture_output=True,timeout=seconds,check=False)

def bind(project=None, overrides=None, fixture_home=None):
    overrides = overrides or {}
    if 'HOME' in overrides or 'SUPPORT' in overrides: raise Unsafe('fixed root override')
    home = str(canonical(fixture_home or pwd.getpwuid(os.getuid()).pw_dir))
    roots = {'HOME':home, **{k:str(Path(home)/v) for k,v in DEFAULTS.items()}}
    sources = {k:'default' for k in roots}; sources['HOME']='fixture' if fixture_home else 'pwd_uid'
    if project:
        roots['PROJECT']=str(canonical(project))
        roots.update({k:str(Path(project)/v) for k,v in PROJECT_DEFAULTS.items()})
        sources.update({k:'selected_project' for k in ['PROJECT',*PROJECT_DEFAULTS]})
    if not fixture_home:
        for k,e in ENV_KEYS.items():
            if os.environ.get(e):
                value=os.environ[e]
                roots[k]=str(canonical(value)) if value.startswith('/') else None
                sources[k]='environment:'+e
        for key,tool,args in [('NPM_CACHE','npm',['config','get','cache','--logs-max=0']),('UV_CACHE','uv',['cache','dir'])]:
            exe=shutil.which(tool)
            if exe:
                try:
                    p=run([exe,*args]); val=p.stdout.decode().strip()
                    if p.returncode==0: roots[key]=str(canonical(val)); sources[key]='native_query'
                except (ValueError,OSError,subprocess.TimeoutExpired): pass
    for k,v in overrides.items():
        if k not in DEFAULTS and k not in PROJECT_DEFAULTS: raise Unsafe('unknown root')
        value=canonical(v)
        if value==Path(home) or str(value)=='/' or any(within(value,Path(home)/x) for x in ['.ssh','.aws','Library/Keychains']):
            raise Unsafe('unsafe custom domain')
        roots[k]=str(value); sources[k]='explicit'
    records={}
    for k,p in roots.items():
        try: records[k]={'path':p,'source':sources.get(k),'status':'bound','snapshot':snapshot(p)} if p else {'status':'root_unresolved'}
        except FileNotFoundError: records[k]={'path':p,'source':sources.get(k),'status':'absent'}
        except (OSError,Unsafe) as e: records[k]={'path':p,'source':sources.get(k),'status':'root_unresolved','error':str(e)}
    return roots,records

def regular(p):
    try: return snapshot(p)['kind']=='file'
    except (OSError,Unsafe): return False

def directory(p):
    try: return snapshot(p)['kind']=='directory'
    except (OSError,Unsafe): return False

def untracked(path, project):
    if not project: return False
    # A nested project can belong to a repository rooted above the selected directory.
    if not any((p/'.git').exists() for p in (Path(project),*Path(project).parents)): return True
    git=shutil.which('git')
    if not git: return False
    try:
        r=run([git,'--no-optional-locks','-C',project,'ls-files','-z','--',str(path)])
        return r.returncode==0 and not r.stdout
    except (OSError,subprocess.TimeoutExpired): return False

def probe(name, path, anchor, roots):
    p,a=Path(path),Path(anchor); project=Path(roots['PROJECT']) if roots.get('PROJECT') else None
    try:
        if name=='project_untracked': return untracked(p,str(project) if project else None)
        if name=='python_project': return bool(project and any(regular(project/x) for x in ['pyproject.toml','setup.cfg','setup.py','requirements.txt']))
        if name=='rust_project': return bool(project and regular(project/'Cargo.toml'))
        if name=='next_project':
            j=json.loads(read_limited(project/'package.json'))
            return any(isinstance(j.get(k),dict) and 'next' in j[k] for k in ['dependencies','devDependencies'])
        if name=='python_source_pair': return regular(Path(importlib.util.source_from_cache(str(p))))
        if name=='cache_tag':
            root=roots.get('PYTEST_CACHE') if within(a,roots.get('PYTEST_CACHE','/nonexistent')) else roots.get('RUFF_CACHE')
            return bool(root and read_prefix(Path(root)/'CACHEDIR.TAG',43)==b'Signature: 8a477f597d28d172789f06886806bc55')
        if name=='ruff_layout':
            rel=p.relative_to(roots['RUFF_CACHE'])
            return str(rel)=='.' or rel.parts[0] in {'CACHEDIR.TAG','.gitignore'} or bool(re.fullmatch(r'\d+(?:\.\d+)+',rel.parts[0]))
        if name in {'chromium_layout','browser_profile'}:
            root=a.parent
            markers=['Code Cache','GPUCache','ShaderCache','GrShaderCache','DawnCache','GraphiteDawnCache','DawnGraphiteCache','DawnWebGPUCache']
            layout=sum(directory(root/x) for x in markers)>=2
            return layout and (name!='browser_profile' or bool(re.fullmatch(r'(Default|Guest Profile|System Profile|Profile [0-9]+)',root.name)))
        if name=='editor_layout':
            apps={'Code':'Visual Studio Code','Code - Insiders':'Visual Studio Code - Insiders','VSCodium':'VSCodium'}
            app=apps.get(a.parent.name)
            if not app or not directory(a.parent/'User'):return False
            bundle_ids={'Code':'com.microsoft.VSCode','Code - Insiders':'com.microsoft.VSCodeInsiders','VSCodium':'com.vscodium'}
            for x in [Path('/Applications'),Path(roots['HOME'])/'Applications']:
                try:
                    info=plistlib.loads(read_limited(x/(app+'.app')/'Contents/Info.plist'))
                    if info.get('CFBundleIdentifier')==bundle_ids[a.parent.name]:return True
                except (OSError,ValueError):continue
            return False
        if name=='native_domain_verified':
            root=roots.get('UV_CACHE') if within(a,roots.get('UV_CACHE','/nonexistent')) else roots.get('NPM_CACHE')
            return bool(root and root not in {roots['HOME'],'/'} and directory(root))
        if name=='native_supported': return False # enabled only by versioned native adapter, not a boolean supplied by caller
        if name=='playwright_layout': return bool(re.fullmatch(r'(chromium|chromium_headless_shell|firefox|webkit|ffmpeg)-[0-9]+',a.name) and regular(a/'INSTALLATION_COMPLETE'))
        # Runtime lifecycle/signature/metadata protocols are explicitly gated until integration validated.
        return False
    except (OSError,ValueError,TypeError,KeyError,subprocess.TimeoutExpired): return False
