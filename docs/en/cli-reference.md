# CLI reference

[Español](../es/cli-reference.md) · [Operations](operations.md) · [Transcript contracts](transcripts.md)

Commands, flags, schema keys and enums retain their existing Spanish/runtime spelling. Run from the product root with a Python containing `requirements.txt` dependencies. These are local scripts, not REST endpoints. Inspect each command's `--help` before use; no command line proves the operator has genuine authorization.

```bash
python scripts/cerebro.py --help
python scripts/cerebro.py doctor
python scripts/transcripciones.py --help
```

`cerebro.py` has no global dry-run/commit switch. Some commands write immediately; use the effect table. Most business operations require `--vault`. Resolve existing destinations before reading them. All paths below are synthetic placeholders.

## Business CLI: read-only operations

| Command | Arguments beyond command name | Behavior |
|---|---|---|
| `doctor` | optional `--vault` | Diagnose runtime/dependencies without installing. |
| `estado` | `--vault` | Structural summary, not business completion. |
| `validar` | `--vault` | Validate notes, IDs, links and transfers, not truth. |
| `tipos` | optional `--tipo` | Show candidate type registry. |
| `buscar` | `--vault --texto`, optional `--limite` (12) | Literal vault search. |
| `autoridad` | `--vault --tema --ambito`, optional `--fecha` | Exact declared authority in imported contract; date defaults to today. |
| `consulta-contextual` | `--vault --texto`, optional `--tema --ambito --fecha --limite` (10), `--orientar` | Retrieve block candidates; optional ordering is not semantic answer generation. |
| `plan-conocimiento` | `--vault --archivo` | Validate private architecture JSON before drafting; no notes/relations created. |
| `previsualizar-dx` | `--vault --doc-id --archivo`, repeatable `--fuente` | Compare existing D/X with external draft. |
| `relaciones` | `--vault`, optional `--id` | Query typed edges and review state. |
| `mapa-conocimiento` | `--vault` | Preview derived Markdown/Canvas, hashes and limits. |
| `aceptacion` | `--vault` | Structural pilot preflight, not owner acceptance. |

## Creation and provisional writes

| Command | Required arguments | Additional options and effect |
|---|---|---|
| `crear` | `--id --nombre --dest` | Create a new vault without overwrite; infrastructure without business knowledge. Never repeat on existing business. |
| `ficha` | `--vault --tipo --titulo` | `--resumen`, `--archivo`, repeatable `--fuente --etiqueta`; new draft typed note. External Markdown for `--archivo` has no YAML. |
| `fuente` | `--vault --id --titulo --localizador --clase` | `--lectura` = `no_verificada`/`leida_parcial`/`leida_completa`; `--fecha-evento`. Records reference, does not copy original. |
| `capturar` | `--vault --titulo --archivo` | Repeatable `--fuente`; preserve provisional discovery. |
| `documento` | `--vault --clase --titulo --archivo` | `--doc-id`, `--estado` = `borrador`/`en_revision`, `--cobertura`, `--fecha-corte`, repeatable `--fuente --etiqueta`; create developed D/X. |
| `proponer` | `--vault --id --motivo --archivo` | Stage a suggested change without changing target. |
| `preparar-dx` | `--vault --doc-id --archivo` | Repeatable `--fuente`; store PRDX proposal/snapshot, preserve current D/X. |
| `evaluar-dx` | `--vault --doc-id --acta --sha-actual` | Store G1–G7 evaluation, not approval. |
| `relacion-proponer` | `--vault --origen --destino --predicado --fuente --ambito --motivo` | `--fuente` repeatable; create proposed edge only. |
| `continuidad` | `--vault --resumen --siguiente` | Optional `--revisado-por`; save session continuity. |
| `grafo` | `--vault` | Optional `--output`; writes JSON **inside** vault, default `90_Sistema/grafo.json`. Not a read-only query. |
| `importar` | `--vault --manifest` | Optional `--permitir-real` only with authorization and internal admissible data; staged vNext-0.9 import, not synchronization. |

Document coverage choices are `sin_fuente`, `parcial`, `suficiente_para_tarea`, `no_aplica`. Without an explicit choice, sources imply partial coverage, not sufficiency. Do not infer source reading, human identity or approved commercial terms from these flags.

## Controlled changes

