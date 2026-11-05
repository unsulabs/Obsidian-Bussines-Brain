"""Lotes locales revisables; autorización declarada, nunca aprobación empresarial.

El journal externo permite terminar o revertir después de una caída. flock
serializa integradores; las huellas protegen frente a editores no cooperantes.
"""
from __future__ import annotations

import base64
from contextlib import contextmanager
import difflib
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
from uuid import uuid4
import yaml

if os.name != 'nt':
    import fcntl
from platform_fs import is_link_or_reparse, private_directory

from lib_ce import split_frontmatter, notes_in_vault, resolve_link, target_index, wiki_targets
from revisiones_dx import _document, _next_revision, _check_body, _write_atomic
from validar_boveda import validate
from transcripciones_permisos import authorized, permission_snapshot
from transcripciones_pipeline import source, coverage_report
from transcripciones_modelo import safe_id, safe_path
from referencias_externas import verify_references, read_reference
from integracion_d import KINDS_D, validate_d, target_binding
from transcripciones_evolucion import validate_transition
from operacion import load_registry
from transcripciones_destino import destination, classification, maximum, LEVELS

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"source": "fuente", "entity": None, "navigation": "mapa", "dx": "documento",
         "transcript_view": "transcripcion"}
NAVIGATION_PATHS = {"Inicio.md", "Como_usar.md", "90_Sistema/Como_usar.md"}


def _navigation_adapter(entry):
    if entry["path"] in NAVIGATION_PATHS and entry["kind"] not in {"navigation_append", "navigation_patch"}:
        raise ValueError("Navegación existente requiere adaptador navigation_append/navigation_patch")


def _base_view(vault, entry, raw, base_sha):
    p = _target(vault, entry["path"])
    if p.parent != vault / "90_Sistema" / "Vistas" / "Transcripciones" or p.suffix != ".base" or base_sha is not None:
        raise ValueError("Base nueva sólo bajo Vistas/Transcripciones; no sobrescribir vistas")
    data = yaml.safe_load(raw.decode())
    filters = data.get("filters") if isinstance(data, dict) else None
    if not isinstance(filters, dict) or not filters.get("and") or not isinstance(data.get("views"), list) or not data["views"]:
        raise ValueError("Base requiere filters.and y views nativos")
    expressions = filters["and"]
    if not isinstance(expressions, list) or not all(isinstance(x, str) for x in expressions):
        raise ValueError("Filtros Base deben ser expresiones nativas")
    if not any(x in {'tipo == "fuente"', 'note.tipo == "fuente"'} for x in expressions) or not any("transcripcion_id" in x for x in expressions):
        raise ValueError("Base debe filtrar tipo fuente y transcripcion_id")
    if not isinstance(entry.get("id"), str) or not entry["id"].strip():
        raise ValueError("Base necesita identidad externa")


