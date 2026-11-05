# Flujo de conocimiento

[English](../en/knowledge-workflow.md) · [Metodología](methodology.md) · [CLI](cli-reference.md)

## Partir de la tarea real

Una empresa existente entra por `ce-continuidad` o `ce-consulta`; no crear otra bóveda, sobrescribir D01 ni repetir entrevista inicial. Resolver bóveda e instrucciones antes de leerla. Una nueva entra por `ce-desarrollo-empresa`, que coordina instalación, descubrimiento, primera pieza útil, revisión, uso y continuidad. Pedir un plan autoriza diseño, no migración.

Una conversación o transcripción nueva activa el [ciclo completo](transcripts.md). Ante intención ambigua, conservar la tarea expresada sin ingerir archivos ordinarios ni preguntas automáticamente. Recuperar metadatos, candidatos y pasajes con vecinos antes de ampliar al original completo cuando el significado lo exija. Si sólo se leyó una ficha, declararlo.

## Arquitectura antes de redactar

Una narración con varios mecanismos, ofertas, procesos o decisiones exige `ce-arquitectura-conocimiento` antes de un D01 largo o fichas automáticas. Recuperar IDs existentes y fuentes admisibles. Asignar dueño canónico a cada asunto material: reutilizar, revisar, crear una unidad mantenible de manera independiente o conservar en su fuente con razón explícita.

Preparar JSON privado según [el ejemplo sintético](../../ejemplos/planes_conocimiento/plan_empresa_sintetica.json): `pregunta`, `asuntos`, `unidades`, `relaciones`. Las unidades usan `crear`, `revisar`, `referenciar` o `no_crear`, con justificación, fuentes, etiquetas e IDs existentes cuando corresponda. Las relaciones candidatas usan vocabulario controlado, dirección, ámbito y evidencia.

Ejecutar `plan-conocimiento` en lectura y mostrar el mapa antes de redactar. El validador revisa cobertura, referencias, duplicados, etiquetas y posibles monolitos; no decide importancia estratégica. La autorización previa para desarrollar esas piezas permite continuar propuestas sin volver a preguntar por cada mapa; no aprueba relaciones, sobrescribe notas aprobadas ni publica mapas. Una nota puede bastar. No imponer cuotas ni inventar un `no_crear` obligatorio.

## Desarrollar conocimiento útil

Por ronda sustantiva: releer original y correcciones; explicar mecanismo, destinatario, valor, criterios, alternativas y excepciones; distinguir decisión del dueño e hipótesis del agente; desarrollar cada unidad canónica; cotejar fuente→nota y nota→fuente. Un producto futuro no debe reducirse a mejora interna, ni un patrón de decisión a lista de temas.

Escribir para el equipo que usa el conocimiento. El cuerpo explica hechos, actividades, capacidades e implicaciones útiles. La mayor parte de procedencia, huecos y controles va en CONTROL; la incertidumbre material permanece en el cuerpo. El dueño es fuente primaria de estrategia y criterio interno; los sistemas acreditan sus hechos; contratos y mediciones sostienen transacciones y resultados. La ausencia de factura no borra una intención estratégica, ni esa intención prueba ingresos.

El legado expresamente rechazado no se importa, resume, indexa ni usa como borrador encubierto. Conservar respaldos intactos; reconstruir con fuentes primarias autorizadas o criterio experto nuevo. Una excepción requiere aprobación por fuente. Ante una corrección, detener propagación, releer el original, identificar unidades afectadas y proponer versión corregida antes de continuar.

## Captura, documentos y revisiones

Con autorización para conservar trabajo, `fuente` registra el localizador y `capturar` guarda progreso provisional en `90_Sistema/Descubrimiento/`. Mostrar IDs/rutas y ejecutar `estado` y `validar`. No es aprobación documental ni sustituye desarrollar la empresa.

