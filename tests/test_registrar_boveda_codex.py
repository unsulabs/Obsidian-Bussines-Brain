"""Registro local de una bóveda nueva tras abrirla en Obsidian."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from registrar_boveda_codex import canonical, register


class RegistroBovedaCodexTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.vault = self.root / "Empresa ficticia"
        (self.vault / "90_Sistema").mkdir(parents=True)
        (self.vault / "90_Sistema" / "Como_usar.md").write_text("# Uso\n")
        (self.vault / "Inicio.md").write_text("# Inicio\n")
        self.native = self.root / "obsidian.json"
        self.registry = self.root / "vaults.json"
        self.project = canonical(self.root / "Proyecto Codex")
        self.project.mkdir()
        self.native.write_text(json.dumps({"vaults": {"abc123": {"path": str(self.vault)}}}))

    def call_register(self):
        return register(self.vault, "Empresa ficticia", "EMP-FIC", self.registry,
                        self.native, "90_Sistema/Como_usar.md", "Inicio.md")

    def test_register_and_repeat_without_rewriting(self):
        first = self.call_register()
        self.assertEqual(first["status"], "registrada")
        self.assertEqual(first["id"], "abc123")
        before = self.registry.read_bytes()
        second = self.call_register()
        self.assertEqual(second["status"], "ya_registrada")
        self.assertEqual(before, self.registry.read_bytes())
        self.assertEqual(json.loads(before)["vaults"][0]["aliases"], ["EMP-FIC"])

    def test_native_registration_required(self):
        self.native.write_text(json.dumps({"vaults": {}}))
        with self.assertRaisesRegex(ValueError, "Abre primero"):
            self.call_register()
        self.assertFalse(self.registry.exists())

    def test_collision_preserves_existing_registry(self):
        self.registry.write_text(json.dumps({"format": "codex-obsidian-vaults/1",
                                             "vaults": [{"name": "Otra empresa", "id": "xyz",
                                                         "aliases": ["EMP-FIC"],
                                                         "path": str(self.root / "Otra")}]}) + "\n")
        before = self.registry.read_bytes()
        with self.assertRaisesRegex(ValueError, "colisiona"):
            self.call_register()
        self.assertEqual(before, self.registry.read_bytes())

    def test_existing_registry_is_backed_up(self):
        self.registry.write_text('{"format":"codex-obsidian-vaults/1","vaults":[]}\n')
        before = self.registry.read_bytes()
        result = self.call_register()
        self.assertEqual(Path(result["respaldo"]).read_bytes(), before)
        self.assertEqual(len(json.loads(self.registry.read_text())["vaults"]), 1)

    def test_new_vault_is_associated_with_exact_project(self):
        result = register(self.vault, "Empresa ficticia", "EMP-FIC", self.registry,
                          self.native, "90_Sistema/Como_usar.md", "Inicio.md", self.project)
        self.assertEqual(result["status"], "registrada")
        self.assertEqual(json.loads(self.registry.read_text())["vaults"][0]["projects"],
                         [str(self.project)])
        before = self.registry.read_bytes()
        repeated = register(self.vault, "Empresa ficticia", "EMP-FIC", self.registry,
                            self.native, "90_Sistema/Como_usar.md", "Inicio.md", self.project)
        self.assertEqual(repeated["status"], "ya_registrada")
        self.assertEqual(self.registry.read_bytes(), before)

    def test_existing_vault_adds_project_with_backup(self):
        self.call_register()
        before = self.registry.read_bytes()
        result = register(self.vault, "Empresa ficticia", "EMP-FIC", self.registry,
                          self.native, "90_Sistema/Como_usar.md", "Inicio.md", self.project)
        self.assertEqual(result["status"], "proyecto_asociado")
        self.assertEqual(Path(result["respaldo"]).read_bytes(), before)
        self.assertEqual(json.loads(self.registry.read_text())["vaults"][0]["projects"],
                         [str(self.project)])

    def test_project_collision_does_not_rewrite_registry(self):
        other = {"name": "Otra empresa", "id": "xyz", "aliases": ["OTRA"],
                 "path": str(self.root / "Otra"),
                 "projects": [str(self.project)]}
        self.registry.write_text(json.dumps({"format": "codex-obsidian-vaults/1",
                                             "vaults": [other]}) + "\n")
        before = self.registry.read_bytes()
        with self.assertRaisesRegex(ValueError, "colisiona"):
            register(self.vault, "Empresa ficticia", "EMP-FIC", self.registry,
                     self.native, "90_Sistema/Como_usar.md", "Inicio.md", self.project)
        self.assertEqual(self.registry.read_bytes(), before)

    def test_nonexistent_project_does_not_register(self):
        with self.assertRaisesRegex(ValueError, "Proyecto inexistente"):
            register(self.vault, "Empresa ficticia", "EMP-FIC", self.registry,
                     self.native, "90_Sistema/Como_usar.md", "Inicio.md", self.root / "No existe")
        self.assertFalse(self.registry.exists())


if __name__ == "__main__":
    unittest.main()
