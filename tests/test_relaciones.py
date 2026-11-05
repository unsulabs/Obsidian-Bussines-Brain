"""Propuestas de relaciones y ratificaciones explícitas con fuente y ámbito."""
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
from operacion import create_source
from relaciones import propose,query,confirm
from validar_boveda import validate
from exportar_grafo import graph


class RelacionesTest(unittest.TestCase):
    def setUp(self):
        folder=tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root=Path(folder.name)
        self.vault=create("EMP-REL-SINTETICA","Prueba ficticia",self.root/"boveda")
        create_source(self.vault,"F-DEMORL-01","Original sintético","urn:synthetic:regla","nota")
        self.body=self.root/"borrador_d01.md"
        self.body.write_text(
            "# Empresa ficticia\n\n## Actividades\n\n<!-- kb:id=D01-B001 -->\n"
            "El proceso de ejemplo organiza solicitudes internas y distingue el "
            "trabajo realizado de los compromisos aprobados.\n\n"
            "## CONTROL\n\nDocumento sintético para test de relaciones.\n",encoding="utf8")
        create_document(self.vault,"D01","Modelo de trabajo",self.body,
                        sources=["F-DEMORL-01"],editorial="en_revision")
        self.kw={"fuentes":["F-DEMORL-01"],"ambito":"documentación de un proceso ficticio",
                 "motivo":"La fuente se propone como apoyo a la explicación del ejemplo sintético."}

    def make(self):
        return propose(self.vault,"D01","F-DEMORL-01","sustentado_por",**self.kw)

    def test_proposal_does_not_imply_validity(self):
        record=self.make()
        self.assertEqual(record["estado"],"propuesta")
        self.assertFalse(record["validada"])
        self.assertEqual(validate(self.vault)["errores"],[])
        rows=query(self.vault)["relaciones"]
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]["estado_efectivo"],"propuesta")
        g=graph(self.vault)
        self.assertTrue(any(edge["capa"]=="local_propuesta"
                            and edge["origen"]=="D01" for edge in g["aristas"]))

    def test_confirm_requires_sha_and_literal_human_step(self):
        record=self.make()
        target=Path(record["ruta"])
        sha=hashlib.sha256(target.read_bytes()).hexdigest()
        with self.assertRaises(ValueError):
            confirm(self.vault,record["relacion_id"],sha,revisor="Owner ficticio",
                    referencia_autorizacion="Decisión escrita de prueba",
                    confirmacion="SI")
        self.assertEqual(query(self.vault)["relaciones"][0]["estado_efectivo"],"propuesta")
        result=confirm(self.vault,record["relacion_id"],sha,revisor="Owner ficticio",
                       referencia_autorizacion="Decisión escrita de prueba",
                       confirmacion="CONFIRMAR "+record["relacion_id"]+" "+sha[:12])
        self.assertEqual(result["estado"],"validada_por_revisor")
        self.assertEqual(query(self.vault)["relaciones"][0]["estado_efectivo"],
                         "validada_por_revisor")
        self.assertTrue(any(e["capa"]=="local_ratificada_por_revisor"
                            for e in graph(self.vault)["aristas"]))
        self.assertEqual(validate(self.vault)["errores"],[])
        with self.assertRaises(ValueError):
            confirm(self.vault,record["relacion_id"],sha,revisor="Owner ficticio",
                    referencia_autorizacion="Decisión escrita de prueba",
                    confirmacion="CONFIRMAR "+record["relacion_id"]+" "+sha[:12])

    def test_unknown_refs_unknown_predicate_and_duplicate_blocked(self):
        with self.assertRaises(ValueError):
            propose(self.vault,"D01","NO-EXISTE","sustentado_por",**self.kw)
        with self.assertRaises(ValueError):
            propose(self.vault,"D01","F-DEMORL-01","amigo_de",**self.kw)
        with self.assertRaises(ValueError):
            propose(self.vault,"D01","F-DEMORL-01","sustentado_por",
                    fuentes=["F-NO-EXISTE"],ambito=self.kw["ambito"],motivo=self.kw["motivo"])
        self.make()
        with self.assertRaises(FileExistsError):self.make()

    def test_tampered_relations_detected_by_validator(self):
        record=self.make()
        path=Path(record["ruta"])
        data=json.loads(path.read_text())
        data["destino_id"]="NOTA-INVENTADA"
        path.write_text(json.dumps(data))
        result=validate(self.vault)
        self.assertTrue(any("Relación" in x for x in result["errores"]))
        with self.assertRaises(ValueError): query(self.vault)

    def test_cli_query_includes_candidature_state(self):
        self.make()
        cmd=[sys.executable,str(ROOT/"scripts"/"cerebro.py"),"relaciones",
             "--vault",str(self.vault),"--id","D01"]
        result=subprocess.run(cmd,capture_output=True,text=True,check=True)
        data=json.loads(result.stdout)
        self.assertEqual(data["total"],1)
        self.assertEqual(data["relaciones"][0]["estado_efectivo"],"propuesta")


if __name__=="__main__":
    unittest.main()
