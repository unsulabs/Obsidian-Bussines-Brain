"""El informe para Codex no publica notas ni cambia la bóveda del usuario."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))

from aceptacion_integracion_local import _git_info, _inventory, _private_output, diagnosticar, entregar, preflight
from crear_instancia import create
from documentos import create_document
from operacion import create_source


class IntegracionLocalTest(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base=Path(temp.name)
        self.vault=create("EMPRESA-PRUEBA","Empresa simulada",self.base/"vault")
        create_source(self.vault,"F-TEST-001","Fuente inventada","urn:synthetic:test","ejemplo")
        file=self.base/"d01.md"
        file.write_text(
            "# Ficticia\n\n## Negocio\n\n<!-- kb:id=D01-B001 -->\n"
            "La empresa de prueba evalúa necesidades y registra sus procesos "
            "sin afirmar ventas ni acuerdos que no se hayan observado.\n",
            encoding="utf8")
        create_document(self.vault,"D01","Modelo",file,
                        sources=["F-TEST-001"],editorial="en_revision")
        self.before={p.relative_to(self.vault):p.read_bytes()
                     for p in self.vault.rglob("*") if p.is_file()}

    @unittest.skipUnless((ROOT / '.git').exists(), 'requiere checkout Git real')
    def test_real_vault_stays_byte_identical_in_audit(self):
        commit=_git_info()["sha"]
        result=diagnosticar(self.vault,esperado=commit,ejecutar_tests=False)
        self.assertTrue(result["boveda"]["intacta_en_esta_ejecucion"])
        self.assertEqual(result["boveda"]["documentos_dx"],1)
        self.assertEqual(result["boveda"]["fuentes"],1)
        self.assertEqual(result["boveda"]["D01"]["revision"],"0.1")
        self.assertFalse(result["bases"]["aplicacion_ejecutada"])
        self.assertFalse(result["mapa"]["publicacion_ejecutada"])
        self.assertEqual(result["manual"]["obsidian_gui_y_16_bases"],"NO_VERIFICADO")
        self.assertEqual(result["pruebas_mac_o_local"]["estado"],"NO_VERIFICADO")
        after={p.relative_to(self.vault):p.read_bytes()
               for p in self.vault.rglob("*") if p.is_file()}
        self.assertEqual(self.before,after)

    @unittest.skipUnless((ROOT / '.git').exists(), 'requiere checkout Git real')
    def test_zip_is_sanitized_and_stored_outside_vault(self):
        commit=_git_info()["sha"]
        result=diagnosticar(self.vault,esperado=commit,ejecutar_tests=False)
        output=self.base/"revision_privada"
        dest=_private_output(output,self.vault)
        delivered=entregar(result,dest)
        zip_path=Path(delivered["paquete"])
        self.assertTrue(zip_path.is_file())
        self.assertTrue(output not in self.vault.parents)
        with zipfile.ZipFile(zip_path) as z:
            self.assertEqual(set(z.namelist()),{
                "REPORTE_INTEGRACION_SANEADO.json","RESUMEN_INTEGRACION.md"})
            payload=z.read("REPORTE_INTEGRACION_SANEADO.json").decode("utf8")
            self.assertNotIn(str(self.base),payload)
            self.assertNotIn("Empresa simulada",payload)
            self.assertNotIn("La empresa de prueba evalúa",payload)
            parsed=json.loads(payload)
            self.assertTrue(parsed["boveda"]["intacta_en_esta_ejecucion"])
        self.assertEqual(self.before,{p.relative_to(self.vault):p.read_bytes()
                                     for p in self.vault.rglob("*") if p.is_file()})

    @unittest.skipUnless((ROOT / '.git').exists(), 'requiere checkout Git real')
    def test_outdated_bases_not_mistaken_for_pass(self):
        standard=self.vault/"90_Sistema"/"Vistas"/"Ofertas.base"
        before=standard.read_bytes()
        legacy=(ROOT/"tests"/"fixtures_bases_v0_2"/"Ofertas.base").read_bytes()
        standard.write_bytes(legacy)
        try:
            with patch('aceptacion_integracion_local._git_info',
                       return_value={'sha':_git_info()['sha'],'rama':'main',
                                     'arbol_limpio':True,'cambios_locales_cantidad':0}):
                result=diagnosticar(self.vault,esperado=_git_info()["sha"],ejecutar_tests=False)
            self.assertEqual(result["resultado_integracion"],
                             "CODIGO_VALIDADO_BOVEDA_PENDIENTE_BASES")
            self.assertEqual(result["bases"]["por_actualizar"],1)
            self.assertFalse(result["bases"]["aplicacion_ejecutada"])
        finally:
            standard.write_bytes(before)

    @unittest.skipUnless((ROOT / '.git').exists(), 'requiere checkout Git real')
    def test_wrong_expected_git_sha_blocks_acceptance(self):
        result=diagnosticar(self.vault,esperado="0"*40,ejecutar_tests=False)
        self.assertEqual(result["resultado_integracion"],"FALLO_O_REQUIERE_CORRECCION")
        self.assertFalse(result["repositorio"]["coincide"])

    def test_cannot_write_report_inside_vault_or_repo(self):
        for p in (self.vault/"resumen", ROOT/"salida_integracion", self.vault):
            with self.subTest(p=p):
                with self.assertRaisesRegex(ValueError,"fuera de Git y de la bóveda"):
                    _private_output(p,self.vault)

    def test_inventory_covers_revision_snapshots_and_attachments(self):
        history=self.vault/"90_Sistema"/"Historial_DX"/"D01"
        history.mkdir(parents=True)
        snapshot=history/"anterior.snapshot"
        snapshot.write_bytes(b"revision original")
        attachment=self.vault/"evidencia.pdf"
        attachment.write_bytes(b"%PDF-1.4 synthetic")
        finder=self.vault/".DS_Store"
        finder.write_bytes(b"cache")
        inventory=_inventory(self.vault)
        self.assertIn("90_Sistema/Historial_DX/D01/anterior.snapshot",inventory)
        self.assertIn("evidencia.pdf",inventory)
        self.assertNotIn(".DS_Store",inventory)
        before=inventory["90_Sistema/Historial_DX/D01/anterior.snapshot"]
        snapshot.write_bytes(b"revision alterada")
        self.assertNotEqual(before,_inventory(self.vault)["90_Sistema/Historial_DX/D01/anterior.snapshot"])

    def test_inventory_rejects_symlink_inside_vault(self):
        link=self.vault/"enlace-a-fuente.md"
        link.symlink_to(self.base/"fuente-externa.md")
        with self.assertRaisesRegex(ValueError,"enlace simbólico"):
            _inventory(self.vault)

    @unittest.skipUnless((ROOT / '.git').exists(), 'requiere checkout Git real')
    def test_snapshot_changed_during_diagnostic_blocks_pass(self):
        history=self.vault/"90_Sistema"/"Historial_DX"/"D01"
        history.mkdir(parents=True)
        snapshot=history/"anterior.snapshot"
        snapshot.write_bytes(b"revision original")

        def mutate_then_preflight(vault):
            snapshot.write_bytes(b"revision alterada")
            return preflight(vault)

        with patch('aceptacion_integracion_local.preflight',side_effect=mutate_then_preflight):
            result=diagnosticar(self.vault,esperado=_git_info()['sha'],ejecutar_tests=False)
        self.assertFalse(result['boveda']['intacta_en_esta_ejecucion'])
        self.assertEqual(result['boveda']['archivos_modificados'],1)
        self.assertEqual(result['resultado_integracion'],'FALLO_O_REQUIERE_CORRECCION')

    def test_existing_destination_never_overwritten(self):
        existing=self.base/"evidencia"
        existing.mkdir()
        with self.assertRaises(FileExistsError):
            _private_output(existing,self.vault)


if __name__=="__main__":
    unittest.main()
