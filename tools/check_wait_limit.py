import fcntl,json,sys,tempfile,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'macos-disk-auditor/scripts'))
from maclean_core.native import prepare,execute
with tempfile.TemporaryDirectory(prefix='maclean-wait-') as temp:
 root=Path(temp).resolve();cache=root/'uv';cache.mkdir();(cache/'CACHEDIR.TAG').write_text('Signature: 8a477f597d28d172789f06886806bc55');(cache/'wheels-v5').mkdir();f=cache/'wheels-v5/data';f.write_bytes(b'test')
 with (cache/'.lock').open('wb') as lock:
  fcntl.flock(lock,fcntl.LOCK_SH);native=prepare('native_uv',{'HOME':str(root),'UV_CACHE':str(cache)});start=time.monotonic();r=execute(native);elapsed=time.monotonic()-start
 assert r['status']=='pending' and f.exists() and 29<=elapsed<35,(r,elapsed)
 print(json.dumps({'status':'passed','elapsed_seconds':elapsed,'result':r,'cache_preserved':True}))
