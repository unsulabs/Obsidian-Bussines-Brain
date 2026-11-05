"""No confundir recuperación textual de bloques con autoridad o semántica."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
from crear_instancia import create
from documentos import create_document
from operacion import create_source, create_ficha
from lib_ce import make_note, split_frontmatter
from consulta_contextual import consulta


class ContextualQueryTest(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.work=Path(t.name)
        self.vault=create("EMP-QUERY-TEST","Empresa sintética",self.work/"boveda")
        create_source(self.vault,"F-SINTET-01","Fuente ficticia","urn:synthetic:case","nota")
        self.body=self.work/"borrador.md"
        self.body.write_text(
            "# Documentación de prueba\n\n"
            "## 01 Actividad\n\n<!-- kb:id=D01-B001 -->\n"
            "El proceso ficticio registra asignaciones y conserva la decisión "
            "de quién puede autorizar una excepción operativa.\n\n"
            "## 02 Calidad\n\n<!-- kb:id=D01-B002 -->\n"
            "Los responsables comprueban la entrega y su documentación "
            "sin confundir pruebas técnicas con aprobación comercial.\n\n"
            "## CONTROL — fuente y límites\n\n"
            "SOLO_CONTROL_TEST: este texto no debe confundirse con conocimiento empresarial.\n",
            encoding="utf8")
        result=create_document(self.vault,"D01","Modelo ficticio",self.body,
                               editorial="en_revision",sources=["F-SINTET-01"])
        self.doc=Path(result["ruta"])

    def test_match_block_with_source_and_provisional_status(self):
        r=consulta(self.vault,"asignaciones",fecha="2026-10-28")
        self.assertEqual(r["total_coincidencias"],1)
        self.assertFalse(r["respuesta_semantica_generada"])
        row=r["candidatos"][0]
        self.assertEqual(row["bloque_id"],"D01-B001")
        self.assertEqual(row["estado_editorial"],"en_revision")
        self.assertEqual(row["fuentes_nivel_documento"],["[[50_Fuentes/Fuente ficticia]]"])
        self.assertEqual(row["fuente_demuestra_bloque"],"NO_COMPROBADO")

    def test_control_material_is_excluded_from_search(self):
        r=consulta(self.vault,"SOLO_CONTROL_TEST")
        self.assertEqual(r["total_coincidencias"],0)
        self.assertFalse(r["candidatos"])

    def test_document_without_vnext_markers_remains_searchable_as_provisional_sections(self):
        content=self.work/"proceso_sin_bloques.md"
        content.write_text(
            "# Reparaciones de prueba\n\n"
            "## Urgencias\n\nLa dueña decide si una urgencia adelanta el turno.\n\n"
            "## Mantenimiento\n\nNo hay precio ni acuerdo de mantenimiento mensual.\n\n"
            "## CONTROL\n\nSECRETO_CONTROL_NO_BUSCAR.\n",encoding="utf8")
        created=create_document(self.vault,"X02","Reparaciones de prueba",content,
                                doc_id="X02-REPARACIONES-TEST",editorial="en_revision",
                                sources=["F-SINTET-01"])
        doc=Path(created["ruta"])
        original=doc.read_bytes()
        result=consulta(self.vault,"urgencia adelantar",orientar=True)
        matching=[c for c in result["candidatos"] if c["doc_id"]=="X02-REPARACIONES-TEST"]
        self.assertTrue(matching)
        self.assertEqual(matching[0]["tipo_fragmento"],"seccion_derivada_sin_id_estable")
        self.assertEqual(matching[0]["estado_editorial"],"en_revision")
        self.assertFalse(consulta(self.vault,"SECRETO_CONTROL_NO_BUSCAR",orientar=True)["candidatos"])
        self.assertEqual(doc.read_bytes(),original)

    def test_does_not_infer_authority_from_commercial_word(self):
        r=consulta(self.vault,"aprobación comercial",tema="precio",ambito="oferta:inexistente")
        self.assertEqual(r["total_coincidencias"],1)
        self.assertEqual(r["autoridad_contextual"]["estado"],"sin_autoridad_explicita")
        self.assertFalse(r["respuesta_semantica_generada"])

    def test_date_scope_excludes_expired_and_future_docs(self):
        meta,body=split_frontmatter(self.doc.read_text())
        meta["valid_from"]="2026-10-10"
        meta["valid_to"]="2026-10-30"
        self.doc.write_text(make_note(meta,body))
        early=consulta(self.vault,"asignaciones",fecha="2026-10-09")
        inside=consulta(self.vault,"asignaciones",fecha="2026-10-28")
        late=consulta(self.vault,"asignaciones",fecha="2026-10-31")
        self.assertEqual(early["total_coincidencias"],0)
        self.assertEqual(inside["total_coincidencias"],1)
        self.assertEqual(late["total_coincidencias"],0)
        self.assertEqual(early["documentos_fuera_vigencia_explicita"],1)

    def test_restricted_document_is_not_returned(self):
        meta,body=split_frontmatter(self.doc.read_text())
        meta["sensibilidad"]="restringido"
        self.doc.write_text(make_note(meta,body))
        r=consulta(self.vault,"asignaciones")
        self.assertEqual(r["total_coincidencias"],0)

    def test_typed_offer_is_retrieved_without_promoting_historical_price(self):
        content=self.work/"oferta.md"
        content.write_text(
            "# Oferta imaginaria\n\n## Antecedente\n\n"
            "Se mencionó un precio histórico de 125 pesos para un piloto; "
            "la tarifa actual no está decidida.\n\n"
            "## CONTROL — fuentes\n\n"
            "SOLO_CONTROL_OFERTA: este localizador no es texto comercial.\n",
            encoding="utf8")
        item=create_ficha(self.vault,"oferta","Oferta imaginaria",
                          content_file=content,sources=["F-SINTET-01"])
        row=consulta(self.vault,"precio histórico")["candidatos"][0]
        self.assertEqual(row["doc_id"],item["id"])
        self.assertEqual(row["tipo_nota"],"oferta")
        self.assertNotEqual(row["estado_editorial"],"aprobado")
        self.assertEqual(row["vigencia_declarada"],"sin_verificar")
        self.assertFalse(consulta(self.vault,"SOLO_CONTROL_OFERTA")["candidatos"])
        self.assertFalse(consulta(self.vault,"precio histórico")["respuesta_semantica_generada"])

    def test_cli_structured_without_claiming_answer(self):
        p=subprocess.run([
            sys.executable,str(ROOT/"scripts"/"cerebro.py"),"consulta-contextual",
            "--vault",str(self.vault),"--texto","asignaciones","--fecha","2026-10-28"
        ],capture_output=True,text=True,check=True)
        d=json.loads(p.stdout)
        self.assertEqual(d["modo"],"busqueda_literal_de_bloques_con_contexto")
        self.assertEqual(d["total_coincidencias"],1)

    def test_natural_request_orients_without_promoting_a_result(self):
        question="¿Quién decide cómo comenzar con una empresa que necesita asignar trabajo y resolver excepciones?"
        self.assertEqual(consulta(self.vault,question)["total_coincidencias"],0)
        r=consulta(self.vault,question,orientar=True)
        self.assertEqual(r["modo"],"orientacion_lexica_de_bloques")
        self.assertGreater(r["total_coincidencias"],0)
        self.assertIn("D01-B001",[x["bloque_id"] for x in r["candidatos"]])
        self.assertTrue(all("SOLO_CONTROL_TEST" not in x["extracto_literal"] for x in r["candidatos"]))
        self.assertTrue(all(x["fuente_demuestra_bloque"]=="NO_COMPROBADO" for x in r["candidatos"]))
        self.assertFalse(r["respuesta_semantica_generada"])

    def test_orientation_keeps_scope_and_permissions(self):
        meta,body=split_frontmatter(self.doc.read_text())
        meta["valid_from"]="2026-10-10"
        meta["valid_to"]="2026-10-30"
        self.doc.write_text(make_note(meta,body))
        q="¿Quién autoriza una excepción en las asignaciones?"
        self.assertEqual(consulta(self.vault,q,orientar=True,fecha="2026-10-09")["total_coincidencias"],0)
        self.assertGreater(consulta(self.vault,q,orientar=True,fecha="2026-10-28")["total_coincidencias"],0)
        meta["sensibilidad"]="restringido"
        self.doc.write_text(make_note(meta,body))
        self.assertEqual(consulta(self.vault,q,orientar=True,fecha="2026-10-28")["total_coincidencias"],0)

    def test_cli_orients_a_question_without_claiming_semantics(self):
        p=subprocess.run([
            sys.executable,str(ROOT/"scripts"/"cerebro.py"),"consulta-contextual",
            "--vault",str(self.vault),"--texto","¿Cómo resolver asignaciones y excepciones?",
            "--orientar"
        ],capture_output=True,text=True,check=True)
        d=json.loads(p.stdout)
        self.assertEqual(d["modo"],"orientacion_lexica_de_bloques")
        self.assertFalse(d["respuesta_semantica_generada"])
        self.assertTrue(d["candidatos"])


if __name__=="__main__":
    unittest.main()
