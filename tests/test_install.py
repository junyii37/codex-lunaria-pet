import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('lunaria_install', Path(__file__).resolve().parents[1] / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_install_and_repeat_preserve_files(self):
        with tempfile.TemporaryDirectory() as folder:
            home = Path(folder) / 'custom home'
            target, changed = installer.install(codex_home=home)
            self.assertTrue(changed)
            for name in installer.FILES:
                self.assertEqual((target / name).read_bytes(), (installer.SOURCE / name).read_bytes())
            (target / 'my-notes.txt').write_text('keep me')
            self.assertEqual(installer.install(codex_home=home), (target, False))
            (target / 'pet.json').write_text('customized')
            with self.assertRaises(FileExistsError):
                installer.install(codex_home=home)
            self.assertEqual((target / 'pet.json').read_text(), 'customized')
            self.assertEqual((target / 'my-notes.txt').read_text(), 'keep me')

    def test_unset_or_empty_codex_home_uses_home_directory(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(Path, 'home', return_value=Path(folder)):
            for env in ({}, {'CODEX_HOME': ''}):
                with patch.dict(os.environ, env, clear=True):
                    target, _ = installer.install()
                    self.assertEqual(target, Path(folder).resolve() / '.codex/pets/lunaria')

    def test_environment_override(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {'CODEX_HOME': folder}):
            self.assertEqual(installer.install()[0], Path(folder).resolve() / 'pets/lunaria')

    def test_invalid_source_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'pet.json').write_text('{}')
            with self.assertRaises(ValueError):
                installer.install(source=root, codex_home=root / 'destination')
            self.assertFalse((root / 'destination').exists())


if __name__ == '__main__':
    unittest.main()
