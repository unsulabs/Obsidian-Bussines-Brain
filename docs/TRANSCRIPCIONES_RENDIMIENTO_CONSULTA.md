# Lecturas por consulta

`buscar` y `build_context` comparten una memoria temporal de catálogo verificado,
cadena de permisos y grafos de invalidación/sustitución. Su alcance termina al
retornar o fallar la consulta; otra consulta vuelve a validar desde disco. No se
guardan permisos en el índice ni se usa la memoria para autorizar escrituras.

La optimización evita reconstruir el ledger y el catálogo por cada fuente,
claim y pasaje. Mantiene los validadores, los hashes de originales, las citas,
los propósitos y los filtros previos al límite. Cada consumidor recibe copias
de los datos mutables memorizados. Grants y puntos UTF8 usan conjuntos inmutables;
los puntos se identifican por bytes exactos y cada span conserva sus checks de
SHA, offset y extracto. Las operaciones bajo `bank_lock` suspenden esta memoria
para validar sus decisiones contra el estado vivo.

Antes de iniciar y después de producir el resultado se calculan huellas de todos
los archivos relevantes de receipts, journal, versiones, originales, análisis,
eventos, taxonomía y permisos. Una diferencia rechaza el resultado con
`SNAPSHOT_CHANGED`, aunque se hayan usado permisos memorizados durante el trabajo.
La lectura final no usa la memoria: lee y hashea bytes reales, detecta archivos
agregados/retirados y conserva los controles de rutas sin symlinks. Las comprobaciones
existentes de watermark, citas y revisión siguen activas.

Es una comprobación optimista: los escritores pueden continuar y provocar rechazo;
no se bloquea el banco durante una consulta. Las huellas son lineales en bytes
del banco y todavía incluyen fuentes ajenas al scope para comprobar integridad,
sin incorporarlas a resultados. No es un índice persistente ni una garantía de
lectura atómica del sistema de archivos. La consulta léxica y sus reglas de tokens
no cambian: esta optimización no agrega operadores booleanos ni inferencia semántica.

Pruebas dirigidas: `test_transcripciones_lectura.py` comprueba escala, revocación
concurrente, cambios de igual tamaño, nuevas derivaciones, errores y caducidad de
la memoria; `test_transcripciones_recuperacion.py` cubre citas, scope, filtros y
modos; `test_transcripciones_pipeline.py` cubre vigencia e invalidación.
