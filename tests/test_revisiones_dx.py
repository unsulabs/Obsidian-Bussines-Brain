"""Ciclo D/X no destructivo: previsualización, autorización, historial y restauración."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch
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
from lib_ce import make_note, split_frontmatter
from operacion import create_source
from revisiones_dx import previsualizar, preparar, aplicar, restaurar
from validar_boveda import validate


class CicloRevisionTest(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.work=Path(t.name)
        self.vault=create("EMPRESA-DEMO", "Empresa sintética", self.work/"vault")
        self.backup=self.work/"resguardos_externos"
        self.original=self.work/"borrador_v1.md"
        self.original.write_text(
            "# Empresa ficticia\n\n"
            "## Identidad\n\n<!-- kb:id=D01-B001 -->\n"
            "El proceso sintético organiza las solicitudes de trabajo en un registro "
            "y permite que el equipo compruebe quién las recibe y cuándo.\n\n"
            "## CONTROL\n\nMaterial ficticio para prueba de cambios.\n",encoding="utf8")
        create_source(self.vault,"F-DEMO-001","Fuente sintética","urn:demo:001","nota")
        self.record=create_document(self.vault,"D01","Dirección sintética",self.original,
                                    sources=["F-DEMO-001"],editorial="en_revision")
        self.doc=Path(self.record["ruta"])
        self.before=self.doc.read_bytes()
        self.next=self.work/"borrador_v2.md"
        self.next.write_text(
            self.original.read_text().replace(
                "organiza las solicitudes de trabajo en un registro",
                "organiza las solicitudes de trabajo en un registro de tareas auditables"
            ),encoding="utf8")

    def prepare(self):
        return preparar(self.vault,"D01",self.next)

    def apply(self,proposal,**opts):
        return aplicar(self.vault,proposal["propuesta_id"],
                       expected_sha=opts.get("expected_sha",proposal["sha_original"]),
                       candidate_sha=opts.get("candidate_sha",proposal["sha_candidato"]),
                       source_sha=opts.get("source_sha"),
                       responsable=opts.get("responsable","operador autorizado de prueba"),
                       referencia_autorizacion=opts.get("referencia","decisión explícita demo-001"),
                       backup_dir=opts.get("backup_dir",self.backup))

    def test_dryrun_does_not_touch_vault(self):
        old=validate(self.vault)["notas"]
        result=previsualizar(self.vault,"D01",self.next)
        self.assertEqual(result["operacion"],"SOLO_LECTURA")
        self.assertEqual(result["revision_propuesta"],"0.2")
        self.assertIn("auditables",result["resumen_diff"])
        self.assertEqual(self.doc.read_bytes(),self.before)
        self.assertEqual(validate(self.vault)["notas"],old)
        self.assertFalse((self.vault/"90_Sistema"/"Propuestas_DX").exists())

    def test_prepare_no_overwrite_or_duplicate_note(self):
        p=self.prepare()
        self.assertTrue(Path(p["ruta_propuesta"]).is_dir())
        self.assertEqual(self.doc.read_bytes(),self.before)
        self.assertFalse(p["documento_modificado"])
        self.assertEqual(validate(self.vault)["errores"],[])
        self.assertEqual(validate(self.vault)["notas"],9)

    def test_preserve_document_permissions_and_protect_history(self):
        import stat
        self.doc.chmod(0o600)
        p=self.prepare()
        self.assertEqual(stat.S_IMODE((self.vault/"90_Sistema"/"Propuestas_DX").stat().st_mode),0o700)
        out=self.apply(p)
        self.assertEqual(stat.S_IMODE(self.doc.stat().st_mode),0o600)
        self.assertEqual(stat.S_IMODE((self.vault/"90_Sistema"/"Historial_DX").stat().st_mode),0o700)
        self.assertTrue(Path(out["historial"]).is_dir())

    def test_apply_with_backup_and_review_status(self):
        p=self.prepare()
        out=self.apply(p)
        self.assertEqual(out["revision"],"0.2")
        self.assertFalse(out["aprobado"])
        meta,body=split_frontmatter(self.doc.read_text())
        self.assertEqual(meta["revision"],"0.2")
        self.assertEqual(meta["estado_editorial"],"en_revision")
        self.assertEqual(meta["doc_id"],"D01")
        self.assertEqual(meta["revisado_por"],"por_validar")
        self.assertIn("[[50_Fuentes/Fuente sintética]]",meta["fuentes"])
        self.assertIn("auditables",body)
        self.assertEqual((Path(out["historial"])/"anterior.snapshot").read_bytes(),self.before)
        self.assertEqual((Path(out["respaldo_externo"])/"anterior.snapshot").read_bytes(),self.before)
        self.assertEqual(validate(self.vault)["errores"],[])
        with self.assertRaises(ValueError):
            self.apply(p)

    def test_corrective_source_is_reviewed_and_added_to_properties(self):
        create_source(self.vault,"F-DEMO-002","Corrección sintética","urn:demo:002","nota")
        self.next.write_text(self.next.read_text()+
            "\nCorrección sustentada por [[50_Fuentes/Corrección sintética|F-DEMO-002]].\n",encoding="utf8")
        p=preparar(self.vault,"D01",self.next,sources=["F-DEMO-002"])
        self.assertEqual(self.doc.read_bytes(),self.before)
        self.assertEqual(p["fuentes_adicionales"],["F-DEMO-002"])
        self.assertEqual(len(p["fuentes_resultantes"]),2)
        with self.assertRaisesRegex(ValueError,"Huella de fuentes"):
            self.apply(p)
        with self.assertRaisesRegex(ValueError,"Huella de fuentes"):
            self.apply(p,source_sha="0"*64)
        out=self.apply(p,source_sha=p["sha_fuentes"])
        meta,_=split_frontmatter(self.doc.read_text())
        self.assertEqual(meta["revision"],"0.2")
        self.assertEqual(meta["estado_editorial"],"en_revision")
        self.assertEqual(len(meta["fuentes"]),2)
        self.assertIn("[[50_Fuentes/Corrección sintética]]",meta["fuentes"])
        self.assertEqual(validate(self.vault)["errores"],[])
        restored=restaurar(self.vault,"D01",out["historial_id"],
                           expected_sha=hashlib.sha256(self.doc.read_bytes()).hexdigest(),
                           responsable="operador de prueba",
                           referencia_autorizacion="restauración sintética",
                           backup_dir=self.backup)
        meta,_=split_frontmatter(self.doc.read_text())
        self.assertEqual(restored["revision"],"0.3")
        self.assertEqual(meta["fuentes"],["[[50_Fuentes/Fuente sintética]]"])

    def test_unknown_corrective_source_is_rejected_before_proposal(self):
        with self.assertRaisesRegex(ValueError,"No existe el ID"):
            preparar(self.vault,"D01",self.next,sources=["F-NO-EXISTE"])
        self.assertEqual(self.doc.read_bytes(),self.before)

    def test_cli_corrective_source_roundtrip(self):
        create_source(self.vault,"F-DEMO-002","Corrección sintética","urn:demo:002","nota")
        command=[sys.executable,str(ROOT/"scripts"/"cerebro.py")]
        prep=subprocess.run(command+["preparar-dx","--vault",str(self.vault),
                                    "--doc-id","D01","--archivo",str(self.next),
                                    "--fuente","F-DEMO-002"],capture_output=True,text=True,check=True)
        proposal=json.loads(prep.stdout)
        self.assertEqual(proposal["fuentes_adicionales"],["F-DEMO-002"])
        applied=subprocess.run(command+["aplicar-dx","--vault",str(self.vault),
                                       "--propuesta",proposal["propuesta_id"],
                                       "--sha-original",proposal["sha_original"],
                                       "--sha-candidato",proposal["sha_candidato"],
                                       "--sha-fuentes",proposal["sha_fuentes"],
                                       "--responsable","operador de prueba",
                                       "--referencia-autorizacion","corrección sintética",
                                       "--respaldo",str(self.backup)],
                               capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(applied.stdout)["revision"],"0.2")
        meta,_=split_frontmatter(self.doc.read_text())
        self.assertIn("[[50_Fuentes/Corrección sintética]]",meta["fuentes"])

    def test_restore_creates_forward_revision_and_keeps_history(self):
        applied=self.apply(self.prepare())
        now=self.doc.read_bytes()
        restored=restaurar(self.vault,"D01",applied["historial_id"],
                          expected_sha=hashlib.sha256(now).hexdigest(),
                          responsable="operador autorizado",
                          referencia_autorizacion="restaurar demo-002",
                          backup_dir=self.backup)
        self.assertEqual(restored["revision"],"0.3")
        meta,body=split_frontmatter(self.doc.read_text())
        self.assertEqual(meta["revision"],"0.3")
        self.assertEqual(meta["estado_editorial"],"en_revision")
        self.assertNotIn("auditables",body)
        self.assertEqual((Path(restored["historial"])/"anterior.snapshot").read_bytes(),now)
        self.assertEqual((Path(applied["historial"])/"anterior.snapshot").read_bytes(),self.before)
        self.assertEqual(validate(self.vault)["errores"],[])

    def test_concurrent_change_blocks_apply_without_backup(self):
        p=self.prepare()
        self.doc.write_bytes(self.before+"\nCambio externo en otra sesión.\n".encode("utf8"))
        changed=self.doc.read_bytes()
        with self.assertRaises(ValueError):
            self.apply(p)
        self.assertEqual(self.doc.read_bytes(),changed)
        self.assertFalse(self.backup.exists())

    def test_tampering_candidate_blocks_apply(self):
        p=self.prepare()
        (Path(p["ruta_propuesta"])/"candidato.snapshot").write_bytes(b"contenido alterado")
        with self.assertRaises(ValueError):
            self.apply(p)
        self.assertEqual(self.doc.read_bytes(),self.before)

    def test_auth_reference_and_sha_required(self):
        p=self.prepare()
        with self.assertRaises(ValueError):
            self.apply(p,referencia="")
        with self.assertRaises(ValueError):
            self.apply(p,expected_sha="0"*64)
        self.assertEqual(self.doc.read_bytes(),self.before)

    def test_approved_document_cannot_be_rewritten(self):
        meta,body=split_frontmatter(self.doc.read_text())
        meta["estado_editorial"]="aprobado"
        self.doc.write_text(make_note(meta,body))
        with self.assertRaises(ValueError):
            previsualizar(self.vault,"D01",self.next)

    def test_does_not_remove_block_ids_or_bypass_links(self):
        self.next.write_text("# Documento falso\n\n"+("contenido sin bloques. "*10)+"\n")
        with self.assertRaises(ValueError):
            self.prepare()
        self.next.write_text(self.original.read_text()+"\n[[NOTA-QUE-NO-EXISTE]]\n")
        with self.assertRaises(ValueError):
            self.prepare()
        self.assertEqual(self.doc.read_bytes(),self.before)

    def test_failed_validation_restores_bytes(self):
        p=self.prepare()
        # Simula validación adversarial solo DESPUÉS de sustituir la nota.
        from revisiones_dx import validate as actual_validate
        call_count=[0]
        def synthetic_validate(vault):
            call_count[0]+=1
            return {"errores":["error de validación sintética"]} if call_count[0]==2 else actual_validate(vault)
        with patch("revisiones_dx.validate",side_effect=synthetic_validate):
            with self.assertRaises(ValueError):
                self.apply(p)
        self.assertEqual(self.doc.read_bytes(),self.before)
        self.assertEqual(validate(self.vault)["errores"],[])

    def test_external_backup_is_owner_private_and_rejects_world_readable(self):
        self.backup.mkdir(mode=0o755)
        self.backup.chmod(0o755)
        p=self.prepare()
        with self.assertRaises(ValueError):
            self.apply(p)
        self.assertEqual(self.doc.read_bytes(),self.before)
        self.backup.chmod(0o700)
        self.assertEqual(self.apply(p)["revision"],"0.2")

    def test_restoration_can_remove_block_added_in_intermediate_revision(self):
        self.next.write_text(self.next.read_text(encoding="utf8")+
                             "\n<!-- kb:id=D01-B002 -->\nBloque adicional creado durante la revisión.\n",
                             encoding="utf8")
        modified=self.apply(self.prepare())
        self.assertIn("D01-B002",self.doc.read_text())
        current_hash=hashlib.sha256(self.doc.read_bytes()).hexdigest()
        result=restaurar(self.vault,"D01",modified["historial_id"],
                         expected_sha=current_hash,responsable="revisor autorizado",
                         referencia_autorizacion="Restauración sintética validada",
                         backup_dir=self.backup)
        self.assertEqual(result["revision"],"0.3")
        self.assertNotIn("D01-B002",self.doc.read_text())
        self.assertEqual(validate(self.vault)["errores"],[])

    def test_manifest_completion_failure_restores_original(self):
        self.prepare()
        p=self.prepare()
        from revisiones_dx import _write_atomic as writer
        tripped=[False]
        def glitch(path,contents):
            if (path.name=="manifest.json" and
                b'"estado": "aplicado"' in contents and not tripped[0]):
                tripped[0]=True
                raise OSError("Fallo de almacenamiento simulado")
            return writer(path,contents)
        with patch("revisiones_dx._write_atomic",side_effect=glitch):
            with self.assertRaises(OSError):
                self.apply(p)
        self.assertTrue(tripped[0])
        self.assertEqual(self.doc.read_bytes(),self.before)
        self.assertEqual(validate(self.vault)["errores"],[])

    def test_cli_simulation_and_proposal(self):
        proc=subprocess.run(
            [sys.executable,str(ROOT/"scripts"/"cerebro.py"),"previsualizar-dx",
             "--vault",str(self.vault),"--doc-id","D01","--archivo",str(self.next)],
            capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(proc.stdout)["revision_propuesta"],"0.2")
        proc=subprocess.run(
            [sys.executable,str(ROOT/"scripts"/"cerebro.py"),"preparar-dx",
             "--vault",str(self.vault),"--doc-id","D01","--archivo",str(self.next)],
            capture_output=True,text=True,check=True)
        self.assertIn("propuesta_id",json.loads(proc.stdout))
        self.assertEqual(self.doc.read_bytes(),self.before)


if __name__=="__main__":
    unittest.main()