def _entity(meta, candidate, previous=None):
    """Entidades operativas propuestas; el catálogo no concede permisos."""
    tipo = meta.get("tipo")
    registry = load_registry()
    if not isinstance(tipo, str) or tipo not in registry or tipo in KINDS.values():
        raise ValueError("Tipo de entidad fuera del catálogo operativo")
    spec = registry[tipo]
    identity = safe_id(meta.get("id"))
    if identity != candidate["id"] or not identity.startswith(spec["prefijo"] + "-") or identity == spec["prefijo"] + "-":
        raise ValueError("Identidad de entidad incompatible con catálogo")
    if meta.get("clase") != tipo or any(k not in meta for k in spec["campos_comunes"]):
        raise ValueError("Metadatos comunes/clase de entidad incompletos")
    if (meta.get("estado_editorial") not in {"borrador", "en_revision"}
            or meta.get("estado_conocimiento") != "propuesta" or meta.get("vigencia") != "sin_verificar"
            or meta.get("sensibilidad") != "interno"):
        raise ValueError("Entidad requiere propuesta sin_verificar interna, borrador/en_revision")
    try:
        datetime.fromisoformat(str(meta["registrado_en"]).replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Entidad requiere registrado_en ISO explícito") from exc
    path = Path(candidate["path"])
    if path.suffix != ".md" or path.parent.as_posix() not in {spec["carpeta"], "90_Sistema/Bandeja_Propuestas"}:
        raise ValueError("Entidad requiere carpeta del catálogo o Bandeja_Propuestas")
    if not isinstance(meta.get("fuentes"), list) or not meta["fuentes"]:
        raise ValueError("Entidad sin fuentes")
    if not all(isinstance(x, str) and x.startswith("[[") and x.endswith("]]") and len(wiki_targets(x)) == 1 for x in meta["fuentes"]):
        raise ValueError("Fuentes deben ser wikilinks resolubles")
    if previous is not None:
        oldmeta, _ = split_frontmatter(previous.decode("utf8"))
        if any(oldmeta.get(k) != meta.get(k) for k in ("id", "tipo", "clase")):
            raise ValueError("No se puede cambiar identidad/tipo/clase")
        if (oldmeta.get("estado_editorial") not in {"borrador", "en_revision"}
                or oldmeta.get("estado_conocimiento") != "propuesta"
                or oldmeta.get("vigencia") != "sin_verificar" or oldmeta.get("sensibilidad") != "interno"):
            raise ValueError("No sobrescribir entidad aprobada, histórica o ratificada")


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _json(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def _safe(path):
    path = Path(path).expanduser()
    if not path.is_absolute() or any(is_link_or_reparse(p) for p in (path, *path.parents)):
        raise ValueError("Ruta absoluta sin symlinks requerida")
    return path.resolve()


def _target(vault, relative):
    p = Path(relative)
    if p.is_absolute() or ".." in p.parts or "Plantillas" in p.parts or p.suffix not in {".md", ".base"} or any(x.startswith(".") for x in p.parts):
        raise ValueError("Ruta de nota inválida")
    return _safe(vault / p)


def _inventory(vault):
    result = {}
    for path in sorted(vault.rglob("*")):
        if path.is_symlink():
            raise ValueError("Symlink en bóveda")
        if path.is_file():
            result[path.relative_to(vault).as_posix()] = _sha(path.read_bytes())
    return result


def _paths(snapshot):
    vault = _safe(snapshot["vault"])
    backup = _safe(snapshot["backup_dir"])
    bank = _safe(snapshot["bank_root"])
    if not vault.is_dir():
        raise ValueError("Bóveda inexistente")
    for forbidden in (vault, ROOT, bank):
        if backup == forbidden or forbidden in backup.parents or backup in forbidden.parents:
            raise ValueError("Respaldo debe estar separado de bóveda, Git y banco")
    if any((p / ".git").exists() for p in (backup, *backup.parents)):
        raise ValueError("Respaldo dentro de Git")
    return vault, backup


def _backend_errors(vault):
    """Extiende sólo resolución .base, sin silenciar otros errores del backend."""
    errors = validate(vault)["errores"]
    bases = list(vault.rglob("*.base"))
    for p in notes_in_vault(vault):
        for target in wiki_targets(p.read_text(encoding='utf-8')):
            if not target.endswith(".base"):
                continue
            matches = [b for b in bases if b.relative_to(vault).as_posix() == target]
            if not matches and "/" not in target:
                matches = [b for b in bases if b.name == target]
            if len(matches) == 1 and not matches[0].is_symlink():
                message = f"{p.relative_to(vault)}: enlace roto o ambiguo [[{target}]]"
                if message in errors:
                    errors.remove(message)
    return errors


def _access(candidate, bank, vault=None):
    """Reevalúa dependencias declaradas; nunca infiere derechos de una ruta."""
    raw = candidate.get("content")
    if raw is None:
        raw = base64.b64decode(candidate["content_b64"]).decode()
    if isinstance(raw, bytes):
        raw = raw.decode()
    fm, _ = split_frontmatter(raw)
    binding = candidate.get('destination_profile')
    private_policy = binding is not None
    if private_policy and (vault is None or candidate.get('destination_vault') != str(vault)):
        raise ValueError('DESTINATION_VAULT_MISMATCH')
    if not private_policy and (candidate.get("local_private_only") is True or candidate.get("sensibilidad", "interno") != "interno"):
        raise ValueError("Contenido privado no materializable por defecto")
    if not private_policy and fm.get("sensibilidad", "interno") != "interno":
        raise ValueError("Sensibilidad del contenido no materializable")
    if not private_policy and candidate["kind"] in {"source", "transcript_view"} and fm.get("sensibilidad") != "interno":
        raise ValueError("Fuente requiere sensibilidad interno explícita")
    checks = candidate.get("access_checks", [])
    if "source_refs" in candidate or "external_refs" in candidate:
        checks = [candidate, *checks]
    if not checks:
        raise ValueError("Candidato sin dependencias/permisos explícitos")
    verified_external, bound_sources = {}, set()
    for check in checks:
        refs, scope = check.get("source_refs"), check.get("scope")
        if not isinstance(scope, dict) or set(scope) != {"company", "audience", "purpose"} or scope["purpose"] != "local_analysis":
            raise ValueError("Contexto de permisos explícito inválido")
        if private_policy:
            if check.get('destination_profile') != binding or check.get('destination_vault') != str(vault):
                raise ValueError('DESTINATION_DEPENDENCY_MISMATCH')
            policy = destination(binding, vault, scope)
            required = classification(policy, refs or [])
            declared = maximum([check.get('sensibilidad', 'restringido'), required])
            if check.get('sensibilidad') != declared:
                raise ValueError('SENSITIVITY_DOWNGRADE')
            actual = ((yaml.safe_load(raw) or {}).get('sensibilidad') if candidate['kind'] == 'base_view'
                      else fm.get('sensibilidad'))
            if (candidate.get('sensibilidad') not in policy['allowed_sensitivities']
                    or actual != candidate.get('sensibilidad')
                    or actual not in LEVELS or LEVELS.index(actual) < LEVELS.index(declared)
                    or LEVELS.index(candidate['sensibilidad']) < LEVELS.index(declared)):
                raise ValueError('SENSITIVITY_DOWNGRADE')
        elif check.get("local_private_only") is True or check.get("sensibilidad", "interno") != "interno":
            raise ValueError("Dependencia privada no materializable")
        if "external_refs" in check:
            for purpose, field in (("local_analysis", "external_snapshot_sha256"), ("internal_query", "external_query_snapshot_sha256")):
                report = verify_references(bank, check["external_refs"], {**scope, "purpose": purpose},
                                           require_read=True, require_internal=True)
                if check.get(field, report["snapshot_sha256"]) != report["snapshot_sha256"]:
                    raise ValueError("Referencias/permisos externos cambiaron desde preparación")
                check[field] = report["snapshot_sha256"]
                for item in report["references"]:
                    ref = item["reference"]
                    verified_external[_json(ref)] = ref
                    if ref["kind"] == "external":
                        record = read_reference(bank, ref["reference_id"], ref["version_id"])
                        if record["source_type"] == "primary":
                            bound_sources.update(record.get("note_ids", []))
            if refs is None:
                continue
        if not isinstance(refs, list) or not refs:
            raise ValueError("Contexto de permisos explícito inválido")
        if permission_snapshot(bank, source_refs=refs, **scope) != check.get("permission_snapshot"):
            raise ValueError("Permisos cambiaron desde render/prepare")
        query_scope = {**scope, "purpose": "internal_query"}
        query_snapshot = permission_snapshot(bank, source_refs=refs, **query_scope)
        if check.get("query_permission_snapshot", query_snapshot) != query_snapshot:
            raise ValueError("Permisos de consulta cambiaron")
        for ref in refs:
            if _sha(source(bank, ref["tr_id"], ref["version_id"], scope)) != ref.get("sha256"):
                raise ValueError("Original cambió")
            if not authorized(bank, ref["tr_id"], ref["version_id"], **query_scope):
                raise ValueError("Fuente sin permiso internal_query")
        if check.get("run_id"):
            runpath = safe_path(bank, "analisis/" + safe_id(check["run_id"]) + ".json")
            if _sha(runpath.read_bytes()) != check.get("analysis_sha256"):
                raise ValueError("Bundle analítico cambió desde render")
            if not coverage_report(bank, check["tr_id"], check["run_id"], **scope)["evidence"]["current"]:
                raise ValueError("Análisis ya no vigente")
            bundle = json.loads(runpath.read_text(encoding='utf-8'))
            if bundle["source_refs"] != refs:
                raise ValueError("Dependencias analíticas alteradas")
            if check.get("semantic_review"):
                from transcripciones_fichas import validate_semantic_review
                validate_semantic_review(check["semantic_review"], bundle)
        check["query_permission_snapshot"] = query_snapshot
    if candidate["kind"] in {"source", "transcript_view"} and not any((r["tr_id"], r["version_id"]) == (fm.get("transcripcion_id"), fm.get("version_id")) for r in candidate.get("source_refs", [])):
        raise ValueError("Identidad de ficha no corresponde a sus dependencias")
    if candidate["kind"] == "source" and candidate.get("run_id") and candidate["run_id"] != fm.get("run_id"):
        raise ValueError("Ficha no corresponde al análisis verificado")
    # Estos campos son resultados de verificación, nunca autoridad del caller.
    candidate["verified_external_refs"] = [verified_external[k] for k in sorted(verified_external)]
    candidate["bound_source_ids"] = sorted(bound_sources)
    if candidate["kind"] in KINDS_D and not verified_external:
        raise ValueError("Adaptador D requiere dependencias externas verificadas")
    if verified_external and candidate["kind"] not in KINDS_D:
        raise ValueError("Referencias externas requieren adaptador D y revisión ligada")


def _validate_overlay(vault, entries):
    # Copia efímera privada: ejecuta el mismo validador del producto sin mutar origen.
    with tempfile.TemporaryDirectory(prefix="ce-preflight-") as folder:
        copy = Path(folder).resolve() / "vault"
        shutil.copytree(vault, copy)
        for e in entries:
            p = _target(copy, e["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(base64.b64decode(e["content_b64"], validate=True))
        errors = _backend_errors(copy)
        paths, names = target_index(copy)
        for e in entries:
            text = base64.b64decode(e["content_b64"]).decode()
            linked_text = text
            oldpath = _target(vault, e["path"])
            preserved_links = set()
            if (e["kind"] in {"legacy_source", "navigation_patch", "control_proposal"} or e.get("source_transition")) and oldpath.exists():
                preserved_links = set(wiki_targets(oldpath.read_text(encoding='utf-8')))
            if e["kind"] in {"navigation", "navigation_append", "navigation_patch"} and oldpath.exists():
                oldtext = oldpath.read_text(encoding='utf-8')
                if text.startswith(oldtext):
                    linked_text = text[len(oldtext):]
            checks = ([e] if "source_refs" in e else []) + e.get("access_checks", [])
            dependencies = {(r["tr_id"], r["version_id"]) for check in checks for r in check.get("source_refs", [])}
            dependencies.update((r["tr_id"], r["version_id"]) for r in e.get("verified_external_refs", []) if r["kind"] == "transcript")
            def permitted_source(meta):
                return ((meta.get("transcripcion_id"), meta.get("version_id")) in dependencies
                        or (not meta.get("transcripcion_id") and meta.get("id") in e.get("bound_source_ids", [])))
            for link in wiki_targets(linked_text):
                if link in preserved_links:
                    continue
                target = resolve_link(link, paths, names)
                if target:
                    linked_meta, _ = split_frontmatter(target.read_text(encoding='utf-8'))
                    if linked_meta.get("tipo") == "fuente" and not permitted_source(linked_meta):
                        errors.append("Fuente enlazada no está cubierta por permisos/dependencias del candidato")
            if e["kind"] not in {"entity", "dx"}:
                continue
            fm, _ = split_frontmatter(text)
            for source in fm.get("fuentes", []):
                links = wiki_targets(source)
                target = resolve_link(links[0], paths, names) if len(links) == 1 else None
                if target is None or split_frontmatter(target.read_text(encoding='utf-8'))[0].get("tipo") != "fuente":
                    errors.append("Referencia fuentes no resuelve a una fuente")
                else:
                    source_meta, _ = split_frontmatter(target.read_text(encoding='utf-8'))
                    if not permitted_source(source_meta):
                        errors.append("Fuente enlazada no está cubierta por permisos/dependencias del candidato")
        versions = set()
        for p in notes_in_vault(copy):
            fm, _ = split_frontmatter(p.read_text(encoding='utf-8'))
            if fm.get("tipo") in {"fuente", "transcripcion"} and fm.get("transcripcion_id"):
                identity = (fm["tipo"], fm["transcripcion_id"], fm.get("version_id"),
                            fm.get("view_variant") if fm["tipo"] == "transcripcion" else None)
                if identity in versions:
                    errors.append("Ficha/vista duplicada para original y versión")
                versions.add(identity)
        if errors:
            raise ValueError("Preflight: " + "; ".join(errors[:5]))


def _navigation_append(entry, raw, old):
    """El sello acredita bytes, no el alcance append-only de la operación."""
    meta, body = split_frontmatter(raw.decode("utf8"))
    previous_meta, previous_body = split_frontmatter(old.decode("utf8")) if old is not None else ({}, "")
    preserved = old is not None and raw.startswith(old)
    preserved_meta = meta == previous_meta
    if old is not None and entry.get("destination_profile"):
        preserved = body.startswith(previous_body)
        preserved_meta = {k: v for k, v in meta.items() if k != "sensibilidad"} == {
            k: v for k, v in previous_meta.items() if k != "sensibilidad"}
        old_level, new_level = previous_meta.get("sensibilidad", "interno"), meta.get("sensibilidad", "interno")
        if maximum([old_level, new_level]) != new_level:
            raise ValueError("SENSITIVITY_DOWNGRADE")
    if entry["path"] not in NAVIGATION_PATHS or not preserved or raw == old:
        raise ValueError("Navegación existente sólo append exacto en Inicio/Como_usar")
    if not preserved_meta or entry.get("id") != meta.get("id"):
        raise ValueError("Navegación requiere SHA e identidad/metadatos preservados")


def prepare_batch(candidates, vault_snapshot):
    """No escribe en la bóveda ni en el backup. Devuelve manifest JSON serializable."""
    vault, backup = _paths(vault_snapshot)
    before = _inventory(vault)
    if vault_snapshot.get("hashes") is not None and before != vault_snapshot["hashes"]:
        raise ValueError("Snapshot obsoleto")
    entries, seen, identities = [], set(), set()
    for c in candidates:
        c = json.loads(_json({k: v for k, v in c.items() if k != "content"})) | {"content": c["content"]}
        if c.get('destination_profile') != vault_snapshot.get('destination_profile'):
            raise ValueError('DESTINATION_PROFILE_MISMATCH')
        _access(c, _safe(vault_snapshot["bank_root"]), vault)
        p = _target(vault, c["path"])
        rel = p.relative_to(vault).as_posix()
        _navigation_adapter({**c, "path": rel})
        if rel in seen:
            raise ValueError("Destino duplicado")
        seen.add(rel)
        if not isinstance(c.get("id"), str) or not c["id"] or c["id"] in identities:
            raise ValueError("Identidad de candidato ausente/duplicada")
        identities.add(c["id"])
        raw = c["content"].encode() if isinstance(c["content"], str) else bytes(c["content"])
        meta, body = split_frontmatter(raw.decode("utf8"))
        if p.exists() and c.get('destination_profile'):
            old_meta = yaml.safe_load(p.read_text(encoding='utf-8')) if c['kind'] == 'base_view' else split_frontmatter(p.read_text(encoding='utf-8'))[0]
            new_meta = yaml.safe_load(raw) if c['kind'] == 'base_view' else meta
            old_level = old_meta.get('sensibilidad', 'interno')
            if maximum([old_level, new_meta.get('sensibilidad', 'interno')]) != new_meta.get('sensibilidad', 'interno'):
                raise ValueError('SENSITIVITY_DOWNGRADE')
        kind = c["kind"]
        special = kind in {"base_view", "navigation_append"} or kind in KINDS_D
        if not special and (kind not in KINDS or (kind != "entity" and meta.get("tipo") != KINDS[kind]) or not c.get("id") or meta.get("id") != c["id"]):
            raise ValueError("Tipo/identidad de candidato inválido")
        if not special and meta.get("estado_editorial") not in {"borrador", "en_revision"}:
            raise ValueError("Salida semántica debe ser borrador/en_revision")
        old = p.read_bytes() if p.exists() else None
        if "expected_sha256" in c and c["expected_sha256"] != (_sha(old) if old is not None else None):
            raise ValueError("Candidato con SHA base obsoleto")
        if old is not None and not special:
            oldmeta, _ = split_frontmatter(old.decode("utf8"))
            if oldmeta.get("id") != meta["id"] or oldmeta.get("tipo") != meta["tipo"]:
                raise ValueError("No se puede cambiar identidad/tipo")
            if oldmeta.get("estado_editorial") not in {"borrador", "en_revision"}:
                raise ValueError("No sobrescribir nota aprobada o histórica")
            sensitivity = {"interno": 0, "confidencial": 1, "restringido": 2}
            if oldmeta.get("sensibilidad") in sensitivity and sensitivity.get(meta.get("sensibilidad"), -1) < sensitivity[oldmeta["sensibilidad"]]:
                raise ValueError("No rebajar sensibilidad existente")
        if kind in KINDS_D:
            target_binding(vault, c)
            validate_d(vault, _safe(vault_snapshot["bank_root"]), c, raw, old)
        elif kind == "base_view":
            _base_view(vault, c, raw, _sha(old) if old is not None else None)
        elif kind == "navigation_append":
            _navigation_append({**c, "path": rel}, raw, old)
            if "expected_sha256" not in c:
                raise ValueError("Navegación requiere SHA e identidad/metadatos preservados")
        elif p.suffix != ".md":
            raise ValueError("Notas requieren extensión Markdown")
        elif kind in {"source", "transcript_view"}:
            location_ok = (p.parent == vault / "50_Fuentes" if kind == "source"
                           else vault / "50_Fuentes" / "Transcripciones" in p.parents)
            if not location_ok or not meta.get("transcripcion_id") or not meta.get("version_id"):
                raise ValueError("Fuente requiere carpeta canónica, transcripcion_id y version_id")
            if old is not None and oldmeta.get("transcripcion_id") != meta.get("transcripcion_id"):
                raise ValueError("No sustituir identidad de transcripción")
            if kind == "transcript_view" and old is not None and old != raw:
                raise ValueError("Vista íntegra existente es inmutable")
            if kind == "source" and old is not None:
                if any(oldmeta.get(k) != meta.get(k) for k in ("version_id", "run_id")) and not c.get("source_transition"):
                    raise ValueError("Cambio de versión/análisis requiere transición verificada")
                if c.get("source_transition"):
                    c["source_previous_b64"] = base64.b64encode(old).decode()
                    _check_evolution(vault, _safe(vault_snapshot["bank_root"]), c, raw)
        elif kind == "entity":
            _entity(meta, c, old)
        elif kind == "navigation":
            if p.parent != vault / "00_Mapas":
                raise ValueError("Navegación sólo en 00_Mapas")
        else:
            target, previous_meta, previous_body, _ = _document(vault, meta.get("doc_id", ""))
            if target != p or str(meta.get("revision")) != _next_revision(str(previous_meta["revision"])):
                raise ValueError("D/X requiere revisión consecutiva de documento existente")
            stable = set(previous_meta) - {"revision", "estado_editorial", "fuentes"}
            if any(meta.get(k) != previous_meta[k] for k in stable) or not set(previous_meta.get("fuentes", [])).issubset(meta.get("fuentes", [])):
                raise ValueError("D/X no permite retirar metadatos/fuentes previos")
            _check_body(vault, p, previous_body, body)
        protections = {k: c[k] for k in ("scope", "source_refs", "permission_snapshot", "query_permission_snapshot",
                       "access_checks", "local_private_only", "sensibilidad", "tr_id", "run_id", "analysis_sha256", "semantic_review",
                       "external_refs", "external_snapshot_sha256", "external_query_snapshot_sha256", "verified_external_refs", "bound_source_ids",
                       "candidate_ref", "target_binding", "review_binding", "patches", "destination_profile", "destination_vault") if k in c}
        for key in ("source_transition", "source_previous_b64"):
            if key in c:
                protections[key] = c[key]
        if kind in KINDS_D:
            protections["base_content_b64"] = base64.b64encode(old).decode() if old is not None else None
        entries.append({**protections, "path": rel, "id": c["id"], "kind": kind,
                        "base_sha": _sha(old) if old is not None else None,
                        "proposed_sha": _sha(raw), "content_b64": base64.b64encode(raw).decode(),
                        "diff": "\n".join(difflib.unified_diff((old or b"").decode().splitlines(), raw.decode().splitlines(), fromfile=rel, tofile=rel))})
    if not entries:
        raise ValueError("Lote vacío")
    _validate_overlay(vault, entries)
    written_paths = {_target(vault, e["path"]) for e in entries}
    for e in entries:
        _access(e, _safe(vault_snapshot["bank_root"]), vault)
        if e["kind"] in {"proposal_staging", "control_proposal"} and _target(vault, e["target_binding"]["path"]) in written_paths:
            raise ValueError("Un lote de propuestas no modifica sus objetivos empresariales")
        if any(_target(vault, v["path"]) in written_paths for v in e.get("source_transition", {}).get("history_views", [])):
            raise ValueError("El lote no debe reescribir vistas históricas")
        for ref in e.get("verified_external_refs", []):
            if ref["kind"] == "external":
                record = read_reference(_safe(vault_snapshot["bank_root"]), ref["reference_id"], ref["version_id"])
                if Path(record["locator"]["value"]) in written_paths:
                    raise ValueError("Una referencia externa no puede ser objetivo mutable del mismo lote")
    if _inventory(vault) != before:
        raise ValueError("Bóveda cambió durante prepare")
    manifest = {"schema": 1, "batch_id": uuid4().hex, "vault": str(vault), "backup_dir": str(backup),
                "bank_root": str(_safe(vault_snapshot["bank_root"])), "snapshot": before, "entries": entries}
    manifest["manifest_sha"] = _sha(_json(manifest))
    return manifest


def _manifest(m):
    payload = {k: v for k, v in m.items() if k != "manifest_sha"}
    if _sha(_json(payload)) != m.get("manifest_sha"):
        raise ValueError("Manifest alterado")
    if len(m["batch_id"]) != 32 or any(c not in "0123456789abcdef" for c in m["batch_id"]):
        raise ValueError("Batch ID inválido")
    vault, backup = _paths(m)
    for i, e in enumerate(m["entries"]):
        target = _target(vault, e["path"])
        _navigation_adapter({**e, "path": target.relative_to(vault).as_posix()})
        raw = base64.b64decode(e["content_b64"], validate=True)
        if _sha(raw) != e["proposed_sha"]:
            raise ValueError("Contenido alterado")
        checks = ([e] if "external_refs" in e else []) + e.get("access_checks", [])
        if any("external_refs" in check and any(not isinstance(check.get(key), str) or len(check[key]) != 64
               for key in ("external_snapshot_sha256", "external_query_snapshot_sha256")) for check in checks):
            raise ValueError("Manifest externo sin snapshots explícitos")
        fm, _ = split_frontmatter(raw.decode())
        path = _target(vault, e["path"])
        previous = path.read_bytes() if path.exists() else None
        operational_types = set(load_registry()) - {"fuente"}
        oldmeta = split_frontmatter(previous.decode())[0] if previous is not None else {}
        if e.get('destination_profile') and previous is not None and _sha(previous) == e['base_sha']:
            old_level = (yaml.safe_load(previous) if e['kind'] == 'base_view' else oldmeta).get('sensibilidad', 'interno')
            new_level = (yaml.safe_load(raw) if e['kind'] == 'base_view' else fm).get('sensibilidad', 'interno')
            if maximum([old_level, new_level]) != new_level:
                raise ValueError('SENSITIVITY_DOWNGRADE')
        if e["kind"] != "entity" and any(meta.get("tipo") in operational_types for meta in (fm, oldmeta)):
            raise ValueError("Tipo operativo requiere adapter entity; no cambiar identidad/tipo")
        if e.get("source_transition"):
            _check_evolution(vault, _safe(m["bank_root"]), e, raw)
        if e["kind"] in KINDS:
            if fm.get("id") != e["id"] or (e["kind"] != "entity" and fm.get("tipo") != KINDS[e["kind"]]) or fm.get("estado_editorial") not in {"borrador", "en_revision"}:
                raise ValueError("Manifest no puede aprobar ni cambiar tipo/identidad")
            if previous is not None and _sha(previous) == e["base_sha"]:
                oldmeta, _ = split_frontmatter(previous.decode())
                if any(oldmeta.get(k) != fm.get(k) for k in ("id", "tipo")):
                    raise ValueError("Manifest no puede cambiar identidad/tipo existente")
                if oldmeta.get("estado_editorial") not in {"borrador", "en_revision"}:
                    raise ValueError("No sobrescribir nota aprobada o histórica")
            if e["kind"] == "entity":
                if e["base_sha"] != m["snapshot"].get(e["path"]):
                    raise ValueError("Entidad no corresponde al snapshot base")
                _entity(fm, e, previous)
        elif e["kind"] in KINDS_D:
            previous = base64.b64decode(e["base_content_b64"], validate=True) if e.get("base_content_b64") is not None else None
            if (_sha(previous) if previous is not None else None) != e["base_sha"]:
                raise ValueError("Bytes base D alterados")
            validate_d(vault, _safe(m["bank_root"]), e, raw, previous)
        elif e["kind"] == "navigation_append":
            if e["base_sha"] is None or e["base_sha"] != m["snapshot"].get(e["path"]):
                raise ValueError("Navegación no corresponde al snapshot base")
            # Tras escribir (o durante rollback) la bóveda ya no contiene la base.
            # Sólo el backup del journal de este manifest puede sustituirla.
            if previous is None or _sha(previous) != e["base_sha"]:
                directory, _, journal = _journal(m, backup)
                if journal is None:
                    raise ValueError("Conflicto SHA en navegación")
                previous = _safe(directory / f"{i}.backup").read_bytes()
                if _sha(previous) != e["base_sha"]:
                    raise ValueError("Respaldo de navegación alterado")
            _navigation_append(e, raw, previous)
        elif e["kind"] == "base_view":
            if e["path"] in m["snapshot"]:
                raise ValueError("Base nueva no puede sobrescribir snapshot existente")
            _base_view(vault, e, raw, e["base_sha"])
        else:
            raise ValueError("Tipo de operación desconocido")
    return vault, backup


@contextmanager
def _lock(vault):
    # Ubicación estable por bóveda, independiente del directorio de backup.
    folder = _safe(vault.parent / (".ce-integracion-" + _sha(str(vault).encode())[:20]))
    if os.name == 'nt':
        from windows_fs import file_lock
        private_directory(folder)
        with file_lock(folder / 'writer.lock', blocking=False):
            yield folder
        return
    folder.mkdir(mode=0o700, exist_ok=True)
    lock = _safe(folder / "writer.lock")
    with lock.open("a+b") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield folder
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def _save(path, obj):
    _safe(path)
    _write_atomic(path, _json(obj))
    if os.name == 'nt':
        from windows_fs import flush_directory
        flush_directory(path.parent)
        return
    fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _checkpoint(stage, path):
    """Punto de fallo inyectable únicamente por tests, sin configuración productiva."""


def _journal(m, backup):
    directory = _safe(backup / m["batch_id"])
    path = _safe(directory / "journal.json")
    if not path.exists():
        return directory, path, None
    journal = json.loads(path.read_text(encoding='utf-8'))
    if journal.get("manifest_sha") != m["manifest_sha"]:
        raise ValueError("Journal pertenece a otro manifest")
    return directory, path, journal


def _current(vault, entry):
    p = _target(vault, entry["path"])
    return _sha(p.read_bytes()) if p.exists() else None


def _check_evolution(vault, bank, entry, raw=None):
    proof = entry["source_transition"]
    previous = base64.b64decode(entry["source_previous_b64"], validate=True)
    if entry["kind"] != "source" or proof["path"] != entry["path"] or _sha(previous) != proof["previous_source_sha256"]:
        raise ValueError("Transición no corresponde a ficha/bytes previos")
    if entry.get("run_id") != proof["next_run_id"] or entry.get("tr_id") != proof["tr_id"]:
        raise ValueError("Transición no corresponde al análisis actual")
    if "base_sha" in entry and _sha(previous) != entry["base_sha"]:
        raise ValueError("Transición no corresponde al snapshot base")
    snapshot = {v["path"]: _target(vault, v["path"]).read_text(encoding='utf-8') for v in proof["history_views"]}
    candidate = raw if raw is not None else base64.b64decode(entry["content_b64"], validate=True)
    validate_transition(bank, proof, previous.decode(), candidate.decode(), snapshot, entry["scope"])


def _live_d(vault, bank, entry):
    target_binding(vault, entry, allow_self_proposed=True)
    previous = base64.b64decode(entry["base_content_b64"], validate=True) if entry.get("base_content_b64") is not None else None
    validate_d(vault, bank, entry, base64.b64decode(entry["content_b64"], validate=True), previous)


def apply_batch(manifest, authorization, fencing_token):
    """Autorización declarada ligada al manifest y a quiescencia de editores."""
    m = manifest
    vault, backup = _manifest(m)
    if (authorization.get("manifest_sha") != m["manifest_sha"] or authorization.get("scope") != "apply_batch"
            or authorization.get("writers_quiescent") is not True
            or not str(authorization.get("responsable", "")).strip() or not str(authorization.get("referencia", "")).strip()):
        raise ValueError("Autorización explícita ligada al manifest requerida")
    if type(fencing_token) is not int or fencing_token < 1:
        raise ValueError("Fencing token entero positivo requerido")
    with _lock(vault) as lockroot:
        for e in m["entries"]:
            _access(e, _safe(m["bank_root"]), vault)
            if e.get("source_transition"):
                _check_evolution(vault, _safe(m["bank_root"]), e)
            if e["kind"] in KINDS_D:
                _live_d(vault, _safe(m["bank_root"]), e)
        fencefile = _safe(lockroot / "fence.json")
        fence = json.loads(fencefile.read_text(encoding='utf-8')) if fencefile.exists() else {"token": 0}
        if fencing_token < fence["token"] or (fencing_token == fence["token"] and fence.get("batch") != m["batch_id"]):
            raise ValueError("Fencing token obsoleto")
        _save(fencefile, {"token": fencing_token, "batch": m["batch_id"]})
        directory, jpath, j = _journal(m, backup)
        if j and j["state"] == "rolled_back":
            raise ValueError("Lote revertido; preparar nuevo manifest")
        if j and j["state"] == "rolling_back":
            raise ValueError("Completar rollback antes de otro apply")
        expected = dict(m["snapshot"])
        if j:
            for e in m["entries"]:
                if e["path"] in j["intents"] and _current(vault, e) == e["proposed_sha"]:
                    expected[e["path"]] = e["proposed_sha"]
        if _inventory(vault) != expected:
            raise ValueError("Conflicto SHA; ningún archivo nuevo se escribe")
        _validate_overlay(vault, m["entries"])
        if j is None:
            # Una caída entre mkdir y journal deja sólo un directorio vacío.
            directory.mkdir(mode=0o700, parents=True, exist_ok=True)
            if any(directory.iterdir()):
                raise ValueError("Directorio de lote sin journal contiene archivos desconocidos")
            j = {"manifest_sha": m["manifest_sha"], "state": "backing_up", "intents": [], "authorization": authorization}
            _save(jpath, j)
        if j["state"] == "backing_up":
            for i, e in enumerate(m["entries"]):
                if e["base_sha"] is not None:
                    raw = _target(vault, e["path"]).read_bytes()
                    if _sha(raw) != e["base_sha"]:
                        raise ValueError("Cambio durante respaldo")
                    bp = _safe(directory / f"{i}.backup")
                    _write_atomic(bp, raw)
                    if _sha(bp.read_bytes()) != e["base_sha"]:
                        raise ValueError("Respaldo no verificable")
                    _checkpoint("backup_written", e["path"])
            j["state"] = "prepared"
            _save(jpath, j)
        _checkpoint("backups_ready", None)
        for i, e in enumerate(m["entries"]):
            if e["base_sha"] is not None:
                bp = _safe(directory / f"{i}.backup")
                if _sha(bp.read_bytes()) != e["base_sha"]:
                    raise ValueError("Respaldo alterado")
        for e in m["entries"]:
            _access(e, _safe(m["bank_root"]), vault)
            if e.get("source_transition"):
                _check_evolution(vault, _safe(m["bank_root"]), e)
            if e["kind"] in KINDS_D:
                _live_d(vault, _safe(m["bank_root"]), e)
            if e["path"] in j["intents"] and _current(vault, e) == e["proposed_sha"]:
                continue
            if _current(vault, e) != e["base_sha"]:
                raise ValueError("Conflicto concurrente; reanudar/revertir con journal")
            if e["path"] not in j["intents"]:
                j["intents"].append(e["path"])
            j["state"] = "applying"
            _save(jpath, j)
            _checkpoint("intent_saved", e["path"])
            target = _target(vault, e["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            if _current(vault, e) != e["base_sha"]:
                raise ValueError("Conflicto concurrente antes de replace")
            _access(e, _safe(m["bank_root"]), vault)
            if e.get("source_transition"):
                _check_evolution(vault, _safe(m["bank_root"]), e)
            if e["kind"] in KINDS_D:
                _live_d(vault, _safe(m["bank_root"]), e)
            _write_atomic(target, base64.b64decode(e["content_b64"]))
            _checkpoint("file_written", e["path"])
        if _backend_errors(vault):
            raise ValueError("Validación posterior falló; journal permite recuperación")
        j["state"] = "applied"
        _save(jpath, j)
        return {"state": "applied", "batch_id": m["batch_id"], "journal": str(jpath), "aprobado": False}


def rollback_batch(manifest):
    """Revierte sólo bytes escritos por este lote; nunca pisa ediciones posteriores."""
    m = manifest
    vault, backup = _manifest(m)
    with _lock(vault):
        for e in m["entries"]:
            if e["kind"] in KINDS_D or e.get("verified_external_refs") or e.get("source_transition"):
                _access(e, _safe(m["bank_root"]), vault)
            if e.get("source_transition"):
                _check_evolution(vault, _safe(m["bank_root"]), e)
            if e["kind"] in KINDS_D:
                _live_d(vault, _safe(m["bank_root"]), e)
        directory, jpath, j = _journal(m, backup)
        if j is None:
            raise ValueError("No existe journal para revertir")
        if j["state"] == "rolled_back":
            return {"state": "rolled_back", "batch_id": m["batch_id"]}
        restore = []
        for i, e in enumerate(m["entries"]):
            current = _current(vault, e)
            if current == e["base_sha"]:
                continue
            if e["path"] not in j["intents"] or current != e["proposed_sha"]:
                raise ValueError("Edición posterior; rollback rechazado")
            raw = None
            if e["base_sha"] is not None:
                raw = _safe(directory / f"{i}.backup").read_bytes()
                if _sha(raw) != e["base_sha"]:
                    raise ValueError("Respaldo alterado")
            restore.append((e, raw))
        j["state"] = "rolling_back"
        _save(jpath, j)
        for e, raw in restore:
            if e["kind"] in KINDS_D or e.get("verified_external_refs") or e.get("source_transition"):
                _access(e, _safe(m["bank_root"]), vault)
            if e.get("source_transition"):
                _check_evolution(vault, _safe(m["bank_root"]), e)
            if e["kind"] in KINDS_D:
                _live_d(vault, _safe(m["bank_root"]), e)
            if _current(vault, e) != e["proposed_sha"]:
                raise ValueError("Edición concurrente; rollback detenido")
            p = _target(vault, e["path"])
            if raw is None:
                p.unlink()
            else:
                _write_atomic(p, raw)
            _checkpoint("file_restored", e["path"])
        j["state"] = "rolled_back"
        _save(jpath, j)
        return {"state": "rolled_back", "batch_id": m["batch_id"]}
