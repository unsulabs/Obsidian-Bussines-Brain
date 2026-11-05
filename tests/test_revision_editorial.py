"""La evaluación G1–G7 registra revisión sin inferir aprobación."""
from __future__ import annotations
import hashlib
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
from lib_ce import make_note,split_frontmatter
from operacion import create_source
from revision_editorial import registrar_evaluacion,aprobar_documento
from validar_boveda import validate


class EvaluacionDXTest(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root=Path(temp.name)
        self.vault=create("DEMO-EDITORIAL","Empresa ficticia",self.root/"boveda")
        create_source(self.vault,"F-PRUEBA-01","Referencia sintética","urn:synthetic:test","nota")
        self.body=self.root/"contenido_D01.md"
        self.body.write_text(
            "# Dirección de una empresa inventada\n\n"
            "## 01 Actividad\n\n<!-- kb:id=D01-B001 -->\n"
            "El equipo de prueba recopila los trabajos que realiza, distingue"
            " decisiones de registros y utiliza esas distinciones para organizarse.\n\n"
            "## 02 Decisiones\n\n<!-- kb:id=D01-B002 -->\n"
            "La revisión sintética exige explicar quién decide y por qué,"
            " sin simular contratos ni ingresos.\n\n"
            "## CONTROL\n\nEsta demostración no afirma datos de ninguna empresa real.\n",
            encoding="utf8")
        result=create_document(self.vault,"D01","Dirección ficticia",self.body,
                               sources=["F-PRUEBA-01"],editorial="en_revision")
        self.file=Path(result["ruta"])
        self.act=self.root/"evaluacion.json"
        self.backup=self.root/"backups"
        self.set_coverage("suficiente_para_tarea")

    def set_coverage(self,coverage):
        fm,body=split_frontmatter(self.file.read_text(encoding="utf8"))
        fm["cobertura"]=coverage
        self.file.write_text(make_note(fm,body),encoding="utf8")

    def sha(self):
        return hashlib.sha256(self.file.read_bytes()).hexdigest()

    def write_act(self,decision="recomendar_integral",scope=None,gates=None):
        if scope is None:scope=["D01-B001","D01-B002"]
        if gates is None:
            gates={f"G{i}":{"estado":"cumple",
                            "fundamento":f"Se comprobó el aspecto G{i} en la evaluación ficticia."}
                   for i in range(1,8)}
        act={"doc_id":"D01","sha_documento":self.sha(),"decision":decision,
             "revisor":"Responsable ficticio",
             "referencia_decision":"Acta interna sintética con revisión del alcance",
             "alcance_bloques":scope,"gates":gates}
        self.act.write_text(json.dumps(act,ensure_ascii=False),encoding="utf8")
        return act

    def test_gates_create_audit_not_approval(self):
        self.write_act(decision="recomendar_parcial",scope=["D01-B001"])
        original=self.file.read_bytes()
        result=registrar_evaluacion(self.vault,"D01",self.act,expected_sha=self.sha())
        self.assertEqual(result["decision"],"recomendar_parcial")
        self.assertFalse(result["documento_modificado"])
        self.assertEqual(self.file.read_bytes(),original)
        self.assertEqual(validate(self.vault)["errores"],[])
        self.assertTrue(Path(result["ruta"]).is_file())

    def test_partial_coverage_blocks_full_promotion(self):
        self.set_coverage("parcial")
        self.write_act()
        with self.assertRaises(ValueError):
            registrar_evaluacion(self.vault,"D01",self.act,expected_sha=self.sha())
        self.assertFalse((self.vault/"90_Sistema"/"Evaluaciones_DX").exists())

    def test_missing_critical_gate_prevents_recommendation(self):
        g={f"G{i}":{"estado":"cumple","fundamento":"Evaluación ficticia suficientemente argumentada."}
           for i in range(1,8)}
        g["G2"]={"estado":"no_cumple","fundamento":"Falta criterio experto en el ejemplo."}
        self.write_act(gates=g)
        with self.assertRaises(ValueError):
            registrar_evaluacion(self.vault,"D01",self.act,expected_sha=self.sha())
        self.write_act(decision="requiere_cambios",gates=g)
        self.assertEqual(registrar_evaluacion(self.vault,"D01",self.act,
                                             expected_sha=self.sha())["decision"],"requiere_cambios")

    def test_wrong_scope_and_missing_gate_rejected(self):
        self.write_act(scope=["D01-B099"])
        with self.assertRaises(ValueError):
            registrar_evaluacion(self.vault,"D01",self.act,expected_sha=self.sha())
        self.write_act()
        obj=json.loads(self.act.read_text())
        del obj["gates"]["G7"]
        self.act.write_text(json.dumps(obj))
        with self.assertRaises(ValueError):
            registrar_evaluacion(self.vault,"D01",self.act,expected_sha=self.sha())

    def test_promote_only_after_exact_confirmation_with_history(self):
        self.write_act()
        eid=registrar_evaluacion(self.vault,"D01",self.act,
                                 expected_sha=self.sha())["evaluacion_id"]
        before=self.file.read_bytes()
        oldsha=self.sha()
        with self.assertRaises(ValueError):
            aprobar_documento(self.vault,eid,expected_sha=oldsha,
                               responsable="operador sintético",
                               referencia_autorizacion="autorización literal ficticia",
                               backup_dir=self.backup,confirmacion="SI")
        self.assertEqual(self.file.read_bytes(),before)
        result=aprobar_documento(self.vault,eid,expected_sha=oldsha,
                                responsable="operador sintético",
                                referencia_autorizacion="autorización literal ficticia",
                                backup_dir=self.backup,
                                confirmacion="APROBAR D01 "+oldsha[:12])
        fm,body=split_frontmatter(self.file.read_text(encoding="utf8"))
        self.assertEqual(fm["estado_editorial"],"aprobado")
        self.assertEqual(fm["revision"],"0.2")
        self.assertEqual(fm["revisado_por"],"Responsable ficticio")
        self.assertEqual(fm["vigencia"],"sin_verificar")
        self.assertTrue(result["aprobacion_editorial"])
        self.assertFalse(result["aprobacion_semantica_automatica"])
        self.assertEqual((Path(result["respaldo_externo"])/"anterior.snapshot").read_bytes(),before)
        self.assertEqual(validate(self.vault)["errores"],[])

    def test_stale_sha_blocks_promotion_without_writing(self):
        self.write_act()
        eid=registrar_evaluacion(self.vault,"D01",self.act,
                                 expected_sha=self.sha())["evaluacion_id"]
        oldsha=self.sha()
        fm,body=split_frontmatter(self.file.read_text())
        fm["fecha_corte"]="2026-10-27"
        self.file.write_text(make_note(fm,body))
        before=self.file.read_bytes()
        with self.assertRaises(ValueError):
            aprobar_documento(self.vault,eid,expected_sha=oldsha,
                               responsable="operador sintético",
                               referencia_autorizacion="autorización literal ficticia",
                               backup_dir=self.backup,
                               confirmacion="APROBAR D01 "+oldsha[:12])
        self.assertEqual(self.file.read_bytes(),before)

    def test_cli_evaluate_synthetic(self):
        self.write_act(decision="recomendar_parcial",scope=["D01-B001"])
        result=subprocess.run(
            [sys.executable,str(ROOT/"scripts"/"cerebro.py"),"evaluar-dx",
             "--vault",str(self.vault),"--doc-id","D01",
             "--acta",str(self.act),"--sha-actual",self.sha()],
            capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout)["doc_id"],"D01")


if __name__=="__main__":
    unittest.main()
