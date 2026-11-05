# Custodia, análisis e integración de transcripciones

[English](../en/transcripts.md) · [CLI](cli-reference.md) · [Seguridad](security.md)

## Ciclo asistido completo

Para material identificado como conversación/transcripción nueva, activar `ce-banco-transcripciones` antes de resumir: custodia exacta → análisis de todos los asuntos → antecedentes y taxonomía → arquitectura → ficha, texto íntegro y conexiones aplicadas → verificación. Esta preferencia portable no traslada permisos entre empresas. Recuperar configuración y autoridad privadas; una instrucción posterior puede limitar una entrega. No implica vigilancia, entrenamiento, publicación, servicios externos ni descarga de cuentas completas.

El pipeline determinista almacena trabajo del agente; no llama a un modelo para analizar. Su éxito no acredita aceptación semántica independiente ni empresarial. Separar originales, propuestas de análisis y conocimiento aprobado.

## Recepción y custodia exacta

Todos los subcomandos de `scripts/transcripciones.py` exigen `--bank`, `--profile`, `--request-id`, `--purpose`. El perfil declara `company_id`, `allowed_purposes` y opcionalmente `bank`/`vault` esperados. Limita capacidades, pero no concede permisos de fuentes. Banco y reportes privados quedan fuera de Git/bóvedas. Mutaciones previsualizan por defecto; `--commit` aplica. `--output` crea reporte inmutable nuevo. Resultados usan `resultado.v1`; errores pueden devolver `BLOCKED` normalizado.

`registrar` recibe `capture-manifest.v1.json` sellado. `ingresar` acepta archivo, stdin o `--parts-manifest`, con IDs de cuenta/fuente/intento. Identifican recepciones, no personas. Rutas de `parts: [{number, path}]` son relativas al descriptor; ensamblar por número sin separadores ni normalización. Declarar cierre y partes esperadas sólo cuando se conozcan. Recepciones abiertas/incompletas siguen incompletas. Un URL solo no es contenido capturado.

`permiso` registra grant/revoke explícito por `tr_id`, `version_id`, `company`, `audience`, `purpose`, con `authority`, `evidence`, `decided_at`. La operación se ejecuta con finalidad `custody`; la decisión lleva la finalidad que otorga/revoca. No copiar grants entre versiones, cuentas ni finalidades. El ledger registra declaraciones, no identidad autenticada.

## Segmentos, análisis y selección vigente

`segmentar` verifica permiso vivo y bytes. `utf8-bytes-1` usa núcleos de 4096 bytes y contexto de 256 por defecto; los núcleos cubren una vez, el solapamiento sólo es contexto. Conservar `bundle_id` y `permission_snapshot` exacto.

`analizar` recibe `tr_id`, `version_id`, `segment_bundle`, `run_id`, `permission_snapshot`, `agent_results`, `claims`, `relations`, `subject_matrix`, `global_reconciliation`, `analyzer_version`, `taxonomy_version`, `canonical_context_refs`, `supersedes_run_id`, `dependency_ids`. Seguir esquemas: cada núcleo necesita trabajo sustantivo o excepción explícita. Los asuntos usan categorías/ejes preservados. Afirmaciones/relaciones siguen `propuesta` o `en_revision`. Cobertura valida spans, hashes, referencias y conciliación; no certifica significado.

Contexto canónico usa `{tr_id, version_id, sha256}` de fuentes preservadas y permitidas, nunca una ruta arbitraria a nota. Snapshots cubren todas las fuentes citadas, contextuales e históricas, no un hash global del ledger. Actualizar taxonomía exige `previous_version` y evento de invalidación; una base reemplazada no bifurca silenciosamente. Se releen/verifican dependencias históricas.

`cobertura` revisa originales, permisos, taxonomía y bundles. Un run sustituido puede tener `dependency_current: true`, `current: false`, motivo `superseded`; cambios adicionales de permiso/dependencia/contexto lo excluyen. Corrupción o revocación bloquean incluso el acceso histórico. Los bytes antiguos permanecen.

## Recuperación y revisión retrospectiva

