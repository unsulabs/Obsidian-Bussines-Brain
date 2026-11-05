"""Behavioral failures in an isolated bilingual documentation tree."""
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from check_docs import check


class CheckDocsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for lang in ('en', 'es'):
            path = self.root / 'docs' / lang
            path.mkdir(parents=True)
            (path / 'guide.md').write_text('# Guide\n\n## Acción útil\n\n## Repeat\n\n## Repeat\n', encoding='utf-8', newline='\n')
        (self.root / 'docs/documentation-map.json').write_text(json.dumps({
            'version': 1, 'primary_language': 'en',
            'pairs': [{'id': 'guide', 'en': 'docs/en/guide.md', 'es': 'docs/es/guide.md'}]}), encoding='utf-8', newline='\n')

    def test_valid_cross_language_anchor_and_fenced_example(self):
        with (self.root / 'docs/en/guide.md').open('a', encoding='utf-8', newline='\n') as out:
            out.write('\n[Spanish](../es/guide.md#acción-útil)\n[Repeat](#repeat-1)\n'
                      '\n```markdown\n[Example](does-not-exist.md)\n```\n')
        self.assertEqual(check(self.root), [])

    def test_missing_translation_fails(self):
        (self.root / 'docs/es/guide.md').unlink()
        self.assertTrue(any('missing or unsafe es' in e for e in check(self.root)))
        run = subprocess.run([sys.executable, str(Path(__file__).resolve().parent.parent / 'scripts/check_docs.py'),
                              '--root', str(self.root)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 1)
        self.assertIn('FAIL', run.stdout)

    def test_root_entry_language_roles_cannot_be_swapped(self):
        path = self.root / 'docs/documentation-map.json'
        inventory = json.loads(path.read_text(encoding='utf-8'))
        for en, es in [('README.md', 'README.es.md'),
                       ('START_HERE.md', 'EMPIEZA_AQUI.md'),
                       ('GET_STARTED_WITH_CODEX.md', 'PROMPT_INICIO_CODEX.md'),
                       ('CONTINUE_WITH_CODEX.md', 'PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md')]:
            with self.subTest(en=en):
                (self.root / en).write_text('# English', encoding='utf-8', newline='\n')
                (self.root / es).write_text('# Español', encoding='utf-8', newline='\n')
                inventory['pairs'].append({'id': 'entry', 'en': en, 'es': es})
                path.write_text(json.dumps(inventory), encoding='utf-8', newline='\n')
                self.assertEqual(check(self.root), [])
                inventory['pairs'][-1].update(en=es, es=en)
                path.write_text(json.dumps(inventory), encoding='utf-8', newline='\n')
                errors = check(self.root)
                self.assertIn(f'wrong locale path: {en}', errors)
                self.assertIn(f'wrong locale path: {es}', errors)
                inventory['pairs'].pop()

    def test_duplicate_path_in_conflicting_roles_fails(self):
        path = self.root / 'docs/documentation-map.json'
        inventory = json.loads(path.read_text(encoding='utf-8'))
        inventory['pairs'].append({'id': 'other', 'en': 'docs/en/guide.md', 'es': 'docs/en/guide.md'})
        path.write_text(json.dumps(inventory), encoding='utf-8', newline='\n')
        errors = check(self.root)
        self.assertIn('duplicate path: docs/en/guide.md', errors)
        self.assertIn('wrong locale path: docs/en/guide.md', errors)

    def test_unregistered_translation_fails(self):
        (self.root / 'docs/en/extra.md').write_text('# Extra', encoding='utf-8', newline='\n')
        self.assertTrue(any('unpaired document' in e for e in check(self.root)))

    def test_broken_link_fails(self):
        (self.root / 'docs/en/guide.md').write_text('[Missing](missing.md)', encoding='utf-8', newline='\n')
        self.assertTrue(any('broken link' in e for e in check(self.root)))

    def test_broken_anchor_fails(self):
        (self.root / 'docs/en/guide.md').write_text('[Missing](../es/guide.md#absent)', encoding='utf-8', newline='\n')
        self.assertTrue(any('broken anchor' in e for e in check(self.root)))

    def test_broken_reference_link_fails(self):
        (self.root / 'docs/en/guide.md').write_text('[Missing][ref]\n\n[ref]: missing.md', encoding='utf-8', newline='\n')
        self.assertTrue(any('broken link' in e for e in check(self.root)))

    def test_escape_fails(self):
        (self.root / 'docs/en/guide.md').write_text('[Outside](../../../outside.md)', encoding='utf-8', newline='\n')
        self.assertTrue(any('escapes repository' in e for e in check(self.root)))

    def test_missing_preserved_source_fails(self):
        path = self.root / 'docs/documentation-map.json'
        inventory = json.loads(path.read_text(encoding='utf-8'))
        inventory['preserved_documents'] = [{'path': 'docs/missing.md', 'topic_guide': 'docs/en/guide.md'}]
        path.write_text(json.dumps(inventory), encoding='utf-8', newline='\n')
        self.assertTrue(any('source reference path' in e for e in check(self.root)))


if __name__ == '__main__':
    unittest.main()
