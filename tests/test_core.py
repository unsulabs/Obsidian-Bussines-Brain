"""Pruebas técnicas del kit con la empresa ficticia del paquete vNext."""
from __future__ import annotations
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / 'scripts'))
from crear_instancia import create
from importar_traspaso import import_package
from validar_boveda import validate
from exportar_grafo import graph

MANIFEST = REPO / 'ejemplos' / 'traspaso_sintetico' / 'manifest.json'


class CoreTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name) / 'brisa'
        create('BRISA-SINTETICA', 'Brisa Modular FICTICIA', self.vault)

    def test_vault_template_validates(self):
        result = validate(self.vault)
        self.assertEqual(result['errores'], [])
        self.assertEqual(result['traspasos'], 0)

    def test_importer_rejects_modified_map_even_with_old_phrase(self):
        from importar_traspaso import _intact_relation_placeholder, LEGACY_RELATION_PLACEHOLDER
        template=(REPO/'plantilla_boveda/00_Mapas/Relaciones_de_conocimiento.md').read_text(encoding='utf8')
        self.assertTrue(_intact_relation_placeholder(template))
        self.assertTrue(_intact_relation_placeholder(LEGACY_RELATION_PLACEHOLDER))
        self.assertFalse(_intact_relation_placeholder(template+'\n# Cambio manual importante\n'))
        self.assertFalse(_intact_relation_placeholder(LEGACY_RELATION_PLACEHOLDER+'\n# Cambio manual\n'))

    def test_import_and_graph(self):
        stats = import_package(MANIFEST, self.vault)
        self.assertEqual(stats['documentos'], 4)
        self.assertEqual(stats['bloques'], 5)
        self.assertEqual(stats['pruebas_semanticas_pendientes'], 3)
        result = validate(self.vault)
        self.assertEqual(result['errores'], [])
        self.assertEqual(result['traspasos'], 1)
        self.assertEqual(result['bloques'], 5)
        canvas = json.loads((self.vault / '00_Mapas' / 'Mapa_de_relaciones.canvas').read_text())
        self.assertEqual(len(canvas['nodes']), 6)
        self.assertGreaterEqual(len(canvas['edges']), 4)
        g = graph(self.vault)
        preds = {x['predicado'] for x in g['aristas'] if x['capa'] == 'contrato'}
        self.assertIn('refiere_oferta', preds)
        self.assertIn('sustentado_por', preds)
        self.assertIn('pertenece_a', preds)
        self.assertIn('autoridad_en_precio_modulo_estandar', preds)
        self.assertIn('no_ejecutada', (self.vault / '90_Sistema' / 'Pruebas_de_recuperacion.md').read_text())

    def test_non_destructive(self):
        import_package(MANIFEST, self.vault)
        with self.assertRaises(FileExistsError):
            import_package(MANIFEST, self.vault)
        with self.assertRaises(FileExistsError):
            create('BRISA-SINTETICA', 'Ficticia', self.vault)

    def test_broken_link_detected(self):
        note = self.vault / '00_Mapas' / 'Mapa_de_empresa.md'
        note.write_text(note.read_text()+'\n[[No_existe_este_documento]]\n')
        self.assertTrue(any('enlace roto' in e for e in validate(self.vault)['errores']))

    def test_company_isolation(self):
        with self.assertRaises(ValueError):
            create('mal id', 'Nombre', Path(self.temp.name) / 'invalida')
        other = Path(self.temp.name) / 'otra'
        create('OTRA-SINTETICA', 'Otra', other)
        with self.assertRaises(ValueError): import_package(MANIFEST, other)

    def test_contract_rejects_tampered_document(self):
        # El paquete original queda intacto; se copia y cambia un archivo de prueba.
        import shutil
        base = Path(self.temp.name) / 'tampered'
        shutil.copytree(MANIFEST.parent, base)
        (base/'Ejemplo_sintetico'/'D03_Portafolio.md').write_text('alterado')
        with self.assertRaises(ValueError) as ctx: import_package(base/'manifest.json', self.vault)
        self.assertIn('HASH document', str(ctx.exception))
        self.assertEqual(list((self.vault/'10_Conocimiento').glob('*.md')), [])

    def test_sensitive_material_is_refused(self):
        import shutil
        base = Path(self.temp.name) / 'sensitive'
        shutil.copytree(MANIFEST.parent, base)
        manifest = base / 'manifest.json'
        obj = json.loads(manifest.read_text())
        obj['sources'][0]['access'] = 'restringido'
        manifest.write_text(json.dumps(obj, ensure_ascii=False))
        with self.assertRaises(ValueError) as ctx:
            import_package(manifest, self.vault)
        self.assertIn('no tiene ACL', str(ctx.exception))
        self.assertEqual(list((self.vault / '10_Conocimiento').glob('*.md')), [])

    def test_name_with_apostrophe_yaml_safe(self):
        other = Path(self.temp.name) / 'name'
        create('ACME-TEST', "Compañía O'Connor", other)
        from lib_ce import split_frontmatter
        import yaml
        company = yaml.safe_load((other / '90_Sistema' / 'config_empresa.yaml').read_text())
        self.assertEqual(company['company_name'], "Compañía O'Connor")
        self.assertEqual(validate(other)['errores'], [])


if __name__ == '__main__': unittest.main()
