"""Compatibilidad del validador general con enlaces a vistas Bases nativas."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from lib_ce import make_note, target_index, resolve_link
from validar_boveda import validate


class BaseLinksTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.vault = Path(self.tmp.name).resolve()

    def write(self, relative, text):
        path = self.vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8', newline='\n')
        return path

    def note(self, body):
        self.write('Inicio.md', make_note({'id': 'HOME', 'tipo': 'inicio'}, body))

    def base(self, path):
        return self.write(path, 'views:\n  - type: table\n    name: Vista propia\n')

    def test_exact_path_alias_embed_and_unique_basename(self):
        self.base('90_Sistema/Vistas/Transcripciones/Transcripciones.base')
        self.note('[[90_Sistema/Vistas/Transcripciones/Transcripciones.base|Ver]]\n'
                  '![[Transcripciones.base]]\n')
        before = {p.relative_to(self.vault): p.read_bytes() for p in self.vault.rglob('*') if p.is_file()}
        result = validate(self.vault)
        self.assertEqual(result['errores'], [])
        self.assertEqual(result['notas'], 1)
        self.assertEqual(result['ids'], 1)
        self.assertEqual(before, {p.relative_to(self.vault): p.read_bytes() for p in self.vault.rglob('*') if p.is_file()})

    def test_ambiguous_basename_fails_but_explicit_path_resolves(self):
        first = self.base('uno/Compartida.base')
        self.base('dos/Compartida.base')
        index = target_index(self.vault, include_assets=True)
        self.assertIsNone(resolve_link('Compartida.base', *index))
        self.assertEqual(resolve_link('uno/Compartida.base', *index), first)
        self.note('[[Compartida.base]] [[uno/Compartida.base]]')
        self.assertEqual(len(validate(self.vault)['errores']), 1)

    def test_missing_base_and_wrong_qualified_path_do_not_resolve(self):
        self.base('Vistas/Existe.base')
        self.note('[[Falta.base]] [[Otro/Existe.base]] [[Nota ausente]]')
        errors = validate(self.vault)['errores']
        self.assertEqual(len(errors), 3)
        self.assertTrue(any('Falta.base' in e for e in errors))
        self.assertTrue(any('Otro/Existe.base' in e for e in errors))

    def test_base_and_markdown_same_stem_remain_distinct(self):
        base = self.base('Vistas/Clientes.base')
        md = self.write('Clientes.md', make_note({'id': 'CLIENTES'}, '# Clientes'))
        index = target_index(self.vault, include_assets=True)
        self.assertEqual(resolve_link('Clientes.base', *index), base)
        self.assertEqual(resolve_link('Clientes', *index), md)
        self.note('[[Clientes]] [[Clientes.md]] [[Clientes.base]]')
        self.assertEqual(validate(self.vault)['errores'], [])

    def test_other_validation_errors_and_symlink_are_not_hidden(self):
        self.base('Vistas/Real.base')
        self.write('Duplicada.md', make_note({'id': 'HOME'}, '# Duplicada'))
        (self.vault / 'Alias.base').symlink_to(self.vault / 'Vistas/Real.base')
        self.note('[[Vistas/Real.base]] [[Alias.base]]')
        errors = validate(self.vault)['errores']
        self.assertTrue(any('ID duplicado' in e for e in errors))
        self.assertTrue(any('Alias.base' in e for e in errors))

    def test_markdown_named_like_base_does_not_hide_missing_asset(self):
        self.write('Clientes.base.md', make_note({'id': 'ODD'}, '# Nota Markdown'))
        self.note('[[Clientes.base]]')
        self.assertEqual(len(validate(self.vault)['errores']), 1)
        self.base('Vistas/Clientes.base')
        self.assertEqual(validate(self.vault)['errores'], [])

    def test_explicit_literal_base_markdown_and_graph_remain_notes_only(self):
        from exportar_grafo import graph
        self.write('90_Sistema/config_empresa.yaml', 'company_id: SYNTHETIC\n')
        literal = self.write('a/Odd.base.md', make_note({'id': 'LITERAL'}, '# Literal'))
        self.base('a/Odd.base')
        self.note('[[a/Odd.base]] [[a/Odd.base.md]]')
        self.assertEqual(validate(self.vault)['errores'], [])
        self.assertEqual(resolve_link('a/Odd.base.md', *target_index(self.vault, include_assets=True)), literal)
        self.assertIsNone(resolve_link('a/Odd.base', *target_index(self.vault)))
        exported = graph(self.vault)
        self.assertEqual({n['id'] for n in exported['nodos']}, {'HOME', 'LITERAL'})
        self.assertEqual(len(exported['aristas']), 1)
        self.assertEqual(exported['aristas'][0]['destino'], 'LITERAL')
        script = Path(__file__).resolve().parents[1] / 'scripts' / 'cerebro.py'
        cli = subprocess.run([sys.executable, str(script), 'grafo', '--vault', str(self.vault)],
                             capture_output=True, text=True)
        self.assertEqual(cli.returncode, 0, cli.stdout + cli.stderr)
        self.assertEqual(json.loads((self.vault / '90_Sistema/grafo.json').read_text(encoding='utf-8'))['nodos'], exported['nodos'])

    def test_rename_preserves_explicit_markdown_type_and_base_link(self):
        from nombres_legibles import _rewrite_wiki
        old = self.write('a/Odd.base.md', make_note({'id': 'LITERAL'}, '# Literal'))
        self.base('a/Odd.base')
        new = self.vault / 'a' / 'Título humano.md'
        text, count = _rewrite_wiki('[[a/Odd.base]] [[a/Odd.base.md|Nota]]', self.vault,
                                    {old: new}, *target_index(self.vault))
        self.assertEqual(count, 1)
        self.assertEqual(text, '[[a/Odd.base]] [[a/Título humano.md|Nota]]')

    def test_general_cli_validar_success_then_missing_failure(self):
        self.base('90_Sistema/Vistas/Transcripciones/Transcripciones.base')
        self.note('[[90_Sistema/Vistas/Transcripciones/Transcripciones.base]]')
        script = Path(__file__).resolve().parents[1] / 'scripts' / 'cerebro.py'
        command = [sys.executable, str(script), 'validar', '--vault', str(self.vault)]
        good = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        self.note('[[No existe.base]]')
        bad = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn('No existe.base', bad.stdout + bad.stderr)


if __name__ == '__main__':
    unittest.main()
