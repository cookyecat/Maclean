"""Version-gated native cache maintenance, never shell commands."""
import os
import re
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
from .fs import Unsafe, same, snapshot, within, names, Budget, read_limited
from .probes import run

TESTED={'uv':'0.12.5','npm':'12.2.0'}

def prepare(protocol,roots,shared_budget=None):
    if protocol not in {'native_uv','native_npm','native_npx'}: return None
    tool='uv' if protocol=='native_uv' else 'npm'
    found=shutil.which(tool)
    if not found: return None
    exe=str(Path(found).resolve())
    try:
        version=run([exe,'--version',*(['--logs-max=0'] if tool=='npm' else [])]).stdout.decode().strip()
        if (version.split()[1] if tool=='uv' else version)!=TESTED[tool]: return None
        root=roots['UV_CACHE' if tool=='uv' else 'NPM_CACHE']
        if not root or root in {roots['HOME'],'/'}: return None
        bound=snapshot(root)
        if bound['kind']!='directory': return None
        children=list(names(root,Budget(50000,10,parent=shared_budget)))
        if tool=='uv':
            if read_limited(Path(root)/'CACHEDIR.TAG')[:43]!=b'Signature: 8a477f597d28d172789f06886806bc55': return None
            if any(not re.fullmatch(r'(CACHEDIR.TAG|\.gitignore|\.lock|[a-z0-9-]+-v[0-9]+)',n) for n in children): return None
        else:
            if any(n not in {'_cacache','_npx','_logs','_update-notifier-last-checked'} for n in children): return None
        if any(snapshot(Path(root)/n)['kind']=='special' for n in children): return None
        if tool=='uv':
            query=run([exe,'cache','dir','--cache-dir',root,'--no-config']).stdout.decode().strip()
            if query!=root: return None
            argv=[exe,'cache','clean','--cache-dir',root,'--no-config','--offline']
        else:
            query=run([exe,'config','get','cache','--cache',root,'--logs-max=0']).stdout.decode().strip()
            if query!=root: return None
            argv=[exe,'cache',*(['npx','rm','--force'] if protocol=='native_npx' else ['clean','--force']),'--cache',root,'--logs-max=0']
        return {'protocol':protocol,'roots':roots,'tool':tool,'version':version,'executable':snapshot(exe),'domain':bound,'argv':argv,
                'effect':'完整 uv 缓存域，保留原生锁' if tool=='uv' else 'npm 缓存维护域；可能更新诊断元数据（禁用日志保留）；不涉及全局安装包'}
    except (OSError,ValueError,subprocess.TimeoutExpired): return None

def execute(native,cancel=lambda:False,timeout=30):
    if not same(native['executable']) or not same(native['domain'],False): return {'status':'pending','reason':'native_identity_changed'}
    fresh=prepare(native['protocol'],native['roots'])
    if not fresh or fresh['argv']!=native['argv']:return {'status':'pending','reason':'native_domain_layout_changed'}
    if native['argv'][2:4]==['npx','rm']:
        from .runtime import in_use
        if in_use(str(Path(native['domain']['path'])/'_npx')): return {'status':'pending','reason':'npx_target_in_use'}
    with tempfile.TemporaryDirectory(prefix='maclean-native-') as cwd:
        env={'PATH':'/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin','HOME':cwd,'LANG':'C','UV_LOCK_TIMEOUT':'30','npm_config_update_notifier':'false'}
        # Child output goes to temporary files, not unbounded PIPE buffers or user reports.
        with tempfile.TemporaryFile() as output:
            p=subprocess.Popen(native['argv'],cwd=cwd,env=env,stdout=output,stderr=output,start_new_session=True)
            deadline=time.monotonic()+timeout
            while p.poll() is None:
                if cancel() or time.monotonic()>=deadline:
                    p.terminate()
                    try: p.wait(timeout=2)
                    except subprocess.TimeoutExpired: p.kill(); p.wait()
                    return {'status':'pending','reason':'cancelled_or_native_lock_timeout','requires_rescan':True}
                time.sleep(.05)
            return {'status':'completed' if p.returncode==0 else 'pending','reason':'native_exit','exit_code':p.returncode,'requires_rescan':True}
