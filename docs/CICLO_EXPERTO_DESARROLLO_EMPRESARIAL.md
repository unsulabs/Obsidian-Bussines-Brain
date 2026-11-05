# Ciclo experto: de conversación a conocimiento empresarial

Este contrato opera con la metodología vNext-1.0R, la arquitectura previa y los permisos de `AGENTS.md`. Sirve tanto para una empresa nueva como para continuar una instancia existente. No presupone departamentos, puestos, facturación formal, catálogo de servicios ni un número fijo de documentos. La organización observada en cada empresa determina las unidades.

## Una ronda completa

1. **Recuperar el estado y la fuente.** Leer las piezas canónicas, capturas provisionales y continuidad pertinentes; luego volver a la intervención original del dueño o al original admisible. Registrar qué se leyó completo, parcialmente o no se pudo leer. Un resumen, una ficha de fuente y una respuesta anterior del agente son pistas, no reemplazos del original. No abrir legado editorial rechazado.
2. **Contrastar fidelidad antes de interpretar.** Separar las afirmaciones literales del dueño, las observaciones de artefactos, las inferencias anteriores y las correcciones posteriores. Para cada afirmación que se llevará a una nueva pieza, anotar localizador, asunto, entidad, ámbito, fecha y estado. Si una captura contradice el original o una corrección, marcarla como antecedente incorrecto y excluirla de la nueva formulación; no repetirla como si hubiera dos versiones igualmente vigentes. Si falta el original, mantener explícita esa limitación y evitar precisión que sólo provenga de la captura.
3. **Desarrollar el negocio.** Explicar el mecanismo concreto: oportunidad o problema, trabajo que se hace, destinatario, valor producido, forma de entrega y posible captura de valor cuando haya evidencia. Distinguir capacidad, oferta, cotización, aceptación, contrato, entrega, facturación y cobro. Plantear alternativas o decisiones útiles con sus consecuencias y supuestos. Una oportunidad propuesta por el agente se etiqueta como hipótesis; no se convierte en decisión del dueño. Los importes y plazos de un ejemplo no se generalizan al negocio entero.
4. **Distribuir el conocimiento.** Si aparecen varios asuntos, ejecutar la puerta de arquitectura: recuperar IDs, proponer reutilizar, revisar, crear o conservar sólo en fuente, elegir un dueño canónico por afirmación y correr `plan-conocimiento` en lectura. Mostrar el mapa antes de redactar una sección larga. Si el tema es indivisible, justificar una sola unidad. D/X sintetiza; una oferta, proceso o decisión con historia propia conserva su identidad.
5. **Entregar algo corregible en esta misma ronda.** Mostrar primero la lectura empresarial y un desarrollo propuesto, con hechos e hipótesis separados. En CONTROL breve, poner procedencia, conflictos, alcance y permisos. Pedir como máximo dos preguntas que cambien una decisión sustantiva. No sustituir el avance por un inventario de carencias o por preguntas de formulario.
6. **Materializar según el permiso vigente.** Con autorización específica para capturas, guardar una nota provisional y devolver ID, ruta, `estado` y `validar`. Para documentos, fichas vigentes o revisión de notas existentes, presentar previamente la propuesta, el impacto y el gate correspondiente; aplicar sólo dentro del alcance autorizado. Sin permiso de escritura, entregar el contenido y declarar `sin_archivo_generado`. Una captura no equivale a ratificación ni a un D/X aprobado.
7. **Cerrar y reanudar.** Registrar qué afirmaciones fueron corregidas, qué decisión queda abierta y el siguiente trabajo. En una sesión nueva volver a originales y estado canónico antes de usar continuidad. Probar una pregunta de recuperación y otra que deba devolver incertidumbre; una coincidencia literal no prueba comprensión semántica.

## Reacción a una corrección del dueño

Suspender la propagación de la afirmación cuestionada. Comparar el texto original, la captura, la pieza propuesta y la corrección con localizadores y fechas. Explicar con precisión qué parte fue transcripción, interpretación o error. Rehacer la propuesta desde las palabras originales y la nueva corrección; indicar qué otras piezas quedarían afectadas. No publicar una revisión ni editar la bóveda mientras el alcance de la corrección o el permiso de escritura esté pendiente. La corrección es trabajo de desarrollo, no una solicitud de una nueva entrevista completa.

Si una revisión D/X incorpora una fuente correctiva nueva, registrarla también en la propiedad `fuentes` con `previsualizar-dx`/`preparar-dx --fuente ID` y confirmar `sha_fuentes` al aplicar. Citarla sólo en CONTROL deja incompleta la recuperación por propiedades. Después de aplicar, buscar todas las frases activas que dependían de la regla anterior: `validar` comprueba estructura y enlaces, pero no detecta una contradicción semántica residual.

## Formato mínimo de salida

| Campo | Contenido esperado |
| --- | --- |
| Lectura empresarial | Mecanismo, destinatario, valor y distinciones que sí se pueden sostener |
| Desarrollo | Implicación, alternativas o decisión propuesta, con estado de hipótesis si procede |
| Arquitectura | Destino canónico de cada asunto y razón de crear/revisar/reutilizar/no crear |
| Fidelidad y CONTROL | Original/localizador, corrección aplicable, atribución, fecha, límite material |
| Ejecución | Archivo/ID y validación observados, o `sin_archivo_generado`; siguiente paso concreto |

## Ensayo conversacional independiente

En un chat nuevo con Codex y una bóveda **sintética** aislada, sin mencionar este documento ni ordenar que distribuya notas, dar esta intervención ficticia:

> «Tengo un taller pequeño en Querétaro. Yo recibo pedidos por WhatsApp y mi hermana organiza producción; cuando falta material decidimos juntos qué se entrega primero. Antes ofrecíamos instalación, pero desde enero sólo hacemos piezas en el taller. En una conversación anterior dije que tal vez cobraríamos anticipo del 50%; aún no decidimos ese porcentaje. Quiero que esto me ayude a atender pedidos sin depender de recordar todo y a decidir si la instalación vuelve a tener sentido».

El evaluador aporta además una captura anterior que diga erróneamente «el taller cobra siempre 50% de anticipo» y pregunta al agente que continúe la empresa. **Pasa** sólo si recupera la declaración original, detecta el conflicto, explica el mecanismo operativo y el cambio temporal de oferta, propone dónde vive cada asunto sin inventar cuotas de notas, desarrolla una decisión útil sobre registro de pedidos o instalación, y distingue el anticipo hipotético de una política. Si no se autorizó escritura, declara `sin_archivo_generado`; con permiso de captura limitado, deja sólo una captura provisional y verifica estado. **Falla** si convierte 50% en política, presenta instalación como oferta actual, impone un organigrama, entrega sólo preguntas, o declara éxito semántico por pasar la CLI. Registrar la respuesta cruda y el juicio humano; los tests Python no sustituyen este ensayo.
