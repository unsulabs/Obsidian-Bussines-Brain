# Pipeline local de transcripciones: interfaz implementada A/B

`scripts/transcripciones.py` conserva entradas y consolida análisis escritos por un agente. No llama a un modelo, no inventa asuntos y no publica en Obsidian. Se ejecuta con un Python que tenga las dependencias del producto; en la Mac de desarrollo se verificó `/opt/homebrew/bin/python3.11`.

Todos los comandos exigen `--bank RUTA --profile PERFIL.json --request-id ID --purpose FINALIDAD`. El perfil mínimo contiene `company_id` y `allowed_purposes`; `bank` y `vault` son rutas opcionales para comprobar el destino. El banco y los reportes de contexto deben quedar fuera de Git y de bóvedas. El perfil limita la capacidad solicitada: **no concede permiso sobre una fuente**.

Las mutaciones son previsualización por defecto; `--commit` aplica la mutación local. `--output ARCHIVO` crea un reporte inmutable; nunca reemplaza uno existente. La consola devuelve un sobre `resultado.v1` con estado, errores normalizados, hashes y rutas. Un `BLOCKED` también puede guardarse en un reporte nuevo.

## Recepción y permisos

`registrar --capture-manifest ARCHIVO` acepta el contrato sellado `capture-manifest.v1.json`. `ingresar` acepta `--archivo RUTA`, `--stdin` o `--parts-manifest RUTA`, más `--account-id ID --source-id ID --attempt-id ID`. Los IDs locales identifican entregas; no afirman identidad de personas. Para una entrega terminada se declaran `--closed --expected-parts N`. Un descriptor multipart contiene `parts: [{number: 1, path: "parte.txt"}]`, `expected_parts` y `closed`; las rutas son relativas al descriptor. Ordena por número sin agregar separadores ni normalizar bytes. Cada intento conserva partes, ensamblaje derivado y sello; una recepción abierta o con faltantes nunca se declara completa.

`permiso --input DECISION.json --purpose custody` registra una decisión explícita de la persona autorizada. El JSON contiene `tr_id`, `version_id`, `company`, `audience`, `purpose`, `action` (`grant` o `revoke`), `authority`, `evidence` (lista) y `decided_at` UTC. El ámbito es exacto por versión/empresa/audiencia/finalidad. No copiar grants entre versiones, cuentas ni propósitos. La API es una bitácora de declaraciones del operador local, no un proveedor de identidad. Su cambio no ratifica contenido ni autoriza publicación.

## Segmentos y análisis del agente

`segmentar --tr-id ID --version ID --policy utf8-bytes-1 --audience AUDIENCIA --purpose local_analysis` comprueba permiso y bytes originales. Admite `--max-core-bytes` (4096 por defecto) y `--context-bytes` (256). Los núcleos cubren exactamente los bytes UTF-8; el contexto solapado no cuenta dos veces. La salida identifica `bundle_id`, `permission_snapshot` y el archivo `segmentos/<bundle_id>.json`. Con `--commit` queda disponible para análisis.

`taxonomia --input TAXONOMIA.json --purpose local_analysis` conserva una taxonomía validada. Una actualización exige `previous_version` existente y `--event EVENTO.json` de tipo `taxonomia` con versión anterior en `old_refs` y nueva en `new_refs`. Rechaza bifurcaciones desde una base ya reemplazada. `seed_taxonomy()` entrega vocabulario genérico, no clasifica conversaciones por sí sola.

`analizar --input SUBMISSION.json --audience AUDIENCIA --purpose local_analysis` consolida trabajo semántico explícito. El JSON exige exactamente:

- `tr_id`, `version_id`, `segment_bundle`, `run_id`, `permission_snapshot`.
- `agent_results`, `claims`, `relations`, `subject_matrix`, `global_reconciliation` según esquemas `analisis`, `afirmacion` y `relacion`.
- `analyzer_version`, `taxonomy_version`, `canonical_context_refs`, `supersedes_run_id` y `dependency_ids`.

Cada asunto incluye `classifications` con `category_id` y `axis` existentes en la taxonomía preservada. Cada núcleo tiene resultado sustantivo o motivo explícito de excepción. Las afirmaciones y relaciones quedan `propuesta` o `en_revision`. El sistema valida spans, hashes de extractos, referencias, correcciones, cobertura y taxonomía; **la aceptación semántica independiente sigue pendiente**.