`indexar` construye SQLite derivado para ámbito y watermark exactos (`current` o valor de `estado`). `buscar` exige `--output` privado; consola devuelve ruta/hash/conteos, no pasajes. JSON requiere `query`, `company`, `audience`, `purpose`; opcionales: `task`, `entities`, `period`, `mode`, `references`, `limit`. Rechaza campos desconocidos. `task` usa query por defecto; si se aporta es texto no vacío hasta 2000 caracteres y no sustituye términos léxicos. `entities` es lista única de identidades resueltas en taxonomía; etiquetas de hablantes sin resolver no bastan. Ninguno acepta null.

`period` es null o `{from,to}` ISO inclusivo y ordenado; filtra fechas empresariales conocidas (`asserted_at` o `valid_time` interpretable), no captura/importación. Sin fecha conocida no coincide. Filtrar antes de FTS y límite 1–40 (10 por defecto), también pasajes y relaciones proyectados.

| `mode` | Selección |
|---|---|
| `exploracion` | Predeterminado: fuentes permitidas y análisis no sustituidos con dependencias vigentes; conserva estados no verificados. |
| `actual` | Análisis actuales y afirmaciones `vigente`/`en_conflicto`; no las ratifica. |
| `historico` | Runs sustituidos sólo con dependencias y permisos actuales válidos; rotula `historical_superseded`, nunca vigente. |

Sin coincidencias no demuestra ausencia en todo el banco. Referencias externas siguen como localizadores no leídos. El paquete no genera respuesta empresarial. Memorias por solicitud caducan y las huellas finales detectan cambios concurrentes; ver [arquitectura](architecture.md).

`estado --audience` genera snapshot con elegibilidad por versión. `revisar-antecedentes` exige `sweep_snapshot` coincidente del evento; resultados del agente aportan job/hash, intento, versiones revisadas, estado/razón, relaciones y propuestas. `--previous` reanuda revisión inmutable. Sin resultados quedan trabajos semánticos pendientes. Fuentes nuevas o cambios de permiso exigen snapshot nuevo. Identidad resuelta exige `--taxonomy-version` preservada explícita, sin elegir la última por defecto.

## Representaciones y fichas derivadas

`importar_representacion` / `import_representation` es API Python, no CLI. Preserva DOM sellado, texto con encabezados y HTML opcional para versión canónica existente. Artefactos/hashes tienen mismas claves, obligatorias `dom_source` y `with_speakers`. `provider-groups-lf-v1` reconstruye raw/encabezados exactamente, sin normalizar espacios ni saltos. Guarda offsets UTF-8 `[start,end)`, IDs de sentencias y etiquetas sin resolver. HH:MM:SS terminal no verifica hablantes ni alineación audiovisual. Publica blobs antes del manifiesto; reintento completa interrupciones sin sobrescribir.

`render_source(tr_id, run_id, profile)` y `propose_navigation` devuelven candidatos sin escribir. Revalidan cobertura, originales y permisos. Sensibilidad se atesta por fuente, por defecto `restringido`; gana la más restrictiva entre dependencias/ficha. Fichas conservan asuntos, afirmaciones, razones, excepciones y conflictos, con vistas íntegras y enlaces estables a pasajes. Conservan F-ID/ruta existente. Dictamen semántico opcional liga hashes sellados de entrega/revisión al run; independencia es atestación del operador y la ficha sigue sin ratificar.

Paquetes de arquitectura limitan a 30 asuntos, 30 destinos existentes y 90000 bytes; un asunto que excede bloquea sin truncar. Deben razonarse hacia `plan-conocimiento`, no aceptarse automáticamente como arquitectura empresarial. La navegación propone cuatro Bases nuevas de transcripciones, mapa de corpus y anexos mínimos a Inicio/Como_usar con identidad; no reemplaza manuales personalizados ni las 16 Bases existentes.

## Integración, evolución y propuestas de archivos ordinarios

