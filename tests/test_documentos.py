"""Ciclo documental mínimo: crear contenido real D/X sin inventar aprobaciones."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from crear_instancia import create
from documentos import create_document
from lib_ce import split_frontmatter
from operacion import create_source
from validar_boveda import validate


class DocumentosTest(unittest.TestCase):
    def setUp(self):
        t = tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.base = Path(t.name)
        self.vault = create("DEMO-DOCUMENTOS", "Empresa ficticia", self.base / "empresa")
        self.draft = self.base / "borrador_externo.md"
        self.body = (
            "# Laboratorio ficticio\n\n"
            "## Actividad documentada\n\n"
            "Esta empresa sintética estudia flujos de trabajo y registra decisiones, "
            "sin afirmar contratos, pagos ni resultados de terceros.\n\n"
            "## CONTROL\n\n"
            "Fuente original pendiente; la estrategia no se ha aprobado.\n"
        )
        self.draft.write_text(self.body, encoding="utf8")

    def source(self):
        return create_source(self.vault, "F-DEMO-001", "Fuente ficticia", "urn:synthetic:example", "nota")

    def test_D01_review_does_not_approve_and_preserves_content(self):
        self.source()
        result = create_document(self.vault, "D01", "Identidad de la empresa", self.draft,
                                 sources=["F-DEMO-001"], editorial="en_revision", as_of="2026-10-28")
        self.assertEqual(result["doc_id"], "D01")
        self.assertFalse(result["aprobado"])
        p = Path(result["ruta"])
        self.assertEqual(p.relative_to(self.vault).as_posix(), "10_Conocimiento/Identidad de la empresa.md")
        fm, body = split_frontmatter(p.read_text(encoding="utf8"))
        self.assertEqual(body, self.body)
        self.assertEqual(fm["id"], "D01")
        self.assertEqual(fm["doc_id"], "D01")
        self.assertEqual(fm["tipo"], "documento")
        self.assertEqual(fm["clase"], "D01")
        self.assertEqual(fm["empresa_id"], "DEMO-DOCUMENTOS")
        self.assertEqual(fm["revision"], "0.1")
        self.assertEqual(fm["estado_editorial"], "en_revision")
        self.assertEqual(fm["cobertura"], "parcial")
        self.assertEqual(fm["revisado_por"], "por_validar")
        self.assertEqual(fm["fecha_corte"], "2026-10-28")
        self.assertEqual(fm["fuentes"], ["[[50_Fuentes/Fuente ficticia]]"])
        self.assertEqual(validate(self.vault)["errores"], [])

    def test_coverage_is_declared_without_approving_the_document(self):
        result = create_document(self.vault, "D05", "Economía ficticia", self.draft,
                                 coverage="sin_fuente", editorial="en_revision")
        fm, _ = split_frontmatter(Path(result["ruta"]).read_text(encoding="utf8"))
        self.assertEqual(fm["cobertura"], "sin_fuente")
        self.assertEqual(fm["estado_editorial"], "en_revision")
        self.assertEqual(validate(self.vault)["errores"], [])
        with self.assertRaises(ValueError):
            create_document(self.vault, "D06", "Personas ficticias", self.draft,
                            coverage="completo")

    def test_family_is_singleton_and_original_is_not_overwritten(self):
        first = create_document(self.vault, "D01", "Primera versión", self.draft)
        first_meta, _ = split_frontmatter(Path(first["ruta"]).read_text(encoding="utf8"))
        self.assertEqual(first_meta["cobertura"], "sin_fuente")
        before = Path(first["ruta"]).read_bytes()
        with self.assertRaises(FileExistsError):
            create_document(self.vault, "D01", "Intento duplicado", self.draft)
        self.assertEqual(Path(first["ruta"]).read_bytes(), before)
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "Otro", self.draft, doc_id="D02")

    def test_manual_document_with_other_filename_blocks_same_doc_id(self):
        manual = self.vault / "10_Conocimiento" / "texto_inicial.md"
        manual.parent.mkdir(exist_ok=True)
        manual.write_text(
            "---\nid: D01-MANUAL\ndoc_id: D01\ntipo: documento\nclase: D01\n"
            "estado_editorial: borrador\n---\n# Contenido anterior\n",
            encoding="utf8"
        )
        self.assertFalse(validate(self.vault)["errores"])
        with self.assertRaises(FileExistsError):
            create_document(self.vault, "D01", "Duplicado", self.draft)
        self.assertFalse((self.vault / "10_Conocimiento" / "D01.md").exists())

    def test_validator_detects_duplicate_doc_id_even_with_unique_ids(self):
        doc = create_document(self.vault, "D01", "Primero", self.draft)
        other = self.vault / "10_Conocimiento" / "otra_nota.md"
        other.write_text(
            "---\nid: ID-DISTINTO\ndoc_id: D01\ntipo: documento\n"
            "clase: D01\nestado_editorial: borrador\n---\n# Otro\n"
        )
        problems = validate(self.vault)["errores"]
        self.assertTrue(any("Doc_id duplicado D01" in x for x in problems))
        self.assertTrue(Path(doc["ruta"]).exists())

    def test_X01_independent_identity_and_fixed_id(self):
        x = create_document(self.vault, "X01", "Oferta ficticia", self.draft,
                            doc_id="X01-EJEMPLO-001")
        y = create_document(self.vault, "X01", "Otra oferta ficticia", self.draft)
        self.assertNotEqual(x["doc_id"], y["doc_id"])
        self.assertTrue(y["doc_id"].startswith("X01-"))
        self.assertEqual(validate(self.vault)["errores"], [])

    def test_invalid_class_reviewer_state_and_ids_rejected(self):
        for kwargs in [
            {"class_id": "D08"}, {"class_id": "X09"},
            {"class_id": "D01", "editorial": "aprobado"},
            {"class_id": "X01", "doc_id": "../../otro"},
            {"class_id": "X01", "doc_id": "X02-ABC"},
            {"class_id": "D01", "as_of": "2026-99-99"},
        ]:
            with self.subTest(kwargs=kwargs):
                cls = kwargs.pop("class_id")
                with self.assertRaises(ValueError):
                    create_document(self.vault, cls, "No debería escribirse", self.draft, **kwargs)
        self.assertFalse((self.vault / "10_Conocimiento" / "D01.md").exists())

    def test_reject_unknown_source_without_writing(self):
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "Sin fuente", self.draft,
                            sources=["F-NO-EXISTE"])
        self.assertFalse((self.vault / "10_Conocimiento" / "D01.md").exists())

    def test_reject_private_key_and_untrusted_frontmatter(self):
        self.draft.write_text("---\nid: APROBADO\n---\n" + self.body)
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "YAML no permitido", self.draft)
        self.draft.write_text(self.body + "\n-----BEGIN PRIVATE KEY-----\n")
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "Credencial", self.draft)

    def test_rollback_invalid_wikilink(self):
        self.draft.write_text(self.body + "\n[[FUENTE-NO-EXISTENTE]]\n")
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "Con enlace roto", self.draft)
        self.assertFalse((self.vault / "10_Conocimiento" / "D01.md").exists())
        self.assertEqual(validate(self.vault)["errores"], [])

    def test_reject_source_inside_vault_or_repo(self):
        internal = self.vault / "90_Sistema" / "borrador.md"
        internal.write_text(self.body)
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "Desde bóveda", internal)
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "Desde Git", ROOT / "README.md")

    def test_untrusted_symlink_in_ancestors_is_rejected(self):
        from documentos import _is_symlinked
        import os
        real = self.base / "real_directory"
        real.mkdir()
        alias = self.base / "custom_alias"
        alias.symlink_to(real, target_is_directory=True)
        redirected = alias / "candidate.md"
        self.assertTrue(_is_symlinked(redirected))
        with self.assertRaises(ValueError):
            create_document(self.vault, "D01", "No leer alias de usuario", redirected)

    def test_only_verified_macos_var_alias_is_exempt(self):
        from documentos import _is_symlinked
        from unittest.mock import patch
        candidate = Path("/var/folders/synthetic/temporary/draft.md")
        original_is_symlink = Path.is_symlink
        original_resolve = Path.resolve

        def synthetic_symlink(p):
            return str(p) == "/var" or original_is_symlink(p)

        def synthetic_resolve(p, strict=False):
            return Path("/private/var") if str(p) == "/var" else original_resolve(p, strict=strict)

        with patch("documentos.sys.platform", "darwin"), \
             patch.object(Path, "is_symlink", synthetic_symlink), \
             patch.object(Path, "resolve", synthetic_resolve):
            with patch("documentos.os.readlink", return_value="private/var"):
                self.assertFalse(_is_symlinked(candidate))
            with patch("documentos.os.readlink", return_value="somewhere-else"):
                self.assertTrue(_is_symlinked(candidate))
            with patch("documentos.os.readlink", return_value="/private/var"):
                self.assertFalse(_is_symlinked(candidate))
        with patch("documentos.sys.platform", "linux"), \
             patch.object(Path, "is_symlink", synthetic_symlink):
            self.assertTrue(_is_symlinked(candidate))

    def test_only_verified_macos_tmp_alias_is_exempt(self):
        from documentos import _is_symlinked
        from unittest.mock import patch
        candidate = Path("/tmp/ce-test/ficticia.md")
        original_is_symlink = Path.is_symlink
        original_resolve = Path.resolve

        def synthetic_symlink(p):
            return str(p) == "/tmp" or original_is_symlink(p)

        def synthetic_resolve(p, strict=False):
            return (Path("/private/tmp") if str(p) == "/tmp"
                    else original_resolve(p, strict=strict))

        with patch("documentos.sys.platform", "darwin"), \
             patch.object(Path, "is_symlink", synthetic_symlink), \
             patch.object(Path, "resolve", synthetic_resolve):
            for trusted in ("private/tmp", "/private/tmp"):
                with patch("documentos.os.readlink", return_value=trusted):
                    self.assertFalse(_is_symlinked(candidate))
            for untrusted in ("another/path", "/var", "../private/tmp", "private/var"):
                with patch("documentos.os.readlink", return_value=untrusted):
                    self.assertTrue(_is_symlinked(candidate))
        with patch("documentos.sys.platform", "linux"), \
             patch.object(Path, "is_symlink", synthetic_symlink):
            self.assertTrue(_is_symlinked(candidate))

    def test_user_symlink_under_trusted_macos_tmp_stays_blocked(self):
        from documentos import _is_symlinked
        from unittest.mock import patch
        candidate = Path("/tmp/user-created-alias/file.md")
        original_is_symlink = Path.is_symlink

        def synthetic_symlink(p):
            return str(p) in {"/tmp", "/tmp/user-created-alias"} or original_is_symlink(p)

        with patch("documentos.sys.platform", "darwin"), \
             patch.object(Path, "is_symlink", synthetic_symlink), \
             patch.object(Path, "resolve", return_value=Path("/private/tmp")):
            with patch("documentos.os.readlink", return_value="private/tmp"):
                self.assertTrue(_is_symlinked(candidate))

    def test_actual_darwin_system_aliases_if_present(self):
        from documentos import _is_symlinked
        import sys
        if sys.platform != "darwin":
            self.skipTest("Requiere ejecución nativa sobre macOS")
        for alias, expected in (("/tmp", "/private/tmp"), ("/var", "/private/var")):
            root=Path(alias)
            if root.is_symlink() and root.resolve(strict=True) == Path(expected):
                with self.subTest(alias=alias):
                    self.assertFalse(_is_symlinked(root / "synthetic" / "draft.md"))

    def test_cli_creation_synthetic(self):
        cmd = [sys.executable, str(ROOT / "scripts" / "cerebro.py"), "documento",
               "--vault", str(self.vault), "--clase", "D03", "--titulo", "Portafolio de prueba",
               "--archivo", str(self.draft), "--estado", "en_revision",
               "--cobertura", "sin_fuente"]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(proc.stdout)
        self.assertEqual(data["doc_id"], "D03")
        self.assertFalse(data["aprobado"])
        front, _ = split_frontmatter(Path(data["ruta"]).read_text(encoding="utf8"))
        self.assertEqual(front["cobertura"], "sin_fuente")
        self.assertEqual(validate(self.vault)["errores"], [])


if __name__ == "__main__":
    unittest.main()
