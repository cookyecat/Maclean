"""Descriptor-relative filesystem operations; no symlink traversal."""
import contextlib
import hashlib
import json
import os
from pathlib import Path
import stat
import secrets
import time

class Unsafe(ValueError):
    pass

class BudgetExceeded(RuntimeError):
    pass

class Budget:
    def __init__(self, entries=50000, seconds=180, cancel=lambda:False, parent=None):
        self.limit, self.deadline, self.used = entries, time.monotonic()+seconds, 0
        self.cancel=cancel
        self.parent=parent
    def tick(self):
        if self.parent:self.parent.tick()
        if self.cancel():raise BudgetExceeded('cancelled')
        self.used += 1
        if self.used > self.limit:
            raise BudgetExceeded('entry_limit')
        if time.monotonic() > self.deadline:
            raise BudgetExceeded('time_limit')

def canonical(path):
    s = str(path)
    if not s.startswith('/') or '\x00' in s or any(x in {'.','..'} for x in s.split('/')) or '//' in s:
        raise Unsafe('absolute canonical path required')
    return Path(s)

def within(path, root):
    return Path(path).is_relative_to(Path(root))

def identity(st, full=False):
    result = [st.st_dev, st.st_ino, stat.S_IFMT(st.st_mode)]
    if full:
        result += [st.st_size, st.st_mtime_ns, st.st_ctime_ns, st.st_nlink]
    return result

@contextlib.contextmanager
def parent_fd(path, expected=None):
    p = canonical(path)
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    chain = []
    try:
        chain.append(identity(os.fstat(fd)))
        for part in p.parts[1:-1]:
            new = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = new
            chain.append(identity(os.fstat(fd)))
        if expected is not None and chain != expected:
            raise Unsafe('ancestor_identity_changed')
        yield fd, p.name, chain
    finally:
        os.close(fd)

def snapshot(path):
    with parent_fd(path) as (fd, name, chain):
        st = os.stat(name, dir_fd=fd, follow_symlinks=False)
        return {'path':str(path), 'identity':identity(st, True), 'ancestors':chain,
                'logical_bytes':st.st_size if stat.S_ISREG(st.st_mode) else 0,
                'allocated_bytes':st.st_blocks*512 if stat.S_ISREG(st.st_mode) else 0,
                'kind':'file' if stat.S_ISREG(st.st_mode) else 'directory' if stat.S_ISDIR(st.st_mode) else 'special'}

def same(record, full=True):
    try:
        new = snapshot(record['path'])
        return new['ancestors'] == record['ancestors'] and (new['identity'] == record['identity'] if full else new['identity'][:3] == record['identity'][:3])
    except (OSError, Unsafe):
        return False

def read_limited(path, limit=1048576):
    with parent_fd(path) as (fd, name, _):
        f = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
        try:
            st = os.fstat(f)
            if not stat.S_ISREG(st.st_mode) or st.st_size > limit:
                raise Unsafe('manifest_type_or_size')
            data = os.read(f, limit+1)
            if len(data) > limit: raise Unsafe('manifest_size')
            return data
        finally:
            os.close(f)

def names(path, budget):
    with parent_fd(path) as (fd, name, _):
        child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
        try:
            with os.scandir(child) as it:
                for item in it:
                    budget.tick()
                    yield item.name
        finally:
            os.close(child)

def unlink_record(record):
    with parent_fd(record['path'], record['ancestors']) as (fd, name, _):
        st = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if identity(st, True) != record['identity'] or not stat.S_ISREG(st.st_mode):
            raise Unsafe('file_identity_changed')
        # Capture the directory entry atomically, then verify the captured inode.
        # A replacement between stat and rename is restored, never unlinked.
        private='.maclean-action-'+secrets.token_hex(16)
        os.mkdir(private,0o700,dir_fd=fd)
        tmp=os.open(private,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
        captured=False
        try:
            os.rename(name,'item',src_dir_fd=fd,dst_dir_fd=tmp);captured=True
            moved=os.stat('item',dir_fd=tmp,follow_symlinks=False)
            got=identity(moved,True);want=record['identity']
            # rename changes ctime on some filesystems; all other file fields must match.
            if got[:5]!=want[:5] or got[6:]!=want[6:]: raise Unsafe('captured_identity_changed')
            with parent_fd(record['path'],record['ancestors']): pass
            os.unlink('item',dir_fd=tmp);captured=False
        finally:
            if captured:
                try:
                    # linkat refuses to overwrite a new entry at the original name.
                    os.link('item',name,src_dir_fd=tmp,dst_dir_fd=fd,follow_symlinks=False)
                    os.unlink('item',dir_fd=tmp);captured=False
                except OSError:
                    os.close(tmp)
                    raise Unsafe('restore_conflict: preserved at '+str(Path(record['path']).parent/private/'item'))
            os.close(tmp)
            if not captured: os.rmdir(private,dir_fd=fd)

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()).hexdigest()


def read_prefix(path,count):
    with parent_fd(path) as (fd,name,_):
        child=os.open(name,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd)
        try:
            if not stat.S_ISREG(os.fstat(child).st_mode):raise Unsafe('not_regular')
            return os.read(child,count)
        finally:os.close(child)


def unique_bytes(records,field='logical_bytes'):
    seen=set();total=0
    for r in records:
        key=tuple(r['identity'][:2])
        if key not in seen:total+=r[field];seen.add(key)
    return total


def residual_bytes(records):
    current=[]
    for r in records:
        try:current.append(snapshot(r['path']))
        except (OSError,Unsafe):continue
    return unique_bytes(current)


def inventory(path, budget, descend=lambda record: True):
    """One metadata visit per entry; reuse pinned directory descriptors, never follow links."""
    def record(p, st, chain):
        return {'path': str(p), 'identity': identity(st, True), 'ancestors': chain,
                'logical_bytes': st.st_size if stat.S_ISREG(st.st_mode) else 0,
                'allocated_bytes': st.st_blocks * 512 if stat.S_ISREG(st.st_mode) else 0,
                'kind': 'file' if stat.S_ISREG(st.st_mode) else 'directory' if stat.S_ISDIR(st.st_mode) else 'special'}
    def visit(p, fd, name, chain, depth):
        budget.tick()
        st = os.stat(name, dir_fd=fd, follow_symlinks=False)
        r = record(p, st, chain)
        yield r
        if r['kind'] != 'directory' or not descend(r): return
        if depth >= 256: raise Unsafe('directory_depth_limit')
        child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
        try:
            if identity(os.fstat(child)) != identity(st): raise Unsafe('directory_identity_changed')
            child_chain = chain + [identity(st)]
            with os.scandir(child) as entries:
                for entry in entries:
                    yield from visit(p / entry.name, child, entry.name, child_chain, depth + 1)
        finally:
            os.close(child)
    p = canonical(path)
    with parent_fd(p) as (fd, name, chain):
        yield from visit(p, fd, name, chain, 0)
