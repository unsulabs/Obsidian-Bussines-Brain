# Transcript custody, analysis and integration

[Español](../es/transcripts.md) · [CLI](cli-reference.md) · [Security](security.md)

## Complete assisted cycle

For material identified as a new conversation/transcript, activate `ce-banco-transcripciones` before summarizing: exact custody → analysis of all subjects → prior evidence and taxonomy → knowledge architecture → applied source card, complete text and justified connections → verification. This portable preference does not carry a company's permissions to another instance. Recover its private configuration and authority; a later instruction may narrow a particular delivery. No surveillance, training, publication, external services or account-wide download is implied.

The deterministic pipeline stores agent-authored work; it does not produce semantic analysis by calling a model. Its successful result is not independent semantic or business acceptance. Keep originals, analysis proposals and approved business knowledge distinct.

## Receipt and exact custody

All `scripts/transcripciones.py` subcommands require `--bank`, `--profile`, `--request-id`, `--purpose`. The profile declares `company_id` and `allowed_purposes`, optionally expected `bank`/`vault`. It limits requested capability but grants no source permission. Keep bank and private reports outside Git and vaults. Mutations preview by default; `--commit` applies them. `--output` writes a new immutable report, never replaces one. Results use `resultado.v1`; failures may return `BLOCKED` with normalized errors.

`registrar` accepts a sealed `capture-manifest.v1.json`. `ingresar` accepts a file, stdin or `--parts-manifest`, with account/source/attempt IDs. Those IDs identify receipts, not people. Multipart `parts: [{number, path}]` paths are relative to the descriptor; assembly follows numbers without separators or byte normalization. Declare closure and expected part count only when known. Open or incomplete receipts remain incomplete. A URL by itself is not captured content.

`permiso` records explicit grant/revoke decisions by `tr_id`, `version_id`, `company`, `audience`, `purpose`, with `authority`, `evidence`, `decided_at`. Purpose of the recording operation is `custody`; the decision carries its target purpose. No grant is copied across versions, accounts or purposes. The ledger records declarations, not authenticated identity.

## Segments, analysis and current selection

`segmentar` checks live permission and original bytes. `utf8-bytes-1` uses 4096-byte cores and 256-byte context by default; cores cover exactly once, overlap is context only. Preserve `bundle_id` and the exact `permission_snapshot`.

`analizar` accepts a submission with `tr_id`, `version_id`, `segment_bundle`, `run_id`, `permission_snapshot`, `agent_results`, `claims`, `relations`, `subject_matrix`, `global_reconciliation`, `analyzer_version`, `taxonomy_version`, `canonical_context_refs`, `supersedes_run_id`, `dependency_ids`. Use the schemas; each core needs substantive work or an explicit exception. Subjects classify against preserved category/axis IDs. Claims and relations remain `propuesta` or `en_revision`. Coverage checks spans, hashes, references and reconciliation; it does not certify meaning.

Canonical context is `{tr_id, version_id, sha256}` for preserved, permitted sources, never an arbitrary note path. Snapshots cover every cited/context/historical source, not a global ledger hash. Taxonomy updates require `previous_version` and an invalidation event; replaced bases cannot branch silently. Historical dependencies are reread and verified.

`cobertura` rechecks sources, permissions, taxonomy and bundles. A directly superseded run can have `dependency_current: true`, `current: false`, reason `superseded`; additional permission/dependency/context changes make it ineligible. Corruption or revoked permission blocks even historical access. Old bytes are retained.

## Retrieval and retrospective review

`indexar` builds a derived SQLite index for the exact scope and watermark (`current` or the value from `estado`). `buscar` requires private `--output`; console returns path/hash/counts, not source passages. Query JSON requires `query`, `company`, `audience`, `purpose`; optional fields are `task`, `entities`, `period`, `mode`, `references`, `limit`. Unknown fields are rejected. `task` defaults to query, must otherwise be nonempty text up to 2000 characters, and does not replace lexical query terms. `entities` is a unique list of resolved taxonomy identities; unresolved speaker labels do not qualify. Neither field accepts null.

`period` is null or inclusive ISO `{from,to}` with ordered endpoints, evaluated against known claim business dates (`asserted_at`, otherwise interpretable `valid_time`), not capture/import dates. No known date means no match. Filtering precedes FTS and the 1–40 result limit (default 10), including projected passages and relationships.

| `mode` | Selection |
|---|---|
| `exploracion` | Default: permitted sources and nonsuperseded analyses with current dependencies, retaining unverified states. |
| `actual` | Current analyses and `vigente`/`en_conflicto` claims; this still does not ratify them. |
| `historico` | Superseded runs only if dependencies and current permissions remain valid; labeled `historical_superseded`, never current. |

No match does not prove absence across the whole bank. References to external material remain unread locators. The package does not generate a business answer. Request-local caches expire and final disk fingerprints detect concurrent changes; see [architecture](architecture.md).

`estado --audience` produces a review snapshot with each version's eligibility. `revisar-antecedentes` requires the event's matching `sweep_snapshot`; agent results provide job/input hash, attempt, reviewed versions, state/reason, relations and proposals. `--previous` resumes an immutable review. Without results, semantic jobs remain pending. New sources or permission changes require a new snapshot. Resolved identities require an explicit preserved `--taxonomy-version`; no latest-version guess.