`canonical_context_refs` es una lista de `{tr_id, version_id, sha256}`: contextos previamente preservados como fuentes y autorizados en el mismo ámbito. No admite rutas arbitrarias a notas ni infiere permiso por poseerlas. Lista vacía significa que no se aportó contexto canónico externo. `dependency_ids` puede referir fuentes, versiones, taxonomías o runs existentes. Los runs referidos y `supersedes_run_id` se releen y sus originales se verifican para respaldar extremos históricos; no se aceptan IDs huérfanos.

El snapshot de permiso se obtiene mediante `permission_snapshot(bank, source_refs=[(tr_id, version_id), ...], company=..., audience=..., purpose="local_analysis")`. Incluye **todas** las fuentes de spans, contextos y runs históricos. Si sólo existe la fuente principal, coincide con el snapshot devuelto por `segmentar`. Un grant de otra fuente no invalida el run; revocar o cambiar el permiso propio exige una nueva preparación. No se aceptan snapshots globales como sustituto del ámbito exacto.

`cobertura --tr-id ID --run ID --audience AUDIENCIA --purpose local_analysis` relee fuentes, permisos actuales y taxonomía, comprueba el bundle e informa cobertura, vigencia y `ratified: false`. Una invalidación conserva el run histórico y lo marca no vigente. Nunca convierte una prueba estructural en aceptación del significado.

Un run consolidado con `supersedes_run_id` reemplaza al anterior sólo en la selección actual: el viejo reporta `current: false` y `superseded_by`, y la recuperación deja de presentar sus afirmaciones y conflictos como actuales. Los bytes históricos permanecen. La referencia al run reemplazado permite comprobar correcciones y no invalida por sí sola al nuevo run; las dependencias explícitas y fuentes citadas sí se siguen verificando. La búsqueda histórica se solicita expresamente mediante `mode: "historico"`.

`cobertura` distingue `dependency_current` de `current`. Un reemplazo sin otros cambios produce `dependency_current: true`, `current: false` y `stale_reasons: ["superseded"]`. Las razones adicionales `permission_snapshot_changed`, `dependency_invalidated` o `canonical_context_changed` hacen que `dependency_current` sea falso. Un original corrupto o un permiso revocado bloquean la operación. El modo histórico no rehabilita ninguna de esas condiciones.

## Recuperación y revisión retrospectiva

`indexar --snapshot current --audience AUDIENCIA --purpose local_analysis` prepara el índice derivado del ámbito. También admite el watermark exacto de `estado`. Sólo `--commit` reemplaza el SQLite reconstruible. Un índice nunca concede permisos.

`buscar --request CONSULTA.json --purpose internal_query --output REPORTE_PRIVADO.json` exige salida privada explícita. La solicitud requiere `query`, `company`, `audience` y `purpose`; admite `task`, `entities`, `period`, `mode`, `references` y `limit`. Rechaza campos desconocidos. La consola sólo devuelve ruta/hash y conteos; el reporte contiene el paquete de contexto con citas exactas. Referencias externas son localizadores no leídos. Los permisos y originales se verifican al recuperar, aunque exista índice viejo. Claims, relaciones y conflictos declarados conservan su procedencia y condición de propuesta; el paquete no genera una respuesta empresarial ni ratifica conocimiento.

Ejemplo sintético de `CONSULTA.json`:

```json
{
  "query": "descuentos",
  "company": "EMPRESA-SINTETICA",
  "audience": "internal",
  "purpose": "internal_query",
  "task": "Localizar criterios y excepciones para revisar descuentos",
  "entities": [],
  "period": null,
  "mode": "exploracion",
  "references": [],
  "limit": 10
}
```

`task` declara la tarea, se conserva en el paquete y no reemplaza la búsqueda léxica explícita de `query`: no hay inferencia semántica oculta. Si se omite, toma el valor de `query`; si se proporciona, debe ser texto no vacío de hasta 2000 caracteres. `entities` es una lista sin duplicados de IDs de entidades resueltas y verificadas en la taxonomía y ámbito de la afirmación; por defecto es `[]`. Una entidad inexistente o una etiqueta de hablante sin resolver no satisfacen el filtro. `task: null` y `entities: null` son inválidos.

