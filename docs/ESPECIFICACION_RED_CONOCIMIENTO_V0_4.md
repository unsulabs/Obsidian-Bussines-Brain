# Especificación de red de conocimiento — v0.4 candidato

## Propósito y definición de éxito

Cerebro Empresarial es un **método de desarrollo y recuperación de conocimiento empresarial apoyado en Obsidian y Codex**. No es un redactor de ensayos, una plantilla de 14 documentos ni un ERP/CRM. Instalar el software, comprender la empresa, registrar afirmaciones y responder una decisión son tareas diferentes.

Una persona puede explicar varios aspectos de su negocio sin conocer Obsidian. El agente debe identificar asuntos autónomos, recuperar notas existentes, proponer un mapa de propiedad del conocimiento, desarrollar piezas sustantivas y conectarlas con evidencia. **El usuario no tiene que recordarle esa arquitectura.**

El modelo funciona con una empresa sin datos iniciales y una con años de fuentes dispersas. No presupone departamentos, roles, productos, clientes, contratos ni un modelo de precios uniforme.

## Arquitectura de capas

| Capa | Unidad | Identidad / autoridad | Qué NO hace |
| --- | --- | --- | --- |
| Origen | Fuente, conversación o sistema externo | ID F-... y localizador, permiso, fecha/lectura | No copia todo ni aprueba afirmaciones |
| Trabajo provisional | Captura CAP y continuidad SES | Rondas sin autoridad empresarial | No es documento aprobado |
| Conocimiento independiente | Nota tipada: oferta, proceso, decisión, investigación, proyecto, caso, etc. | ID estable, tipo, fuentes, estado, etiquetas; vida/versión propia | No nace sólo por una mención |
| Síntesis o expediente | D01–D07 y X01–X07 | ID documental, revisión, sección/bloque, estados | No absorbe todas las ofertas, precios y procesos |
| Relación | Arista tipada entre IDs | Origen, destino, predicado, ámbito, fuente, estado de revisión | No convierte enlace en prueba de venta o contrato |
| Navegación | Bases + Markdown/Canvas derivados | Etiquetas, enlaces clicables y vistas | No modifica fuentes ni se convierte en autoridad |

El catálogo de **27 tipos operativos** es candidato, no una obligación de crear 27 entidades. D01–D07 son vistas documentales y X01–X07 expedientes condicionales, no una nota nueva por defecto. La arquitectura puede evolucionar sin crear carpetas por departamentos.

## Identidad: decidir antes de escribir

Para cada asunto extraído de fuentes admisibles se determina:

1. Qué afirmación, decisión, mecanismo o pregunta empresarial representa.
2. Qué fuente y autoridad lo respaldan; qué parte es interpretación del agente.
3. Si ya tiene **dueño canónico** en una nota existente. Se recupera su ID y evita duplicar.
4. Si su vigencia, responsable, permisos, consultas, historial o condiciones cambian por separado, justifica una nota autónoma.
5. Si sólo da contexto o es una anécdota, permanece en la fuente. No crear por acumular archivos.
6. Qué documento de dirección o portafolio debe **referenciar** la nota y explicar su significado, sin copiar el dato cambiante como otra fuente autoritativa.

Una nota grande puede ser correcta si describe un mecanismo indivisible; varias notas pueden ser incorrectas si duplican lo mismo. **No hay cuota mínima ni máxima de notas por conversación.**

## Contrato de propiedades de nota

Identidad y estado: id, tipo, clase cuando aplica, empresa_id, estado_editorial, estado_conocimiento cuando exista, vigencia, sensibilidad, fuentes y registrado_en; D/X añade doc_id y revision. El contenido lleva mecanismos, decisiones y evidencia interpretables por un empresario.

Las etiquetas de Obsidian, propiedad tags, describen temas y pueden agruparse jerárquicamente. **No sustituyen** id, tipo, relación, fuente, contrato, autoridad, fecha efectiva ni permiso. Codex propone etiquetas estables y generales, no nombres de personas ni secretos.

No fijar estos campos como obligatorios en material histórico sin migración autorizada. Los comandos de creación incorporan una porción del contrato; la evaluación editorial y la revisión humana siguen separadas.

## Relaciones: dos niveles diferentes

- **Navegación:** enlaces wiki, notas enlazadas, Bases y etiquetas. Sirven para encontrar material; la presencia de un link no demuestra la relación que sugiere.
- **Relación tipada:** archivo privado bajo 90_Sistema/Relaciones con origen y destino por ID estable, predicado de vocabulario controlado, ámbito, motivo y fuente. Su estado inicial es propuesta. Una ratificación registra la declaración del revisor pero no autentica por sí sola su identidad.

Las consultas/visualizaciones deben mostrar **propuesta** distinta de **ratificada por revisor** y mantener fuentes y ámbito. Nunca inferir una contratación de una implementación técnica; distinguir ofrecido, cotizado, aceptado, contratado, entregado, facturado y cobrado.

