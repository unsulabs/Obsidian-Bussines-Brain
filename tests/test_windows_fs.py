"""Native Windows security tests. POSIX skips are explicit platform gates."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import windows_fs as fs


@unittest.skipUnless(os.name == "nt", "native Windows filesystem backend")
class WindowsFilesystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "private"
        fs.ensure_private_directory(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_private_acl_is_real_and_existing_broad_acl_is_rejected(self):
        self.assertTrue(fs.is_private_directory(self.root))
        original = fs.security_descriptor(self.root)
        try:
            fs.set_security_descriptor(self.root, "D:P(A;OICI;FA;;;WD)")
            self.assertFalse(fs.is_private_directory(self.root))
            with self.assertRaisesRegex(ValueError, "PRIVATE_DIRECTORY_REQUIRED"):
                fs.ensure_private_directory(self.root)
            self.assertFalse(fs.is_private_directory(self.root))
        finally:
            fs.set_security_descriptor(self.root, original)

    def test_write_read_immutable_conflict_and_mutable_replace(self):
        fs.atomic_write(self.root, "nested/payload.bin", b"original\x00")
        self.assertEqual(fs.read_bytes(self.root, "nested/payload.bin"), b"original\x00")
        fs.atomic_write(self.root, "nested/payload.bin", b"original\x00")
        with self.assertRaisesRegex(ValueError, "IMMUTABLE_CONFLICT"):
            fs.atomic_write(self.root, "nested/payload.bin", b"different")
        fs.atomic_write(self.root, "nested/payload.bin", b"updated", immutable=False)
        self.assertEqual(fs.read_bytes(self.root, "nested/payload.bin"), b"updated")
        self.assertFalse(list(self.root.rglob(".tmp-*")))

    def test_permission_preserving_replace(self):
        target = self.root / "note.md"
        fs.atomic_write(self.root, target.name, b"old")
        # A read-only grant to Everyone is intentionally distinct from default.
        fs.set_security_descriptor(target,
            f"D:P(A;;FA;;;{fs._user_sid()})(A;;FR;;;WD)")
        before = fs.security_descriptor(target)
        fs.atomic_write(self.root, target.name, b"new", immutable=False, preserve_acl=True)
        self.assertEqual(fs.security_descriptor(target), before)

    def test_restrictive_but_unprotected_acl_is_rejected(self):
        child = self.root / "child"
        fs.ensure_private_directory(child)
        fs.set_security_descriptor(child,
            f"D:(A;OICI;FA;;;{fs._user_sid()})", protected=False)
        self.assertFalse(fs.is_private_directory(child))
        with self.assertRaisesRegex(ValueError, "PRIVATE_DIRECTORY_REQUIRED"):
            fs.ensure_private_directory(child)

    def test_windows_aliases_and_streams_rejected(self):
        for relative in ("file:secret", "NUL", "name.", "name ", "C:escape", "../escape"):
            with self.subTest(relative=relative), self.assertRaises(ValueError):
                fs.atomic_write(self.root, relative, b"bad")

    def test_pinned_directory_cannot_be_renamed(self):
        nested = self.root / "nested"
        fs.ensure_private_directory(nested)
        with fs.directory(nested):
            with self.assertRaises(OSError):
                nested.rename(self.root / "moved")
            with self.assertRaises(OSError):
                self.root.rename(self.root.with_name("moved-root"))

    def test_junction_ancestor_rejected(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (outside / "secret").write_bytes(b"outside")
        junction = self.root / "junction"
        subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(outside)],
                       check=True, capture_output=True)
        try:
            with self.assertRaisesRegex(ValueError, "UNSAFE_PATH"):
                fs.read_bytes(self.root, "junction/secret")
            with self.assertRaisesRegex(ValueError, "UNSAFE_PATH"):
                fs.atomic_write(self.root, "junction/created", b"bad")
            self.assertFalse((outside / "created").exists())
        finally:
            junction.rmdir()

    def test_native_lock_blocks_and_releases_on_process_death(self):
        lock = self.root / ".writer.lock"
        code = ("import sys,time;sys.path.insert(0,sys.argv[1]);import windows_fs as f;"
                "ctx=f.file_lock(sys.argv[2]);ctx.__enter__();print('LOCKED',flush=True);"
                "time.sleep(60)")
        process = subprocess.Popen([sys.executable, "-c", code,
            str(Path(fs.__file__).parent), str(lock)], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True)
        try:
            self.assertEqual(process.stdout.readline().strip(), "LOCKED")
            with self.assertRaises(BlockingIOError):
                with fs.file_lock(lock, blocking=False):
                    pass
            process.kill()
            process.wait(timeout=10)
            with fs.file_lock(lock, blocking=False):
                pass
        finally:
            if process.poll() is None:
                process.kill()
                process.wait(timeout=10)
            process.stdout.close()
            process.stderr.close()


if __name__ == "__main__":
    unittest.main()
