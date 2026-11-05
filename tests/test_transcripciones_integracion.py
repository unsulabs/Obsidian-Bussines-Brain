import copy
import base64
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import transcripciones_integracion as ti
from lib_ce import make_note
import test_transcripciones_pipeline


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.vault = self.root / "vault"
        self.vault.mkdir()
        self.fixture = test_transcripciones_pipeline.PipelineTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.snapshot = {"vault": str(self.vault), "backup_dir": str(self.root / "backup"),
                         "bank_root": str(self.fixture.bank)}
        self.old = self.source("Antes")
        self.write(self.old)
        self.new = self.source("Después")

    def source(self, body, id="F-1", name="Conversación", version="V1"):
        version = self.fixture.vid if version == "V1" else version
        meta = {"id": id, "tipo": "fuente", "transcripcion_id": self.fixture.tr, "version_id": version,
                "estado_editorial": "en_revision", "sensibilidad": "interno"}
        refs = [{"tr_id": self.fixture.tr, "version_id": self.fixture.vid, "sha256": ti._sha(self.fixture.authored["data"])}]
        return {"path": f"50_Fuentes/{name}.md", "kind": "source", "id": id,
                "scope": self.fixture.scope, "source_refs": refs,
                "permission_snapshot": ti.permission_snapshot(self.fixture.bank, source_refs=refs, **self.fixture.scope),
                "content": make_note(meta, "# Conversación\n" + body)}

    def second(self):
        return {"path": "00_Mapas/Otro.md", "kind": "navigation", "id": "NAV-2",
                "content": make_note({"id": "NAV-2", "tipo": "mapa", "estado_editorial": "borrador"}, "# Otro mapa")}

    def entity(self, entity_type="oferta", **overrides):
        tipo = entity_type
        spec = ti.load_registry()[tipo]
        meta = {"id": spec["prefijo"] + "-fixture", "tipo": tipo, "clase": tipo,
                "estado_editorial": "en_revision", "estado_conocimiento": "propuesta",
                "vigencia": "sin_verificar", "sensibilidad": "interno", "registrado_en": "2026-11-04",
                "fuentes": ["[[50_Fuentes/Conversación]]"], **overrides}
        return {"id": meta["id"], "kind": "entity", "path": spec["carpeta"] + "/Propuesta.md",
                "content": make_note(meta, "# Propuesta\nMecanismo sintético.")}

    def forged_entity(self, manifest, **overrides):
        m = copy.deepcopy(manifest)
        e = m["entries"][0]
        meta, body = ti.split_frontmatter(base64.b64decode(e["content_b64"]).decode())
        raw = make_note({**meta, **overrides}, body).encode()
        e["content_b64"] = base64.b64encode(raw).decode()
        e["proposed_sha"] = ti._sha(raw)
        m["manifest_sha"] = ti._sha(ti._json({k: v for k, v in m.items() if k != "manifest_sha"}))
        return m

    def write(self, c):
        path = self.vault / c["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(c["content"], encoding='utf-8', newline='\n')

    def prepare(self, candidates=None):
        candidates = copy.deepcopy(candidates or [self.new])
        for c in candidates:
            if "source_refs" not in c and "access_checks" not in c:
                c["access_checks"] = [{k: self.new[k] for k in ("scope", "source_refs", "permission_snapshot")}]
        return ti.prepare_batch(candidates, self.snapshot)

    def apply(self, m, token=1):
        return ti.apply_batch(m, {"manifest_sha": m["manifest_sha"], "scope": "apply_batch",
                                  "writers_quiescent": True,
                                  "responsable": "Fixture", "referencia": "Autorización sintética"}, token)

    def test_dry_apply_retry_restore_exact_bytes(self):
        before = ti._inventory(self.vault)
        m = self.prepare()
        self.assertEqual(before, ti._inventory(self.vault))
        self.assertFalse(Path(self.snapshot["backup_dir"]).exists())
        other = self.vault / "ajeno.bin"
        self.apply(m)
        self.apply(m)
        self.assertEqual((self.vault / self.new["path"]).read_text(encoding='utf-8'), self.new["content"])
        other.write_bytes(b"Conservar")
        ti.rollback_batch(m)
        ti.rollback_batch(m)
        self.assertEqual((self.vault / self.old["path"]).read_text(encoding='utf-8'), self.old["content"])
        self.assertEqual(other.read_bytes(), b"Conservar")

    def test_stale_sha_preflight_no_partial_writes(self):
        c2 = self.second()
        m = self.prepare([c2, self.new])
        (self.vault / self.old["path"]).write_text("edición humana", encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ValueError, "Conflicto"):
            self.apply(m)
        self.assertFalse((self.vault / c2["path"]).exists())

    def test_interruptions_resume(self):
        for token, stage in enumerate(("backup_written", "backups_ready", "intent_saved", "file_written"), start=10):
            with self.subTest(stage=stage):
                m = self.prepare()
                def fail(current, path):
                    if current == stage:
                        raise RuntimeError("synthetic crash")
                with patch.object(ti, "_checkpoint", fail):
                    with self.assertRaises(RuntimeError):
                        self.apply(m, token * 2)
                self.apply(m, token * 2 + 1)
                ti.rollback_batch(m)

    def test_crash_mid_batch_and_mid_rollback(self):
        c2 = self.second()
        m = self.prepare([self.new, c2])
        def fail(stage, path):
            if stage == "file_written":
                raise RuntimeError("crash")
        with patch.object(ti, "_checkpoint", fail):
            with self.assertRaises(RuntimeError):
                self.apply(m)
        self.apply(m, 2)
        with patch.object(ti, "_checkpoint", side_effect=RuntimeError("rollback crash")):
            with self.assertRaises(RuntimeError):
                ti.rollback_batch(m)
        ti.rollback_batch(m)
        self.assertFalse((self.vault / c2["path"]).exists())
        self.assertEqual((self.vault / self.old["path"]).read_text(encoding='utf-8'), self.old["content"])

    def test_rollback_preserves_later_edit(self):
        m = self.prepare()
        self.apply(m)
        p = self.vault / self.old["path"]
        p.write_text("human later", encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ValueError, "posterior"):
            ti.rollback_batch(m)
        self.assertEqual(p.read_text(encoding='utf-8'), "human later")

    def test_duplicate_ids_versions_and_missing_link(self):
        for c in (self.source("Otro", "F-1", "Otra", "V2"),
                  self.source("Otro", "F-2", "Otra", "V1"),
                  self.source("[[No existe]]")):
            with self.assertRaises(ValueError):
                self.prepare([c])

    def test_ambiguous_link_and_entity_without_sources(self):
        for folder in ("uno", "dos"):
            p = self.vault / folder / "Mismo.md"
            p.parent.mkdir()
            p.write_text(make_note({"id": folder, "tipo": "entidad"}, "# Otra"), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ValueError, "ambiguo"):
            self.prepare([self.source("[[Mismo]]")])
        entity = self.entity(fuentes=[])
        with self.assertRaisesRegex(ValueError, "sin fuentes"):
            self.prepare([entity])

    def test_approval_and_authorization_rejected(self):
        c = copy.deepcopy(self.new)
        c["content"] = c["content"].replace("en_revision", "aprobado")
        with self.assertRaises(ValueError):
            self.prepare([c])
        self.write(c)
        with self.assertRaises(ValueError):
            self.prepare()
        self.write(self.old)
        m = self.prepare()
        with self.assertRaises(ValueError):
            ti.apply_batch(m, {}, 1)
        altered = copy.deepcopy(m)
        altered["entries"][0]["path"] = "Otro.md"
        with self.assertRaisesRegex(ValueError, "alterado"):
            self.apply(altered)

    def test_symlink_traversal_and_backup_tampering(self):
        c = copy.deepcopy(self.new)
        c["path"] = "../escape.md"
        with self.assertRaises(ValueError):
            self.prepare([c])
        for location in (self.vault / "backup", self.fixture.bank / "backup"):
            with self.assertRaises(ValueError):
                ti.prepare_batch([self.new], {**self.snapshot, "backup_dir": str(location)})
        m = self.prepare()
        self.apply(m)
        backup = Path(m["backup_dir"]) / m["batch_id"] / "0.backup"
        backup.unlink()
        backup.symlink_to(self.vault / self.old["path"])
        with self.assertRaises(ValueError):
            ti.rollback_batch(m)

    def test_fencing_and_writer_lock(self):
        m = self.prepare()
        self.apply(m, 3)
        with self.assertRaisesRegex(ValueError, "obsoleto"):
            self.apply(m, 2)
        with ti._lock(self.vault):
            with self.assertRaises(BlockingIOError):
                self.apply(m, 4)

    def test_dx_reuses_existing_revision_contract(self):
        meta = {"id": "DOC-1", "tipo": "documento", "doc_id": "D01", "revision": "1.0",
                "estado_editorial": "en_revision"}
        body = "# Documento\n" + "Criterio experto para interpretar fuentes de la empresa. " * 3
        old = {"path": "10_Conocimiento/Dirección.md", "content": make_note(meta, body)}
        self.write(old)
        c = {"path": old["path"], "kind": "dx", "id": "DOC-1",
             "content": make_note({**meta, "revision": "1.1"}, body + "\nNueva precisión.")}
        m = self.prepare([c])
        self.apply(m)
        ti.rollback_batch(m)
        self.assertEqual((self.vault / old["path"]).read_text(encoding='utf-8'), old["content"])

    def navigation_manifest(self):
        old = make_note({"id": "HOME", "tipo": "inicio"}, "# Inicio\nManual propio\n")
        self.write({"path": "Inicio.md", "content": old})
        return self.prepare([{"path": "Inicio.md", "kind": "navigation_append", "id": "HOME",
                              "expected_sha256": ti._sha(old.encode()),
                              "content": old + "\nNueva navegación\n"}]), old

    def test_navigation_resealed_manifest_preserves_body_metadata_and_scope(self):
        manifest, old = self.navigation_manifest()
        before = ti._inventory(self.vault)
        for mutation in ("erase", "change", "metadata", "identity", "path", "base"):
            with self.subTest(mutation=mutation):
                m = copy.deepcopy(manifest)
                e = m["entries"][0]
                raw = base64.b64decode(e["content_b64"])
                if mutation == "erase":
                    raw = raw.replace(b"# Inicio\nManual propio", b"")
                elif mutation == "change":
                    raw = raw.replace(b"Manual propio", b"Alterado")
                elif mutation == "metadata":
                    raw = raw.replace(b"tipo: inicio", b"tipo: manual")
                elif mutation == "identity":
                    e["id"] = "OTHER"
                elif mutation == "path":
                    e["path"] = "Otro.md"
                else:
                    e["base_sha"] = None
                e["content_b64"] = base64.b64encode(raw).decode()
                e["proposed_sha"] = ti._sha(raw)
                m["manifest_sha"] = ti._sha(ti._json({k: v for k, v in m.items() if k != "manifest_sha"}))
                with self.assertRaises(ValueError):
                    self.apply(m)
                self.assertEqual(ti._inventory(self.vault), before)
                self.assertFalse(Path(m["backup_dir"]).exists())

    def test_navigation_recovery_and_rollback_use_original_bytes(self):
        for token, stage in enumerate(("backup_written", "intent_saved", "file_written"), start=1):
            with self.subTest(stage=stage):
                m, old = self.navigation_manifest()
                def crash(current, path):
                    if current == stage:
                        raise RuntimeError("synthetic crash")
                with patch.object(ti, "_checkpoint", crash):
                    with self.assertRaises(RuntimeError):
                        self.apply(m, token * 2)
                self.apply(m, token * 2 + 1)
                self.apply(m, token * 2 + 1)
                ti.rollback_batch(m)
                ti.rollback_batch(m)
                self.assertEqual((self.vault / "Inicio.md").read_bytes(), old.encode())

    def test_navigation_concurrent_edit_and_postedit_rollback(self):
        m, old = self.navigation_manifest()
        p = self.vault / "Inicio.md"
        p.write_text(old + "Owner edit\n", encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ValueError, "Conflicto"):
            self.apply(m)
        self.assertEqual(p.read_text(encoding='utf-8'), old + "Owner edit\n")
        p.write_text(old, encoding='utf-8', newline='\n')
        def edit(stage, path):
            if stage == "intent_saved":
                p.write_text(old + "Concurrent edit\n", encoding='utf-8', newline='\n')
        with patch.object(ti, "_checkpoint", edit):
            with self.assertRaisesRegex(ValueError, "Conflicto concurrente"):
                self.apply(m)
        self.assertEqual(p.read_text(encoding='utf-8'), old + "Concurrent edit\n")
        p.write_text(old, encoding='utf-8', newline='\n')
        self.apply(m, 2)
        p.write_text(p.read_text(encoding='utf-8') + "Later edit\n", encoding='utf-8', newline='\n')
        before = p.read_bytes()
        with self.assertRaisesRegex(ValueError, "Edición posterior"):
            ti.rollback_batch(m)
        self.assertEqual(p.read_bytes(), before)

    def test_navigation_resealed_adapter_changes_cannot_erase_body(self):
        manifest, old = self.navigation_manifest()
        before = ti._inventory(self.vault)
        for kind in set(ti.KINDS) | ti.KINDS_D | {"base_view"}:
            with self.subTest(kind=kind):
                m = copy.deepcopy(manifest)
                e = m["entries"][0]
                raw = base64.b64decode(e["content_b64"]).replace(b"Manual propio", b"Deleted")
                e.update(kind=kind, content_b64=base64.b64encode(raw).decode(), proposed_sha=ti._sha(raw))
                if kind in ti.KINDS_D:
                    e["base_content_b64"] = base64.b64encode(old.encode()).decode()
                m["manifest_sha"] = ti._sha(ti._json({k: v for k, v in m.items() if k != "manifest_sha"}))
                with self.assertRaises(ValueError):
                    self.apply(m)
                self.assertEqual(ti._inventory(self.vault), before)
                self.assertFalse(Path(m["backup_dir"]).exists())

    def base_candidate(self):
        return {"path": "90_Sistema/Vistas/Transcripciones/Nueva.base", "id": "BASE-T", "kind": "base_view",
                "content": 'filters:\n  and:\n    - tipo == "fuente"\n    - transcripcion_id != null\nviews:\n  - type: table\n    name: Transcripciones\n'}

    def test_base_resealed_manifest_revalidates_create_contract(self):
        manifest = self.prepare([self.base_candidate()])
        for mutation in ("folder", "extension", "base", "snapshot", "id", "yaml", "filters", "views"):
            with self.subTest(mutation=mutation):
                m = copy.deepcopy(manifest)
                e = m["entries"][0]
                raw = base64.b64decode(e["content_b64"])
                if mutation == "folder":
                    e["path"] = "90_Sistema/Otra.base"
                elif mutation == "extension":
                    e["path"] = e["path"].replace(".base", ".md")
                elif mutation == "base":
                    e["base_sha"] = "0" * 64
                elif mutation == "snapshot":
                    m["snapshot"][e["path"]] = ti._sha(raw)
                elif mutation == "id":
                    e["id"] = ""
                elif mutation == "yaml":
                    raw = b"[]\n"
                elif mutation == "filters":
                    raw = raw.replace(b'tipo == "fuente"', b'tipo == "manual"')
                else:
                    raw = raw.split(b"views:")[0] + b"views: []\n"
                e.update(content_b64=base64.b64encode(raw).decode(), proposed_sha=ti._sha(raw))
                m["manifest_sha"] = ti._sha(ti._json({k: v for k, v in m.items() if k != "manifest_sha"}))
                before = ti._inventory(self.vault)
                with self.assertRaises(ValueError):
                    self.apply(m)
                self.assertEqual(ti._inventory(self.vault), before)
                self.assertFalse(Path(m["backup_dir"]).exists())

    def test_new_base_recovery_retry_and_rollback(self):
        candidate = self.base_candidate()
        path = self.vault / candidate["path"]
        for token, stage in enumerate(("backups_ready", "intent_saved", "file_written"), start=1):
            with self.subTest(stage=stage):
                m = self.prepare([candidate])
                def crash(current, target):
                    if current == stage:
                        raise RuntimeError("synthetic crash")
                with patch.object(ti, "_checkpoint", crash):
                    with self.assertRaises(RuntimeError):
                        self.apply(m, token * 2)
                self.apply(m, token * 2 + 1)
                self.apply(m, token * 2 + 1)
                self.assertEqual(path.read_text(encoding='utf-8'), candidate["content"])
                ti.rollback_batch(m)
                ti.rollback_batch(m)
                self.assertFalse(path.exists())

    def test_navigation_append_and_new_base_preserve_existing_views(self):
        home = {"path": "Inicio.md", "content": make_note({"id": "HOME", "tipo": "inicio"}, "# Inicio\nManual propio\n")}
        self.write(home)
        existing = self.vault / "90_Sistema" / "Vistas" / "Existente.base"
        existing.parent.mkdir(parents=True)
        existing.write_text("views: [mis ajustes]\n", encoding='utf-8', newline='\n')
        nav = {**home, "kind": "navigation_append", "id": "HOME",
               "expected_sha256": ti._sha(home["content"].encode()),
               "content": home["content"] + "\n[[50_Fuentes/Conversación]]\n"}
        base = {"path": "90_Sistema/Vistas/Transcripciones/Transcripciones.base", "id": "BASE-T", "kind": "base_view",
                "content": 'filters:\n  and:\n    - tipo == "fuente"\n    - transcripcion_id != null\nviews:\n  - type: table\n    name: Transcripciones\n'}
        m = self.prepare([nav, base])
        self.apply(m)
        self.assertEqual(existing.read_text(encoding='utf-8'), "views: [mis ajustes]\n")
        ti.rollback_batch(m)
        self.assertEqual((self.vault / "Inicio.md").read_text(encoding='utf-8'), home["content"])
        nav["content"] = nav["content"].replace("Manual propio", "Modificado")
        with self.assertRaisesRegex(ValueError, "append"):
            self.prepare([nav])
        self.write(base)
        with self.assertRaisesRegex(ValueError, "sobrescribir"):
            self.prepare([base])

    def test_source_and_full_view_links(self):
        view = {"path": "50_Fuentes/Transcripciones/TR-1/V1.md", "kind": "transcript_view", "id": "VIEW-1",
                **{k: self.new[k] for k in ("scope", "source_refs", "permission_snapshot")},
                "content": make_note({"id": "VIEW-1", "tipo": "transcripcion", "transcripcion_id": self.fixture.tr,
                                      "version_id": self.fixture.vid, "estado_editorial": "borrador", "sensibilidad": "interno"}, "# Original\nPalabras exactas.")}
        source = self.source("[[50_Fuentes/Transcripciones/TR-1/V1]]")
        m = self.prepare([source, view])
        self.apply(m)
        ti.rollback_batch(m)
        self.assertFalse((self.vault / view["path"]).exists())

    def rendered(self, sensitivity="interno"):
        from transcripciones_pipeline import consolidate_analysis
        from transcripciones_fichas import render_source, propose_navigation
        oldpath = self.vault / self.old["path"]
        if oldpath.exists():
            oldpath.unlink()
        consolidate_analysis(self.fixture.bank, self.fixture.submission(), **self.fixture.scope, commit=True)
        home = make_note({"id": "HOME", "tipo": "inicio"}, "# Inicio\nManual propio\n")
        (self.vault / "Inicio.md").write_text(home, encoding='utf-8', newline='\n')
        snapshot = {"Inicio.md": home}
        rendered = render_source(self.fixture.tr, "RUN-fixture", {
            "bank": self.fixture.bank, **self.fixture.scope, "vault_snapshot": snapshot,
            "source_sensitivity": {self.fixture.tr: sensitivity}})
        return rendered["candidates"] + propose_navigation(rendered["candidates"], snapshot)

    def test_renderer_prepare_apply_navigation_base_links_and_rollback(self):
        candidates = self.rendered()
        before = ti._inventory(self.vault)
        m = self.prepare(candidates)
        self.apply(m)
        self.assertEqual(ti._backend_errors(self.vault), [])
        ti.rollback_batch(m)
        self.assertEqual(before, ti._inventory(self.vault))

    def test_canonical_system_manual_append_preserves_id_bytes_and_restores(self):
        from transcripciones_fichas import propose_navigation
        candidates = self.rendered()
        sources = [c for c in candidates if c["kind"] in {"source", "transcript_view"}]
        manual = make_note({"id": "SYS-COMO-USAR", "tipo": "manual"}, "# Cómo usar\nAtajos propios — conservar.\n")
        path = self.vault / "90_Sistema" / "Como_usar.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(manual.encode())
        navigation = propose_navigation(sources, {"90_Sistema/Como_usar.md": manual})
        proposed = next(c for c in navigation if c["path"] == "90_Sistema/Como_usar.md")
        self.assertEqual(proposed["id"], "SYS-COMO-USAR")
        self.assertTrue(proposed["content"].encode().startswith(manual.encode()))
        self.assertEqual(proposed["expected_sha256"], ti._sha(manual.encode()))
        before = ti._inventory(self.vault)
        m = self.prepare(sources + navigation)
        self.apply(m)
        self.assertEqual(path.read_bytes(), proposed["content"].encode())
        self.assertFalse((self.vault / "Como_usar.md").exists())
        ti.rollback_batch(m)
        self.assertEqual(path.read_bytes(), manual.encode())
        self.assertEqual(ti._inventory(self.vault), before)

    def test_revocation_after_render_and_after_prepare_never_writes(self):
        candidates = self.rendered()
        before = ti._inventory(self.vault)
        m = self.prepare(candidates)
        self.fixture.grant("internal_query", "revoke")
        with self.assertRaises(ValueError):
            self.prepare(candidates)
        with self.assertRaises(ValueError):
            self.apply(m)
        self.assertEqual(before, ti._inventory(self.vault))
        self.assertFalse(Path(self.snapshot["backup_dir"]).exists())

    def test_restricted_content_rejected_even_with_false_flag(self):
        candidates = self.rendered("restringido")
        for c in candidates:
            c["local_private_only"] = False
            c["sensibilidad"] = "interno"
        before = ti._inventory(self.vault)
        with self.assertRaisesRegex(ValueError, "Sensibilidad"):
            self.prepare(candidates)
        self.assertEqual(before, ti._inventory(self.vault))

    def test_source_hash_or_bundle_changes_after_prepare(self):
        candidates = self.rendered()
        m = self.prepare(candidates)
        before = ti._inventory(self.vault)
        bundle = self.fixture.bank / "analisis" / "RUN-fixture.json"
        bundle.write_bytes(bundle.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "Bundle"):
            self.apply(m)
        self.assertEqual(before, ti._inventory(self.vault))

    def test_local_analysis_revocation_and_original_tampering(self):
        m = self.prepare()
        before = ti._inventory(self.vault)
        self.fixture.grant("local_analysis", "revoke")
        with self.assertRaises(ValueError):
            self.apply(m)
        self.assertEqual(before, ti._inventory(self.vault))

    def test_derived_candidates_cannot_omit_dependencies(self):
        before = ti._inventory(self.vault)
        for kind in ("entity", "dx", "navigation", "navigation_append", "base_view"):
            c = {"id": "E", "path": "Entidad.md", "kind": kind,
                 "content": make_note({"id": "E", "tipo": "entidad", "estado_editorial": "borrador",
                                       "fuentes": ["[[50_Fuentes/Conversación]]"]}, "# Derivado")}
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "dependencias"):
                ti.prepare_batch([c], self.snapshot)
        m = self.prepare([self.source("Después")])
        original = next((self.fixture.bank / "originales").glob("*.bin"))
        original.write_bytes(b"tampered")
        with self.assertRaises(ValueError):
            self.apply(m)
        self.assertEqual(before, ti._inventory(self.vault))

    def test_allowed_source_cannot_cover_different_linked_source(self):
        changed = {**self.old, "content": self.old["content"].replace(self.fixture.tr, "TR-other")}
        self.write(changed)
        entity = self.entity()
        with self.assertRaisesRegex(ValueError, "dependencias"):
            self.prepare([entity])

    def test_typed_entities_apply_update_rollback(self):
        for number, tipo in enumerate(("oferta", "proceso", "recurso", "investigacion", "proyecto")):
            with self.subTest(tipo=tipo):
                before = ti._inventory(self.vault)
                c = self.entity(tipo)
                m = self.prepare([c])
                self.apply(m, number * 2 + 1)
                updated = {**c, "content": c["content"] + "\nPrecisión propuesta.\n"}
                m2 = self.prepare([updated])
                self.apply(m2, number * 2 + 2)
                ti.rollback_batch(m2)
                self.assertEqual((self.vault / c["path"]).read_text(encoding='utf-8'), c["content"])
                ti.rollback_batch(m)
                self.assertEqual(before, ti._inventory(self.vault))

    def test_entity_staging_folder_and_rejections(self):
        c = self.entity()
        c["path"] = "90_Sistema/Bandeja_Propuestas/Oferta propuesta.md"
        self.prepare([c])
        for overrides in ({"tipo": "entidad"}, {"tipo": "inventado"}, {"tipo": "fuente"},
                          {"clase": "proceso"}, {"id": "PRS-forjado"}, {"id": "../fuera"},
                          {"estado_editorial": "aprobado"}, {"estado_conocimiento": "hecho"},
                          {"vigencia": "vigente"}, {"sensibilidad": "restringido"},
                          {"registrado_en": ""}, {"fuentes": []}, {"fuentes": ["[[Ausente]]"]}):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                self.prepare([self.entity(**overrides)])
        for field in ("clase", "registrado_en", "sensibilidad", "estado_conocimiento", "vigencia"):
            c = self.entity()
            fm, body = ti.split_frontmatter(c["content"])
            del fm[field]
            c["content"] = make_note(fm, body)
            with self.subTest(missing=field), self.assertRaises(ValueError):
                self.prepare([c])

    def test_entity_forged_manifest_cannot_ratify_or_change_adapter(self):
        m = self.prepare([self.entity()])
        before = ti._inventory(self.vault)
        for overrides in ({"tipo": "fuente"}, {"tipo": "inventado"}, {"estado_conocimiento": "hecho"},
                          {"estado_editorial": "aprobado"}, {"vigencia": "vigente"}, {"fuentes": []}):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                self.apply(self.forged_entity(m, **overrides))
        self.assertEqual(before, ti._inventory(self.vault))

    def test_entity_cannot_forge_verified_source_bindings(self):
        c = self.entity()
        fm, body = ti.split_frontmatter(self.old["content"])
        del fm["transcripcion_id"]
        del fm["version_id"]
        self.write({**self.old, "content": make_note(fm, body)})
        c["bound_source_ids"] = ["F-1"]
        c["verified_external_refs"] = [{"kind": "external", "note_ids": ["F-1"]}]
        with self.assertRaisesRegex(ValueError, "dependencias"):
            self.prepare([c])

    def test_entity_cannot_bypass_using_special_kind(self):
        for existing in (False, True):
            c = self.entity()
            if existing:
                self.write(c)
            m = self.prepare([{**c, "content": c["content"] + "\nCambio propuesto.\n"}])
            before = ti._inventory(self.vault)
            for kind in ("base_view", "navigation_append", "proposal_staging", "source"):
                forged = copy.deepcopy(m)
                forged["entries"][0]["kind"] = kind
                forged["manifest_sha"] = ti._sha(ti._json({k: v for k, v in forged.items() if k != "manifest_sha"}))
                with self.subTest(existing=existing, kind=kind), self.assertRaises(ValueError):
                    self.apply(forged)
                self.assertEqual(before, ti._inventory(self.vault))

    def test_entity_existing_approved_or_identity_change_rejected(self):
        candidate = self.entity()
        for changes in ({"estado_editorial": "aprobado"}, {"estado_conocimiento": "hecho"},
                        {"vigencia": "historico"}, {"clase": "proceso"}, {"id": "OFE-distinto"}):
            self.write(self.entity(**changes))
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.prepare([candidate])
        # A self-rehashed manifest cannot bypass protection of an existing note.
        self.write(candidate)
        m = self.prepare([{**candidate, "content": candidate["content"] + "\nCambio.\n"}])
        approved = self.entity(estado_editorial="aprobado")
        self.write(approved)
        forged = copy.deepcopy(m)
        forged["snapshot"] = ti._inventory(self.vault)
        forged["entries"][0]["base_sha"] = ti._sha(approved["content"].encode())
        forged["manifest_sha"] = ti._sha(ti._json({k: v for k, v in forged.items() if k != "manifest_sha"}))
        with self.assertRaises(ValueError):
            self.apply(forged)
        self.assertEqual((self.vault / candidate["path"]).read_text(encoding='utf-8'), approved["content"])
        self.write(candidate)
        forged = self.forged_entity(m, tipo="mapa")
        forged["entries"][0]["kind"] = "navigation"
        forged["manifest_sha"] = ti._sha(ti._json({k: v for k, v in forged.items() if k != "manifest_sha"}))
        with self.assertRaisesRegex(ValueError, "identidad/tipo"):
            self.apply(forged)

    def test_entity_revocation_and_stale_snapshot_never_write(self):
        c = self.entity()
        before = ti._inventory(self.vault)
        m = self.prepare([c])
        self.fixture.grant("internal_query", "revoke")
        with self.assertRaises(ValueError):
            self.apply(m)
        self.assertEqual(before, ti._inventory(self.vault))
        self.fixture.grant("internal_query")
        m = self.prepare([c])
        (self.vault / "new.bin").write_bytes(b"human")
        with self.assertRaisesRegex(ValueError, "Conflicto"):
            self.apply(m)
        self.assertFalse((self.vault / c["path"]).exists())


if __name__ == "__main__":
    unittest.main()