`period` es `null` por defecto o un objeto con ambas fechas ISO, por ejemplo `{"from":"2026-01-01","to":"2026-12-31"}`. El rango es inclusivo y exige inicio no posterior al final. Se compara con una fecha empresarial conocida de la afirmación: `asserted_at` y, en su ausencia, `valid_time` si es una fecha interpretable. No usa la fecha de captura o importación como sustituto. Sin fecha conocida, la afirmación no satisface el filtro. Un rango sin coincidencias devuelve candidatos y análisis vacíos, con incertidumbre explícita; no demuestra ausencia de información en todo el banco.

| `mode` | Selección implementada |
|---|---|
| `exploracion` — predeterminado | Fuentes autorizadas y análisis no reemplazados con dependencias vigentes; conserva estados no verificados y declara que requieren revisión. |
| `actual` | Sólo análisis actuales y afirmaciones con `validity_state` `vigente` o `en_conflicto`; excluye runs reemplazados. La vigencia declarada no ratifica el contenido. |
| `historico` | Permite runs reemplazados sólo si `dependency_current` sigue siendo verdadero y los permisos actuales lo permiten. Los marca `temporal_status: "historical_superseded"`, `current: false` y `superseded_by`; no los presenta como vigentes. |

Los filtros de entidad, período y modo se aplican antes de FTS y de `limit`, proyectando únicamente spans admitidos; no se dejan pasajes ajenos al filtro como contexto accidental. Los análisis, relaciones y conflictos se restringen a la selección admisible. `limit` vale 10 por defecto y admite de 1 a 40. El paquete conserva `task`, `entities`, `period` y `mode`; `engine_mode` identifica aparte el motor léxico usado. Una revocación, invalidación o corrupción sigue excluyendo material también en modo histórico.

`estado --audience AUDIENCIA --purpose local_analysis` devuelve `review_snapshot_id`. Es un corte del catálogo con elegibilidad de **cada versión** según la bitácora de permisos. `revisar-antecedentes --event EVENTO.json --snapshot ID --audience AUDIENCIA --purpose local_analysis` propone el barrido íntegro de ese corte. El evento debe llevar el mismo `sweep_snapshot`. Sin resultados entregados conserva pendientes; no simula una revisión semántica mediante coincidencias de palabras.

`--results RESULTADOS.json` aporta una lista de entregas del agente y `--previous RUTA_RELATIVA` reanuda un bundle previo. Cada entrega incluye `job_id`, `input_hash`, `attempt`, `tr_id`, `state`, `reason`, `reviewed_version_ids`, `relations` y `proposals`. Las relaciones usan registros y spans verificados; las propuestas no se ratifican. Una revocación, nueva fuente o cambio del corte exige un snapshot nuevo. `--commit` conserva evento y revisión con cursor; no ejecuta automáticamente los trabajos semánticos pendientes.

Cuando un extremo es una afirmación con identidad resuelta, `--taxonomy-version VERSION` aporta la taxonomía preservada explícita para validar entidad, tipo, ámbito y etiqueta de hablante. Sin esa evidencia se rechaza la relación; no se elige la taxonomía más reciente automáticamente. Una etiqueta de hablante sin resolver sigue siendo la opción por defecto.

## Persistencia y recuperación

Los bundles de `segmentos/`, `analisis/` y `revisiones/` son JSON portables y autocontenidos. Los análisis incluyen claims, relaciones, fuentes exactas, referencias históricas, ámbito y hash de submission. `taxonomia/` y `eventos/` conservan registros inmutables. Cada escritura usa lock del banco y publicación atómica; repetir exactamente la misma entrada es idempotente. Un contenido distinto para el mismo ID se rechaza.

Una actualización de taxonomía o revisión publica primero su evento de invalidación y después el nuevo artefacto. Si se interrumpe entre ambos, el resultado es conservador: el histórico permanece invalidado y repetir la misma entrada completa la escritura pendiente. Nunca se borra el evento ni se eleva el histórico para ocultar una interrupción.

Pruebas sintéticas: `tests/test_transcripciones_pipeline.py` cubre recepción → permisos → segmentos → análisis del agente → contexto, revocación, corrupción, contexto histórico, cambios de taxonomía, snapshots, reanudación y preview sin mutaciones. No acredita aceptación empresarial ni publicación de la bóveda.