APIs `prepare_batch`, `apply_batch`, `rollback_batch` validan dependencias explícitas, bytes, permisos de análisis/consulta, hashes y snapshot completo de bóveda. Kinds: `source`, `transcript_view`, `entity`, `dx`, `navigation`, `base_view`, `navigation_append`. Entidades nuevas exigen `borrador`/`en_revision`, `propuesta`, `sin_verificar`, `interno`, fecha explícita y tipo real. No sobrescriben aprobados/históricos.

Material protegido exige perfil privado sellado válido para IDs/empresa/audiencia/bóveda exactos y permisos vivos; no desclasifica y mantiene restricciones del adaptador. Ver [contrato compartido de destino privado](../../.agents/skills/ce-banco-transcripciones/references/destino-privado.md). Apply usa respaldo privado externo, journal, lock cooperante, fencing monotónico y quiescencia declarada. Hashes no excluyen carreras microscópicas con editores no cooperantes; ver [operaciones](operations.md).

Evolución de ficha sigue linaje inmediato de versión o sustitución directa de run, nunca fecha más reciente. Conserva ID/ruta, propiedades y texto fuera de delimitadores; el generado previo pasa a historial literal no vigente. Vistas íntegras son inmutables; otro run puede necesitar variante. `historial_fuentes` debe igualar cadena previa más exactamente una entrada verificada. Dependencias históricas necesitan permisos vivos. Ediciones posteriores bloquean restauración.

Archivos ordinarios usan metadatos versionados de `referencias_externas.py`, grants por finalidad y dependencias transitivas, sin copiarlos ni ejecutarlos. Adaptadores D permiten parches únicos exactos del cuerpo en `legacy_source`, `navigation_patch`, `control_proposal`; `proposal_staging` crea propuesta sin editar objetivo empresarial. Candidato/dictamen son referencias de control ligadas por hash; no se autoconcede vínculo primario. Estos adaptadores bloquean sensibilidad no interna. Lectura parcial exige spans explícitos permitidos. Un objetivo mutable no puede ser dependencia propia del lote.

## Candidatos de datasets

`prepare_export` de `transcripciones_datasets.py` es API Python, no entrenamiento ni publicación. Sólo acepta `evaluation` o `training` con grant específico actual por fuente/versión. Falta de permiso excluye candidato completo y anotaciones. Selecciones usan hashes exactos de pasaje/contexto UTF-8 y anotaciones explícitas; la herramienta no verifica calidad semántica.

Agrupación une versiones, hashes originales idénticos, clientes y proyectos en todo el catálogo, incluidas fuentes excluidas y puentes entre cuentas. Atestaciones deben ser completas: null es no aplica; `"unknown"` bloquea. Grupos comprometidos no cruzan finalidades (`SPLIT_LEAKAGE`); revocar no borra uso histórico ni libera split. La garantía se limita al banco.

`dataset-manifest.v2` privado contiene payload permitido y compromiso del control con nonce. Atestaciones completas y nonce aleatorio quedan en `datasets-control`, nunca se entregan al consumidor. Control se publica primero; sólo manifiesto final marca commit. Controles huérfanos no reservan split. Reuso verifica controles exactos, ámbito y permisos frescos; v1 se rechaza sin migración automática. `inspect_exports` informa denegaciones/revocaciones, sin autorizar reuso.

## Referencias detalladas

[Pipeline](../TRANSCRIPCIONES_PIPELINE_B.md), [fichas](../TRANSCRIPCIONES_FICHAS.md), [representaciones](../TRANSCRIPCIONES_REPRESENTACIONES.md), [integración C](../TRANSCRIPCIONES_INTEGRACION_C.md), [evolución](../EVOLUCION_FICHAS_TR.md), [destino privado](../DESTINO_PRIVADO_TRANSCRIPCIONES.md), [referencias externas](../REFERENCIAS_EXTERNAS_D.md), [adaptadores D](../INTEGRACION_D_PROPUESTAS.md), [datasets](../TRANSCRIPCIONES_DATASETS.md), [lecturas por consulta](../TRANSCRIPCIONES_RENDIMIENTO_CONSULTA.md). Conservan contratos detallados y contexto histórico; no prueban aceptación de una instancia privada.
