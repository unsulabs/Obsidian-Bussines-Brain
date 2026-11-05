# Local operations and recovery

[Español](../es/operations.md) · [CLI](cli-reference.md) · [Testing](testing.md)

## Product and instance updates

Updating the checkout never updates a private business automatically. Do not run `crear` again or copy `plantilla_boveda/` over an existing vault. Its version, content, plugins and permissions remain its own. There is no general, proven migration engine for all historical/future schemas. The narrow migrations below have different guards and must not be generalized.

Before an authorized change: resolve the vault with `obsidian-router`; inspect configuration and source authority; identify exact files/versions; create a private external backup and rehearse restoration in an isolated copy; review the diff; stop writers; apply only the approved scope; verify hashes and useful behavior. Preserve unrelated local changes. A dirty checkout may require an isolated candidate to attribute acceptance to a commit; it is not a reason to discard work or block ordinary consultation.

## Python and path diagnosis

Run `python scripts/cerebro.py doctor` first. It is read-only and loads before product dependencies. If a command reports a missing module, inspect the executable and already available Python environments; check `import yaml, jsonschema` with the intended interpreter. On macOS, `/opt/homebrew/bin/python3.11` may be available, but verify it rather than assuming. Install `requirements.txt` only with applicable authorization. Record the interpreter used.

The path guard in `scripts/documentos.py` recognizes only macOS's verified native `/var` → `/private/var` and `/tmp` → `/private/tmp` ancestors. It verifies both readlink target and physical resolution. User-created symlinks, input-file symlinks and other aliases remain rejected; no exception applies outside Darwin. Do not weaken path guards to fix a fixture. Local macOS acceptance checks default temporary paths, `TMPDIR=/tmp` and `TMPDIR=/private/tmp`, while retaining negative symlink tests. A changed TMPDIR alone does not prove a fix.

## D/X revisions and editorial promotion

`previsualizar-dx` is read-only. `preparar-dx` creates PRDX JSON plus a `.snapshot` under `90_Sistema/Propuestas_DX`, without changing the document. `aplicar-dx` checks the original and candidate SHA, source-set SHA when sources change, and external backup. It records internal history under `90_Sistema/Historial_DX`, replaces the file atomically and validates; a validation failure attempts restoration. Keep existing block IDs; ordinary revision cannot silently remove or rename them. Approved/withdrawn documents are refused by this path. Successful application stays in review, not approved.

`restaurar-dx` needs a fresh authorization and current SHA, producing a **new revision** from a historical snapshot. It does not rewind the revision counter or delete history. CLI locks coordinate its own writers, not Obsidian edits.

`evaluar-dx` records human G1–G7 findings without changing the document. Only a valid integral recommendation, sufficient task coverage, exact document hash, explicit authorization, backup and literal `APROBAR <doc_id> <first 12 SHA characters>` allow `aprobar-dx`. The body remains unchanged and revision advances. This is editorial state, not proof of financial/contractual validity or authenticated human identity.

## Transcript batch integration

The APIs are local Python functions; there is no invented integration CLI:

```python
manifest = prepare_batch(candidates, {
    "vault": "/private/business-vault",
    "backup_dir": "/private/backups/batch-001",
    "bank_root": "/private/transcript-bank",
})
# Only after genuine, scope-specific authorization and writer shutdown:
result = apply_batch(manifest, {
    "manifest_sha": manifest["manifest_sha"],
    "scope": "apply_batch",
    "writers_quiescent": True,
    "responsable": "Authorized operator",
    "referencia": "Reference to the actual authorization",
}, fencing_token=1)
# A later authorized recovery may use rollback_batch(manifest).
```

Import these functions from `scripts/transcripciones_integracion.py` in the script environment. `prepare_batch` does not write to the vault or backup: it validates an overlay in a temporary private copy and returns a full private diff/snapshot/manifest. Store that manifest privately because it contains original/proposed bytes. `bank_root` is mandatory; backup must be outside vault, repository and bank, with no symlinks.

Application revalidates source bytes, permission dependencies and the whole snapshot before the first write, then checks access at each write. It uses a cooperative `flock` next to the vault, persistent monotonic fencing and an external intent journal before individual atomic replacements. A new batch needs a larger token; an identical retry can reuse its token. The integrator does not consume queue tokens. It is not a globally atomic batch or a filesystem compare-and-swap against arbitrary editors.

