# Knowledge workflow

[Español](../es/knowledge-workflow.md) · [Methodology](methodology.md) · [CLI](cli-reference.md)

## Start from the actual task

An existing company enters through `ce-continuidad` or `ce-consulta`; do not create another vault, overwrite D01 or repeat an initial interview. Resolve its vault and local instructions before reading it. A new company enters `ce-desarrollo-empresa`, which coordinates installation, discovery, a first useful artifact, review, use and continuity. A request for a plan authorizes design, not migration.

When the owner provides a new conversation or transcript, use the complete [transcript cycle](transcripts.md). When intent is ambiguous, preserve the expressed task instead of ingesting ordinary files or questions automatically. Recover metadata, candidates and relevant passages with neighbors before expanding to a complete original where meaning requires it. Reading only a source card must be reported as such.

## Architecture before drafting

Several mechanisms, offers, processes or decisions in one narrative require `ce-arquitectura-conocimiento` before a long D01 or automatic source-card production. Retrieve existing IDs and admissible evidence. Give every material subject one canonical owner: reuse a note, revise it, create an independently maintainable unit, or retain the material in its source with an explicit reason.

Prepare a private JSON plan following [the synthetic example](../../ejemplos/planes_conocimiento/plan_empresa_sintetica.json): `pregunta`, `asuntos`, `unidades`, `relaciones`. Units use `crear`, `revisar`, `referenciar` or `no_crear`, with identity justification, sources, tags and existing IDs when applicable. Candidate relations use the controlled vocabulary, direction, scope and evidence.

Run `plan-conocimiento` read-only and show the owner the map before drafting. Its validator checks coverage, references, duplicates, tags and possible monoliths; it does not decide strategic importance. Prior authorization to develop these pieces permits continued proposals without asking for each map again; it does not approve relationships, overwrite approved notes or publish maps. One note may be enough. Never invent a note quota or forced `no_crear` item.

## Develop usable knowledge

For each substantive round: reread the original and corrections; explain the mechanism, recipient, value, criteria, alternatives and exceptions; distinguish the owner's decisions from the agent's hypotheses; develop each canonical unit; test the result against the source in both directions. A future product must not shrink into an internal improvement, and a decision pattern must not become a list of topics.

Write for the team using the knowledge. The business body should explain facts, activities, capabilities and useful implications. Put most provenance, gaps and verification controls in CONTROL, retaining uncertainty in the body when material. The owner is a primary source for strategy and internal expertise; systems establish their own facts, while contracts and measurements support transactions and results. A missing invoice does not erase a strategic intention, and a strategic intention does not prove revenue.

Explicitly rejected legacy writing must not be imported, summarized, indexed or quietly used as a draft. Preserve its backups untouched; rebuild from authorized primary sources or new expert judgment. An exception requires approval for that source. If the owner corrects an assertion, stop propagating it, reread the original, identify affected units and propose a corrected version before continuing.

## Capture, documents and revisions

With permission to preserve working notes, `fuente` records a source locator and `capturar` stores provisional progress under `90_Sistema/Descubrimiento/`. Show IDs/paths and run `estado` and `validar`. This is not document approval or a substitute for developing the business.

Use `ficha --archivo` for a developed operational note and `documento` for a justified D/X synthesis. Draft Markdown lives outside Git and the vault until the relevant command applies it. Tags are optional navigation. Sources must already be registered; do not invent clients, payments, roles or commercial status.

For an existing D/X, `previsualizar-dx` reads and compares; `preparar-dx` stores PRDX JSON and a candidate snapshot without editing the document. New corrective sources require repeatable `--fuente` and their resulting `sha_fuentes`; a link only in the body does not update source properties. `aplicar-dx` requires specific authorization, original/candidate/source hashes as applicable, a responsible person, authorization reference and external backup. Approved or withdrawn documents cannot be changed through the ordinary revision path. `restaurar-dx` creates a new revision from history rather than erasing later history. See [operations](operations.md).

## Editorial review and navigation

`evaluar-dx` records an EVALDX evaluation tied to the document SHA, reviewer, decision reference, block scope and G1–G7 findings. Decisions are `requiere_cambios`, `recomendar_parcial`, `recomendar_integral`. Recommendations do not approve the document. G2/G6 cannot be `no_aplica` for approval; integral recommendation covers all blocks with `suficiente_para_tarea`.

Only a separately authorized `aprobar-dx` with exact SHA, backup and literal confirmation promotes the entire document. The body stays unchanged and revision increases. Partial coverage cannot be promoted wholesale. The CLI records human declarations; it neither authenticates the reviewer nor certifies truth.

Propose typed relationships only once endpoints exist, with evidence and scope; confirm with the dedicated review controls. `mapa-conocimiento` previews the network. `publicar-mapa` requires specific human authorization, literal confirmation, old/proposed SHA and external backup. It produces Markdown/Canvas in `00_Mapas` without editing notes, sources, D/X or the 16 existing Bases. Regeneration requires a new authorization; a stale map never becomes authority.

## Acceptance and continuity

`consulta-contextual` retrieves literal D/X blocks and sections of typed notes in `20_Entidades/`. With `--orientar`, it matches question terms and ranks candidates lexically; it does not generate a semantic answer. A document without stable `kb:id` markers may yield `seccion_derivada_sin_id_estable`: this locator can change and is not a contractual block identity. The engine excludes templates, source cards, provisional captures and CONTROL as business-body facts, and excludes confidential/restricted material from this MVP search without granular ACL. Note-level source lists do not prove each assertion. Temporal `valid_from`/`valid_to` constraints apply when present; missing dates do not establish validity. A matching text can still return `sin_autoridad_explicita` for the requested subject/scope. Open candidate notes and relevant originals before answering.

Test a real task and a negative case: distinguish general offer from particular agreement, current from historical, and quotation from payment. Show what was written, what source was actually read, what remains proposed and the next useful business action. Save continuity without automatically feeding memory or scheduled automation.

Spanish source references: [architecture gate](../ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md), [expert cycle](../CICLO_EXPERTO_DESARROLLO_EMPRESARIAL.md), [constructive synthesis](../SINTESIS_EMPRESARIAL_CONSTRUCTIVA.md), [progressive capture](../CAPTURA_PROGRESIVA.md), [legacy admissibility](../RECONSTRUCCION_EDITORIAL_Y_FUENTES.md), [document lifecycle](../CICLO_DOCUMENTAL_DX.md), [revisions](../REVISIONES_DX_CON_HISTORIAL.md), [editorial governance](../GOBIERNO_EDITORIAL_DX.md), [typed relations](../RELACIONES_TIPADAS.md), [contextual queries](../CONSULTA_CONTEXTUAL.md).
