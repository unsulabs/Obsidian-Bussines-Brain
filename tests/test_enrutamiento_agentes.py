"""Integridad documental del routing; no evalúa decisiones semánticas del agente."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'
NEW_SKILLS = {
    'ce-banco-transcripciones', 'ce-extraer-meetgeek',
    'ce-analizar-transcripcion', 'ce-taxonomia-conocimiento',
    'ce-revisar-antecedentes', 'ce-evaluar-recuperacion',
}


def local_links(path):
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if '://' not in target and not target.startswith('#'):
            yield target.split('#', 1)[0]


def missing_links(base):
    return [(str(path.relative_to(base)), link)
            for path in base.rglob('*.md') for link in local_links(path)
            if not (path.parent / link).is_file()]


class EnrutamientoAgentesTests(unittest.TestCase):
    def test_skill_names_are_unique_and_discoverable(self):
        names = []
        for path in SKILLS.glob('*/SKILL.md'):
            pieces = path.read_text(encoding='utf-8').split('---', 2)
            self.assertEqual(pieces[0], '')
            metadata = yaml.safe_load(pieces[1])
            self.assertEqual(metadata['name'], path.parent.name)
            self.assertIsInstance(metadata['description'], str)
            self.assertTrue(metadata['description'].strip())
            names.append(metadata['name'])
        self.assertEqual(len(names), len(set(names)))
        self.assertTrue(NEW_SKILLS <= set(names))

    def test_new_routes_reachable_from_product_contract(self):
        targets = {(ROOT / target).resolve() for target in local_links(ROOT / 'AGENTS.md')}
        for name in NEW_SKILLS:
            self.assertIn((SKILLS / name / 'SKILL.md').resolve(), targets)
        self.assertFalse(missing_links(SKILLS))

    def test_skill_references_survive_distribution_without_workspace(self):
        with tempfile.TemporaryDirectory() as folder:
            isolated = Path(folder) / 'product' / '.agents' / 'skills'
            shutil.copytree(SKILLS, isolated)
            self.assertEqual(missing_links(isolated), [])
            for path in isolated.rglob('*.md'):
                for link in local_links(path):
                    self.assertTrue((path.parent / link).resolve().is_relative_to(isolated.resolve()))

    def test_reference_checker_rejects_missing_dependency(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / 'SKILL.md').write_text('[contrato](references/missing.md)\n', encoding='utf-8', newline='\n')
            self.assertEqual(missing_links(base), [('SKILL.md', 'references/missing.md')])

    def test_new_skills_have_contract_and_shared_boundary(self):
        # This asserts availability of a contract, not correctness of its reasoning.
        for name in NEW_SKILLS:
            path = SKILLS / name / 'SKILL.md'
            text = path.read_text(encoding='utf-8')
            for field in ('Trigger', 'Inputs', 'Outputs', 'Errores', 'Gate'):
                self.assertIn('**' + field + ':**', text, (name, field))
            self.assertTrue(any(link.endswith('contrato-comun.md') for link in local_links(path)))

    def test_acceptance_obligations_are_scoped_away_from_daily_continuity(self):
        contracts = (
            ('AGENTS.md', '## Two entry points:',
             'Only when accepting an installation, migration or integration change'),
            ('docs/es/agent-contract.md', '## Dos entradas distintas:',
             'Sólo al aceptar una instalación, migración o cambio de integración'),
        )
        for name, heading, acceptance_scope in contracts:
            with self.subTest(contract=name):
                text = (ROOT / name).read_text(encoding='utf-8')
                self.assertIn(heading, text)
                section = text.split(heading, 1)[1].split('\n## ', 1)[0]
                paragraphs = section.split('\n\n')
                continuity = next(p for p in paragraphs if '"continúa mi empresa"' in p)
                self.assertIn('`ce-continuidad`', continuity)
                self.assertIn('`ce-consulta`', continuity)
                self.assertNotIn('ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md', continuity)
                self.assertNotIn('aceptacion_integracion_local.py', continuity)
                obligations = [p for p in paragraphs if 'aceptacion_integracion_local.py' in p
                               or 'ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md' in p]
                self.assertEqual(len(obligations), 1)
                self.assertTrue(obligations[0].startswith(acceptance_scope))

    def test_reception_template_resolves_from_external_bank_in_both_layouts(self):
        # Exercise the documented destination, not a new ingestion implementation.
        text = (SKILLS / 'ce-extraer-meetgeek/references/recepcion-v1.md').read_text(encoding='utf-8')
        template = re.search(r'Único destino de escritura del extractor: `([^`]+)`', text).group(1)
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            profiles = [
                (base / 'workspace/cerebro-empresarial', base / 'workspace/banco-transcripciones'),
                (base / 'exportado/producto', base / 'privado/banco'),
            ]
            for product, bank in profiles:
                with self.subTest(product=product):
                    destination = template
                    for key, value in {'bank': str(bank), 'ejecucion': 'run-1',
                                       'cuenta': 'account-1', 'reunion': 'meeting-1',
                                       'intento': 'attempt-1'}.items():
                        destination = destination.replace('<' + key + '>', value)
                    path = Path(destination)
                    self.assertEqual(path, bank / 'recepcion/meetgeek/run-1/account-1/meeting-1/attempt-1')
                    self.assertFalse(path.is_relative_to(product))
        self.assertIn('rechaza un banco dentro de cualquier árbol Git', text)
        self.assertNotIn('relativo a la raíz de este proyecto', text)


if __name__ == '__main__':
    unittest.main()
