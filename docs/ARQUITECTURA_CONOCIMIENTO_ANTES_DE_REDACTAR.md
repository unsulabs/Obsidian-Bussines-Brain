# Arquitectura del conocimiento antes de redactar — contrato operativo

## El problema resuelto

Una clase D01–D07 no obliga a crear un documento largo ni a concentrar todo el conocimiento en él. El Cerebro Empresarial tampoco debe crear docenas de fichas vacías. **Cada asunto con vida independiente merece un destino razonado**: conservar en su fuente, integrar una nota existente, crear una nota autónoma, o explicar el conjunto mediante un documento D/X. La decisión se realiza ANTES de redactar.

Esta es una puerta **obligatoria del flujo agéntico** cuando una narración de un experto mezcla estrategia, oferta, procesos, decisiones, casos o investigación. No esperar a que el dueño lo recuerde.

## Cuatro capas complementarias

- **Fuentes originales:** declaraciones, conversaciones, documentos, aplicaciones y registros con procedencia y permisos. La bóveda guarda referencias, no tiene que duplicar archivos privados.
- **Unidades de conocimiento con identidad:** entidades, ofertas, procesos, decisiones, casos, investigaciones y recursos. Justificarlas por consulta, vigencia, permisos, mantenimiento, responsable e historia propia. Primero buscar ID existente.
- **Síntesis y documentos canónicos:** D01 explica decisiones estratégicas y enlaces a las notas; D03 expone portafolio; D04 sistema de ejecución; D05 economía; X01–X07 sólo cuando se requiere expediente especializado. Un resumen cita su fuente canónica: NO duplica tarifas, procedimientos, decisiones ni compromisos.
- **Navegación:** propiedades y etiquetas de Obsidian para localizar temas; enlaces wiki para recorrer notas; relaciones tipadas con fuente, ámbito, dirección y estado. Las etiquetas NO prueban identidad, autoridad ni vigencia.

## Puerta 0: diseñar dónde vive cada idea

1. Recuperar las fuentes admisibles, lo ya documentado y las notas existentes; no reconstruir desde textos rechazados.
2. Extraer **asuntos concretos** y su importancia para la empresa; distinguir decisiones del dueño, episodios, ofertas, procesos y propuestas del agente. No recortar explicaciones que contienen el porqué de una decisión.
3. Para cada asunto, decidir **un único dueño canónico**: nueva nota, nota existente, documento D/X o sólo fuente. Otras notas pueden enlazarlo. Una mención no es una entidad.
4. Explicar para cada nota independiente por qué tiene historia, alcance, dueño, vigencia o necesidad de consulta propia. Contrastar con la alternativa de conservarlo en la misma nota.
5. Proponer etiquetas temáticas específicas y relaciones tipadas con razón y fuente. Evitar etiquetas con nombres personales o información de clientes.
6. Preparar un JSON de trabajo fuera de Git y de la bóveda, conforme al ejemplo de **ejemplos/planes_conocimiento/plan_empresa_sintetica.json**.
7. Ejecutar en **sólo lectura**: python3 scripts/cerebro.py plan-conocimiento --vault RUTA --archivo RUTA_DEL_PLAN.
8. Mostrar primero al propietario un **mapa de conocimiento** que diga REUTILIZAR, ACTUALIZAR, CREAR o NO CREAR. Si el plan concentra tres asuntos en un solo D/X, explicar por qué no hay ninguna identidad separada. Corregir advertencias.
9. **Después** de revisar y aprobar el mapa, desarrollar el contenido útil de cada unidad. Mantener temporalidad, fuente, estado editorial y una revisión humana por pieza. No hacer modificaciones productivas sin autorización específica.

Los comandos de creación de fichas y documentos aceptan **--etiqueta** repetible para nuevas notas. Además, **ficha --archivo RUTA** permite crear una nota empresarial desarrollada sin bloques de relleno: se verifica el Markdown privado sin YAML y la validez estructural tras guardar. Tags como direccion/modelo-valor o operacion/procesos son índices temáticos, nunca autoridad de hechos.

## Contrato de entrada de plan-conocimiento

El JSON contiene:

- **pregunta**: qué tarea o pregunta empresarial motiva organizar este conocimiento.
- **asuntos**: clave estable de trabajo, criterio fiel a la fuente, por qué importa y IDs de fuente F- existentes o por registrar.
- **unidades**: clave, título, acción (crear / revisar / referenciar / no_crear), tipo del catálogo de 27 entidades o documento D/X, ID existente y clase cuando aplican, asuntos asignados, justificación de identidad y etiquetas si existe nota.
- **relaciones**: lista de aristas candidatas entre claves de unidades, usando el vocabulario controlado del sistema, dirección, ámbito y fundamento concreto.

Ningún asunto debe pertenecer como texto canónico a dos notas distintas; las otras sólo remiten a la nota propietaria o explican una implicación distinta. El plan nunca escribe contenido ni registra relaciones automáticamente. Los IDs reales de nuevas notas se conocen sólo después de crearlas y las relaciones tipadas se preparan cuando ambos extremos existen.

El programa revisa estructura, coberturas, referencias a notas, fuentes, duplicados, etiquetas y posibles monolitos. **No decide por sí solo qué es estratégicamente importante ni mide calidad empresarial**. Codex prepara y justifica la clasificación; el usuario aprueba el mapa.

## Ejemplo 100% sintético

Una firma ficticia explica en una conversación su estrategia, una oferta cambiante, un proceso ejecutable y una anécdota menor. Un plan razonable propondría revisar D01 para el mecanismo estratégico, crear o revisar una oferta por sus términos, conservar el proceso como nota operativa propia y dejar la anécdota en la fuente. Los vínculos entre D01 y las dos notas son candidatos sujetos a fuente y confirmación.

No es un mandato de generar cuatro notas ni un documento por cada frase. Una nota sólo justifica su existencia si puede usarse y mantenerse independientemente.

## Aceptación real

Falla una entrega que:
- Entrega un ensayo largo sin evaluar primero otras ubicaciones para el conocimiento;
- Crea muchas notas vacías o duplica contenido con versiones divergentes;
- Convierte etiquetas o enlaces en hechos aprobados;
- Trata interpretación del agente como decisión del dueño;
- No prueba una pregunta de recuperación sobre las unidades y una contraprueba;
- Requiere que el usuario le recuerde a Codex planificar la arquitectura.

El producto ofrece la capacidad y obliga al agente a activar la puerta en sus instrucciones. La aceptación de su uso real por Codex exige una prueba en una conversación nueva sin decirle que distribuya las notas.

## Continuidad tras la distribución (0.4)

Al crear o revisar notas autorizadas y registrar relaciones tipadas, Codex debe ofrecer **mapa-conocimiento** como previsualización de la red. Markdown muestra las notas y los vínculos clicables; Canvas ofrece flechas entre nodos con su predicado y estado. No se publica automáticamente. Se necesita decisión del dueño, comparación de hashes y respaldo externo para ejecutar **publicar-mapa**; un mapa de empresa no es autoridad y su información puede quedar desactualizada hasta la siguiente generación.

La recomendación de **no_crear** no es requisito: en una conversación con un solo asunto relevante no se deben inventar notas innecesarias sólo para satisfacer al validador. Varias unidades sin vínculos pueden ser correctas si se justifica por qué son independientes.
