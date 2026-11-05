# Evolución de una ficha de transcripción

El renderer y el integrador admiten cambiar una ficha a la versión siguiente de
**la misma TR**, conservando F-ID y ruta visible. No altera bytes originales,
catálogo, preferencia de versión ni permisos. La versión se elige mediante el
run solicitado, nunca por fecha o por ser la última del directorio.

El nuevo original debe pertenecer al mismo catálogo y declarar
`previous_version_id` igual a la versión que muestra la ficha. Deben ser vecinos
en el linaje validado por custodia. No se permiten saltos, versiones ajenas,
retrocesos o ramas; una migración de varios pasos se realiza secuencialmente.
La completitud de la versión preferida del catálogo no se atribuye a otra
versión: el control muestra la evidencia de captura propia del original elegido.
Una ficha aprobada o histórica se rechaza. La transición conserva su estado
borrador/en_revision, identidad, empresa y propiedades personalizadas.

Para otro análisis de la **misma versión**, el run nuevo debe sustituir
directamente al que muestra la ficha. Dos sucesores del mismo run se consideran
ambiguos y bloquean el cambio. El pipeline debe acreditar cobertura actual;
la revisión semántica, cuando se aporta, sigue ligada a los hashes de la entrega
y dictamen de ese run. La revisión del run previo no aprueba el nuevo.

## Qué se conserva

Las vistas íntegras existentes son inmutables. Una versión nueva crea una vista
nueva. Un análisis nuevo de la misma versión puede reutilizar la vista si sus
pasajes y hashes ya están presentes exactamente; si necesita otros pasajes,
crea una variante con identidad/ruta distintas. Nunca reemplaza la vista previa
ni mezcla offsets o hashes entre versiones. Las vistas históricas se comprueban
contra el original y se ligan por SHA al manifest del lote.

Las fichas nuevas delimitan el texto generado con comentarios Markdown. Una
actualización reemplaza sólo esa sección y conserva el texto personalizado
externo a ella. La propuesta anterior queda íntegra en un bloque literal,
rotulado como historial no vigente; no se usa para elaborar el análisis nuevo.
El metadato `historial_fuentes` conserva versión, run, SHA de ficha previa y vista.
Para una ficha anterior sin delimitadores, se archiva íntegro su cuerpo: el
programa no intenta adivinar qué frase fue editada por una persona. Todos los
destinos y anotaciones quedan conservados, aunque ese primer cuerpo legacy se
presenta como historial literal. Los originales siguen disponibles en sus vistas.

Volver a renderizar el mismo run con el mismo contenido conserva la ficha
exactamente y no acumula otra entrada de historial. Las propiedades ajenas a la
sección generada no se reutilizan como afirmaciones nuevas.

## Permisos, propuesta y aplicación

Se usa la misma API `render_source(tr_id, run_id, profile)`, con snapshot completo
de las notas relevantes: ficha actual y vistas que enlaza. No basta entregar sólo
la ficha. El renderer agrega `source_transition` y checks históricos a los
candidatos que necesitan evolucionar. No debe fabricarse ni completarse ese
objeto manualmente para eludir una negativa.

El proof liga bytes de ficha anterior, run anterior, ambos originales, vistas
históricas, referencias y snapshots de permisos. Se revalida durante prepare,
apply y rollback. Todas las fuentes históricas necesarias requieren permisos
vigentes para análisis y consulta interna; quitar `access_checks` del candidato
no evita esta comprobación. Cambiar datos, permisos o vistas después de preparar
el manifest detiene el lote sin sobrescribirlos.

Prepare sigue siendo de sólo lectura. El mismo motor utiliza manifiesto
autorizado, fencing, quiescencia de editores, backup y journal. Un retry del lote
conserva idempotencia. Rollback devuelve exactamente la ficha anterior y elimina
únicamente las vistas nuevas del lote si siguen intactas. Una edición posterior
en ficha o vista nueva impide sobrescribir/eliminar ese archivo. Las vistas
anteriores no se escriben ni se borran.

Cada transición exige que `historial_fuentes` sea exactamente la cadena previa
seguida de una entrada con versión, análisis, SHA de la ficha anterior y ruta de
su vista. Se rechazan entradas ausentes, añadidas, falsificadas o reordenadas;
conservar solamente el prefijo previo no basta.

## Verificación

`python3.11 -m unittest discover -s tests -p test_transcripciones_evolucion.py -v`
prueba linaje directo, identidad/ruta, personalizaciones, historial, vistas
inmutables, variante del mismo original, otro análisis con supersesión directa,
ramas, salto de versión, fuente ajena, grants históricos revocados, ficha aprobada,
edición concurrente, reintento y restauración exacta. Evidencia sintética en
`_verify/evolucion-tr/`; la aceptación empresarial y la aplicación real siguen
siendo gates separados.
