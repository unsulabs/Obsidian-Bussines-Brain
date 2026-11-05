"""Mapa Markdown y Canvas: navegación derivada sin cambiar conocimiento empresarial."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
from crear_instancia import create
from documentos import create_document
from operacion import create_ficha, create_source
from relaciones import propose,confirm
from mapa_conocimiento import previsualizar,publicar,MAP_MD,MAP_CANVAS
from validar_boveda import validate


class MapaConocimientoTest(unittest.TestCase):
    def setUp(self):
        d=tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        self.work=Path(d.name)
        self.vault=create("DEMO-MAPA","Negocio ficticio",self.work/"vault")
        create_source(self.vault,"F-MAPA-001","Episodio de prueba","urn:synthetic:episode","nota")
        draft=self.work/"direccion.md"
        draft.write_text(
            "# Dirección ficticia\n\n## Modelo de trabajo\n\n"
            "<!-- kb:id=D01-B001 -->\n"
            "Una organización de prueba estudia prioridades con su equipo y "
            "distingue qué trabajo acuerda realizar de sus propuestas internas.\n\n"
            "## CONTROL\n\nEjemplo inventado.\n",encoding="utf8")
        a=create_document(self.vault,"D01","Dirección ficticia",draft,
                          sources=["F-MAPA-001"],tags=["direccion/modelo-valor"])
        developed=self.work/"proceso.md"
        developed.write_text(
            "# Flujo del equipo ficticio\n\n## Trabajo\n\n"
            "Un responsable registra una solicitud y consulta con el equipo "
            "antes de asignar una actividad que produzca resultados verificables.\n",
            encoding="utf8")
        b=create_ficha(self.vault,"proceso","Flujo operativo",content_file=developed,
                       sources=["F-MAPA-001"],tags=["operacion/procesos"])
        self.originals={x:Path(x).read_bytes() for x in [a["ruta"],b["ruta"]]}
        self.a=a["doc_id"]
        self.b=b["id"]
        self.backup=self.work/"external"

    def approval(self,r):
        return {
            "sha_actual":r["sha_actual"],
            "sha_propuesto":r["sha_propuesto"],
            "confirmacion":r["confirmacion_requerida"],
            "backup_dir":self.backup}

    def test_read_only_preview_y_map_markdown_canvas(self):
        rel=propose(self.vault,self.a,self.b,"refiere_a",
                    fuentes=["F-MAPA-001"],
                    ambito="flujo de trabajo ficticio",
                    motivo="Se propone un vínculo entre estrategia y proceso del equipo ficticio.")
        before=set(self.vault.rglob("*"))
        r=previsualizar(self.vault)
        self.assertEqual(r["modo"],"SOLO_LECTURA")
        self.assertEqual(r["sha_actual"],"NUEVO")
        self.assertGreaterEqual(r["notas_en_mapa"],3)
        self.assertEqual(r["relaciones_tipadas"],1)
        self.assertEqual(r["canvas_aristas"],1)
        self.assertIn("propuesta",r["vista_previa"])
        self.assertFalse((self.vault/MAP_MD).exists())
        self.assertFalse((self.vault/MAP_CANVAS).exists())
        self.assertEqual(before,set(self.vault.rglob("*")))

    def test_publish_with_permission_and_backups_is_nondestructive(self):
        relation=propose(self.vault,self.a,self.b,"refiere_a",
                         fuentes=["F-MAPA-001"],ambito="contexto ficticio",
                         motivo="La documentación de dirección menciona el proceso en la empresa de ejemplo.")
        r=previsualizar(self.vault)
        with self.assertRaises(ValueError):
            publicar(self.vault,sha_actual=r["sha_actual"],sha_propuesto=r["sha_propuesto"],
                     confirmacion="SI",backup_dir=self.backup)
        self.assertFalse((self.vault/MAP_MD).exists())
        x=publicar(self.vault,**self.approval(r))
        self.assertEqual(x["resultado"],"APLICADO")
        canvas=json.loads((self.vault/MAP_CANVAS).read_text())
        self.assertEqual(canvas["edges"][0]["label"],"refiere_a (propuesta)")
        self.assertTrue(any(n["id"]=="nota-sistema-mapa" and n["type"]=="text"
                            for n in canvas["nodes"]))
        self.assertTrue(all(n["type"]=="file" for n in canvas["nodes"]
                            if n["id"]!="nota-sistema-mapa"))
        md=(self.vault/MAP_MD).read_text()
        self.assertIn("[[10_Conocimiento/Dirección ficticia|Dirección ficticia]]",md)
        self.assertIn("[[",md)
        self.assertIn("operacion/procesos",md)
        self.assertEqual(validate(self.vault)["errores"],[])
        for file,data in self.originals.items():
            self.assertEqual(Path(file).read_bytes(),data)
        self.assertTrue((Path(x["respaldo"])/"manifest.json").exists())
        second=previsualizar(self.vault)
        self.assertTrue(second["sin_cambios"])
        self.assertEqual(publicar(self.vault,**self.approval(second))["resultado"],"SIN_CAMBIOS")

    def test_confirmed_relation_appears_with_separate_layer(self):
        rel=propose(self.vault,self.a,self.b,"refiere_a",
                    fuentes=["F-MAPA-001"],ambito="proceso de la firma",
                    motivo="Un vínculo propuesto para una firma ficticia y su proceso de trabajo.")
        p=Path(rel["ruta"])
        sha=hashlib.sha256(p.read_bytes()).hexdigest()
        confirm(self.vault,rel["relacion_id"],sha,revisor="Ficticio responsable",
                referencia_autorizacion="Decisión de confirmación sintética",
                confirmacion="CONFIRMAR "+rel["relacion_id"]+" "+sha[:12])
        draft=previsualizar(self.vault)
        result=publicar(self.vault,**self.approval(draft))
        self.assertEqual(result["resultado"],"APLICADO")
        canvas=json.loads((self.vault/MAP_CANVAS).read_text())
        self.assertIn("(revisión)",canvas["edges"][0]["label"])
        self.assertIn("validada_por_revisor",(self.vault/MAP_MD).read_text())

    def test_source_changed_after_preview_requires_new_SHA(self):
        r=previsualizar(self.vault)
        created=create_ficha(self.vault,"decision","Decisión provisional")
        original={p:self.vault/p for p in (MAP_MD,MAP_CANVAS)}
        with self.assertRaisesRegex(ValueError,"volver a previsualizar"):
            publicar(self.vault,**self.approval(r))
        self.assertFalse((self.vault/MAP_MD).exists())
        self.assertEqual(validate(self.vault)["errores"],[])

    def test_does_not_overwrite_non_generated_user_map(self):
        path=self.vault/MAP_MD
        path.write_text("---\nid: SYS-MAPA-DERIVADO\ntipo: mapa\n---\n# Mapa manual\n")
        with self.assertRaisesRegex(ValueError,"no sobrescribir"):
            previsualizar(self.vault)
        self.assertEqual((self.vault/MAP_MD).read_text().splitlines()[-1],"# Mapa manual")

    def test_rewrite_requires_matching_existing_SHA(self):
        initial=previsualizar(self.vault)
        publicar(self.vault,**self.approval(initial))
        original=self.vault/MAP_MD
        old=original.read_bytes()
        create_ficha(self.vault,"investigacion","Investigación simulada")
        r=previsualizar(self.vault)
        self.assertFalse(r["sin_cambios"])
        wrong_sha=initial["sha_propuesto"]
        wrong_sha=wrong_sha[:-1]+("1" if wrong_sha[-1]=="0" else "0")
        bad={**self.approval(r),"sha_actual":wrong_sha}
        with self.assertRaisesRegex(ValueError,"Mapa o notas cambiaron"):
            publicar(self.vault,**bad)
        self.assertEqual(original.read_bytes(),old)
        new=publicar(self.vault,**self.approval(r))
        self.assertEqual(new["resultado"],"APLICADO")
        self.assertEqual(validate(self.vault)["errores"],[])
        backup_md=Path(new["respaldo"])/(MAP_MD.name+".anterior.snapshot")
        self.assertEqual(backup_md.read_bytes(),old)

    def test_obsidian_canvas_autosave_does_not_require_republication(self):
        propose(self.vault,self.a,self.b,"refiere_a",
                fuentes=["F-MAPA-001"],ambito="prueba de autoguardado",
                motivo="El documento de dirección ficticio remite al proceso ficticio.")
        first=previsualizar(self.vault)
        publicar(self.vault,**self.approval(first))
        canvas_path=self.vault/MAP_CANVAS
        canvas=json.loads(canvas_path.read_text(encoding="utf8"))
        for edge in canvas["edges"]:
            edge["fromSide"]="right"
            edge["toSide"]="left"
        native=json.dumps(canvas,ensure_ascii=False,separators=(",",":"))
        canvas_path.write_text(native,encoding="utf8")

        preview=previsualizar(self.vault)
        self.assertTrue(preview["sin_cambios"])
        self.assertEqual(publicar(self.vault,**self.approval(preview))["resultado"],"SIN_CAMBIOS")
        self.assertEqual(canvas_path.read_text(encoding="utf8"),native)

        canvas["edges"][0]["label"]="relación distinta"
        canvas_path.write_text(json.dumps(canvas,ensure_ascii=False),encoding="utf8")
        self.assertFalse(previsualizar(self.vault)["sin_cambios"])

        canvas["edges"][0]["label"]="refiere_a (propuesta)"
        canvas["nodes"][1]["x"]+=25
        canvas_path.write_text(json.dumps(canvas,ensure_ascii=False),encoding="utf8")
        self.assertFalse(previsualizar(self.vault)["sin_cambios"])

    def test_cli_preview(self):
        completed=subprocess.run([
            sys.executable,str(ROOT/"scripts"/"cerebro.py"),"mapa-conocimiento",
            "--vault",str(self.vault)],capture_output=True,text=True,check=True)
        data=json.loads(completed.stdout)
        self.assertEqual(data["modo"],"SOLO_LECTURA")
        self.assertIn("sha_propuesto",data)


if __name__=="__main__":
    unittest.main()
