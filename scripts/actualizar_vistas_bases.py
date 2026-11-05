#!/usr/bin/env python3
"""Actualización controlada de filtros Bases desde la v0.2.0-alpha.

Sin --apply, solo informa. Con --apply exige respaldo fuera de Git y bóveda.
Conserva presentaciones personalizadas y no toca documentos empresariales.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
import re
from pathlib import Path
import shutil
import sys
import stat
from uuid import uuid4

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "plantilla_boveda" / "90_Sistema" / "Vistas"
MANIFEST = ROOT / "recursos" / "bases_baseline.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def release_baselines() -> dict[str, str]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf8"))
    if manifest.get("version") != "0.2.0-alpha":
        raise ValueError("Baseline de lanzamiento inesperado; revisar migración")
    return {entry["path"]: entry["sha256"] for entry in manifest["files"]
            if entry["path"].startswith("plantilla_boveda/90_Sistema/Vistas/")
            and entry["path"].endswith(".base")}


def _filters_only_patch(current: Path, master: Path, legacy: Path) -> bytes:
    """Sustituir SOLO filters; conservar todas las vistas personalizadas byte por byte.

    Exige que el filtro actual sea semánticamente el mismo del baseline 0.2.
    Cualquier cambio deliberado al propio filtro bloquea la operación.
    """
    before = current.read_text(encoding="utf8")
    baseline = yaml.safe_load(legacy.read_text(encoding="utf8"))
    prior = yaml.safe_load(before)
    updated = yaml.safe_load(master.read_text(encoding="utf8"))
    if not all(isinstance(x, dict) for x in (baseline, prior, updated)):
        raise ValueError("Base no tiene objeto YAML válido")
    if prior.get("filters") != baseline.get("filters"):
        raise ValueError("Filtro local difiere del original; requiere revisión humana")
    if not isinstance(prior.get("views"), list) or not prior["views"]:
        raise ValueError("La vista personalizada no tiene lista de vistas")
    # Solo reemplazar el bloque raíz de filters; otras claves quedan byte por byte.
    def span(text: str) -> int:
        if not text.startswith("filters:\n"):
            raise ValueError("El filtro no inicia el archivo: requiere revisión manual")
        match = re.search(r"(?m)^views:[ \t]*$", text)
        if not match:
            raise ValueError("No hay sección views reconocible")
        body = text[len("filters:\n"):match.start()]
        if re.search(r"(?m)^[A-Za-z_][A-Za-z0-9_-]*:", body):
            raise ValueError("Se encontraron claves raíz intermedias: migración manual")
        return match.start()
    prefix = master.read_text(encoding="utf8")
    candidate = prefix[:span(prefix)] + before[span(before):]
    proposed = yaml.safe_load(candidate)
    if (not isinstance(proposed, dict)
        or proposed.get("filters") != updated.get("filters")
        or {k:v for k,v in proposed.items() if k!="filters"} !=
           {k:v for k,v in prior.items() if k!="filters"}):
        raise ValueError("El resultado alteraría propiedades ajenas a los filtros")
    return candidate.encode("utf8")


def checked_vault(vault_path: Path) -> Path:
    original = vault_path.expanduser()
    if original.is_symlink():
        raise ValueError("La ruta de bóveda no puede ser enlace simbólico")
    vault = original.resolve()
    if not vault.is_dir() or not (vault / "90_Sistema" / "config_empresa.yaml").is_file():
        raise ValueError("Bóveda no reconocida; falta configuración empresarial")
    if vault == ROOT or vault.is_relative_to(ROOT) or ROOT.is_relative_to(vault):
        raise ValueError("Bóveda y repositorio maestro deben estar separados")
    config = yaml.safe_load((vault / "90_Sistema" / "config_empresa.yaml").read_text(encoding="utf8"))
    if not isinstance(config, dict) or not config.get("company_id"):
        raise ValueError("Configuración empresarial inválida")
    return vault


def plan(vault_path: Path) -> dict:
    vault = checked_vault(vault_path)
    baselines = release_baselines()
    sources = sorted(TEMPLATE.glob("*.base"))
    if len(sources) != 16:
        raise ValueError("El catálogo de vistas ya no coincide con esta migración")
    entries = []
    for source in sources:
        rel = Path("90_Sistema") / "Vistas" / source.name
        target = vault / rel
        old_key = "plantilla_boveda/" + rel.as_posix()
        if old_key not in baselines:
            raise ValueError("Falta baseline para " + old_key)
        new_sha = sha256(source)
        current_sha = sha256(target) if target.is_file() and not target.is_symlink() else None
        proposed_sha = None
        if target.is_symlink():
            state = "BLOQUEADO_SIMBOLICO"
        elif not target.is_file():
            state = "BLOQUEADO_FALTANTE"
        elif current_sha == new_sha:
            state, proposed_sha = "AL_DIA", new_sha
        elif current_sha == baselines[old_key]:
            state, proposed_sha = "LISTO", new_sha
        else:
            fixture = ROOT / "tests" / "fixtures_bases_v0_2" / source.name
            if not fixture.is_file() or sha256(fixture) != baselines[old_key]:
                raise ValueError("Fixture baseline alterado: " + source.name)
            try:
                now = yaml.safe_load(target.read_text(encoding="utf8"))
                master = yaml.safe_load(source.read_text(encoding="utf8"))
                if (isinstance(now, dict) and isinstance(master, dict)
                    and now.get("filters")==master.get("filters")
                    and isinstance(now.get("views"),list) and now["views"]):
                    state, proposed_sha = "AL_DIA_PERSONALIZADO", current_sha
                else:
                    content = _filters_only_patch(target, source, fixture)
                    state = "LISTO_FILTRO"
                    proposed_sha = hashlib.sha256(content).hexdigest()
            except (ValueError, UnicodeError, yaml.YAMLError):
                state = "BLOQUEADO_PERSONALIZADO"
        entries.append({"archivo": rel.as_posix(), "estado": state,
                        "sha_actual": current_sha, "sha_propuesto": proposed_sha})
    blocked = [x for x in entries if x["estado"].startswith("BLOQUEADO")]
    todo = [x for x in entries if x["estado"] in ("LISTO","LISTO_FILTRO")]
    fingerprint = hashlib.sha256(json.dumps(
        [{k: x.get(k) for k in ("archivo","estado","sha_actual","sha_propuesto")}
         for x in entries], sort_keys=True,ensure_ascii=True,
        separators=(",",":")).encode("utf8")).hexdigest()
    return {"boveda": str(vault), "sha_plan": fingerprint,
            "estado": "BLOQUEADO" if blocked else ("LISTO" if todo else "AL_DIA"),
            "por_actualizar": len(todo), "bloqueadas": len(blocked),
            "vistas": entries,
            "limite": "Comparación de hashes; falta prueba en Obsidian GUI"}


def apply(vault_path: Path, backup_dir: Path, *, expected_plan_sha: str | None = None) -> dict:
    report = plan(vault_path)
    if expected_plan_sha is not None and report["sha_plan"] != expected_plan_sha:
        raise ValueError("Las huellas de Bases cambiaron desde la revisión; volver a diagnosticar")
    if report["estado"] == "BLOQUEADO":
        raise ValueError("Hay vistas faltantes o personalizadas; nada se modificó")
    if report["estado"] == "AL_DIA":
        return {"resultado": "SIN_CAMBIOS", "actualizadas": 0, "respaldo": None}
    vault = Path(report["boveda"])
    raw_backup = backup_dir.expanduser()
    if not raw_backup.is_absolute() or raw_backup.is_symlink():
        raise ValueError("Respaldo requiere ruta absoluta sin enlace simbólico")
    backup_root = raw_backup.resolve()
    if (backup_root == vault or backup_root.is_relative_to(vault)
            or backup_root == ROOT or backup_root.is_relative_to(ROOT)):
        raise ValueError("Respaldo debe estar fuera de la bóveda y de Git")
    run = backup_root / ("bases-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                         + "-" + uuid4().hex[:8])
    run.mkdir(mode=0o700, parents=True, exist_ok=False)
    if stat.S_IMODE(run.stat().st_mode) & 0o077:
        raise PermissionError("Respaldo no privado: requiere permisos 0700")
    changed = []
    meta = []
    snapshots = []
    workspace_original = None
    workspace = vault / ".obsidian" / "workspace.json"
    try:
        # Copiar las 16 vistas actuales, incluidas las que ya están al día.
        # Así se conserva exactamente el estado tras cualquier autoguardado GUI.
        for entry in report["vistas"]:
            rel = Path(entry["archivo"])
            dst = vault / rel
            before = run / rel
            before.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dst, before)
            snapshots.append({"archivo": rel.as_posix(),
                              "sha256": sha256(dst)})
            if entry["estado"] not in ("LISTO","LISTO_FILTRO"):
                continue
            meta.append({"archivo": rel.as_posix(),
                         "modo": entry["estado"],
                         "original_sha256": sha256(dst),
                         "nuevo_sha256": entry["sha_propuesto"]})
        if workspace.exists() or workspace.is_symlink():
            if workspace.is_symlink() or not workspace.is_file():
                raise ValueError("Workspace de Obsidian no es archivo normal")
            workspace_original = sha256(workspace)
            target = run / ".obsidian" / "workspace.json"
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(workspace,target)
        (run / "manifiesto.json").write_text(
            json.dumps({"estado": "BACKUP_ANTES_DE_ESCRIBIR",
                        "sha_plan": report["sha_plan"],
                        "instantanea_vistas": snapshots,
                        "workspace_sha256": workspace_original,
                        "archivos": meta},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf8")
        baselines = release_baselines()
        for item in meta:
            rel = Path(item["archivo"])
            dst = vault / rel
            src = TEMPLATE / rel.name
            old_key = "plantilla_boveda/" + rel.as_posix()
            if dst.is_symlink() or sha256(dst) != item["original_sha256"]:
                raise RuntimeError("La vista cambió desde el diagnóstico: " + str(dst))
            if item["modo"] == "LISTO":
                if sha256(dst) != baselines[old_key]:
                    raise RuntimeError("Baseline modificado desde el diagnóstico")
                proposed = src.read_bytes()
            else:
                baseline = ROOT / "tests" / "fixtures_bases_v0_2" / src.name
                if sha256(baseline) != baselines[old_key]:
                    raise RuntimeError("Baseline no coincide con el manifiesto")
                proposed = _filters_only_patch(dst, src, baseline)
            if hashlib.sha256(proposed).hexdigest() != item["nuevo_sha256"]:
                raise RuntimeError("La propuesta cambió desde el preflight")
            temp = dst.with_name("." + dst.name + ".tmp-" + uuid4().hex[:8])
            try:
                shutil.copy2(dst, temp)  # conserva el modo local
                temp.write_bytes(proposed)
                os.replace(temp, dst)
            finally:
                if temp.exists():
                    temp.unlink()
            changed.append(rel)
            if sha256(dst) != item["nuevo_sha256"]:
                raise RuntimeError("Verificación pos-escritura falló: " + str(dst))
        # Una GUI abierta puede reserializar .base justo después de os.replace.
        # Verificar TODO el lote antes de certificar la migración.
        for item in meta:
            if sha256(vault / item["archivo"]) != item["nuevo_sha256"]:
                raise RuntimeError("Obsidian volvió a escribir una Base durante la migración; cerrar la GUI")
        if (workspace_original is not None and
                (not workspace.is_file() or sha256(workspace) != workspace_original)):
            raise RuntimeError("Obsidian reescribió workspace mientras migrábamos; cerrar aplicación y reintentar")
        if workspace_original is None and workspace.exists():
            raise RuntimeError("Obsidian creó workspace mientras migrábamos; cerrar aplicación y reintentar")
    except Exception:
        for rel in reversed(changed):
            shutil.copy2(run / rel, vault / rel)
        raise
    (run / "manifiesto.json").write_text(
        json.dumps({"estado": "APLICADO",
                    "sha_plan": report["sha_plan"],
                    "instantanea_vistas": snapshots,
                    "workspace_sha256": workspace_original,
                    "archivos": meta}, ensure_ascii=False, indent=2)
        + "\n", encoding="utf8")
    return {"resultado": "APLICADO", "actualizadas": len(changed),
            "filtros_sin_perder_personalizaciones":
                sum(1 for x in meta if x["modo"] == "LISTO_FILTRO"),
            "respaldo": str(run),
            "limite": "No prueba Obsidian GUI; verificar desde la aplicación"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, required=True)
    parser.add_argument("--apply", action="store_true",
                        help="Escribir tras autorización explícita y con respaldo")
    parser.add_argument("--backup-dir", type=Path,
                        help="Carpeta privada absoluta fuera de la bóveda y de Git")
    parser.add_argument("--sha-plan", help="Huella SHA-256 del plan revisado, obligatoria para --apply")
    args = parser.parse_args()
    try:
        if args.apply:
            if args.backup_dir is None or args.sha_plan is None:
                raise ValueError("--apply requiere --backup-dir y --sha-plan del diagnóstico vigente")
            data = apply(args.vault, args.backup_dir, expected_plan_sha=args.sha_plan)
        else:
            data = plan(args.vault)
        print(json.dumps(data, ensure_ascii=False, indent=2))
        if data.get("estado") == "BLOQUEADO":
            raise SystemExit(2)
    except (ValueError, OSError, RuntimeError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
