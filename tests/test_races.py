import os
from unittest.mock import patch
from test_core import Fixture
from maclean_core.fs import snapshot, unlink_record, Unsafe

class RaceTests(Fixture):
    def test_replace_between_stat_and_rename_never_deleted(self):
        a=self.file('Library/Caches/A/a');replacement=self.file('replacement',b'unique');record=snapshot(a)
        real=os.rename;fired=[False]
        def race(src,dst,*args,**kw):
            if src==a.name and dst=='item' and not fired[0]:
                fired[0]=True;a.unlink();os.replace(replacement,a)
            return real(src,dst,*args,**kw)
        with patch('maclean_core.fs.os.rename',side_effect=race):
            with self.assertRaises(Unsafe):unlink_record(record)
        self.assertEqual(a.read_bytes(),b'unique')
    def test_replace_with_symlink_at_last_instant(self):
        a=self.file('Library/Caches/A/a');outside=self.file('unique',b'important');record=snapshot(a)
        real=os.rename;fired=[False]
        def race(src,dst,*args,**kw):
            if src==a.name and not fired[0]:fired[0]=True;a.unlink();a.symlink_to(outside)
            return real(src,dst,*args,**kw)
        with patch('maclean_core.fs.os.rename',side_effect=race):
            with self.assertRaises(Unsafe):unlink_record(record)
        self.assertEqual(outside.read_bytes(),b'important');self.assertTrue(a.is_symlink())
