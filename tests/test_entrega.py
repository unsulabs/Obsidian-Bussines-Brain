from pathlib import Path
import json
import sys
import unittest
import yaml

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'scripts'))
from validar_boveda import validate
from auditar_paquete import audit

class EntregaTest(unittest.TestCase):
    def test_example_vault_is_synthetic_and_valid(self):
        v=ROOT/'ejemplos'/'boveda_demo'/'Brisa_Modular'
        self.assertTrue(v.is_dir())
        self.assertEqual(validate(v)['errores'],[])
        self.assertTrue((v/'00_Mapas/Mapa_de_relaciones.canvas').is_file())
        self.assertEqual(yaml.safe_load((v/'90_Sistema/config_empresa.yaml').read_text())['company_id'],'BRISA-SINTETICA')
        manifest=json.loads((v/'90_Sistema/Traspasos/BRISA-SINTETICA/manifest.json').read_text())
        self.assertTrue(manifest['company']['synthetic'])

    def test_skills_triggers_and_content(self):
        files=list((ROOT/'.agents/skills').glob('*/SKILL.md'))
        self.assertGreaterEqual(len(files),11)
        self.assertTrue((ROOT/'.agents/skills/ce-arquitectura-conocimiento/SKILL.md').is_file())
        for p in files:
            s=p.read_text(encoding='utf8')
            self.assertTrue(s.startswith('---\n'))
            fm=yaml.safe_load(s.split('---',2)[1])
            self.assertTrue(fm['name'].startswith('ce-'))
            self.assertGreater(len(fm['description']),45)
            self.assertTrue(len(s)>600)

    def test_assets_are_not_disconnected_references(self):
        self.assertTrue((ROOT/'metodologia/vNext-1.0R/Biblioteca_Prompts_vNext_1_0R.md').stat().st_size>100000)
        self.assertTrue((ROOT/'metodologia/vNext-1.0R/Catalogo_Documentos_Canonicos_vNext_1_0R.md').stat().st_size>50000)
        self.assertTrue((ROOT/'investigacion/videos-2026-10/hallazgos_video.json').stat().st_size>1000)
        self.assertTrue((ROOT/'investigacion/diseno-D0.1/decisiones_abiertas.csv').stat().st_size>300)
        self.assertTrue((ROOT/'recursos/registro_plugins.json').is_file())

    def test_product_audit_excludes_authorized_private_material(self):
        out=audit(ROOT)
        self.assertEqual(out['problemas'],[])
        self.assertEqual(out['material_privado_excluido'], (ROOT/'material_privado').exists())

if __name__=='__main__':unittest.main()