## Navegación en Obsidian

Las 16 vistas Bases existentes son vistas derivadas de propiedades Markdown; siguen excluyendo Plantillas y preservan sus personalizaciones en una migración autorizada. La funcionalidad para filtrar/mostrar tags existe en Obsidian, pero su interfaz concreta requiere comprobación GUI en el sistema del usuario.

La CLI incorpora:

- plan-conocimiento: **sólo lectura**. Codex prepara un JSON privado con asuntos/unidades/relaciones, verifica IDs existentes, fuentes y posibles duplicados; avisa de monolitos y conserva decisiones de no crear.
- ficha y documento: crean notas nuevas con contenido desarrollado, etiquetas y fuentes. No aprueban su semántica; D/X existentes deben revisarse como propuesta.
- relacion-proponer / relacion-confirmar / relaciones: registro de vínculos tipados con consentimiento humano externo.
- mapa-conocimiento: **sólo lectura**. Previsualiza un Markdown y un Canvas nativos de Obsidian a partir de notas y relaciones guardadas, con SHA actual y propuesto; los mapas excluyen notas restringidas y distinguen estados.
- publicar-mapa: **escritura opcional**, sólo del mapa derivado, con SHA original, confirmación literal y respaldo externo. Verifica cambios concurrentes y valida la bóveda; jamás sobrescribe un mapa manual.

Los mapas derivados viven en 00_Mapas/Mapa_Derivado_Conocimiento.md y su par .canvas. Son proyecciones generadas: **no se actualizan automáticamente al editar notas**. Si cambian fuentes/notas/relaciones, Codex vuelve a previsualizar, solicita permiso y regenera. El Canvas prioriza relaciones y limita a 100 las notas para conservar legibilidad; el Markdown puede mostrar más notas. Si el Canvas es parcial, el reporte lo indica.

Las pantallas de Obsidian, compatibilidad específica, permisos multiusuario y comportamiento real de Canvas deben comprobarse en GUI. Un test de Python no los certifica.

## Instalación universal y ciclos repetibles

1. Codex abre el repo maestro, lee AGENTS y la skill de instalación, ejecuta doctor. No crea una empresa si ya tiene una bóveda.
2. Con consentimiento crea bóveda nueva privada **fuera de Git** o diagnostica una ya existente. Las migraciones no se aplican por actualizar código.
3. Recupera fuentes admitidas y pregunta sólo por el criterio K1 que cambie una decisión. No reconstruye desde textos expresamente rechazados.
4. Antes de redactar una narrativa multiasunto, propone **reutilizar, revisar, crear, no crear** con fuentes, etiquetas, relaciones y una única ubicación canónica de cada dato. Ejecuta plan-conocimiento y presenta el mapa al dueño.
5. Tras revisión de significado y permisos, crea o propone modificaciones de notas por unidades; conserva SHA y versiones de documentos anteriores.
6. Registra relaciones sólo después de que ambos ID existan, con fuentes y estados separados.
7. Verifica con validar, estado, consulta-contextual y una pregunta negativa por contexto/fecha. No llamar RAG a una búsqueda textual.
8. Previsualiza mapa-conocimiento; publica con backup y autorización explícita y abre Canvas/Markdown en Obsidian.
9. Registra continuidad SES para que otra sesión relea originales y estados, no memorice una conversación como autoridad.

Este flujo debe funcionar con otra empresa **sin cambiar prompts para adoptar el modelo comercial, los archivos ni las decisiones de la primera**.

## Fallas que bloquean aceptación

- D01 largo sin haber evaluado conocimiento con vida propia; D01 duplicado para incorporar otra sección.
- Crear fichas vacías sólo porque aparecen sustantivos en un relato.
- Etiquetas tratadas como evidencia o relaciones tratadas como contratos.
- Reescribir un documento aprobado, una vista Bases personalizada o un mapa manual sin permiso, SHA y respaldo.
- Ignorar permiso o estado temporal; entregar respuestas como vigentes porque el archivo es el más reciente.
- Capturar secretos o materiales de clientes en el repositorio maestro.
- El agente necesita que el dueño le recuerde la puerta de arquitectura.

## Evidencia y límites del producto

Las suites sintéticas comprueban instalación, contratos, seguridad, validadores, plan, relaciones, grafo, mapa y revisión documental. Se requiere además una **prueba ciega de Codex** en una conversación nueva: ante una empresa ficticia con múltiples asuntos, debe proponer espontáneamente distribución; ante un asunto indivisible, debe justificar una sola nota; debe responder una consulta positiva y una negativa. También falta la aceptación real de Obsidian GUI, restauración aislada y segunda computadora antes de producción multiempresa.

No confundir **código reproducible**, **primer piloto local**, **aceptación editorial** y **producción**.