After a crash, retry the same manifest to distinguish base/proposed states by journal and SHA. Do not replace established backups. Rollback prechecks all affected files/backups, restores only this batch's proposal and removes only its intact newly created files. Later edits block blind overwrite/deletion. A rolled-back batch cannot be reapplied; prepare a new manifest. D-adapter rollback additionally rechecks current external references and permissions; a revocation may require an authorized resolution, never fabricated grants or hand-edited hashes.

## Bases filters

The template's 16 Bases exclude `90_Sistema/Plantillas` and filter Markdown records so templates are not shown as real offers/documents. Existing vaults use `scripts/actualizar_vistas_bases.py`, first without `--apply`.

| Diagnosis | Meaning |
|---|---|
| `LISTO` | Original baseline view, eligible for filter update. |
| `LISTO_FILTRO` | Customized presentation but semantically original filter. |
| `AL_DIA`, `AL_DIA_PERSONALIZADO` | Filter already updated, possibly with custom presentation. |
| `BLOQUEADO_PERSONALIZADO`, `BLOQUEADO_FALTANTE` | Stop; do not force a modified business filter or missing view. |

After GUI observation, close Obsidian and stop synchronizers, **then regenerate the current plan**. GUI autosave can legitimately reserialize `.base` files and `workspace.json`; do not force old bytes back. Review and retain the exact `sha_plan`. With authorization limited to root filters:

```bash
python scripts/actualizar_vistas_bases.py --vault /private/business-vault
python scripts/actualizar_vistas_bases.py --vault /private/business-vault \
  --backup-dir /private/backups/bases-001 --sha-plan SHA_FROM_CURRENT_PLAN --apply
```

The updater backs up all 16 current views and existing workspace data. It replaces root `filters` only when eligible, preserving bytes from `views:` including `groupBy`, columns, tabs and comments, and validating unrelated structure. Concurrent changes trigger conflict/recovery; `workspace.json` is backed up but not automatically restored. Reopen Obsidian, verify offers/documents exclude templates, and verify D01/sources remain unchanged. Expected diagnostic: no pending/blocked views. YAML validity does not prove GUI behavior. These updates do not change sources, permissions, Sync or plugins.

## Readable names

New notes use readable titles with stable IDs in properties. Existing renames use `scripts/nombres_legibles.py` with a private specification such as `{"notas":[{"id":"D01","nombre":"Business direction"}]}`. Preview reports paths, affected links and `sha_plan`; apply requires that exact SHA and a new external backup directory.

```bash
python scripts/nombres_legibles.py --vault /private/business-vault --spec /private/names.json
# Add only after authorized review:
# --apply --sha-plan SHA_FROM_CURRENT_PLAN --backup-dir /private/backups/names-001
```

Close Obsidian and exclude concurrent edits. The tool updates wikilinks and Canvas file nodes, validates and preserves original bytes. Other link formats targeting old paths block for explicit handling; Bases are outside this migration. To reverse, first compare current files with the post-change manifest and restore only manifest paths/affected links. If later edits exist, prepare a reversal preserving them.

## Derived maps and routine closure

`mapa-conocimiento` previews; `publicar-mapa` needs authorization, literal confirmation, old/new SHA and backup. It refuses an unrelated personal map at its reserved path. Regenerate only an owned derived map; do not copy templates or alter notes/relations/Bases. Map freshness never establishes authority.

Close with files/IDs changed, exact checks performed and material pending work. Installation/migration acceptance includes isolated rehearsal and GUI checks; everyday continuity does not require repeating full acceptance or using a second computer. Spanish references: [updates](../ACTUALIZACIONES_Y_ROLLBACK.md), [Bases](../BASES_FILTROS_Y_ACTUALIZACION.md), [names](../NOMBRES_LEGIBLES.md), [macOS paths](../COMPATIBILIDAD_MACOS_RUTAS.md), [D/X revisions](../REVISIONES_DX_CON_HISTORIAL.md), [pilot closure](../CIERRE_DEL_PILOTO_0_3.md), [existing-instance acceptance](../../guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md).
