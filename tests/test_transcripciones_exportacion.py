"""Aislamiento de corpus sintético, incluso dentro de rutas exportables."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from exportar_producto import exportar
from auditar_paquete import audit


class TranscripcionesExportacionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.repo = self.work / 'repo'
        self.repo.mkdir()
        self.private = [f'{prefix}{name}/original.txt'
                        for prefix in ('', 'docs/', 'scripts/datos/')
                        for name in ('banco-transcripciones', 'recepcion', 'corpus',
                                     'transcripciones_completas')]
        self.public = ('AGENTS.md', 'README.md', 'scripts/cerebro.py',
                       '.agents/skills/ce-instalacion/SKILL.md',
                       'scripts/transcripciones.py', 'docs/TRANSCRIPCIONES.md')

    def write(self, name, content):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf8')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True,
                              capture_output=True).stdout

    def test_git_ignores_private_containers_at_any_depth(self):
        self.write('.gitignore', (ROOT / '.gitignore').read_text())
        self.git('init', '-q')
        for name in self.private:
            self.write(name, 'CORPUS_SINTETICO_PRIVADO')
            self.assertEqual(self.git('check-ignore', name).decode().strip(), name)
        self.write('scripts/transcripciones.py', '# software')
        self.assertEqual(self.git('ls-files', '--others', '--exclude-standard').decode().splitlines(),
                         ['.gitignore', 'scripts/transcripciones.py'])

    def test_forced_tracked_corpus_is_not_exported_or_manifested(self):
        private = self.private + ['docs/BANCO-TRANSCRIPCIONES/original.txt',
                                  'docs/material_privado/original.txt']
        for name in self.public:
            self.write(name, 'producto')
        for name in private:
            self.write(name, 'CORPUS_SINTETICO_PRIVADO')
        self.write('.gitignore', (ROOT / '.gitignore').read_text())
        self.git('init', '-q')
        self.git('config', 'user.name', 'Prueba')
        self.git('config', 'user.email', 'test@example.invalid')
        # Sólo rutas enumeradas del fixture; simula una inclusión accidental.
        self.git('add', '--force', '--', '.gitignore', *self.public, *private)
        self.git('commit', '-qm', 'fixture sintetico')
        output = self.work / 'producto.zip'
        exportar(self.repo, output)
        with zipfile.ZipFile(output) as archive:
            names = set(archive.namelist())
            manifest = json.loads(archive.read('PRODUCT_MANIFEST.json'))
            self.assertTrue(set(self.public) <= names)
            self.assertFalse(set(private) & names)
            self.assertFalse(set(private) & {item['ruta'] for item in manifest['archivos']})
            self.assertIn('banco-transcripciones/', manifest['exclusiones'])
            self.assertNotIn(b'CORPUS_SINTETICO_PRIVADO',
                             b''.join(archive.read(name) for name in names))

    def test_audit_reports_private_container_without_opening_corpus(self):
        for name in self.private:
            self.write(name, 'CORPUS_SINTETICO_PRIVADO')
        with patch.object(Path, 'read_text', side_effect=AssertionError('no leer corpus')):
            result = audit(self.repo)
        self.assertEqual(result['estado'], 'REVISAR')
        self.assertEqual(result['archivos_texto_inspeccionados'], 0)
        for name in self.private:
            container = str(Path(name).parent)
            self.assertTrue(any(problem.endswith(container) for problem in result['problemas']),
                            container)


if __name__ == '__main__':
    unittest.main()