| Command | Required controls |
|---|---|
| `aplicar-dx` | `--vault --propuesta --sha-original --sha-candidato --responsable --referencia-autorizacion --respaldo`; `--sha-fuentes` when adding sources. |
| `restaurar-dx` | `--vault --doc-id --historial --sha-actual --responsable --referencia-autorizacion --respaldo`; creates new revision. |
| `aprobar-dx` | `--vault --evaluacion --sha-actual --responsable --referencia-autorizacion --respaldo --confirmacion`; literal `APROBAR <doc_id> <first 12 SHA characters>`. |
| `relacion-confirmar` | `--vault --relacion-id --sha-relacion --revisor --referencia-autorizacion --confirmacion`; use exact runtime confirmation format. |
| `publicar-mapa` | `--vault --sha-actual --sha-propuesto --confirmacion --respaldo`; only authorized derived map publication. |

Obtain the exact confirmation from current help/preview and the relevant skill. Never invent hashes, use example placeholders as approval, or hand-edit a manifest to bypass a rejection. See [revision and rollback rules](operations.md).

## Transcript CLI

Every command requires `--bank --profile --request-id --purpose`; optional `--output` creates a new immutable report. The profile's `allowed_purposes` does not grant access to sources. Only commands marked **preview/commit** accept `--commit`; others are reads/reports. `buscar` requires private `--output` and returns only path/hash/counts to console.

| Command | Specific arguments | Effect |
|---|---|---|
| `registrar` | `--capture-manifest` | Preview/commit sealed capture. |
| `ingresar` | Exactly one of `--archivo`, `--stdin`, `--parts-manifest`; `--source-id --account-id --attempt-id`; optional `--closed --expected-parts` for nonmanifest input | Preview/commit exact receipt. Manifest carries its own closure/count; do not combine them. |
| `estado` | optional `--audience` | Counts, watermark; audience adds review snapshot. |
| `verificar` | no extra arguments | Verify custody. |
| `inventario-validar` | `--snapshot` | Validate authorized inventory snapshot. |
| `conciliar` | `--snapshot` | Reconcile inventory with catalog. |
| `permiso` | `--input` | Preview/commit grant/revoke declaration; operation purpose `custody`. |
| `segmentar` | `--tr-id --version --policy --audience`, optional `--max-core-bytes` (4096), `--context-bytes` (256) | Preview/commit byte core bundle. |
| `taxonomia` | `--input`, optional `--event` required for updates | Preview/commit taxonomy; purpose `local_analysis`. |
| `analizar` | `--input --audience` | Preview/commit agent-authored submission. |
| `cobertura` | `--tr-id --run --audience` | Recheck coverage, permissions and current dependencies. |
| `indexar` | `--snapshot --audience` | Preview/commit derived index; `current` or exact watermark. |
| `buscar` | `--request --output` | Private scoped context package; no business answer generated. |
| `revisar-antecedentes` | `--event --snapshot --audience`, optional `--results --previous --taxonomy-version` | Preview/commit retrospective review; absent semantic results stay pending. |

Example of a read request file, not permission to query any real source:

```json
{
  "query": "descuentos",
  "company": "EMPRESA-SINTETICA",
  "audience": "internal",
  "purpose": "internal_query",
  "task": "Locate discount criteria and exceptions",
  "entities": [],
  "period": null,
  "mode": "exploracion",
  "references": [],
  "limit": 10
}
```

```bash
python scripts/transcripciones.py buscar \
  --bank /private/bank --profile /private/profile.json \
  --request-id QUERY-001 --purpose internal_query \
  --request /private/query.json --output /private/reports/query-001.json
```

Details of scopes, UTF-8 offsets, completeness, history and dataset controls are in [transcripts](transcripts.md). Bank results use `resultado.v1`; `DONE`/`DONE_WITH_CONCERNS` exit 0 and blocked failures exit 2. Business CLI validation errors exit 1; handled input/IO errors exit 2. Inspect both output and exit code; technical success never ratifies meaning.

## Auxiliary scripts and Python APIs

`actualizar_vistas_bases.py` and `nombres_legibles.py` have independent preview/apply interfaces and exact-plan controls; follow [operations](operations.md). `aceptacion_integracion_local.py`, `prueba_integral.py`, `auditar_paquete.py` and `exportar_producto.py` support acceptance/audit/distribution; inspect their own `--help` rather than inventing subcommands of `cerebro.py`.

Rendering (`render_source`), integration (`prepare_batch`/`apply_batch`/`rollback_batch`), representations (`importar_representacion`), external references and datasets (`prepare_export`) are Python APIs. They are not transcript subcommands and do not create network services. Their detailed contracts and boundaries are linked from [transcripts](transcripts.md).
