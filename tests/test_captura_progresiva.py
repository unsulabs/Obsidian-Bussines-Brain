"""Capturas de descubrimiento: prueba aislada con datos completamente ficticios."""
from __future__ import annotations
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from crear_instancia import create
from operacion import create_source, summary
from registro_descubrimiento import capture_discovery
from validar_boveda import validate
from lib_ce import split_frontmatter


class CapturaTest(unittest.TestCase):
    def setUp(self):
        context = tempfile.TemporaryDirectory()
        self.addCleanup(context.cleanup)
        self.tmp = Path(context.name)
        self.vault = create("EMP-PRUEBA", "Empresa Ficticia", self.tmp / "boveda")
        self.note = self.tmp / "captura_autorizada.md"
        self.note.write_text(
            "## Observación documentada\nExiste un documento sintético de muestra.\n\n"
            "## Interpretación provisional\nSe desconoce qué empresa hizo el trabajo.\n\n"
            "## Pendiente\nConfirmar la atribución antes de utilizarlo en una oferta.",
            encoding="utf8"
        )

    def test_provisional_record_with_no_fake_case(self):
        result = capture_discovery(self.vault, "Exploración inicial", self.note)
        self.assertFalse(result["aprobado"])
        dest = Path(result["ruta"])
        self.assertEqual(dest.parent.name, "Descubrimiento")
        props, body = split_frontmatter(dest.read_text(encoding="utf8"))
        self.assertEqual(props["tipo"], "registro_descubrimiento")
        self.assertEqual(props["estado_editorial"], "borrador")
        self.assertEqual(props["estado_conocimiento"], "pendiente")
        self.assertEqual(props["autoridad"], "ninguna")
        self.assertIn("Se desconoce qué empresa", body)
        self.assertEqual(validate(self.vault)["errores"], [])
        self.assertEqual(summary(self.vault)["por_tipo"]["registro_descubrimiento"], 1)
        self.assertFalse(list((self.vault / "20_Entidades").glob("*.md")))

    def test_source_link_must_exist(self):
        create_source(self.vault, "F-DEMO-01", "Original sintético",
                      "urn:synthetic:ejemplo", "prueba")
        result = capture_discovery(self.vault, "Lectura", self.note, sources=["F-DEMO-01"])
        props, _ = split_frontmatter(Path(result["ruta"]).read_text(encoding="utf8"))
        self.assertIn("[[50_Fuentes/Original sintético]]", props["fuentes"])
        with self.assertRaises(ValueError):
            capture_discovery(self.vault, "Mal", self.note, sources=["F-DESCONOCIDA"])

    def test_empty_and_secret_rejected(self):
        self.note.write_text("   ", encoding="utf8")
        with self.assertRaises(ValueError):
            capture_discovery(self.vault, "Vacía", self.note)
        self.note.write_text("-----BEGIN PRIVATE KEY-----\nEjemplo no válido", encoding="utf8")
        with self.assertRaises(ValueError):
            capture_discovery(self.vault, "Secreta", self.note)

    def test_non_destructive_multiple_captures(self):
        first = capture_discovery(self.vault, "Uno", self.note)
        original = Path(first["ruta"]).read_bytes()
        second = capture_discovery(self.vault, "Dos", self.note)
        self.assertNotEqual(first["id"], second["id"])
        self.assertEqual(Path(first["ruta"]).read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