Usar `ficha --archivo` para una nota operativa desarrollada y `documento` para síntesis D/X justificada. Preparar Markdown fuera de Git/bóveda antes del comando aplicable. Tags son navegación opcional. Las fuentes ya deben estar registradas; no inventar clientes, pagos, roles ni estados comerciales.

En D/X existente, `previsualizar-dx` lee y compara; `preparar-dx` almacena PRDX JSON y snapshot candidato sin editar documento. Fuentes correctivas nuevas requieren `--fuente` repetible y `sha_fuentes` resultante; un enlace sólo en cuerpo no actualiza propiedades. `aplicar-dx` exige autorización específica, hashes original/candidato/fuentes cuando aplique, responsable, referencia y respaldo externo. El flujo ordinario no cambia aprobados/retirados. `restaurar-dx` crea nueva revisión desde historial sin borrarlo. Ver [operaciones](operations.md).

## Revisión editorial y navegación

`evaluar-dx` registra EVALDX ligado a SHA, revisor, referencia, alcance de bloques y G1–G7. Decisiones: `requiere_cambios`, `recomendar_parcial`, `recomendar_integral`. Recomendar no aprueba. G2/G6 no pueden ser `no_aplica` para aprobación; recomendación integral cubre todos los bloques con `suficiente_para_tarea`.

Sólo `aprobar-dx` expresamente autorizado con SHA exacto, respaldo y confirmación literal promueve todo el documento. El cuerpo no cambia y aumenta la revisión. Cobertura parcial no se promueve integralmente. La CLI registra declaraciones; no autentica al revisor ni certifica verdad.

Proponer relaciones tipadas cuando existan extremos, con evidencia y ámbito; confirmar con controles específicos. `mapa-conocimiento` previsualiza la red. `publicar-mapa` exige autorización humana específica, confirmación literal, SHA anterior/propuesto y respaldo externo. Genera Markdown/Canvas en `00_Mapas` sin editar notas, fuentes, D/X ni las 16 Bases existentes. Regenerar exige autorización nueva; un mapa desactualizado nunca es autoridad.

## Aceptación y continuidad

`consulta-contextual` recupera bloques literales D/X y secciones de notas tipadas en `20_Entidades/`. `--orientar` busca coincidencias de los términos de la pregunta y ordena los candidatos léxicamente; no genera una respuesta semántica. Sin marcadores estables `kb:id` puede devolver `seccion_derivada_sin_id_estable`: el localizador cambia y no es identidad contractual. Excluye plantillas, fichas de fuente, capturas provisionales y CONTROL como hechos del cuerpo, y material confidencial/restringido de la búsqueda MVP sin ACL granular. Fuentes a nivel de nota no prueban cada afirmación. Restricciones `valid_from`/`valid_to` aplican cuando existen; sin fechas no se acredita vigencia. Una coincidencia puede devolver `sin_autoridad_explicita` para asunto/ámbito. Abrir candidatas y originales pertinentes antes de responder.

Probar una tarea real y una contraprueba: oferta general/acuerdo particular, vigente/histórico y cotización/cobro. Mostrar qué se escribió, qué original se leyó ahora, qué sigue propuesto y la siguiente acción empresarial útil. Guardar continuidad sin alimentar automáticamente memoria ni tareas programadas.

Referencias fuente: [arquitectura](../ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md), [ciclo experto](../CICLO_EXPERTO_DESARROLLO_EMPRESARIAL.md), [síntesis constructiva](../SINTESIS_EMPRESARIAL_CONSTRUCTIVA.md), [captura progresiva](../CAPTURA_PROGRESIVA.md), [admisibilidad del legado](../RECONSTRUCCION_EDITORIAL_Y_FUENTES.md), [ciclo documental](../CICLO_DOCUMENTAL_DX.md), [revisiones](../REVISIONES_DX_CON_HISTORIAL.md), [gobierno editorial](../GOBIERNO_EDITORIAL_DX.md), [relaciones](../RELACIONES_TIPADAS.md), [consultas](../CONSULTA_CONTEXTUAL.md).
