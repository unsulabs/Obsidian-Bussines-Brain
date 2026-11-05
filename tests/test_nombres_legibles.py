"""Identidad técnica estable y rutas humanas en una bóveda sintética."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from crear_instancia import create
from documentos import create_document
from lib_ce import path_by_id, split_frontmatter, visible_filename
from nombres_legibles import plan, apply
from operacion import create_source, save_continuity
from registro_descubrimiento import capture_discovery
from validar_boveda import validate


class NombresLegiblesTest(unittest.TestCase):
    def test_visible_name_requires_subject(self):
        for code in ('D01', 'CAP-ABC123', 'SES-ABC123', 'F-DEMO-01'):
            with self.assertRaisesRegex(ValueError, 'palabras'):
                visible_filename(code)

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.vault = create('FICTICIA-NOMBRES', 'Taller ficticio', self.root/'boveda')
        self.source = create_source(self.vault, 'F-DEMO-01', 'Entrevista de taller',
                                    'urn:synthetic:entrevista', 'conversacion')
        body = self.root/'documento.md'
        body.write_text('# Dirección del taller\n\n## Actividad\n\n'
                        'El taller ficticio registra necesidades y comprueba las decisiones '
                        'antes de operar, usando la entrevista como fuente de trabajo.\n')
        self.document = create_document(self.vault, 'D01', 'Dirección del taller', body,
                                        sources=['F-DEMO-01'])
        capture = self.root/'captura.md'
        capture.write_text('El dueño dijo que el horario era lunes; luego corrigió a martes. '
                           'Conservar la corrección como fuente primaria.', encoding='utf8')
        self.capture = capture_discovery(self.vault, 'Corrección del horario', capture,
                                         sources=['F-DEMO-01'])
        self.continuity = save_continuity(self.vault,
            summary='Corregir horario según la declaración posterior del dueño.',
            next_step='Releer la fuente antes de proponer una decisión.')
        self.spec = self.root/'nombres.json'
        self.spec.write_text(json.dumps({'notas':[
            {'id':'D01','nombre':'Cómo funciona el taller'},
            {'id':self.capture['id'],'nombre':'Corrección del horario del taller'},
            {'id':'F-DEMO-01','nombre':'Entrevista sobre la operación del taller'},
            {'id':self.continuity['id'],'nombre':'2026 - Corrección del horario'},
        ]}),encoding='utf8')

    def test_plan_apply_preserves_ids_content_and_links(self):
        initial = {k:Path(v['ruta']).read_bytes() for k,v in
                   [('document',self.document),('source',self.source),
                    ('capture',self.capture),('continuity',self.continuity)]}
        proposal = plan(self.vault,self.spec)
        self.assertEqual(proposal['renombradas'],4)
        result = apply(self.vault,self.spec,self.root/'respaldo',proposal['sha_plan'])
        self.assertEqual(result['validacion'],'PASS')
        self.assertEqual(validate(self.vault)['errores'],[])
        for key,nid in [('document','D01'),('source','F-DEMO-01'),
                        ('capture',self.capture['id']),('continuity',self.continuity['id'])]:
            p=path_by_id(self.vault,nid)
            self.assertIsNotNone(p)
            self.assertNotIn(nid,p.name)
            fm,body=split_frontmatter(p.read_text())
            self.assertEqual(fm['id'],nid)
            self.assertTrue(body.strip())
            old_fm,old_body=split_frontmatter(initial[key].decode())
            self.assertEqual(old_fm['id'],fm['id'])
            self.assertEqual(old_body,body)
        doc=path_by_id(self.vault,'D01').read_text()
        self.assertIn('[[50_Fuentes/Entrevista sobre la operación del taller]]',doc)
        self.assertTrue((self.root/'respaldo'/'manifest.json').is_file())

    def test_collision_and_stale_plan_do_not_write(self):
        another = self.root/'otra.md'
        another.write_text('Segundo episodio sintético para probar una colisión de títulos.')
        second = capture_discovery(self.vault,'Otra captura',another)
        rows=json.loads(self.spec.read_text())
        rows['notas'].append({'id':second['id'],
                              'nombre':'Corrección del horario del taller'})
        self.spec.write_text(json.dumps(rows))
        with self.assertRaisesRegex(ValueError,'Colisión'):
            plan(self.vault,self.spec)
        rows['notas'][-1]['nombre']='Segunda captura distinta'
        self.spec.write_text(json.dumps(rows))
        before=path_by_id(self.vault,'D01').read_bytes()
        with self.assertRaisesRegex(ValueError,'obsoleto'):
            apply(self.vault,self.spec,self.root/'respaldo','0'*64)
        self.assertEqual(before,path_by_id(self.vault,'D01').read_bytes())
        self.assertFalse((self.root/'respaldo').exists())

    def test_swap_of_existing_names_blocks_without_writing(self):
        second_input = self.root/'otra.md'
        second_input.write_text('Segunda captura ficticia para probar intercambio de nombres.', encoding='utf8')
        second = capture_discovery(self.vault, 'Segunda captura', second_input)
        first_path = Path(self.capture['ruta'])
        second_path = Path(second['ruta'])
        first_bytes, second_bytes = first_path.read_bytes(), second_path.read_bytes()
        spec = self.root/'intercambio.json'
        spec.write_text(json.dumps({'notas':[
            {'id': self.capture['id'], 'nombre': second_path.stem},
            {'id': second['id'], 'nombre': first_path.stem},
        ]}), encoding='utf8')
        with self.assertRaisesRegex(ValueError, 'Destino ocupado'):
            plan(self.vault, spec)
        self.assertEqual(first_path.read_bytes(), first_bytes)
        self.assertEqual(second_path.read_bytes(), second_bytes)
        self.assertEqual(validate(self.vault)['errores'], [])

    def test_broken_link_blocks_plan(self):
        p=Path(self.capture['ruta'])
        p.write_text(p.read_text()+'\n[[Nota inexistente]]\n')
        with self.assertRaisesRegex(ValueError,'Bóveda con errores previos'):
            plan(self.vault,self.spec)

    def test_markdown_link_to_old_path_blocks_plan(self):
        p=Path(self.capture['ruta'])
        old=Path(self.document['ruta']).relative_to(self.vault).as_posix()
        p.write_text(p.read_text()+f'\n[Documento]({old})\n')
        with self.assertRaisesRegex(ValueError,'Enlace Markdown a ruta antigua'):
            plan(self.vault,self.spec)


if __name__ == '__main__': unittest.main()
