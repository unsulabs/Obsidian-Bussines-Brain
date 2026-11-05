# Candidatos de datasets (U29)

`scripts/transcripciones_datasets.py` expone
`prepare_export(selection, purpose, permission_snapshot, *, bank, company, audience, commit=False)`.
Es preparación de candidatos **propuestos**, no entrenamiento, ratificación experta ni publicación.
No escribe en la bóveda ni permite bancos dentro de Git/Obsidian. No tiene CLI.

`purpose` acepta únicamente los enums reales `evaluation` y `training`. Cada
pasaje requiere un grant vigente de esa finalidad, versión, empresa y audiencia
en el ledger existente; `internal_query` no concede ninguno. El argumento
`permission_snapshot` se obtiene de `transcripciones_permisos.permission_snapshot`
con `source_refs` de **todos** los pasajes seleccionados y el mismo scope. El
snapshot no es permiso; candidatos con alguna fuente sin grant se excluyen por
completo, incluidas sus anotaciones. El resultado declara las exclusiones por ID.
Nunca crea decisiones de acceso.

La estructura exacta está en `modelo/transcripciones/dataset-selection.schema.json`:

- `candidates`: IDs únicos, `task`, `criterion`, `expected_result`, `exception`,
  `observed_response`, `expert_correction` y `passages`. Los últimos tres campos
  de contenido aceptan null para ausencia explícita. Las anotaciones las propone
  el operador; el exportador no certifica su corrección semántica ni autoría experta.
- Cada pasaje contiene `tr_id`, `version_id`, `source_sha256`, offsets UTF-8
  **en bytes, fin exclusivo** `start/end` y `context_start/context_end`,
  `passage_sha256` y `context_sha256`. El contexto debe envolver al pasaje; ambas
  selecciones deben coincidir con los bytes originales y sus límites UTF-8.
  La salida añade `text` y `permitted_context`, sólo desde esos bytes autorizados.
- `identities`: mapa por cada conversación del catálogo completo (también las
  no seleccionadas), con `client`, `project` y `evidence` de la atestación humana.
  IDs son identidades estables explícitas, nunca títulos. `null` significa
  **no aplica**, mientras `"unknown"` significa desconocido y rechaza exportar.
  Ausencia de una conversación también rechaza; la atestación no concede acceso.
- `allow_historical`: false por defecto en ejemplos; true debe ser explícito
  para una versión que tenga sucesora. No elude el permiso de su versión.

La separación une todas las versiones de cada conversación y todas las
conversaciones conectadas por SHA original idéntico, cliente o proyecto. Incluye
versiones excluidas y duplicados entre cuentas, incluso como puentes transitivos.
Cada manifiesto comprometido reserva sus grupos para su finalidad en el banco;
otro export de finalidad opuesta falla con `SPLIT_LEAKAGE`. Nuevas capturas que
unan grupos previamente separados también provocan rechazo. Las atestaciones
anteriores no se pueden cambiar para evadir la reserva: una corrección real de
identidad requiere un flujo de migración/revisión futura, no sobrescritura.
No se comparan otros bancos: la garantía se circunscribe al catálogo y ledger
de este banco. No se inventa identidad cuando no está disponible.

Preview devuelve un `resultado.v1` con manifiesto y ruta provisional, sin escribir.
Antes del primer commit, su ID puede cambiar: el compromiso de control utiliza
un nonce aleatorio privado. Después de un commit con igual control, las llamadas
reutilizan ese nonce y mantienen idempotencia. Preview y commit conservan los
mismos candidatos si no cambian entradas, permisos ni fuentes.
`commit=True` toma el lock común de custodia/permisos, prepara dos veces con
lecturas frescas y publica mediante escritura atómica inmutable a
`bank/datasets/DS-<hash>.json`; ese archivo contiene candidatos, linaje,
scope, snapshot de referencias autorizadas, selección permitida y exclusiones.
No contiene identidades de agrupación, texto de atestaciones ni referencias a
fuentes denegadas. El manifiesto es privado y su schema es `dataset-manifest.v2`;
manifiestos v1 se rechazan, no se migran ni autorizan automáticamente.

El control completo de agrupación permanece separado en
`bank/datasets-control/DS-<hash>.json`, escrito primero e inmutable. **No es un
output ni debe entregarse al consumidor del dataset**. Conserva la atestación
de todo el catálogo para detectar puentes y cambios aun en fuentes excluidas.
El manifiesto sólo contiene `control_commitment`: SHA256 del control con nonce
aleatorio privado de 256 bits, que evita búsqueda por diccionario de nombres,
IDs o evidencia. El nonce nunca se devuelve ni forma parte del payload.
La lectura exige schema válido, mismo scope y compromiso exacto; control ausente
o manipulado bloquea reutilización y separación. Un control huérfano por fallo
antes del manifiesto no constituye un export ni reserva un split; se ignora.
El manifiesto es la única marca visible de commit. Repetir el mismo contenido
es idempotente; una colisión no sobrescribe. Todo control está fuera de Git y
bóveda, bajo el banco privado; no forma parte de paquetes de producto.

`inspect_exports(bank=...)` muestra por ID los permisos actualmente denegados o
revocados. La revocación no borra el uso histórico ni libera su grupo para el
otro split. `permission_current` sólo describe acceso, **no habilita reuso**;
siempre se exige una preparación nueva antes de reutilizar. El snapshot exacto
y los hashes de fuentes se vuelven a comprobar antes de commit.

La versión 1 sólo recibe originales y anotaciones nuevas. No acepta referencias
a runs/claims, resúmenes ni dependencias analíticas: por tanto no reutiliza
derivados superseded o contaminados. No detecta semánticamente si una persona
pegó texto derivado en una anotación; la procedencia y corrección de esas
anotaciones necesitan revisión humana antes de cualquier uso posterior.

Pruebas sintéticas: `python3.11 -m unittest discover -s tests -p test_transcripciones_datasets.py -v`.
Cubren bytes/contexto, grants exactos, revocación, versiones, duplicados ocultos,
cliente/proyecto, separación válida, preview, colisiones e interrupción. No
prueban ni autorizan datos reales, entrenamiento o transferencia a terceros.
Incluyen evidencia/cliente/proyecto denegados seleccionados y no seleccionados,
control manipulado o ausente, nonce ausente del payload y controles huérfanos.
