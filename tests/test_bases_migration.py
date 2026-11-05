"""La migración de vistas evita sobrescribir cambios y preserva notas."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from crear_instancia import create
from actualizar_vistas_bases import plan, apply


class BasesMigrationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.work = Path(self.tmp.name)
        self.vault = create("TEST-BASES", "Empresa sintética", self.work / "empresa")

    def simulate_previous_release(self):
        for p in (ROOT / "tests" / "fixtures_bases_v0_2").glob("*.base"):
            target = self.vault / "90_Sistema" / "Vistas" / p.name
            target.write_bytes(p.read_bytes())

    def test_fresh_vault_is_current(self):
        p = plan(self.vault)
        self.assertEqual(p["estado"], "AL_DIA")
        self.assertEqual(p["por_actualizar"], 0)

    def test_legacy_views_are_migrated_only_with_backup(self):
        self.simulate_previous_release()
        p = plan(self.vault)
        self.assertEqual(p["estado"], "LISTO")
        self.assertEqual(p["por_actualizar"], 16)
        before = (self.vault / "Inicio.md").read_bytes()
        first = (self.vault / "90_Sistema" / "Plantillas" / "Ficha_oferta.md").read_bytes()
        result = apply(self.vault, self.work / "respaldo_privado")
        self.assertEqual(result["resultado"], "APLICADO")
        self.assertEqual(result["actualizadas"], 16)
        self.assertTrue((Path(result["respaldo"]) / "manifiesto.json").is_file())
        self.assertEqual(plan(self.vault)["estado"], "AL_DIA")
        self.assertEqual((self.vault / "Inicio.md").read_bytes(), before)
        self.assertEqual((self.vault / "90_Sistema" / "Plantillas" / "Ficha_oferta.md").read_bytes(), first)

    def test_customized_view_blocks_all_writes(self):
        self.simulate_previous_release()
        altered = self.vault / "90_Sistema" / "Vistas" / "Ofertas.base"
        altered.write_text(
            altered.read_text().replace('tipo == "oferta"', 'tipo == "otro_tipo"')
            + "\n# filtro empresarial diferente\n", encoding="utf8")
        p = plan(self.vault)
        self.assertEqual(p["estado"], "BLOQUEADO")
        self.assertEqual(p["bloqueadas"], 1)
        with self.assertRaises(ValueError):
            apply(self.vault, self.work / "respaldos")
        self.assertIn("# filtro empresarial diferente", altered.read_text())
        self.assertFalse((self.work / "respaldos").exists())

    def test_safe_filter_only_migration_preserves_custom_layout(self):
        import yaml
        self.simulate_previous_release()
        docs = self.vault/"90_Sistema"/"Vistas"/"Documentos.base"
        offers = self.vault/"90_Sistema"/"Vistas"/"Ofertas.base"
        # Cambios sintéticos de presentación; mismo filtro 0.2, sin información real.
        docs.write_text(docs.read_text().replace(
            """- 'tipo == "documento"'""", '- tipo == "documento"'
        ).replace('name: "Documentos"', 'name: Documentos'), encoding="utf8")
        data = yaml.safe_load(offers.read_text())
        data["views"][1]["groupBy"]["property"]="tipo"
        offers.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),
                          encoding="utf8")
        original_docs=docs.read_bytes()
        original_offers=offers.read_bytes()
        suffix_docs=original_docs.split(b"views:\n",1)[1]
        suffix_offers=original_offers.split(b"views:\n",1)[1]
        plan_data=plan(self.vault)
        self.assertEqual(plan_data["estado"],"LISTO")
        self.assertEqual(plan_data["por_actualizar"],16)
        matches={Path(x["archivo"]).name:x["estado"] for x in plan_data["vistas"]}
        self.assertEqual(matches["Documentos.base"],"LISTO_FILTRO")
        self.assertEqual(matches["Ofertas.base"],"LISTO_FILTRO")
        self.assertEqual(docs.read_bytes(),original_docs)
        self.assertEqual(offers.read_bytes(),original_offers)
        result=apply(self.vault,self.work/"respaldo_privado")
        self.assertEqual(result["actualizadas"],16)
        self.assertEqual(result["filtros_sin_perder_personalizaciones"],2)
        self.assertEqual(docs.read_bytes().split(b"views:\n",1)[1],suffix_docs)
        self.assertEqual(offers.read_bytes().split(b"views:\n",1)[1],suffix_offers)
        self.assertEqual(yaml.safe_load(offers.read_text())["views"][1]["groupBy"]["property"],"tipo")
        # Las dos personalizadas son funcionalmente actuales aunque no idénticas en bytes.
        refreshed=plan(self.vault)
        self.assertEqual(refreshed["estado"],"AL_DIA")
        self.assertEqual(refreshed["por_actualizar"],0)
        statuses={Path(x["archivo"]).name:x["estado"] for x in refreshed["vistas"]}
        self.assertEqual(statuses["Documentos.base"],"AL_DIA_PERSONALIZADO")
        self.assertEqual(statuses["Ofertas.base"],"AL_DIA_PERSONALIZADO")

    def test_obsidian_normalized_all_16_preserves_current_views_and_workspace(self):
        import json
        import yaml
        self.simulate_previous_release()
        views=self.vault/"90_Sistema"/"Vistas"
        for file in sorted(views.glob("*.base")):
            data=yaml.safe_load(file.read_text(encoding="utf8"))
            # Simula el reserializado YAML de Obsidian y el groupBy observado.
            for view in data.get("views",[]):
                group=view.get("groupBy")
                if isinstance(group,dict) and isinstance(group.get("property"),str):
                    group["property"]=group["property"].replace("note.","")
            file.write_text(yaml.safe_dump(
                data,allow_unicode=True,sort_keys=False)
                + "\n# reserializacion_de_GUI_sintetica\n",encoding="utf8")
        before={p.name:p.read_bytes().split(b"views:\n",1)[1] for p in views.glob("*.base")}
        workspace=self.vault/".obsidian"/"workspace.json"
        workspace.parent.mkdir(exist_ok=True)
        workspace.write_text('{"synthetic":"gui_state"}',encoding="utf8")
        prior_workspace=workspace.read_bytes()
        plan_data=plan(self.vault)
        self.assertEqual(plan_data["estado"],"LISTO")
        self.assertEqual(plan_data["por_actualizar"],16)
        self.assertTrue(all(x["estado"]=="LISTO_FILTRO" for x in plan_data["vistas"]))
        with self.assertRaisesRegex(ValueError,"huellas de Bases cambiaron"):
            apply(self.vault,self.work/"privado",expected_plan_sha="0"*64)
        self.assertFalse((self.work/"privado").exists())
        result=apply(self.vault,self.work/"privado",
                     expected_plan_sha=plan_data["sha_plan"])
        self.assertEqual(result["actualizadas"],16)
        for p in views.glob("*.base"):
            self.assertEqual(before[p.name],p.read_bytes().split(b"views:\n",1)[1])
        self.assertEqual(workspace.read_bytes(),prior_workspace)
        backup=Path(result["respaldo"])
        meta=json.loads((backup/"manifiesto.json").read_text())
        self.assertEqual(len(meta["instantanea_vistas"]),16)
        self.assertEqual(meta["sha_plan"],plan_data["sha_plan"])
        self.assertEqual((backup/".obsidian"/"workspace.json").read_bytes(),prior_workspace)
        self.assertEqual(plan(self.vault)["estado"],"AL_DIA")

    def test_cli_apply_requires_fingerprint_and_backup(self):
        import subprocess
        import json
        self.simulate_previous_release()
        cmd=[sys.executable,str(ROOT/"scripts"/"actualizar_vistas_bases.py"),
             "--vault",str(self.vault),"--backup-dir",str(self.work/"privado"),
             "--apply"]
        bad=subprocess.run(cmd,capture_output=True,text=True)
        self.assertNotEqual(bad.returncode,0)
        self.assertIn("--sha-plan",bad.stderr)
        expected=plan(self.vault)["sha_plan"]
        ok=subprocess.run(cmd+["--sha-plan",expected],capture_output=True,
                          text=True,check=True)
        self.assertEqual(json.loads(ok.stdout)["actualizadas"],16)

    def test_backup_must_not_live_inside_vault(self):
        self.simulate_previous_release()
        with self.assertRaises(ValueError):
            apply(self.vault, self.vault / "90_Sistema" / "Respaldos")


if __name__ == "__main__":
    unittest.main()
