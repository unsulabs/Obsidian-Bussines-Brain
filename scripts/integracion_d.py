"""Adaptadores técnicos D: propuestas y parches acotados, sin aprobación editorial."""
import hashlib
from pathlib import Path

from lib_ce import split_frontmatter
from referencias_externas import read_reference
from transcripciones_modelo import safe_path, safe_id

KINDS_D = {"legacy_source", "navigation_patch", "control_proposal", "proposal_staging"}


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def target_binding(vault, candidate, *, allow_self_proposed=False):
    binding = candidate.get("target_binding")
    if not isinstance(binding, dict) or set(binding) != {"path", "id", "sha256"}:
        raise ValueError("D requiere objetivo path/id/SHA exactos")
    safe_id(binding["id"])
    path = safe_path(vault, binding["path"])
    if path.suffix != ".md" or not path.is_file():
        raise ValueError("Objetivo D debe ser nota existente")
    data = path.read_bytes()
    fm, _ = split_frontmatter(data.decode())
    if fm.get("id") != binding["id"]:
        raise ValueError("Identidad del objetivo D cambió")
    allowed = {binding["sha256"]}
    if allow_self_proposed and binding["path"] == candidate["path"]:
        allowed.add(candidate["proposed_sha"])
    if _sha(data) not in allowed:
        raise ValueError("SHA del objetivo D cambió")
    return binding


def validate_d(vault, bank, candidate, raw, previous):
    """Verifica contrato contra bytes base; derechos se revalidan en _access."""
    kind = candidate["kind"]
    path = safe_path(vault, candidate["path"])
    if kind not in KINDS_D or path.suffix != ".md":
        raise ValueError("Tipo/ruta D no admitido")
    fm, body = split_frontmatter(raw.decode())
    if fm.get("id") != candidate["id"] or fm.get("sensibilidad") != "interno":
        raise ValueError("Identidad/sensibilidad D inválida")
    binding = candidate.get("target_binding", {})
    review = candidate.get("review_binding")
    required = {"review_ref", "candidate_sha256", "target_id", "target_sha256", "decision", "reviewer", "evidence"}
    if not isinstance(review, dict) or set(review) != required:
        raise ValueError("D requiere revisión externa ligada a candidato/objetivo")
    if (review["candidate_sha256"] != _sha(raw) or review["target_id"] != binding.get("id")
            or review["target_sha256"] != binding.get("sha256") or not isinstance(review["reviewer"], str) or not review["reviewer"].strip()
            or not isinstance(review["evidence"], list) or not review["evidence"]
            or not all(isinstance(s, str) and s.strip() for s in review["evidence"])):
        raise ValueError("Revisión D no corresponde a bytes/objetivo")
    decision = "staging_only" if kind == "proposal_staging" else "technical"
    if review["decision"] != decision:
        raise ValueError("Revisión D no autoriza este tipo de operación")
    candidate_ref = candidate.get("candidate_ref")
    checked = candidate.get("verified_external_refs", [])
    for ref in (candidate_ref, review["review_ref"]):
        if not isinstance(ref, dict) or ref.get("kind") != "external" or ref not in checked:
            raise ValueError("Artefacto/revisión D fuera de dependencias verificadas")
        record = read_reference(bank, ref["reference_id"], ref["version_id"])
        if record["source_type"] != "control":
            raise ValueError("Artefacto/revisión D requiere referencia de control")
        if ref == candidate_ref and record["reading_state"] != "complete":
            raise ValueError("El candidato exacto requiere cotejo completo; su fuente puede ser parcial")
    if candidate_ref["sha256"] != _sha(raw):
        raise ValueError("Archivo candidato D no corresponde a versión autorizada")
    if kind == "proposal_staging":
        if previous is not None or path.parent != Path(vault) / "90_Sistema/Bandeja_Propuestas":
            raise ValueError("Staging sólo crea nueva nota en Bandeja")
        expected = {"tipo": "propuesta_de_cambio", "clase": "control", "estado_editorial": "borrador",
                    "estado_conocimiento": "propuesta", "vigencia": "sin_verificar",
                    "objetivo_id": binding.get("id"), "huella_objetivo": binding.get("sha256")}
        if any(fm.get(k) != value for k, value in expected.items()) or binding.get("path") == candidate["path"]:
            raise ValueError("Staging debe ser borrador ligado a objetivo/SHA; no lo reemplaza")
        return
    if previous is None:
        raise ValueError("Parche D requiere archivo existente")
    oldfm, oldbody = split_frontmatter(previous.decode())
    if fm != oldfm or raw[:len(raw) - len(body.encode())] != previous[:len(previous) - len(oldbody.encode())]:
        raise ValueError("Parche D debe preservar frontmatter byte por byte")
    if candidate.get("expected_sha256", candidate.get("base_sha")) != _sha(previous):
        raise ValueError("Parche D requiere SHA base exacto")
    if kind == "legacy_source":
        if path.parent != Path(vault) / "50_Fuentes" or fm.get("tipo") != "fuente" or fm.get("transcripcion_id"):
            raise ValueError("legacy_source sólo ficha previa no TR en 50_Fuentes")
        if binding.get("path") != candidate["path"] or binding.get("id") != fm["id"]:
            raise ValueError("Parche de fuente ligado a su propio objetivo")
    elif kind == "navigation_patch":
        allowed = {"Inicio.md", "Como_usar.md", "90_Sistema/Como_usar.md", "90_Sistema/Autoridades.md", "90_Sistema/Pendientes.md"}
        if (candidate["path"] not in allowed and path.parent != Path(vault) / "00_Mapas") or fm.get("tipo") not in {"mapa", "control", "manual"}:
            raise ValueError("navigation_patch fuera de navegación/control permitido")
        if binding.get("path") != candidate["path"] or binding.get("id") != fm["id"]:
            raise ValueError("Parche de navegación ligado a su propio objetivo")
    elif kind == "control_proposal":
        if path.parent != Path(vault) / "90_Sistema/Bandeja_Propuestas" or fm.get("tipo") != "propuesta_de_cambio" or fm.get("objetivo_id") != binding.get("id"):
            raise ValueError("Control técnico debe conservar propuesta y objetivo existente")
    patches = candidate.get("patches")
    if not isinstance(patches, list) or not patches:
        raise ValueError("Parche D requiere reemplazos explícitos")
    patched = oldbody
    for patch in patches:
        if (not isinstance(patch, dict) or set(patch) != {"old", "new"} or not isinstance(patch["old"], str)
                or not patch["old"] or not isinstance(patch["new"], str) or patched.count(patch["old"]) != 1):
            raise ValueError("Reemplazo D ambiguo o inválido")
        patched = patched.replace(patch["old"], patch["new"], 1)
    if patched != body or patched == oldbody:
        raise ValueError("Reemplazos D no reproducen exactamente el candidato")
