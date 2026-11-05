#!/usr/bin/env python3
"""Aceptación de integración Codex/GitHub/bóveda existente sin escribir en ella.

Inspecciona la bóveda PRIVADA solamente en lectura; crea un paquete mínimo
saneado FUERA de la bóveda y de Git. No instala ni migra. La GUI y el juicio
empresarial requieren comprobación humana adicional.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import zipfile

from aceptacion_piloto import preflight
from actualizar_vistas_bases import plan as bases_plan
from lib_ce import split_frontmatter, path_by_id
from mapa_conocimiento import previsualizar as preview_map
from operacion import safe_vault, summary
from validar_boveda import validate

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_CACHE_NAMES = {".DS_Store"}
PRECONDITION_STATES = {"PASS", "FAIL", "PENDIENTE", "NO_VERIFICADO"}


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _cmd(argv: list[str], cwd: Path, *, env: dict | None = None,
         timeout: int = 300) -> subprocess.CompletedProcess:
    return subprocess.run(argv, cwd=cwd, env=env, capture_output=True,
                          text=True, timeout=timeout, check=False)


def _git_info() -> dict:
    head = _cmd(["git", "rev-parse", "HEAD"], ROOT)
    status = _cmd(["git", "status", "--porcelain", "--untracked-files=normal"], ROOT)
    branch = _cmd(["git", "branch", "--show-current"], ROOT)
    if head.returncode or status.returncode or branch.returncode:
        raise ValueError("No fue posible leer Git; se requiere checkout real")
    return {"sha": head.stdout.strip(), "rama": branch.stdout.strip() or "(detached)",
            "arbol_limpio": not bool(status.stdout.strip()),
            "cambios_locales_cantidad": len(status.stdout.splitlines())}


def _inventory(vault: Path) -> dict[str, str]:
    """Compara todo archivo regular, incluido historial .snapshot y adjuntos.

    Sólo omite el metadato efímero de Finder. Nunca sigue enlaces fuera de la
    bóveda ni devuelve nombres o contenido al paquete saneado.
    """
    keys = {}
    for p in sorted(vault.rglob("*")):
        if p.is_symlink():
            raise ValueError("La bóveda contiene un enlace simbólico; no se puede certificar su integridad")
        if not p.is_file() or p.name in EXCLUDED_CACHE_NAMES:
            continue
        name = p.relative_to(vault).as_posix()
        keys[name] = _sha(p.read_bytes())
    return keys


def _suite(*, tmpdir: str | None) -> dict:
    env = os.environ.copy()
    env.pop("TMPDIR", None)
    if tmpdir is not None:
        env["TMPDIR"] = tmpdir
    try:
        proc = _cmd([sys.executable, "-m", "unittest", "discover",
                     "-s", "tests", "-q"], ROOT, env=env, timeout=300)
    except subprocess.TimeoutExpired:
        return {"estado": "FAIL", "pruebas": None, "causa": "TIEMPO_AGOTADO"}
    output = (proc.stderr or "") + "\n" + (proc.stdout or "")
    counts = re.findall(r"Ran (\d+) tests? in ", output)
    problems = re.findall(r"(?m)^(?:FAIL|ERROR): ([a-zA-Z_0-9.]+)", output)
    return {"estado": "PASS" if proc.returncode == 0 and counts else "FAIL",
            "pruebas": int(counts[-1]) if counts else None,
            "fallos": sorted(set(problems))[:25],
            "codigo_salida": proc.returncode,
            "modalidad": "TMPDIR_ALTERNATIVO" if tmpdir else "TEMPORAL_POR_DEFECTO"}


def _private_output(dest: Path, vault: Path) -> Path:
    raw = dest.expanduser()
    if not raw.is_absolute() or raw.is_symlink():
        raise ValueError("Directorio de informe: ruta absoluta y no simbólica")
    out = raw.resolve()
    if (out == ROOT or ROOT in out.parents or out in ROOT.parents
            or out == vault or vault in out.parents or out in vault.parents):
        raise ValueError("El informe debe estar fuera de Git y de la bóveda")
    if out.exists():
        raise FileExistsError("El directorio del informe ya existe; no sobrescribirlo")
    return out


def diagnosticar(vault_path: Path, *, esperado: str, ejecutar_tests: bool = True) -> dict:
    vault, cfg = safe_vault(vault_path)
    original = _inventory(vault)
    git = _git_info()
    if not re.fullmatch(r"[0-9a-f]{40}", esperado):
        raise ValueError("SHA objetivo Git de 40 caracteres requerido")

    validation = validate(vault)
    state = summary(vault)
    acceptance = preflight(vault)
    bases = bases_plan(vault)
    try:
        map_preview = preview_map(vault)
        map_state = {
            "estado": "PREVISUALIZABLE",
            "notas": map_preview["notas_en_mapa"],
            "relaciones": map_preview["relaciones_tipadas"],
            "sin_cambios": map_preview["sin_cambios"]}
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError):
        map_state = {"estado": "PENDIENTE_REVISION", "notas": None, "relaciones": None}

    d01 = path_by_id(vault, "D01")
    if d01 is not None and d01.parent == vault / "10_Conocimiento" and not d01.is_symlink():
        meta, _ = split_frontmatter(d01.read_text(encoding="utf8"))
        d01_state = {
            "presente": True, "sha256": _sha(d01.read_bytes()),
            "revision": str(meta.get("revision") or "SIN_DECLARAR"),
            "editorial": str(meta.get("estado_editorial") or "SIN_DECLARAR")}
    else:
        d01_state = {"presente": False, "sha256": None}

    tests = {"estado": "NO_VERIFICADO", "pruebas": None} if not ejecutar_tests else _suite(tmpdir=None)
    mac_alias = ({"estado": "NO_APLICA", "pruebas": None}
                 if sys.platform != "darwin" or not Path("/private/tmp").is_dir()
                 else ({"estado": "NO_VERIFICADO", "pruebas": None}
                       if not ejecutar_tests else _suite(tmpdir="/private/tmp")))
    final = _inventory(vault)
    before_keys, after_keys = set(original), set(final)
    changed = sum(original[k] != final[k] for k in before_keys & after_keys)
    unchanged = before_keys == after_keys and changed == 0
    base_states = {p["archivo"].split("/")[-1]: p["estado"] for p in bases["vistas"]}
    fail = (
        git["sha"] != esperado or not git["arbol_limpio"] or
        bool(validation["errores"]) or not unchanged or
        (ejecutar_tests and (tests["estado"] != "PASS" or
         (sys.platform == "darwin" and mac_alias["estado"] != "PASS")))
    )
    if fail:
        outcome = "FALLO_O_REQUIERE_CORRECCION"
    elif bases["estado"] != "AL_DIA":
        outcome = "CODIGO_VALIDADO_BOVEDA_PENDIENTE_BASES"
    elif not ejecutar_tests:
        outcome = "SOLO_LECTURA_SIN_EJECUTAR_SUITE"
    else:
        outcome = "PREFLIGHT_TECNICO_PASS_FALTAN_GATES_HUMANOS"
    return {
        "formato": "ce-integracion-local-1.0",
        "registrado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "modo": "BÓVEDA_SOLO_LECTURA",
        "repositorio": {"sha": git["sha"], "sha_esperado": esperado,
                        "coincide": git["sha"] == esperado,
                        "arbol_limpio": git["arbol_limpio"],
                        "cambios_locales_cantidad": git["cambios_locales_cantidad"]},
        "entorno": {"sistema": sys.platform, "python": platform.python_version(),
                    "temporal_por_defecto": "SIN_TMPDIR_FORZADO"},
        "boveda": {
            "version_instancia": str(cfg.get("version_instancia") or "SIN_DECLARAR"),
            "alcance_inventario": "Todos los archivos regulares salvo .DS_Store; enlaces simbólicos rechazados",
            "notas": validation["notas"], "fuentes": state["capas"]["fuentes"],
            "documentos_dx": state["documentos_dx"]["total"],
            "errores_estructura": len(validation["errores"]),
            "advertencias_estructura": len(validation["advertencias"]),
            "archivos_inventariados_antes": len(original),
            "archivos_inventariados_despues": len(final),
            "archivos_modificados": changed,
            "archivos_agregados": len(after_keys - before_keys),
            "archivos_eliminados": len(before_keys - after_keys),
            "intacta_en_esta_ejecucion": unchanged,
            "D01": d01_state,
        },
        "bases": {"estado": bases["estado"], "por_actualizar": bases["por_actualizar"],
                  "bloqueadas": bases["bloqueadas"], "vistas": base_states,
                  "aplicacion_ejecutada": False},
        "mapa": {**map_state, "publicacion_ejecutada": False},
        "pruebas_mac_o_local": tests,
        "pruebas_con_tmpdir_alternativo": mac_alias,
        "preflight": {"estado": acceptance["estado_tecnico"],
                      "gates_estructura": acceptance["gates"]},
        "manual": {
            "obsidian_gui_y_16_bases": "NO_VERIFICADO",
            "codex_nueva_sesion_sin_recordatorio": "NO_VERIFICADO",
            "restitucion_real_aislada_con_sha": "NO_VERIFICADO",
            "revision_editorial_del_propietario": "NO_VERIFICADO",
            "segundo_equipo_o_segunda_empresa": "NO_VERIFICADO",
            "datos_restringidos_y_permisos_reales": "NO_VERIFICADO",
        },
        "resultado_integracion": outcome,
        "datos_privados": "NO SE INCLUYEN CONTENIDOS NI RUTAS DE FUENTES EN ESTE REPORTE",
        "advertencia": "No se han probado GUI, semántica, identidad humana ni producción; la suite local no sustituye aceptación.",
    }


def entregar(report: dict, output: Path) -> dict:
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    json_file = output / "REPORTE_INTEGRACION_SANEADO.json"
    summary_file = output / "RESUMEN_INTEGRACION.md"
    json_file.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf8")
    lines = [
        "# Informe de integración local (sin documentos empresariales)",
        "",
        "- Git/commit: "+report["repositorio"]["sha"],
        "- Checkout limpio: "+str(report["repositorio"]["arbol_limpio"]),
        "- Bóveda intacta en el alcance inventariado: "+str(report["boveda"]["intacta_en_esta_ejecucion"]),
        "- Alcance del inventario: "+report["boveda"]["alcance_inventario"],
        "- D01: "+str(report["boveda"]["D01"]),
        "- Estructura, errores: "+str(report["boveda"]["errores_estructura"]),
        "- Bases: "+str(report["bases"]["estado"])+", bloqueadas: "+str(report["bases"]["bloqueadas"]),
        "- Pruebas con temporal por defecto: "+str(report["pruebas_mac_o_local"]),
        "- Resultado: "+report["resultado_integracion"],
        "",
        "## Pendiente de prueba con Codex/Obsidian",
        "La GUI, las 16 Bases, la restauración aislada, la nueva sesión autónoma,",
        "la segunda computadora y la aprobación empresarial no son comprobadas por este script.",
        "Nada fue migrado, editado ni publicado en la bóveda.",
    ]
    summary_file.write_text("\n".join(lines)+"\n", encoding="utf8")
    archive = output / "CE_INTEGRACION_LOCAL_SANEADA.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(json_file, "REPORTE_INTEGRACION_SANEADO.json")
        z.write(summary_file, "RESUMEN_INTEGRACION.md")
    return {"paquete": str(archive), "sha256": _sha(archive.read_bytes()),
            "resultado": report["resultado_integracion"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, required=True)
    parser.add_argument("--salida", type=Path, required=True,
                        help="Carpeta NUEVA absoluta, privada y externa a repo/bóveda")
    parser.add_argument("--commit-esperado", required=True)
    parser.add_argument("--sin-pruebas", action="store_true",
                        help="Sólo preflight, omite suites unittest (no da aceptación completa)")
    a = parser.parse_args()
    try:
        vault,_ = safe_vault(a.vault)
        target = _private_output(a.salida, vault)
        result = diagnosticar(vault, esperado=a.commit_esperado,
                              ejecutar_tests=not a.sin_pruebas)
        print(json.dumps(entregar(result, target), ensure_ascii=False, indent=2))
        # Reportes FAIL se entregan para reparar; la salida distinta de 0 no los borra.
        if result["resultado_integracion"] == "FALLO_O_REQUIERE_CORRECCION":
            raise SystemExit(2)
    except (ValueError, FileExistsError, OSError, TypeError, KeyError,
            json.JSONDecodeError) as exc:
        print("ERROR DE INTEGRACIÓN: "+type(exc).__name__+": "+str(exc),file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
