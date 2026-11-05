"""Aceptación preliminar: distinguir verificación estructural y humana."""
from __future__ import annotations
from pathlib import Path
import tempfile
import unittest
import sys

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
from crear_instancia import create
from documentos import create_document
from aceptacion_piloto import preflight


class PilotPreflightTest(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root=Path(temp.name)
        self.vault=create("TEST-PILOTO","Empresa totalmente ficticia",self.root/"boveda")

    def test_empty_vault_not_claimed_ready(self):
        result=preflight(self.vault)
        self.assertEqual(result["gates"]["integridad_y_referencias"],"PASS")
        self.assertEqual(result["gates"]["bases_sin_falsos_registros"],"PASS")
        self.assertEqual(result["gates"]["primera_unidad_empresarial"],"PENDIENTE")
        self.assertEqual(result["estado_tecnico"],"REQUIERE_ATENCION")
        self.assertFalse(result["producto_listo_para_produccion"])

    def test_first_D01_not_automatically_accepted(self):
        text=self.root/"contenido.md"
        text.write_text(
            "# Empresa de prueba\n\n## 01 Actividad\n\n"
            "El equipo ficticio documenta cómo revisa el trabajo que realiza y"
            " conserva criterios para que otras personas comprendan las decisiones."
            "\n\n## CONTROL\n\nEste es un contenido sintético sin resultados comerciales.",
            encoding="utf8")
        create_document(self.vault,"D01","Empresa sintética",text,editorial="en_revision")
        result=preflight(self.vault)
        self.assertEqual(result["estado_tecnico"],"APTO_PARA_PILOTO_LOCAL")
        self.assertEqual(result["gates"]["primera_unidad_empresarial"],"REGISTRADA_NO_APROBADA")
        self.assertEqual(result["gates"]["obsidian_gui_real"],"NO_VERIFICADO")
        self.assertFalse(result["producto_listo_para_produccion"])

    def test_vista_regresada_detected(self):
        base=self.vault/"90_Sistema"/"Vistas"/"Ofertas.base"
        base.write_text('filters:\n  or:\n    - tipo == "oferta"\nviews:\n  - type: table\n    name: Tabla\n')
        result=preflight(self.vault)
        self.assertEqual(result["gates"]["bases_sin_falsos_registros"],"PENDIENTE_MIGRACION_O_VALIDACION")
        self.assertEqual(result["estado_tecnico"],"REQUIERE_ATENCION")


if __name__=="__main__":
    unittest.main()