## Derived representations and source cards

`importar_representacion` / `import_representation` is a Python API, not a CLI. It preserves sealed DOM, speaker-header text and optional HTML bytes for an existing canonical version. Required `dom_source` and `with_speakers` artifacts and hashes must match the same key set. The `provider-groups-lf-v1` adapter reconstructs raw/headered text exactly; no whitespace or newline normalization. It stores UTF-8 `[start,end)` offsets, provider sentence IDs and unresolved provider labels. Parsed terminal HH:MM:SS values do not verify speakers or audiovisual alignment. Blobs publish before the immutable manifest; reruns finish interrupted publication without overwriting.

`render_source(tr_id, run_id, profile)` and `propose_navigation` return candidates without writing. They recheck current coverage, originals and permissions. Sensitivity is explicitly attested per source, defaulting to `restringido`; the most restrictive dependency/card wins. Cards retain all subjects, claims, reasons, exceptions and conflicts, plus exact full-text views and stable passage links. A source card's existing F-ID/path survives rerendering. Optional semantic-review bindings tie sealed submission/review hashes to the run; reviewer independence remains an operator attestation, and the card stays unratified.

Batch architecture packages cap at 30 subjects, 30 existing destinations and 90000 bytes; an oversized single subject blocks instead of truncating. They must be reasoned into `plan-conocimiento`, not accepted as business architecture automatically. Proposed navigation creates four new transcript Bases, a corpus map and minimal append-only additions to identified Inicio/Como_usar notes; it does not replace customized manuals or the existing 16 Bases.

## Integration, evolution and ordinary-file proposals

The Python APIs `prepare_batch`, `apply_batch`, `rollback_batch` validate explicit dependencies, source bytes, analysis and consultation permissions, candidate hashes and the full vault snapshot. Candidate kinds are `source`, `transcript_view`, `entity`, `dx`, `navigation`, `base_view`, `navigation_append`. New entities require `borrador`/`en_revision`, `propuesta`, `sin_verificar`, `interno`, explicit registration date and the real catalog type. Approved/historical notes are not overwritten.

Restricted material needs a valid sealed private-destination profile for the exact IDs/company/audience/vault plus live permissions; it is not declassified and adapter-specific restrictions still apply. See the [shared private-destination contract, Spanish reference](../../.agents/skills/ce-banco-transcripciones/references/destino-privado.md). Apply uses private external backup, journal, cooperative vault lock, monotonic fencing token and declared writer quiescence. Hash checks do not exclude microscopic races with uncooperative editors; see [operations](operations.md).

Source-card evolution follows immediate version lineage or direct run supersession, never a date-based latest choice. It preserves ID/path, custom properties and text outside generated boundaries; previous generated content becomes literal noncurrent history. Full-text views remain immutable; another run may need a new variant. `historial_fuentes` must equal the old chain plus exactly one verified entry. Historical dependencies require live permissions. A later edit blocks restoration.

External ordinary files use versioned `referencias_externas.py` metadata, current purpose grants and transitive dependencies, without copying or executing those files. D adapters allow exact unique body patches for `legacy_source`, `navigation_patch`, `control_proposal`; `proposal_staging` creates a proposal without editing its business target. Candidate/review files are hash-bound control references; primary-source bindings cannot be self-granted. Noninternal sensitivity is blocked in these adapters. Partial reading requires explicit permitted spans. A mutable target cannot also be its own dependency in a batch.

## Dataset candidates

`prepare_export` in `transcripciones_datasets.py` is a Python API, not training or publication. It accepts only `evaluation` or `training` with a separate current grant for every selected source/version. Missing permission excludes a whole candidate and annotations. Selections use exact UTF-8 passage/context hashes and explicit expert annotations; the tool does not validate their semantic quality.

Grouping joins versions, identical original hashes, clients and projects across the complete bank catalog, including excluded and cross-account bridges. Identity attestations must be complete: null means not applicable; `"unknown"` blocks export. Committed groups cannot leak between purposes (`SPLIT_LEAKAGE`); revoked access does not erase historical use or release the split. The guarantee is bank-local.

Private `dataset-manifest.v2` contains permitted payload and a salted control commitment. Full grouping attestations and random nonce remain in separate `datasets-control`, never delivered to consumers. Controls publish first; only the final manifest marks commit. Orphan controls reserve no split. Reuse checks exact controls, scope and fresh permissions; v1 is rejected, not migrated automatically. `inspect_exports` reports revoked/denied access but never authorizes reuse.

## Detailed Spanish references

[Pipeline](../TRANSCRIPCIONES_PIPELINE_B.md), [cards](../TRANSCRIPCIONES_FICHAS.md), [representations](../TRANSCRIPCIONES_REPRESENTACIONES.md), [integration C](../TRANSCRIPCIONES_INTEGRACION_C.md), [source-card evolution](../EVOLUCION_FICHAS_TR.md), [private destination](../DESTINO_PRIVADO_TRANSCRIPCIONES.md), [external references](../REFERENCIAS_EXTERNAS_D.md), [D adapters](../INTEGRACION_D_PROPUESTAS.md), [datasets](../TRANSCRIPCIONES_DATASETS.md), [query reads](../TRANSCRIPCIONES_RENDIMIENTO_CONSULTA.md). These preserve detailed contracts and historical context; they are not evidence that a private instance was accepted.
