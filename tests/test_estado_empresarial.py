"""No confundir plantillas ni continuidad con conocimiento empresarial."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'scripts'))
from crear_instancia import create
from operacion import create_ficha,create_source,save_continuity,summary
from documentos import create_document

class EstadoEmpresarialTest(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.folder=Path(tmp.name)
        self.vault=create('ACME-FICTICIA','Empresa sintética',self.folder/'boveda')
        self.body=self.folder/'borrador.md'
        self.body.write_text('# Laboratorio sintético\n\n## Actividad\n\n'
                             'Diseñamos una forma de representar trabajo con criterios, '
                             'sin afirmar resultados no documentados.\n\n'
                             '## CONTROL\n\nEsta es una prueba ficticia para el producto.\n',encoding='utf8')

    def test_empty_vault_has_infrastructure_not_business(self):
        r=summary(self.vault)
        self.assertEqual(r['capas']['documentos_dx'],0)
        self.assertEqual(r['capas']['entidades_operativas'],0)
        self.assertEqual(r['capas']['fuentes'],0)
        self.assertGreater(r['capas']['infraestructura'],0)
        self.assertEqual(r['documentos_dx']['registros'],[])
        self.assertEqual(r['vistas_bases_instaladas'],16)
        self.assertGreater(r['plantillas_instaladas'],20)
        self.assertEqual(r['total_notas'],r['capas']['infraestructura'])

    def test_sources_and_continuity_are_not_document_or_approved_company(self):
        create_source(self.vault,'F-DEMO-011','Fuente ficticia','urn:synthetic:011','nota',read_status='leida_parcial')
        save_continuity(self.vault,summary='Primera captura sintética.',next_step='Revisar datos de ejemplo')
        r=summary(self.vault)
        self.assertEqual(r['fuentes_resumen']['por_lectura'],{'leida_parcial':1})
        self.assertEqual(r['capas']['fuentes'],1)
        self.assertEqual(r['capas']['trabajo_provisional'],1)
        self.assertEqual(r['documentos_dx']['total'],0)
        self.assertEqual(r['capas']['entidades_operativas'],0)
        self.assertEqual(r['total_notas'],r['capas']['infraestructura']+2)

    def test_D01_draft_is_visible_separately_from_infrastructure(self):
        create_source(self.vault,'F-DEMO-011','Fuente ficticia','urn:synthetic:011','nota')
        create_document(self.vault,'D01','Identidad sintética',self.body,
                        editorial='en_revision',sources=['F-DEMO-011'])
        create_ficha(self.vault,'proyecto','Proyecto ficticio')
        r=summary(self.vault)
        self.assertEqual(r['documentos_dx']['total'],1)
        self.assertEqual(r['documentos_dx']['por_clase'],{'D01':1})
        self.assertEqual(r['documentos_dx']['por_estado_editorial'],{'en_revision':1})
        self.assertEqual(r['documentos_dx']['registros'][0]['ruta'],'10_Conocimiento/Identidad sintética.md')
        self.assertEqual(r['documentos_dx']['registros'][0]['fuentes_referenciadas'],1)
        self.assertEqual(r['capas']['entidades_operativas'],1)
        self.assertEqual(r['por_tipo']['documento'],1)

if __name__=='__main__':unittest.main()
