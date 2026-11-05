"""El producto distribuible no puede incorporar el piloto privado del repositorio."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from exportar_producto import exportar


class ExportarProductoTest(unittest.TestCase):
    @unittest.skipUnless((ROOT / '.git').exists(), 'requiere checkout Git real')
    def test_current_checkout_exports_product_without_private_pilot(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'producto.zip'
            result = exportar(ROOT, output)
            self.assertGreater(result['archivos'], 100)
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
                manifest = json.loads(archive.read('PRODUCT_MANIFEST.json'))
                self.assertEqual(manifest['commit'], result['sha_producto'])
                self.assertEqual(len(manifest['archivos']), result['archivos'])
                self.assertEqual(result['manifest_sha256'],
                                 hashlib.sha256(archive.read('PRODUCT_MANIFEST.json')).hexdigest())
                for item in manifest['archivos']:
                    data = archive.read(item['ruta'])
                    self.assertEqual(len(data), item['bytes'])
                    self.assertEqual(hashlib.sha256(data).hexdigest(), item['sha256'])
                self.assertIn('.agents/skills/ce-desarrollo-empresa/SKILL.md', names)
                self.assertIn('plantilla_boveda/Inicio.md', names)
                self.assertFalse(any(name.startswith('.github/workflows/')
                                     for name in names))
                self.assertFalse(any(name.startswith('material_privado/')
                                     for name in names))

    def test_real_company_material_never_enters_product_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp)
            repo = work / 'repo'
            repo.mkdir()
            for name in ('AGENTS.md', 'README.md', 'scripts/cerebro.py',
                         '.agents/skills/ce-instalacion/SKILL.md', 'LICENSE', 'CONTRIBUTING.md',
                         'README.es.md', '.cursor-init.yaml', 'THIRD_PARTY_NOTICES.md',
                         '.cursor/commands/cursor-init/check-docs.md',
                         'docs/en/onboarding.md', 'docs/es/onboarding.md',
                         'START_HERE.md', 'GET_STARTED_WITH_CODEX.md', 'CONTINUE_WITH_CODEX.md',
                         '.cursor/corpus/private.md',
                         'scripts/.venv/tool.txt',
                         'material_privado/EMPRESA-SINTETICA/originales/privado.md'):
                path = repo / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('SECRETO_EMPRESARIAL' if 'material_privado' in name
                                else 'producto', encoding='utf8', newline='\n')
            for cmd in (('init', '-q'), ('config', 'user.name', 'Prueba'),
                        ('config', 'user.email', 'test@example.invalid'),
                        ('add', '.'), ('commit', '-qm', 'base')):
                subprocess.run(['git', '-C', str(repo), *cmd], check=True,
                               stdout=subprocess.DEVNULL)
            output = work / 'producto.zip'
            result = exportar(repo, output)
            self.assertFalse(result['material_privado_incluido'])
            with zipfile.ZipFile(output) as archive:
                self.assertIn('scripts/cerebro.py', archive.namelist())
                self.assertIn('LICENSE', archive.namelist())
                self.assertIn('CONTRIBUTING.md', archive.namelist())
                for expected in ('README.es.md', '.cursor-init.yaml', 'THIRD_PARTY_NOTICES.md',
                                 '.cursor/commands/cursor-init/check-docs.md',
                                 'docs/en/onboarding.md', 'docs/es/onboarding.md',
                                 'START_HERE.md', 'GET_STARTED_WITH_CODEX.md', 'CONTINUE_WITH_CODEX.md'):
                    self.assertIn(expected, archive.namelist())
                self.assertNotIn('.cursor/corpus/private.md', archive.namelist())
                self.assertNotIn('scripts/.venv/tool.txt', archive.namelist())
                self.assertFalse(any(x.startswith('material_privado/')
                                     for x in archive.namelist()))
                self.assertNotIn(b'SECRETO_EMPRESARIAL',
                                 b''.join(archive.read(x) for x in archive.namelist()))

    def test_cannot_export_inside_repository(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaisesRegex(ValueError, 'fuera del repositorio'):
                exportar(root, root / 'producto.zip')


if __name__ == '__main__':
    unittest.main()
