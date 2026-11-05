# Guía de metodología de documentación empresarial con IA

**Paso 1 de 2 — Del conocimiento disperso al conocimiento de negocio confiable**  
**Versión:** vNext-1.0R — revisión del piloto; conserva la investigación y especificaciones vNext-0.9  
**Fecha:** 26 de octubre de 2026  
**Aplicabilidad:** PyME de servicios, productos, híbridas, familiares, con equipo y por proyectos.  
**Entregable siguiente:** contrato portable para un Paso 2 en Obsidian/agentes; **NO** diseño físico de bóveda.

---

## Para quién es esta guía y qué obtiene

Esta guía es para una persona que dirige una empresa pequeña o mediana, conoce su negocio y ya conversa con una IA comercial, pero no quiere aprender ingeniería documental. El objetivo **no** es reunir archivos «por si acaso»: es recuperar información verdadera y producir explicaciones que permitan vender, decidir, operar, delegar, proteger caja y aprender, manteniendo su historial.

**Resultado del Paso 1:** un conjunto adaptado de documentos para personas, con fuentes y estados claros, y un paquete estructurado que un agente de Paso 2 podrá recibir. **No se construye Obsidian todavía**. El método debe tener valor incluso si no se hace el Paso 2.

### Qué cambió frente a generaciones anteriores

El brief DR-BRIEF-1.0 relata 64 assets, 45 tipos, ocho capítulos y DC-1.0. Sirven como advertencia, no como catálogo obligatorio. La investigación externa no determina por sí misma un número mágico de documentos; distingue tareas de conocimiento, unidades de negocio, autoridad y mantenimiento [S01,S10,S22,S27]. Este diseño usa **familias** para explicar temas y **expedientes** solo cuando tienen razón propia para existir. No cambia una PyME de tres personas en una corporación con departamentos ficticios.

### Qué corrige esta revisión tras el piloto real

La investigación que definió D01–D07 y X01–X07 **se conserva**: sus propósitos, contenidos obligatorios, estructuras, fuentes, relaciones, reglas de actualización, pruebas de utilidad, señales de extracción y prompts especializados siguen siendo la base de esta guía. El fallo observado en el piloto no fue que faltara esa especificación, sino que el flujo permitía redactarla demasiado pronto a partir de lo que la IA encontraba en archivos.

La revisión vNext-1.0R corrige **el mecanismo de adquisición del conocimiento antes de redactar**, sin sustituir el catálogo investigado:

1. **Recuperación documental:** leer y contrastar lo que ya existe.
2. **Mapa de huecos por autoridad:** distinguir lo que el experto sabe (K1), lo que debe venir de un sistema/documento (K2), lo que nadie sabe todavía (K3) y lo que no es necesario para la tarea actual (K4).
3. **Elicitación experta adaptativa:** para K1, extraer criterio, señales, trade-offs, excepciones y razonamiento mediante episodios reales; no rellenar el hueco con disclaimers.
4. **Gate de conocimiento:** ningún documento se considera listo para redacción final si falta criterio experto material, particularidad de la empresa o una tarea real que pueda resolver.
5. **Síntesis empresarial:** el cuerpo explica cómo funciona la empresa; CONTROL conserva el detalle de procedencia, limitaciones y auditoría.
6. **Auditoría reforzada:** la no-genericidad no se prueba con nombres, fechas o cantidades; se prueba con mecanismos, criterios, decisiones, excepciones y vocabulario propio de la empresa.

**Lo que no cambia:** el contenido exacto que debe tener cada D/X, la diferenciación semántica investigada, la temporalidad, la autoridad por asunto, la trazabilidad, las pruebas de utilidad y el handoff al Paso 2.

### Qué hará realmente el dueño (y qué no)

1. Elegirá la IA que ya usa y pondrá a su alcance las fuentes autorizadas.
2. Corregirá significado cuando la IA interprete mal algo que sí conoce.
3. Responderá **preguntas expertas de alto valor** únicamente sobre huecos K1: criterios, señales, excepciones, decisiones y razonamiento que todavía no estén documentados.
4. No tendrá que recordar de memoria cifras, contratos, inventarios o transacciones que deban venir de un sistema: para K2 se buscará la fuente correcta.
5. Probará los documentos con situaciones reales y autorizará decisiones o políticas cuando le corresponda.

No tendrá que programar Obsidian, escribir YAML, nombrar archivos técnicos, rellenar formularios extensos, repetir información que la IA ya leyó ni convertir una conversación en un examen general de su empresa. La entrevista se adapta a lo ya recuperado.

### Lo que la IA sí tiene que hacer

Antes de preguntar: buscar, leer el contenido importante, comparar fuentes, verificar versiones y detectar estado temporal. Después debe distinguir **qué clase de conocimiento falta**. Si el hueco es K1, debe elicitarlo del experto; si es K2, debe localizar o pedir la fuente exacta; si es K3, debe conservarlo como hipótesis/pendiente; si es K4, no debe bloquear.

Durante la escritura: sintetizar fuentes + criterio experto y explicar la empresa, no narrar el proceso interno de investigación. Después: contrastar lo escrito con las fuentes adecuadas, probar la utilidad, marcar pendientes, registrar impactos y separar CONTROL del cuerpo empresarial. Si una herramienta carece de conexión o permisos, debe decirlo; eso no autoriza a convertir el hueco en una conclusión ni a llenar el documento de frases defensivas.

## Fundamentos que cambiaron el método (síntesis de investigación)

- Las elecciones, renuncias y actividades coordinadas son más importantes para estrategia que la retórica de misión [S01]. Un operating model permite ver integración y procesos, no tiene que convertirse en un sistema de arquitectura corporativa [S03].
- Un canvas explica hipótesis de creación/captura de valor [S04,S05], pero no acredita lo que se contrató. Los trabajos a resolver deben confirmarse con episodios y comportamiento, no buyer personas inventadas [S06,S07].
- La taxonomía APQC ayuda a detectar huecos y explícitamente se personaliza a la empresa [S10]. Para experiencias de servicio, el blueprint ayuda a hallar fallas y dependencias [S09]; los SOP se justifican por riesgo/recurrencia/delegación y no por simetría [S11,S12].
- Resultados financieros, compromisos y escenarios requieren base y temporalidad diferentes [S13,S15]. Los derechos de decisión pueden documentarse por facultades incluso sin organigrama [S16,S17].
- El conocimiento produce valor cuando se revisa, comparte, encuentra y utiliza [S22], y las lecciones necesitan evidencia de episodios antes de modificar supuestos [S21,S23,S24].
- La procedencia y la autoría modular pueden tomar principios de PROV y DITA [S26,S27] sin obligar al dueño a escribir RDF o XML. Las particularidades de Obsidian [S28,S29] solo se usan para compatibilidad posterior.

**Qué NO demuestra la bibliografía:** que una determinada cifra de archivos sea la óptima, que un formato JSON garantice interpretación exacta o que todo conocimiento tácito pueda documentarse perfectamente. Esas son hipótesis prácticas que deberán probarse.

## Matriz de autoridad por tipo de conocimiento

La metodología no exige el mismo tipo de prueba para todo. Antes de declarar que «falta evidencia», la IA debe identificar qué fuente **debe** tener autoridad para esa pregunta.

| Tipo de conocimiento | Fuente primaria preferida | Corroboración útil | Error que debe evitarse |
|---|---|---|---|
| Estrategia, prioridades, renuncias | dueño/decisor autorizado | decisiones pasadas, asignación de recursos, resultados | exigir «prueba de mercado» para saber qué decidió la empresa |
| Criterio profesional y señales de calidad | experto que ejecuta | casos, contrastes, resultados | tratar conocimiento experto como simple opinión irrelevante |
| Oferta, precio y política comercial vigente | autoridad comercial + versión vigente | catálogo, propuesta, contrato, historial de cambios | generalizar un precio particular o usar una cotización antigua |
| Hecho transaccional, caja, pago | sistema de registro/comprobante/conciliación | factura, banco, contabilidad | usar memoria o testimonio como sustituto del registro |
| Proceso real | ejecutor + observación/caso | SOP, checklist, logs | confundir procedimiento ideal con práctica real |
| Voz/preferencia del cliente o mercado | cliente, episodios y datos agregados | CRM, entrevistas, ventas, pérdidas | convertir la opinión del fundador en voz del mercado |
| Obligación contractual/legal | contrato/norma/asesoría aplicable | anexos, actas, resoluciones | presentar interpretación de IA como autoridad |
| Riesgo y criticidad operativa | dueño/equipo experto + incidentes | controles, fallos, historial | inventar puntuaciones para aparentar precisión |
| Resultado de negocio | sistema/medición | evidencia del caso y periodo | inferir causalidad desde una anécdota |
| Hipótesis futura | decisor/analista | experimento posterior | redactarla como hecho vigente |

**Regla práctica:** la declaración de un dueño puede ser fuente primaria válida de una decisión estratégica que él tiene facultad de tomar; no sirve por sí sola para certificar una transferencia bancaria, una preferencia general del mercado o una obligación legal externa.

## Mapa de necesidades antes de escoger documentos

La IA no debe comenzar con «¿cuántas carpetas quieres?». Recorre necesidades por decisiones:

- **Necesidad y propósito:** ¿Qué problema resuelve y dónde gana/pierde valor?
- **Clientes y contexto:** ¿Quién usa, paga y decide y en qué situación?
- **Promesa verificable:** ¿Qué se vende y cuáles son exclusiones?
- **Captación y conversión:** ¿Cómo llega una demanda hasta un acuerdo?
- **Experiencia y entrega:** ¿Qué secuencia, contingencia y aceptación funcionan?
- **Economía por unidad:** ¿Qué cobra, cuesta y deja cada modalidad?
- **Liquidez y compromisos:** ¿Qué entra y sale de caja y en qué fecha?
- **Quién decide:** ¿Quién puede autorizar promesas/gasto/excepciones?
- **Capacidad y continuidad:** ¿Qué falla al faltar persona, sistema, activo o proveedor?
- **Obligaciones:** ¿A qué se comprometió la empresa, con qué límites?
- **Información sensible:** ¿Quién puede acceder, conservar y compartir?
- **Aprendizaje:** ¿Qué pasó, qué se aprendió, qué política sí se aprobó?
- **Temporalidad:** ¿Qué era verdad antes, qué es vigente y qué se está probando?
- **Recuperación/autoridad:** ¿Dónde está la fuente y quién prevalece si hay conflicto?

## Secuencia de trabajo del propietario y del asistente

## El recorrido completo, de cero a un handoff

### Etapa 0. Preparar acceso sin trasladar secretos

Entregar a la IA únicamente fuentes autorizadas, preferiblemente copiadas o enlazadas desde un sistema conocido. Prioridad: contratos/propuestas reales, conversaciones sustantivas, documentos de ejecución, ventas, costos, procedimientos, incidentes y decisiones. Cuando el negocio usa correo/CRM/Drive, la IA solo puede recuperarlos mediante conexión efectiva y permisos. Si una plataforma no puede recuperar conversaciones históricas, se exportan o seleccionan las conversaciones relevantes.

**Salida:** mapa de conexiones probadas y fuentes disponibles, con restricciones; sin copiar contraseñas ni tokens.

### Etapa 1. Recuperar para decidir qué NO preguntar

La IA ejecuta P01, lee el contenido sustantivo y registra cada fuente una sola vez. Extrae hechos, decisiones, compromisos, casos, cambios, excepciones, cifras, procesos y criterios ya explícitos. Un contrato puede aportar a varios documentos, pero no se pega cuatro veces. Si una fuente histórica contradice un resumen, se relee el original.

Después clasifica cada hueco:

- **K1 — conocimiento experto disponible:** el dueño/equipo probablemente lo sabe y debe elicitarse.
- **K2 — conocimiento registrado:** debe venir de un archivo/sistema/comprobante concreto.
- **K3 — conocimiento no resuelto:** nadie lo sabe todavía; se vuelve hipótesis, investigación o decisión pendiente.
- **K4 — no necesario ahora:** no bloquea la tarea actual.

**Salida:** registro de fuentes + preguntas ya respondidas + mapa K1/K2/K3/K4.

### Etapa 2. Elicitar criterio experto y elegir qué desarrollar primero

Para los huecos K1, la IA ejecuta P01C. No usa una entrevista genérica. Parte de episodios reales y pregunta por señales, elecciones, contrastes, excepciones, errores, trade-offs y criterios que un novato no vería. Cada ronda tiene como máximo cinco preguntas, todas ligadas a un contenido obligatorio concreto del D/X que se quiere desarrollar.

Para K2 solicita/localiza la fuente exacta; para K3 no fuerza una respuesta; para K4 continúa.

Después aplica P02 y elige el documento/sección que permita más decisiones reales por unidad de esfuerzo. El criterio de separación sigue siendo identidad, ciclo de vida, audiencia, permiso, autoridad y recuperación, no simetría.

**Salida:** conocimiento documental + conocimiento experto + lista corta y razonada de unidades de trabajo.

### Etapa 3. Pasar el gate de conocimiento y construir documentación con contenido

Antes de ejecutar DES-[ID], la unidad debe pasar el **Gate G1–G7** descrito más adelante. En particular, si faltan criterio experto material (G2) o particularidad empresarial (G6), **no se redacta una versión final llena de reservas**: se regresa a P01C o se pide una fuente K2.

Una vez superado el gate, DES-[ID] conserva íntegramente el contenido obligatorio, estructura, relaciones, actualización, prueba de utilidad y contrato de extracción definidos por la investigación. La IA sintetiza fuentes + conocimiento experto. Si queda un K3 real, lo delimita brevemente en el documento y mantiene el detalle en CONTROL.

**Salida:** documento empresarial que explica cómo funciona la empresa y puede usarse en una tarea real.

### Etapa 4. Revisar significado, criterio y utilidad, no solo formato

P03 coteja fuente→documento y documento→fuente, pero además verifica que el documento capture el criterio experto apropiado, no promueva un caso a regla y no sea «específico» sólo por tener nombres, fechas y montos. Una persona autorizada revisa decisiones materiales.

**Salida:** documento corregido + prueba empresarial ejecutada + confirmación de Q1–Q10.

### Etapa 5. Versionar y rastrear efectos

El asistente conserva versión anterior, fecha efectiva, ID estable de bloque y referencias. Al cambiar una condición, actualiza la autoridad correspondiente y marca derivados; no reescribe históricos. Los cambios se registran en CONTROL y se propagan únicamente con permiso.

### Etapa 6. Mantener con trabajo nuevo

La persona comparte una conversación/audio/archivo y pide incorporarlo. P06 procesa la fuente una vez, distingue hechos/propuestas, identifica impactos y clasifica nuevos huecos K1–K4. Si el cambio revela criterio experto faltante, P01C lo elicita antes de reescribir la autoridad. P07 reanuda desde manifest + fuentes + conocimiento experto documentado, no desde memoria.

### Etapa 7. Verificar, entregar y NO construir la bóveda todavía

P08 ejecuta pruebas prácticas, E01–E16 y C01–C11 con el criterio reforzado de esta revisión. P09 construye manifiesto, esquema, autoridades y tests consulta→bloque→fuente. La aprobación del handoff no equivale a implementación de Obsidian.

## Gate de conocimiento antes de una redacción final

Cada D/X puede estar en descubrimiento, pero sólo se considera listo para redacción final si pasa:

- **G1 Base recuperada:** se leyeron las fuentes sustantivas accesibles.
- **G2 Criterio experto:** se extrajo el razonamiento que no estaba en archivos y que el experto sí conoce.
- **G3 Episodio real:** al menos un caso/episodio muestra cómo opera el criterio, cuando la naturaleza del documento lo permite.
- **G4 Excepción o límite:** se conoce cuándo no aplica, qué excepción existe o qué sigue siendo K3.
- **G5 Autoridad correcta:** se sabe quién decide o qué sistema manda para cada asunto material.
- **G6 Particularidad:** hay mecanismos, elecciones, vocabulario, trade-offs, reglas o señales propias de la empresa; nombres y cantidades no cuentan por sí solos.
- **G7 Utilidad:** el documento permite ejecutar o preparar una tarea empresarial verificable.

**Regla de bloqueo:** un fallo G2 o G6 impide declarar el documento «desarrollado». La IA entrega un borrador de descubrimiento y continúa la elicitación; no rellena páginas con «no hay evidencia».

## Regla de separación: documento empresarial vs. CONTROL

El cuerpo D/X explica la empresa. CONTROL conserva la auditoría detallada: localizadores, lecturas parciales, conflictos, estados, trazabilidad y razones de incertidumbre. Un límite aparece en el cuerpo sólo cuando cambia una decisión o acción. Como señal de alerta, si el texto empresarial dedica gran parte de su narrativa a explicar lo que la IA no pudo demostrar, debe regresar a K1/K2/K3 antes de cerrar.

## Estados, autoridad y formato legible

## Cómo leer un documento y sus estados

**Una persona lee primero la narración**, la tabla de condiciones si aplica, el alcance, los criterios y las acciones. **La IA administra después** los IDs, fechas y fuentes. Nunca cambia el documento de negocio por una bitácora interminable de cómo lo generó.**Cuatro ejes independientes, nunca un estado único:**

1. **Editorial:** `borrador` / `en_revision` / `aprobado` / `retirado`. Indica quién revisó la redacción, no que toda la materia está completa.
2. **Cobertura por pregunta:** `sin_fuente` / `parcial` / `suficiente_para_tarea` / `no_aplica` (con justificación). En cuanto cambie una tarea o contexto puede cambiar la suficiencia.
3. **Conocimiento de cada afirmación:** `hecho_observado` / `decision_aprobada` / `propuesta` / `hipotesis` / `historico` / `pendiente` / `desconocido` / `conflicto`. No se deduce la certeza de la confianza retórica de la IA.
4. **Vigencia temporal:** `vigente` / `futuro` / `superseded` / `caducado` / `sin_verificar`, con `valid_from`, `valid_to` cuando se conoce. Además guardar `recorded_at` para separar fecha de ocurrencia de fecha en que se registró.

La **clase de soporte** es independiente: `documental_directo`, `testimonio_atribuido`, `observacion`, `derivado_calculado`, `sin_fuente`, `fuentes_en_conflicto`. Una decisión puede estar aprobada pero apoyarse en una hipótesis no validada. Un precio aprobado puede ser histórico. Una sección editada puede mantener cobertura insuficiente. Registrar sensibilidad (`interno`, `confidencial`, `restringido`) y acceso por unidad; no exponer datos porque el PDF se vea bonito.
**Regla operativa de autoridad:** una afirmación no tiene autoridad global: se resuelve por *asunto + entidad + contexto + vigencia + fuente + ámbito*. Para un cliente y proyecto concreto, un acuerdo aceptado puede prevalecer sobre una condición comercial general para ese alcance, pero no convierte la excepción en política universal. Para datos de caja mandan transacciones registradas/conciliadas, no un PDF presupuestal. Para intención estratégica manda el decisor autorizado; para preferencias de clientes la evidencia observada y su muestra; para leyes, la fuente normativa y asesoría aplicable, no una propuesta de IA.

**Una sola autoridad por asunto y contexto:** si X01 gobierna el precio específico de una oferta, D03 no copia su valor como regla alternativa: enlaza la ficha y muestra una síntesis *no autoritativa*. Si no existe X01, la subsección versionada de D03 es autoridad. Si X05 gobierna contrato particular, D03/X01 no lo sobreescriben. Lo que una fuente demuestra y su alcance prevalecen sobre resúmenes posteriores.

**Separación de hechos comerciales:** `usado` ≠ `ofrecido` ≠ `cotizado` ≠ `aceptado` ≠ `contratado` ≠ `entregado` ≠ `facturado` ≠ `cobrado`. Son eventos distintos que requieren evidencia diferente. `Autorizado para usar material` tampoco significa `autorizado para compartirlo fuera del equipo`.
Cada pieza canónica de Markdown lleva al inicio **sólo estos campos, administrados automáticamente por la IA** (no el propietario):

```yaml
---
doc_id: D03
schema_version: '0.9'
revision: '1.0'
editorial_status: 'en_revision'
as_of: '2026-10-25'
access: 'interno'
---
```

El cuerpo utiliza encabezados específicos para cada clase, texto humano comprensible, tablas sólo donde aporten, y comentarios de bloque **invisibles en la lectura** con IDs estables (`<!-- kb:id=D03-B004 -->`) para segmentos que requieren extracción o versionado. Las fuentes sustantivas se anotan cerca de afirmaciones sensibles mediante `[F-0007]` y se explican en la sección final «Fuentes y límites» (`F-0007 → identificador de origen + ubicación + fecha`). Un **manifest JSON auxiliar generado por IA** guarda estado, ámbito, vigencia, relaciones y procedencia de cada bloque; no necesita estar incrustado en cada párrafo. La misma fuente tiene un único ID en el registro de fuentes y puede respaldar múltiples documentos.

Si la plataforma no puede crear archivos automáticamente, debe entregar Markdown completo listo para guardar y el registro de origen copiables. Si no puede recuperar una fuente, no debe declarar que la ha revisado. Los comentarios pueden faltar en documentos legados, pero en ese caso el traspaso **no pasa el gate de parsabilidad** hasta asignar y validar IDs.

## Cómo se forma el catálogo sin duplicar conocimiento

**Familias D01–D07**: áreas de explicación de decisiones empresariales. No son «departamentos». Una microempresa puede guardarlas como secciones con IDs estables en un dossier; se independizan solo con razones reales. **Expedientes X01–X07**: oferta, procedimiento, relación, caso, acuerdo, recurso, decisión/experimento; jamás se crean todos por obligación.

Regla de independencia: necesidad de ciclo de cambio distinto, authority específica, historia, permisos, consulta útil, reutilización y sensibilidad. Si no hay motivo, mantener subsección. No separar solo para que Obsidian vea otro nodo. Hay una fuente maestra por asunto+ámbito+periodo; otras piezas referencian, no copian como autoridad.| ID | Clase documental | Independencia |
|---|---|---|
| D01 | Dirección, modelo de negocio y límites estratégicos | según utilidad/ciclo |
| D02 | Conocimiento del mercado, clientes y marca | según utilidad/ciclo |
| D03 | Portafolio y sistema comercial | según utilidad/ciclo |
| D04 | Ejecución, experiencia y calidad | según utilidad/ciclo |
| D05 | Economía, caja y criterios financieros | según utilidad/ciclo |
| D06 | Personas reales, responsabilidades y facultades | según utilidad/ciclo |
| D07 | Riesgos, compromisos y dependencias críticas | según utilidad/ciclo |
| X01 | Ficha viva de oferta individual | condicional, por identidad |
| X02 | Proceso o instrucción de trabajo autónoma | condicional, por identidad |
| X03 | Ficha de relación con una cuenta o cliente | condicional, por identidad |
| X04 | Expediente de proyecto, caso o episodio | condicional, por identidad |
| X05 | Acuerdo u obligación autónoma | condicional, por identidad |
| X06 | Recurso, sistema o proveedor crítico | condicional, por identidad |
| X07 | Decisión, experimento o lección con identidad propia | condicional, por identidad |


## Fichas completas de las clases documentales — incluyendo sus prompts

Cada ficha tiene contenido obligatorio, estructura **diferente** según su función, fuentes, estados, relaciones, actualización, prueba empresarial, señales de extracción y **los prompts íntegros de desarrollar y actualizar**. No es un formulario a rellenar: la IA redacta desde fuentes y el dueño aprueba decisiones materiales.

## D01 — Dirección, modelo de negocio y límites estratégicos

**Naturaleza:** Familia principal.  
**Propósito:** Hacer visibles las elecciones de negocio que deben orientar prioridades, concesiones y asignación de recursos; no es un folleto corporativo.  
**Preguntas que permite responder:** ¿Por qué existimos comercialmente y a quién servimos?; ¿Cómo creamos, entregamos y capturamos valor?; ¿Qué oportunidades priorizamos y cuáles rechazamos?; ¿Qué decisión se volvería inconsistente con nuestra estrategia?.

**Cuándo debe existir:** Siempre debe estar cubierto; puede ser una sección integrada en el dossier inicial cuando la empresa es muy pequeña.

**Cuándo NO crear archivo independiente:** No requiere archivo independiente si no hay más de un modelo de negocio, ciclos de revisión diferentes o decisiones estratégicas complejas.

**Entradas y fuentes que deben buscarse:**

- Propuestas/contratos ganados y perdidos
- Conversaciones fundacionales, decisiones y notas de planificación
- Datos de ventas por línea, costos y restricciones de entrega
- Evidencia del entorno y decisiones pasadas

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- Compara oportunidades reales aceptadas y rechazadas: ¿qué señales hacen que una oportunidad sí encaje o no?
- ¿Qué trabajo puede pagar bien pero deliberadamente no quiere la empresa, y por qué?
- ¿Qué prioriza cuando precio, capacidad, reputación, calidad y tiempo chocan?
- ¿Qué actividad o combinación de capacidades considera difícil de copiar y por qué?
- ¿Qué quiere construir o dejar de hacer en los próximos periodos, y qué evidencia cambiaría esa decisión?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Identidad verificable: negocio real y oferta efectivamente prestada; distinguir aspiración de actividad actual
2. Modelo de valor: pagador, usuario, comprador, trabajo a resolver, intercambio y mecánica de cobro
3. Segmentos elegidos y no elegidos, alcance geográfico, restricciones y renuncias explícitas
4. Diferencias competitivas apoyadas por actividades reales; no adjetivos aspiracionales
5. Prioridades temporales, capacidades/hitos, criterios para elegir y reglas de revisión
6. Supuestos críticos, contraevidencias, indicadores de avance con fuentes y dueño de decisión
7. Cambios de estrategia, motivos, fechas efectivas y decisiones formalmente aprobadas

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Lectura ejecutiva y fecha de corte
2. 01 Negocio efectivamente observado
3. 02 Modelo de creación–entrega–captura de valor
4. 03 Elecciones y renuncias estratégicas
5. 04 Sistema de actividades y ventajas sustentables
6. 05 Prioridades, métricas y límites
7. 06 Hipótesis, alternativas y decisiones pendientes
8. 07 Cambios y referencias de autoridad

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Los claims sobre ventas, modelo, diferenciación y compromisos llevan evidencia o estado [HIPÓTESIS]. La intención del fundador no es prueba de mercado.

**Relaciones y autoridad:** D02 valida demanda; D03 define oferta vigente; D04 capacidades; D05 márgenes/caja; D06 autoridad de decisión; X07 conserva decisiones históricas.

**Actualización y conservación histórica:** Disparadores: nueva línea material de negocio, giro de segmento, pérdida de rentabilidad, decisión de inversión, cambio explícito de prioridad. Mantener comparación antes/después y vigencias; no reescribir el pasado.

**Prueba de utilidad empresarial:** Ante dos oportunidades reales incompatibles, un decisor puede justificar cuál aceptar y por qué, sin añadir valores genéricos.

**Señales de extracción para agentes:** Bloques de MODELO, ELECCIÓN, RENUNCIA, OBJETIVO, HIPÓTESIS, INDICADOR; autoridad por asunto para estrategia aprobada.

**Ejemplo sintético (no fuente real):** SINTÉTICO: Brisa Modular decide no aceptar instalaciones fuera de 80 km en 2027 por incompatibilidad entre costo de traslado y margen. Es decisión aprobada sólo si existe acta o validación del dueño; una cotización rechazada por sí sola es un caso.

**Fundamento externo relacionado:** [S01], [S03], [S04], [S14], [S21], [S32]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D01 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D01 — DIRECCIÓN, MODELO DE NEGOCIO Y LÍMITES ESTRATÉGICOS
    Objetivo de negocio: Hacer visibles las elecciones de negocio que deben
    orientar prioridades, concesiones y asignación de recursos; no es un folleto
    corporativo.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Propuestas/contratos ganados y perdidos
- Conversaciones fundacionales, decisiones y notas de planificación
- Datos de ventas por línea, costos y restricciones de entrega
- Evidencia del entorno y decisiones pasadas

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Contrastaste elegir/no elegir y actividades reales; redacta al menos una
    renuncia, un trade-off, una prueba que podría falsar un supuesto y una
    decisión pendiente.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Identidad verificable: negocio real y oferta efectivamente prestada;
    distinguir aspiración de actividad actual
2. Modelo de valor: pagador, usuario, comprador, trabajo a resolver,
intercambio y mecánica de cobro
3. Segmentos elegidos y no elegidos, alcance geográfico, restricciones y
renuncias explícitas
4. Diferencias competitivas apoyadas por actividades reales; no adjetivos
aspiracionales
5. Prioridades temporales, capacidades/hitos, criterios para elegir y reglas
de revisión
6. Supuestos críticos, contraevidencias, indicadores de avance con fuentes y
dueño de decisión
7. Cambios de estrategia, motivos, fechas efectivas y decisiones formalmente
aprobadas

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Lectura ejecutiva y fecha de corte
2. 01 Negocio efectivamente observado
3. 02 Modelo de creación–entrega–captura de valor
4. 03 Elecciones y renuncias estratégicas
5. 04 Sistema de actividades y ventajas sustentables
6. 05 Prioridades, métricas y límites
7. 06 Hipótesis, alternativas y decisiones pendientes
8. 07 Cambios y referencias de autoridad

    INSTRUCCIÓN DE PROCEDENCIA: Los claims sobre ventas, modelo, diferenciación y
    compromisos llevan evidencia o estado [HIPÓTESIS]. La intención del fundador
    no es prueba de mercado.
    CONEXIONES A VERIFICAR: D02 valida demanda; D03 define oferta vigente; D04
    capacidades; D05 márgenes/caja; D06 autoridad de decisión; X07 conserva
    decisiones históricas.
    CONTROL DE VIGENCIA: Disparadores: nueva línea material de negocio, giro de
    segmento, pérdida de rentabilidad, decisión de inversión, cambio explícito de
    prioridad. Mantener comparación antes/después y vigencias; no reescribir el
    pasado.
    PRUEBA DE UTILIDAD A EJECUTAR: Ante dos oportunidades reales incompatibles,
    un decisor puede justificar cuál aceptar y por qué, sin añadir valores
    genéricos.
    CONTRATO DE EXTRACCIÓN: Bloques de MODELO, ELECCIÓN, RENUNCIA, OBJETIVO,
    HIPÓTESIS, INDICADOR; autoridad por asunto para estrategia aprobada.

    Si D01 no necesita archivo autónomo según el criterio «No requiere archivo
    independiente si no hay más de un modelo de negocio, ciclos de revisión
    diferentes o decisiones estratégicas complejas.», desarrolla la unidad como
    sección identificada dentro del documento de autoridad apropiado y explica
    por qué. Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=D01-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D01 — Prompt completo de actualización

```text
ACTUALIZA D01 — Dirección, modelo de negocio y límites estratégicos
conservando continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D01.
    Especial atención a: Contrastaste elegir/no elegir y actividades reales;
    redacta al menos una renuncia, un trade-off, una prueba que podría falsar un
    supuesto y una decisión pendiente.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: nueva línea material de
    negocio, giro de segmento, pérdida de rentabilidad, decisión de inversión,
    cambio explícito de prioridad. Mantener comparación antes/después y
    vigencias; no reescribir el pasado.
    5. Verifica autoridad y destinos afectados: D02 valida demanda; D03 define
    oferta vigente; D04 capacidades; D05 márgenes/caja; D06 autoridad de
    decisión; X07 conserva decisiones históricas.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Ante dos oportunidades reales
    incompatibles, un decisor puede justificar cuál aceptar y por qué, sin añadir
    valores genéricos.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## D02 — Conocimiento del mercado, clientes y marca

**Naturaleza:** Familia principal.  
**Propósito:** Separar lo que se sabe de compradores reales de lo que se presume sobre ellos y decidir qué promesas de marca están probadas.  
**Preguntas que permite responder:** ¿Qué situaciones hacen que alguien compre o no compre?; ¿Quién decide, paga, usa e influye?; ¿Qué atributos de marca reconocen los clientes?; ¿Qué segmentos son evidencia y cuáles hipótesis?.

**Cuándo debe existir:** Siempre existe cobertura mínima de clientes o usuarios; la separación física crece con heterogeneidad de segmentos y datos de investigación.

**Cuándo NO crear archivo independiente:** Puede quedar integrado con D03 si solo hay una audiencia y dos o tres observaciones verificadas; no inventar buyer personas por ausencia de datos.

**Entradas y fuentes que deben buscarse:**

- Entrevistas situadas y transcripciones con consentimiento
- Preguntas repetidas de prospectos y razones de pérdida de propuestas
- Ventas/CRM con fecha y segmento
- Quejas, reseñas, servicio y postventa
- Elementos existentes de identidad visual/verbal

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- Compara clientes excelentes y problemáticos: ¿qué señales aparecen antes de contratar?
- ¿Qué pregunta, comportamiento o circunstancia revela mejor el trabajo que el cliente intenta resolver?
- ¿Qué objeciones son literales y cuáles suelen esconder otra preocupación?
- ¿Qué promesa o claim nunca haría la empresa aunque ayudara a vender?
- ¿Qué creencia sobre clientes ha cambiado después de experiencias reales?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Distinción explícita entre comprador, aprobador, pagador y usuario
2. Situaciones/Jobs to Be Done reconstruidos a partir de episodios concretos
3. Evidencia por segmento, tamaño y sesgo de la muestra; no extrapolación
4. Obstáculos, alternativas usadas, criterios de decisión y disparadores de compra
5. Canales donde se observa contacto y mensajes comprobables
6. Posicionamiento: asociaciones deseadas versus percibidas; claims autorizados/prohibidos
7. Vacíos de conocimiento, preguntas de descubrimiento y señal de actualización

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Hallazgos verificables y grado de certeza
2. 01 Actores y circunstancias de compra
3. 02 Segmentos observados e hipótesis
4. 03 Trabajos, fricciones y alternativas por episodio
5. 04 Evidencia de demanda y objeciones
6. 05 Posicionamiento, señales de marca y lenguaje
7. 06 Lo que NO sabemos y experimentos de contraste
8. 07 Fuentes, alcance y revisiones

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Cada insight indica número y diversidad de episodios, fechas y dónde se observó; opinión del fundador se registra separada de voz del cliente.

**Relaciones y autoridad:** D01 selecciona segmentos; D03 recoge promesas publicables; X03 documenta relaciones específicas; X04 episodios de entrega y contraevidencia.

**Actualización y conservación histórica:** Disparadores: nueva investigación, cambios en objeciones/alternativas, pérdida de clientes, nueva evidencia de asociaciones, segmentos nuevos. Registrar discrepancias y no borrar casos.

**Prueba de utilidad empresarial:** Un vendedor prepara una conversación para un comprador específico sin recurrir a una persona psicológica inventada.

**Señales de extracción para agentes:** ACTOR, SEGMENTO, JOB, OBSERVACIÓN, CLAIM, PROHIBICIÓN; cada generalización tiene alcance, muestra y fuente.

**Ejemplo sintético (no fuente real):** SINTÉTICO: 3 de 5 compradores entrevistados describieron miedo a retrasos de instalación; esto es una observación contextual, NO «el 60 % del mercado».

**Fundamento externo relacionado:** [S05], [S06], [S07], [S08], [S32]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D02 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D02 — CONOCIMIENTO DEL MERCADO, CLIENTES Y MARCA
    Objetivo de negocio: Separar lo que se sabe de compradores reales de lo que
    se presume sobre ellos y decidir qué promesas de marca están probadas.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Entrevistas situadas y transcripciones con consentimiento
- Preguntas repetidas de prospectos y razones de pérdida de propuestas
- Ventas/CRM con fecha y segmento
- Quejas, reseñas, servicio y postventa
- Elementos existentes de identidad visual/verbal

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Reconstruye al menos dos momentos de compra reales si hay fuentes; si faltan,
    distingue explícitamente conjetura y plan de investigación. No fabricar
    porcentajes ni citas de clientes.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Distinción explícita entre comprador, aprobador, pagador y usuario
2. Situaciones/Jobs to Be Done reconstruidos a partir de episodios concretos
3. Evidencia por segmento, tamaño y sesgo de la muestra; no extrapolación
4. Obstáculos, alternativas usadas, criterios de decisión y disparadores de
compra
5. Canales donde se observa contacto y mensajes comprobables
6. Posicionamiento: asociaciones deseadas versus percibidas; claims
autorizados/prohibidos
7. Vacíos de conocimiento, preguntas de descubrimiento y señal de actualización

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Hallazgos verificables y grado de certeza
2. 01 Actores y circunstancias de compra
3. 02 Segmentos observados e hipótesis
4. 03 Trabajos, fricciones y alternativas por episodio
5. 04 Evidencia de demanda y objeciones
6. 05 Posicionamiento, señales de marca y lenguaje
7. 06 Lo que NO sabemos y experimentos de contraste
8. 07 Fuentes, alcance y revisiones

    INSTRUCCIÓN DE PROCEDENCIA: Cada insight indica número y diversidad de
    episodios, fechas y dónde se observó; opinión del fundador se registra
    separada de voz del cliente.
    CONEXIONES A VERIFICAR: D01 selecciona segmentos; D03 recoge promesas
    publicables; X03 documenta relaciones específicas; X04 episodios de entrega y
    contraevidencia.
    CONTROL DE VIGENCIA: Disparadores: nueva investigación, cambios en
    objeciones/alternativas, pérdida de clientes, nueva evidencia de
    asociaciones, segmentos nuevos. Registrar discrepancias y no borrar casos.
    PRUEBA DE UTILIDAD A EJECUTAR: Un vendedor prepara una conversación para un
    comprador específico sin recurrir a una persona psicológica inventada.
    CONTRATO DE EXTRACCIÓN: ACTOR/SEGMENTO/JOB/OBSERVACIÓN/CLAIM/PROHIBICIÓN;
    cada generalización tiene alcance, muestra y fuente.

    Si D02 no necesita archivo autónomo según el criterio «Puede quedar integrado
    con D03 si solo hay una audiencia y dos o tres observaciones verificadas; no
    inventar buyer personas por ausencia de datos.», desarrolla la unidad como
    sección identificada dentro del documento de autoridad apropiado y explica
    por qué. Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=D02-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D02 — Prompt completo de actualización

```text
ACTUALIZA D02 — Conocimiento del mercado, clientes y marca conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D02.
    Especial atención a: Reconstruye al menos dos momentos de compra reales si
    hay fuentes; si faltan, distingue explícitamente conjetura y plan de
    investigación. No fabricar porcentajes ni citas de clientes.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: nueva investigación,
    cambios en objeciones/alternativas, pérdida de clientes, nueva evidencia de
    asociaciones, segmentos nuevos. Registrar discrepancias y no borrar casos.
    5. Verifica autoridad y destinos afectados: D01 selecciona segmentos; D03
    recoge promesas publicables; X03 documenta relaciones específicas; X04
    episodios de entrega y contraevidencia.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Un vendedor prepara una conversación
    para un comprador específico sin recurrir a una persona psicológica
    inventada.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## D03 — Portafolio y sistema comercial

**Naturaleza:** Familia principal.  
**Propósito:** Permitir vender correctamente sin confundir un servicio prestado, una herramienta usada, un producto propuesto o un acuerdo particular.  
**Preguntas que permite responder:** ¿Qué compró realmente el cliente?; ¿Qué incluye/excluye cada modalidad?; ¿Qué precio y vigencia se pueden cotizar?; ¿Qué pasos y facultades requiere una venta?.

**Cuándo debe existir:** Siempre que haya ventas o compromisos comerciales; si la empresa sólo tiene una oferta estable y pocos canales, puede vivir dentro de un dossier.

**Cuándo NO crear archivo independiente:** No separar comercial y ofertas si cambiar cualquiera no ocasiona revisiones en agendas/usuarios distintos; abrir X01 por autonomía real.

**Entradas y fuentes que deben buscarse:**

- Cotizaciones aprobadas/emitidas, condiciones generales, folletos
- Facturas/contratos y registros de aceptación
- Registros de leads, propuestas y pérdidas
- Listas de precios vigentes con fecha y responsable
- Políticas de descuentos y reembolsos

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Cómo construye la empresa un precio cuando el trabajo no coincide con una oferta estándar?
- ¿Qué componentes, costos, condiciones o exclusiones nunca deben omitirse al cotizar?
- ¿Cuándo conviene precio global, desglose, módulo, paquete o cotización personalizada?
- ¿Qué excepción comercial puede autorizar cada persona y cuál necesita otra aprobación?
- ¿Qué señales indican que una propuesta todavía no está lista para enviarse?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Mapa de líneas reales: vendidos, pilotos, productos en desarrollo, herramientas internas, discontinuados
2. Promesa y alcance por modalidad, exclusiones, condiciones y evidencia del cliente
3. Mecanismo comercial: origen, calificación, diagnóstico, oferta, aprobación, cierre y seguimiento
4. Definición de precio público/particular, moneda, impuestos, descuento, vigencia y aprobador
5. Pruebas de venta y separaciones: prestación, compra, entrega, uso de herramienta y cancelación
6. Reglas de mensajes, afirmaciones y claims autorizados por D02
7. Tratamiento de excepciones, devoluciones, garantía y transferencia a operación

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Qué se puede ofrecer hoy
2. 01 Mapa de modalidades y estado comercial
3. 02 Promesa, alcance y exclusiones por modalidad
4. 03 Precios y condiciones: autoridad y vigencia
5. 04 Recorrido comercial de oportunidad a acuerdo
6. 05 Materiales, claims y objeciones autorizadas
7. 06 Excepciones, descuentos y cambios
8. 07 Reglas de entrega comercial–operativa

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. No concluir venta por la presencia de una herramienta en una reunión. Una factura, orden aceptada o contrato sustentan el estado de contratación; cotización solo demuestra propuesta.

**Relaciones y autoridad:** D02 fundamenta necesidades y claims; D04 capacidad; D05 costos; X01 es autoridad de precio/alcance por oferta autónoma; X05 acuerdo particular prima sobre condiciones generales para su objeto.

**Actualización y conservación histórica:** Disparadores: cambio de precio, tarifa, impuesto, paquete, garantía, mensajes, flujo de aprobación o modalidad. Recalcular derivados de propuesta y catálogo; no alteraciones retroactivas de acuerdos.

**Prueba de utilidad empresarial:** Generar una propuesta realista con alcance, exclusiones, moneda, impuestos y vigencia, sin inventar contratación ni precios.

**Señales de extracción para agentes:** OFERTA, ESTADO_COMERCIAL, PRECIO, VIGENCIA, CONDICIÓN, FLUJO, CLAIM; distinguir sistema comercial de cada cotización.

**Ejemplo sintético (no fuente real):** SINTÉTICO: un cliente contrató consultoría y durante ella utilizó una herramienta de IA. El documento NO debe decir «compró la herramienta» sin acuerdo específico.

**Fundamento externo relacionado:** [S04], [S05], [S07], [S32]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D03 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D03 — PORTAFOLIO Y SISTEMA COMERCIAL
    Objetivo de negocio: Permitir vender correctamente sin confundir un servicio
    prestado, una herramienta usada, un producto propuesto o un acuerdo
    particular.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Cotizaciones aprobadas/emitidas, condiciones generales, folletos
- Facturas/contratos y registros de aceptación
- Registros de leads, propuestas y pérdidas
- Listas de precios vigentes con fecha y responsable
- Políticas de descuentos y reembolsos

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Para cada modalidad, clasifica explícitamente vendida, usada internamente,
    piloto, propuesta o retirada; busca prueba de compra distinta de prueba de
    utilización.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Mapa de líneas reales: vendidos, pilotos, productos en desarrollo,
    herramientas internas, discontinuados
2. Promesa y alcance por modalidad, exclusiones, condiciones y evidencia del
cliente
3. Mecanismo comercial: origen, calificación, diagnóstico, oferta,
aprobación, cierre y seguimiento
4. Definición de precio público/particular, moneda, impuestos, descuento,
vigencia y aprobador
5. Pruebas de venta y separaciones: prestación, compra, entrega, uso de
herramienta y cancelación
6. Reglas de mensajes, afirmaciones y claims autorizados por D02
7. Tratamiento de excepciones, devoluciones, garantía y transferencia a
operación

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Qué se puede ofrecer hoy
2. 01 Mapa de modalidades y estado comercial
3. 02 Promesa, alcance y exclusiones por modalidad
4. 03 Precios y condiciones: autoridad y vigencia
5. 04 Recorrido comercial de oportunidad a acuerdo
6. 05 Materiales, claims y objeciones autorizadas
7. 06 Excepciones, descuentos y cambios
8. 07 Reglas de entrega comercial–operativa

    INSTRUCCIÓN DE PROCEDENCIA: No concluir venta por la presencia de una
    herramienta en una reunión. Una factura, orden aceptada o contrato sustentan
    el estado de contratación; cotización solo demuestra propuesta.
    CONEXIONES A VERIFICAR: D02 fundamenta necesidades y claims; D04 capacidad;
    D05 costos; X01 es autoridad de precio/alcance por oferta autónoma; X05
    acuerdo particular prima sobre condiciones generales para su objeto.
    CONTROL DE VIGENCIA: Disparadores: cambio de precio, tarifa, impuesto,
    paquete, garantía, mensajes, flujo de aprobación o modalidad. Recalcular
    derivados de propuesta y catálogo; no alteraciones retroactivas de acuerdos.
    PRUEBA DE UTILIDAD A EJECUTAR: Generar una propuesta realista con alcance,
    exclusiones, moneda, impuestos y vigencia, sin inventar contratación ni
    precios.
    CONTRATO DE EXTRACCIÓN:
    OFERTA/ESTADO_COMERCIAL/PRECIO/VIGENCIA/CONDICIÓN/FLUJO/CLAIM; distinguir
    sistema comercial de cada cotización.

    Si D03 no necesita archivo autónomo según el criterio «No separar comercial y
    ofertas si cambiar cualquiera no ocasiona revisiones en agendas/usuarios
    distintos; abrir X01 por autonomía real.», desarrolla la unidad como sección
    identificada dentro del documento de autoridad apropiado y explica por qué.
    Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=D03-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D03 — Prompt completo de actualización

```text
ACTUALIZA D03 — Portafolio y sistema comercial conservando continuidad y
evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D03.
    Especial atención a: Para cada modalidad, clasifica explícitamente vendida,
    usada internamente, piloto, propuesta o retirada; busca prueba de compra
    distinta de prueba de utilización.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: cambio de precio, tarifa,
    impuesto, paquete, garantía, mensajes, flujo de aprobación o modalidad.
    Recalcular derivados de propuesta y catálogo; no alteraciones retroactivas de
    acuerdos.
    5. Verifica autoridad y destinos afectados: D02 fundamenta necesidades y
    claims; D04 capacidad; D05 costos; X01 es autoridad de precio/alcance por
    oferta autónoma; X05 acuerdo particular prima sobre condiciones generales
    para su objeto.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Generar una propuesta realista con
    alcance, exclusiones, moneda, impuestos y vigencia, sin inventar contratación
    ni precios.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## D04 — Ejecución, experiencia y calidad

**Naturaleza:** Familia principal.  
**Propósito:** Explicar cómo se transforma una promesa en una entrega repetible, cómo se decide ante variaciones y cómo se detecta una falla.  
**Preguntas que permite responder:** ¿Qué ocurre desde la aceptación hasta el cierre?; ¿Dónde se requiere juicio y dónde procedimiento?; ¿Qué controles evitan fallos?; ¿Cómo se entrega un proyecto distinto sin inventar un departamento?.

**Cuándo debe existir:** Siempre que se realice una entrega; puede ser sección breve o ampliarse a mapa de procesos y X02 por independencia.

**Cuándo NO crear archivo independiente:** No crear un SOP por cada actividad; si la tarea cambia siempre y depende de criterio experto, documentar decisiones y ejemplos más que pasos rígidos.

**Entradas y fuentes que deben buscarse:**

- Órdenes, libros de proyecto, checklists utilizados y evidencia de entrega
- Conversaciones de incidentes, rectificaciones, devoluciones
- Rutas reales de información y decisiones
- Observación de trabajo y entrevistas a ejecutores

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- Reconstruye un trabajo real difícil desde confirmación hasta cierre: ¿dónde hubo decisiones críticas?
- ¿Qué señal temprana permite anticipar que la entrega puede salir mal?
- ¿Qué parte puede seguir una checklist y qué parte exige juicio experto?
- ¿Qué error es costoso/difícil de corregir y qué control lo evita?
- ¿Qué significa «terminado» o «aceptado» para la empresa en la práctica?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Promesa de entrada, criterios de aceptación y handoff de ventas
2. Mapa de flujo real de entrega con disparadores, entradas, salidas y excepciones
3. Responsables por tarea y quién decide, sin cargos inventados
4. Puntos críticos de calidad y evidencias mínimas de terminación
5. Dependencias de personas, sistemas, materiales y proveedores
6. Escalamientos y variantes por tipo de oferta
7. Aprendizajes comprobados y cambios aprobados a la práctica

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Resultado prometido y criterio de entrega
2. 01 Entradas y transferencias
3. 02 Flujo de trabajo observado (no idealizado)
4. 03 Decisiones, excepciones y fallas
5. 04 Controles y evidencias de calidad
6. 05 Recursos y capacidad disponible
7. 06 Tratamiento de retrabajo, cierre y aprendizaje
8. 07 Procesos autónomos y registro de mejoras

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Separar procedimientos vigentes de práctica observada, y ambos de propuestas de mejora; toda excepción conserva episodio y fecha.

**Relaciones y autoridad:** D03 promesas; D06 facultades; D07 dependencias/seguridad; D05 costos operativos; X02 SOP/proceso si es recurrente; X04 casos de ejecución.

**Actualización y conservación histórica:** Disparadores: incidente, nueva variante de servicio, exigencia de calidad, sustitución de herramienta/proveedor, traspaso de tarea. Versionar cambios que alteran evidencia o facultades.

**Prueba de utilidad empresarial:** Una persona nueva puede ejecutar un caso habitual o sabe con precisión cuándo detenerse y preguntar, sin asumir conocimiento tácito invisible.

**Señales de extracción para agentes:** PROCESO, ETAPA, PUNTO_DECISIÓN, CONTROL, EXCEPCIÓN, EVIDENCIA_DE_ENTREGA; mapear SOP e historial por vínculo, no copiar casos.

**Ejemplo sintético (no fuente real):** SINTÉTICO: venta de mostrador modular exige medidas firmadas antes de fabricar; si faltan, el proceso se detiene, aunque la cotización esté aceptada.

**Fundamento externo relacionado:** [S03], [S09], [S10], [S11], [S12], [S20]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D04 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D04 — EJECUCIÓN, EXPERIENCIA Y CALIDAD
    Objetivo de negocio: Explicar cómo se transforma una promesa en una entrega
    repetible, cómo se decide ante variaciones y cómo se detecta una falla.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Órdenes, libros de proyecto, checklists utilizados y evidencia de entrega
- Conversaciones de incidentes, rectificaciones, devoluciones
- Rutas reales de información y decisiones
- Observación de trabajo y entrevistas a ejecutores

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Para un caso de entrega real, reconstruye etapas en orden, 2 puntos de fallo,
    1 criterio de aceptación y qué tarea requiere criterio humano.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Promesa de entrada, criterios de aceptación y handoff de ventas
2. Mapa de flujo real de entrega con disparadores, entradas, salidas y
excepciones
3. Responsables por tarea y quién decide, sin cargos inventados
4. Puntos críticos de calidad y evidencias mínimas de terminación
5. Dependencias de personas, sistemas, materiales y proveedores
6. Escalamientos y variantes por tipo de oferta
7. Aprendizajes comprobados y cambios aprobados a la práctica

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Resultado prometido y criterio de entrega
2. 01 Entradas y transferencias
3. 02 Flujo de trabajo observado (no idealizado)
4. 03 Decisiones, excepciones y fallas
5. 04 Controles y evidencias de calidad
6. 05 Recursos y capacidad disponible
7. 06 Tratamiento de retrabajo, cierre y aprendizaje
8. 07 Procesos autónomos y registro de mejoras

    INSTRUCCIÓN DE PROCEDENCIA: Separar procedimientos vigentes de práctica
    observada, y ambos de propuestas de mejora; toda excepción conserva episodio
    y fecha.
    CONEXIONES A VERIFICAR: D03 promesas; D06 facultades; D07
    dependencias/seguridad; D05 costos operativos; X02 SOP/proceso si es
    recurrente; X04 casos de ejecución.
    CONTROL DE VIGENCIA: Disparadores: incidente, nueva variante de servicio,
    exigencia de calidad, sustitución de herramienta/proveedor, traspaso de
    tarea. Versionar cambios que alteran evidencia o facultades.
    PRUEBA DE UTILIDAD A EJECUTAR: Una persona nueva puede ejecutar un caso
    habitual o sabe con precisión cuándo detenerse y preguntar, sin asumir
    conocimiento tácito invisible.
    CONTRATO DE EXTRACCIÓN:
    PROCESO/ETAPA/PUNTO_DECISIÓN/CONTROL/EXCEPCIÓN/EVIDENCIA_DE_ENTREGA; mapear
    SOP e historial por vínculo, no copiar casos.

    Si D04 no necesita archivo autónomo según el criterio «No crear un SOP por
    cada actividad; si la tarea cambia siempre y depende de criterio experto,
    documentar decisiones y ejemplos más que pasos rígidos.», desarrolla la
    unidad como sección identificada dentro del documento de autoridad apropiado
    y explica por qué. Si sí corresponde separar, crea Markdown completo con
    `doc_id`, `schema_version`, `revision`, `editorial_status`, `as_of`,
    `access`; comentarios estables `<!-- kb:id=D04-B001 -->` y referencias
    [F-0001] a fuentes reales. Los IDs no deben inventarse como procedencia: crea
    fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D04 — Prompt completo de actualización

```text
ACTUALIZA D04 — Ejecución, experiencia y calidad conservando continuidad y
evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D04.
    Especial atención a: Para un caso de entrega real, reconstruye etapas en
    orden, 2 puntos de fallo, 1 criterio de aceptación y qué tarea requiere
    criterio humano.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: incidente, nueva variante
    de servicio, exigencia de calidad, sustitución de herramienta/proveedor,
    traspaso de tarea. Versionar cambios que alteran evidencia o facultades.
    5. Verifica autoridad y destinos afectados: D03 promesas; D06 facultades; D07
    dependencias/seguridad; D05 costos operativos; X02 SOP/proceso si es
    recurrente; X04 casos de ejecución.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Una persona nueva puede ejecutar un caso
    habitual o sabe con precisión cuándo detenerse y preguntar, sin asumir
    conocimiento tácito invisible.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## D05 — Economía, caja y criterios financieros

**Naturaleza:** Familia principal.  
**Propósito:** Aportar una base verificable para decidir precios, gastos, cobros, inversión y sostenibilidad; no duplicar contabilidad ni ERP.  
**Preguntas que permite responder:** ¿De dónde entra el dinero y cuándo se cobra?; ¿Qué cuesta realmente cada modalidad?; ¿Qué compromisos pueden poner en riesgo la caja?; ¿Qué números son reales y cuáles escenarios?.

**Cuándo debe existir:** Debe cubrirse siempre: al menos mecánica de ingresos, principales costos, compromisos y regla de caja.

**Cuándo NO crear archivo independiente:** Puede ser sección breve mientras no existan varias unidades económicas, financiamiento o múltiples responsables; estados financieros permanecen en sistema fuente.

**Entradas y fuentes que deben buscarse:**

- Estados contables o exportaciones y conciliaciones
- Facturas/cuentas por cobrar y pagar
- Presupuestos, proyecciones y fórmulas con versión
- Comprobantes de costos directos y tablas vigentes
- Condiciones de cobro y contratos

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Cómo estima el experto si un trabajo vale la pena antes de tener todos los costos cerrados?
- ¿Qué costos o consumos suele olvidar una persona que no conoce bien el negocio?
- ¿Cuándo un proyecto grande puede ser peor negocio que uno pequeño?
- ¿Qué criterio usa para anticipos, descuentos, crédito, compras o gastos extraordinarios?
- ¿Qué cifra o señal mira primero al tomar una decisión económica y qué limitaciones reconoce?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Mecánicas de ingreso: precio pactado, facturado, devengado y cobrado por separado
2. Costos variables/directos, fijos/compartidos y criterios de reparto declarados
3. Unidad económica por línea o trabajo: numerador, denominador, periodo, fuentes y excepciones
4. Caja: saldo de referencia, entradas/salidas esperadas, vencimientos y escenarios
5. Políticas de anticipo, crédito, descuento y autorización económica
6. Metas y umbrales con fórmulas, moneda, impuestos y responsable
7. Sensibilidades y alertas; conciliación entre narración y sistema contable

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Lectura financiera con fecha y unidad monetaria
2. 01 Modelo de ingresos y reconocimiento
3. 02 Estructura de costos y drivers
4. 03 Economía por oferta/proyecto
5. 04 Cobros, pagos y caja
6. 05 Presupuestos, escenarios y supuestos
7. 06 Criterios y facultades para decisiones de dinero
8. 07 Discrepancias, fuentes y cierres

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Para cada cifra sustantiva: fuente de sistema, corte, moneda, tratamiento de impuestos aplicables, método, exactitud y si es observado o escenario. No convertir cobrado en facturado ni presupuestado en real.

**Relaciones y autoridad:** D03 determina precio ofrecido/condición comercial; X01 precio por modalidad si autónoma; D04 driver operativo; X05 deuda/compromiso; D01 priorización; D06 facultades.

**Actualización y conservación histórica:** Disparadores: cierre mensual, cambio de costo, inversión, cambio de regla contable, retraso de cobro, desvío material. Recalcular dependencias; no sobrescribir supuestos de escenarios cerrados.

**Prueba de utilidad empresarial:** Antes de dar un descuento de 15 %, evaluar efecto en margen y caja, distinguiendo datos reales, fórmula y supuestos incompletos.

**Señales de extracción para agentes:** MÉTRICA, CIFRA, PERIODO, MONEDA, UNIDAD, FÓRMULA, FUENTE, ESCENARIO; conservar IDs de exportación y corte de datos.

**Ejemplo sintético (no fuente real):** SINTÉTICO: cotización 120,000 MXN + IVA; anticipo 40 % y costo material 58,000 MXN. No afirmar rentabilidad sin mano de obra, impuestos, indirectos y momento de salida.

**Fundamento externo relacionado:** [S02], [S13], [S14], [S15], [S32]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D05 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D05 — ECONOMÍA, CAJA Y CRITERIOS FINANCIEROS
    Objetivo de negocio: Aportar una base verificable para decidir precios,
    gastos, cobros, inversión y sostenibilidad; no duplicar contabilidad ni ERP.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Estados contables o exportaciones y conciliaciones
- Facturas/cuentas por cobrar y pagar
- Presupuestos, proyecciones y fórmulas con versión
- Comprobantes de costos directos y tablas vigentes
- Condiciones de cobro y contratos

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Usa tablas con unidades, fórmula explícita y fuente; separa movimiento de
    efectivo, resultado y proyección. Si el dato no existe, enseña exactamente
    qué decisión queda bloqueada.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Mecánicas de ingreso: precio pactado, facturado, devengado y cobrado por
    separado
2. Costos variables/directos, fijos/compartidos y criterios de reparto
declarados
3. Unidad económica por línea o trabajo: numerador, denominador, periodo,
fuentes y excepciones
4. Caja: saldo de referencia, entradas/salidas esperadas, vencimientos y
escenarios
5. Políticas de anticipo, crédito, descuento y autorización económica
6. Metas y umbrales con fórmulas, moneda, impuestos y responsable
7. Sensibilidades y alertas; conciliación entre narración y sistema contable

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Lectura financiera con fecha y unidad monetaria
2. 01 Modelo de ingresos y reconocimiento
3. 02 Estructura de costos y drivers
4. 03 Economía por oferta/proyecto
5. 04 Cobros, pagos y caja
6. 05 Presupuestos, escenarios y supuestos
7. 06 Criterios y facultades para decisiones de dinero
8. 07 Discrepancias, fuentes y cierres

    INSTRUCCIÓN DE PROCEDENCIA: Para cada cifra sustantiva: fuente de sistema,
    corte, moneda, tratamiento de impuestos aplicables, método, exactitud y si es
    observado o escenario. No convertir cobrado en facturado ni presupuestado en
    real.
    CONEXIONES A VERIFICAR: D03 determina precio ofrecido/condición comercial;
    X01 precio por modalidad si autónoma; D04 driver operativo; X05
    deuda/compromiso; D01 priorización; D06 facultades.
    CONTROL DE VIGENCIA: Disparadores: cierre mensual, cambio de costo,
    inversión, cambio de regla contable, retraso de cobro, desvío material.
    Recalcular dependencias; no sobrescribir supuestos de escenarios cerrados.
    PRUEBA DE UTILIDAD A EJECUTAR: Antes de dar un descuento de 15 %, evaluar
    efecto en margen y caja, distinguiendo datos reales, fórmula y supuestos
    incompletos.
    CONTRATO DE EXTRACCIÓN:
    MÉTRICA/CIFRA/PERIODO/MONEDA/UNIDAD/FÓRMULA/FUENTE/ESCENARIO; conservar IDs
    de exportación y corte de datos.

    Si D05 no necesita archivo autónomo según el criterio «Puede ser sección
    breve mientras no existan varias unidades económicas, financiamiento o
    múltiples responsables; estados financieros permanecen en sistema fuente.»,
    desarrolla la unidad como sección identificada dentro del documento de
    autoridad apropiado y explica por qué. Si sí corresponde separar, crea
    Markdown completo con `doc_id`, `schema_version`, `revision`,
    `editorial_status`, `as_of`, `access`; comentarios estables `<!--
    kb:id=D05-B001 -->` y referencias [F-0001] a fuentes reales. Los IDs no deben
    inventarse como procedencia: crea fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D05 — Prompt completo de actualización

```text
ACTUALIZA D05 — Economía, caja y criterios financieros conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D05.
    Especial atención a: Usa tablas con unidades, fórmula explícita y fuente;
    separa movimiento de efectivo, resultado y proyección. Si el dato no existe,
    enseña exactamente qué decisión queda bloqueada.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: cierre mensual, cambio de
    costo, inversión, cambio de regla contable, retraso de cobro, desvío
    material. Recalcular dependencias; no sobrescribir supuestos de escenarios
    cerrados.
    5. Verifica autoridad y destinos afectados: D03 determina precio
    ofrecido/condición comercial; X01 precio por modalidad si autónoma; D04
    driver operativo; X05 deuda/compromiso; D01 priorización; D06 facultades.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Antes de dar un descuento de 15 %,
    evaluar efecto en margen y caja, distinguiendo datos reales, fórmula y
    supuestos incompletos.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## D06 — Personas reales, responsabilidades y facultades

**Naturaleza:** Familia principal.  
**Propósito:** Hacer explícito quién sabe, hace, decide, sustituye y capacita, aunque una sola persona concentre varias funciones.  
**Preguntas que permite responder:** ¿Quién puede comprometer a la empresa?; ¿Qué funciones dependen del fundador?; ¿Quién cubre una ausencia?; ¿Qué saber no está escrito y cómo se transfiere?.

**Cuándo debe existir:** Siempre que haya al menos un operador y decisiones; puede ser una sección reducida de roles reales para una empresa unipersonal.

**Cuándo NO crear archivo independiente:** No necesita organigrama/archivo separado si hay una sola persona y pocas responsabilidades; nunca inventar CFO, departamento o junta.

**Entradas y fuentes que deben buscarse:**

- Asignaciones efectivas en proyectos y autorizaciones
- Entrevistas a ejecutores y fundador
- Listados internos de colaboradores externos
- Casos de cuellos de botella/decisiones demoradas
- Acuerdos de funciones y cobertura

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- Si el fundador/dueño falta varios días, ¿qué puede seguir y qué se detiene realmente?
- ¿Qué decisiones sólo puede tomar hoy una persona específica y por qué?
- ¿Qué tarea podría delegarse si se explicitara mejor el criterio experto?
- ¿Qué conocimiento crítico vive en la cabeza de una persona y cómo se reconoce que alguien ya lo aprendió?
- ¿Qué diferencia existe entre ejecutar una tarea y tener facultad para comprometer a la empresa?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Personas/capacidades existentes y funciones realmente ejecutadas
2. Matriz simple de decisiones: asunto, quién decide, quién prepara, quién actúa y límites
3. Compromisos que requieren aprobación y delegaciones vigentes
4. Dependencias de conocimiento tácito, acceso y capacidad
5. Sustituciones realistas y límites de continuidad
6. Transferencia de aprendizaje y onboarding basado en tareas
7. Brechas y proyectos de mejora sin presentar cargos propuestos como reales

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Cómo se organiza el trabajo
2. 01 Funciones observadas, no departamentos
3. 02 Quién decide qué y bajo qué límites
4. 03 Ejecución, autorizaciones y delegación
5. 04 Conocimientos críticos en personas
6. 05 Sustituciones, accesos y continuidad
7. 06 Onboarding y transferencia
8. 07 Cambios de responsabilidades e incertidumbres

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Asignación de responsabilidad debe estar sustentada por autorización o corroboración; distinguir «lo hizo una vez» de «es responsable de».

**Relaciones y autoridad:** D01 facultad estratégica; D03 descuentos/firma comercial; D04 operación; D05 gasto; D07 accesos; X02 procedimiento; X07 decisiones delegadas.

**Actualización y conservación histórica:** Disparadores: ingreso/salida de persona, cambio de aprobación, ausencia, delegación, incidente de continuidad. No preservar datos privados innecesarios.

**Prueba de utilidad empresarial:** Simular ausencia del fundador durante tres días: otra persona sabe qué decisiones puede tomar, qué no y dónde encontrar el procedimiento.

**Señales de extracción para agentes:** PERSONA_ROL, FUNCIÓN, FACULTAD, DELEGACIÓN, COBERTURA, CONOCIMIENTO_TÁCITO; no inferir jerarquía por títulos.

**Ejemplo sintético (no fuente real):** SINTÉTICO: Luisa recibe pedidos, calcula costos y coordina entregas. Eso NO demuestra que sea gerente de ventas, directora financiera y directora de operaciones.

**Fundamento externo relacionado:** [S16], [S17], [S20], [S33]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D06 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D06 — PERSONAS REALES, RESPONSABILIDADES Y FACULTADES
    Objetivo de negocio: Hacer explícito quién sabe, hace, decide, sustituye y
    capacita, aunque una sola persona concentre varias funciones.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Asignaciones efectivas en proyectos y autorizaciones
- Entrevistas a ejecutores y fundador
- Listados internos de colaboradores externos
- Casos de cuellos de botella/decisiones demoradas
- Acuerdos de funciones y cobertura

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Usa nombres de funciones y autoridad real; si una persona lleva ventas,
    finanzas y producción, refléjalo sin crear tres departamentos.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Personas/capacidades existentes y funciones realmente ejecutadas
2. Matriz simple de decisiones: asunto, quién decide, quién prepara, quién
actúa y límites
3. Compromisos que requieren aprobación y delegaciones vigentes
4. Dependencias de conocimiento tácito, acceso y capacidad
5. Sustituciones realistas y límites de continuidad
6. Transferencia de aprendizaje y onboarding basado en tareas
7. Brechas y proyectos de mejora sin presentar cargos propuestos como reales

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Cómo se organiza el trabajo
2. 01 Funciones observadas, no departamentos
3. 02 Quién decide qué y bajo qué límites
4. 03 Ejecución, autorizaciones y delegación
5. 04 Conocimientos críticos en personas
6. 05 Sustituciones, accesos y continuidad
7. 06 Onboarding y transferencia
8. 07 Cambios de responsabilidades e incertidumbres

    INSTRUCCIÓN DE PROCEDENCIA: Asignación de responsabilidad debe estar
    sustentada por autorización o corroboración; distinguir «lo hizo una vez» de
    «es responsable de».
    CONEXIONES A VERIFICAR: D01 facultad estratégica; D03 descuentos/firma
    comercial; D04 operación; D05 gasto; D07 accesos; X02 procedimiento; X07
    decisiones delegadas.
    CONTROL DE VIGENCIA: Disparadores: ingreso/salida de persona, cambio de
    aprobación, ausencia, delegación, incidente de continuidad. No preservar
    datos privados innecesarios.
    PRUEBA DE UTILIDAD A EJECUTAR: Simular ausencia del fundador durante tres
    días: otra persona sabe qué decisiones puede tomar, qué no y dónde encontrar
    el procedimiento.
    CONTRATO DE EXTRACCIÓN:
    PERSONA_ROL/FUNCIÓN/FACULTAD/DELEGACIÓN/COBERTURA/CONOCIMIENTO_TÁCITO; no
    inferir jerarquía por títulos.

    Si D06 no necesita archivo autónomo según el criterio «No necesita
    organigrama/archivo separado si hay una sola persona y pocas
    responsabilidades; nunca inventar CFO, departamento o junta.», desarrolla la
    unidad como sección identificada dentro del documento de autoridad apropiado
    y explica por qué. Si sí corresponde separar, crea Markdown completo con
    `doc_id`, `schema_version`, `revision`, `editorial_status`, `as_of`,
    `access`; comentarios estables `<!-- kb:id=D06-B001 -->` y referencias
    [F-0001] a fuentes reales. Los IDs no deben inventarse como procedencia: crea
    fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D06 — Prompt completo de actualización

```text
ACTUALIZA D06 — Personas reales, responsabilidades y facultades conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D06.
    Especial atención a: Usa nombres de funciones y autoridad real; si una
    persona lleva ventas, finanzas y producción, refléjalo sin crear tres
    departamentos.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: ingreso/salida de
    persona, cambio de aprobación, ausencia, delegación, incidente de
    continuidad. No preservar datos privados innecesarios.
    5. Verifica autoridad y destinos afectados: D01 facultad estratégica; D03
    descuentos/firma comercial; D04 operación; D05 gasto; D07 accesos; X02
    procedimiento; X07 decisiones delegadas.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Simular ausencia del fundador durante
    tres días: otra persona sabe qué decisiones puede tomar, qué no y dónde
    encontrar el procedimiento.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## D07 — Riesgos, compromisos y dependencias críticas

**Naturaleza:** Familia principal.  
**Propósito:** Hacer visibles las condiciones que pueden impedir operar, cobrar, proteger datos o cumplir obligaciones; conectar prevención con recuperación.  
**Preguntas que permite responder:** ¿Qué acuerdo nos obliga?; ¿Qué falla podría detener la operación?; ¿Qué permisos, datos o dependencias necesitan revisión profesional?; ¿Qué hacemos al fallar proveedor o sistema?.

**Cuándo debe existir:** Siempre debe existir cobertura mínima de riesgos materiales y continuidad; profundidad proporcional a la exposición.

**Cuándo NO crear archivo independiente:** Puede integrarse como sección si sólo existen pocas dependencias controladas; no elaborar evaluación legal/regulatoria ficticia.

**Entradas y fuentes que deben buscarse:**

- Contratos firmados, permisos, pólizas, licencias
- Inventarios y lista de sistemas/proveedores
- Registros de incidentes, accesos y respaldos
- Políticas de privacidad reales o informes especializados
- Historial de incumplimientos y pagos comprometidos

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué problema real ha causado más daño, retrabajo, pérdida de dinero o riesgo reputacional?
- ¿Qué dependencia dejaría a la empresa sin poder entregar si falla mañana?
- ¿Qué riesgo acepta deliberadamente y cuál nunca aceptaría?
- ¿Qué control o respaldo se da por supuesto pero no se ha probado de extremo a extremo?
- ¿Qué compromisos, permisos o revisiones requieren fuente contractual/profesional en vez de criterio interno?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Obligaciones materiales y fuente jurídica/documental sin sustituir contrato
2. Riesgo: evento, causa, impacto sobre cliente/caja/continuidad, probabilidad argumentada o «sin estimar»
3. Controles existentes versus propuestos, señales de alerta y responsable
4. Proveedores/sistemas/recursos cuya pérdida interrumpe oferta
5. Datos sensibles, clasificación, acceso, conservación y límites
6. Continuidad: medida de contingencia, recuperación, fuente y prueba
7. Permisos/licencias y dudas que requieren validación de especialista por jurisdicción

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Exposiciones y compromisos que importan hoy
2. 01 Obligaciones acreditadas y vencimientos
3. 02 Riesgos priorizados por consecuencias
4. 03 Controles reales y brechas
5. 04 Recursos, proveedores y sistemas críticos
6. 05 Datos, accesos y restricciones
7. 06 Continuidad, recuperación y responsables
8. 07 Verificaciones legales/financieras pendientes

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. «Existe obligación» requiere localizar contrato/norma aplicable; opinión no es dictamen. Marcar jurisdicción, vigencia, objeto y fuente. No almacenar claves secretas.

**Relaciones y autoridad:** X05 autoridad por acuerdo; X06 dependencia con historia; D05 compromisos de caja; D04 mitigación operativa; D06 permisos/decisores.

**Actualización y conservación histórica:** Disparadores: firma/vencimiento de acuerdo, incidente, pérdida de proveedor, cambio normativo verificado, cambio de permisos, modificación de accesos. Registrar control probado y periodicidad.

**Prueba de utilidad empresarial:** Ante interrupción del proveedor principal, se puede identificar las entregas afectadas, opción de sustitución y quién autoriza, sin inventar respaldo.

**Señales de extracción para agentes:** OBLIGACIÓN, RIESGO, CONTROL, RECURSO, RESTRICCIÓN, VENCIMIENTO, JURISDICCIÓN; prohibido inferir legalidad por ausencia de alerta.

**Ejemplo sintético (no fuente real):** SINTÉTICO: único archivo de diseño vive en cuenta personal sin respaldo probado; riesgo de interrupción del montaje. La contingencia «usar copia» sólo puede declararse si hay copia verificada.

**Fundamento externo relacionado:** [S18], [S19], [S25], [S14]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-D07 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO D07 — RIESGOS, COMPROMISOS Y DEPENDENCIAS CRÍTICAS
    Objetivo de negocio: Hacer visibles las condiciones que pueden impedir
    operar, cobrar, proteger datos o cumplir obligaciones; conectar prevención
    con recuperación.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Contratos firmados, permisos, pólizas, licencias
- Inventarios y lista de sistemas/proveedores
- Registros de incidentes, accesos y respaldos
- Políticas de privacidad reales o informes especializados
- Historial de incumplimientos y pagos comprometidos

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Prioriza por consecuencia y capacidad de respuesta, no por una matriz de
    puntuaciones inventadas. Marca qué cuestiones exigen revisión jurídica,
    contable o de seguridad.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Obligaciones materiales y fuente jurídica/documental sin sustituir
    contrato
2. Riesgo: evento, causa, impacto sobre cliente/caja/continuidad,
probabilidad argumentada o «sin estimar»
3. Controles existentes versus propuestos, señales de alerta y responsable
4. Proveedores/sistemas/recursos cuya pérdida interrumpe oferta
5. Datos sensibles, clasificación, acceso, conservación y límites
6. Continuidad: medida de contingencia, recuperación, fuente y prueba
7. Permisos/licencias y dudas que requieren validación de especialista por
jurisdicción

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Exposiciones y compromisos que importan hoy
2. 01 Obligaciones acreditadas y vencimientos
3. 02 Riesgos priorizados por consecuencias
4. 03 Controles reales y brechas
5. 04 Recursos, proveedores y sistemas críticos
6. 05 Datos, accesos y restricciones
7. 06 Continuidad, recuperación y responsables
8. 07 Verificaciones legales/financieras pendientes

    INSTRUCCIÓN DE PROCEDENCIA: «Existe obligación» requiere localizar
    contrato/norma aplicable; opinión no es dictamen. Marcar jurisdicción,
    vigencia, objeto y fuente. No almacenar claves secretas.
    CONEXIONES A VERIFICAR: X05 autoridad por acuerdo; X06 dependencia con
    historia; D05 compromisos de caja; D04 mitigación operativa; D06
    permisos/decisores.
    CONTROL DE VIGENCIA: Disparadores: firma/vencimiento de acuerdo, incidente,
    pérdida de proveedor, cambio normativo verificado, cambio de permisos,
    modificación de accesos. Registrar control probado y periodicidad.
    PRUEBA DE UTILIDAD A EJECUTAR: Ante interrupción del proveedor principal, se
    puede identificar las entregas afectadas, opción de sustitución y quién
    autoriza, sin inventar respaldo.
    CONTRATO DE EXTRACCIÓN:
    OBLIGACIÓN/RIESGO/CONTROL/RECURSO/RESTRICCIÓN/VENCIMIENTO/JURISDICCIÓN;
    prohibido inferir legalidad por ausencia de alerta.

    Si D07 no necesita archivo autónomo según el criterio «Puede integrarse como
    sección si sólo existen pocas dependencias controladas; no elaborar
    evaluación legal/regulatoria ficticia.», desarrolla la unidad como sección
    identificada dentro del documento de autoridad apropiado y explica por qué.
    Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=D07-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-D07 — Prompt completo de actualización

```text
ACTUALIZA D07 — Riesgos, compromisos y dependencias críticas conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE D07.
    Especial atención a: Prioriza por consecuencia y capacidad de respuesta, no
    por una matriz de puntuaciones inventadas. Marca qué cuestiones exigen
    revisión jurídica, contable o de seguridad.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Disparadores: firma/vencimiento de
    acuerdo, incidente, pérdida de proveedor, cambio normativo verificado, cambio
    de permisos, modificación de accesos. Registrar control probado y
    periodicidad.
    5. Verifica autoridad y destinos afectados: X05 autoridad por acuerdo; X06
    dependencia con historia; D05 compromisos de caja; D04 mitigación operativa;
    D06 permisos/decisores.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Ante interrupción del proveedor
    principal, se puede identificar las entregas afectadas, opción de sustitución
    y quién autoriza, sin inventar respaldo.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X01 — Ficha viva de oferta individual

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Asegurar identidad, alcance y versión de una oferta que necesita condiciones propias; autoridad comercial de esa oferta.  
**Preguntas que permite responder:** ¿Qué se contrata exactamente?; ¿Qué edición se puede vender?; ¿Qué varía según modalidad/segmento?; ¿Cómo se entrega y cobra?.

**Cuándo debe existir:** Crear cuando la oferta tiene precio/alcance/versiones distintas, ventas recurrentes, responsable o aprobación separados.

**Cuándo NO crear archivo independiente:** Si sólo hay un servicio estable con un único precio y la ficha repetirá D03, dejar como subsección con ID semántico.

**Entradas y fuentes que deben buscarse:**

- Ficha/contrato oficial de oferta
- Propuestas aceptadas y excepciones
- Catálogo de precios vigente
- Procedimiento de entrega y costos unitarios

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué debe poder entender el comprador sin conversación adicional para contratar esta oferta?
- ¿Qué parte del alcance cambia más y cuál nunca debe quedar implícita?
- ¿Cómo se construye o autoriza el precio de esta oferta y qué excepciones existen?
- ¿Qué condición hace que la oferta no sea adecuada para un cliente/caso?
- ¿Qué criterio de aceptación/soporte/garantía es realmente aplicable?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Identidad: nombre, tipo producto/servicio/paquete, variantes y estado
2. Problema/circunstancia de uso y destinatario validado
3. Entregables, cantidades, especificaciones, exclusiones, responsabilidades del cliente
4. Reglas de precio, impuestos, moneda, fechas y aprobador
5. Condiciones de aceptación, cambios, garantías o soporte comprobado
6. Capacidad, requisitos, riesgos y dependencia operativa
7. Versiones: vigencia, sustituciones y comunicación a derivados

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Ficha de compra verificable
2. 01 Cliente/problema y resultado prometido
3. 02 Alcance y entregables medibles
4. 03 Variantes y exclusiones
5. 04 Precio, condiciones y fechas
6. 05 Admisión, ejecución y aceptación
7. 06 Riesgos, garantías, responsables
8. 07 Versiones y referencias

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Citar tarifa aprobada, cotización/contrato y política; no extrapolar un precio particular como precio general.

**Relaciones y autoridad:** D03 cataloga y enlaza; D04/X02 entregan; D05 costes; X05 acuerdo particular puede prevalecer solo para su ámbito.

**Actualización y conservación histórica:** Cambio de alcance, precio, especificación, capacidad, garantía: nueva revisión; conservar oferta anterior y acuerdos activos como históricos.

**Prueba de utilidad empresarial:** Preparar cotización sin aclaraciones inventadas de precio, exclusiones ni condiciones.

**Señales de extracción para agentes:** OFERTA_ID + versión + vigencia + reglas de precio; derivados afectados: propuestas, web y procedimientos.

**Ejemplo sintético (no fuente real):** SINTÉTICO: OFR-014 v2 incluye fabricación y entrega local, NO instalación. La instalación es add-on separado, no implícito.

**Fundamento externo relacionado:** [S04], [S05], [S07]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X01 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X01 — FICHA VIVA DE OFERTA INDIVIDUAL
    Objetivo de negocio: Asegurar identidad, alcance y versión de una oferta que
    necesita condiciones propias; autoridad comercial de esa oferta.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Ficha/contrato oficial de oferta
- Propuestas aceptadas y excepciones
- Catálogo de precios vigente
- Procedimiento de entrega y costos unitarios

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Escribe requisitos concretos de compra y aceptación; diferencia paquete,
    licencia, uso interno, piloto y trabajo contratado.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Identidad: nombre, tipo producto/servicio/paquete, variantes y estado
2. Problema/circunstancia de uso y destinatario validado
3. Entregables, cantidades, especificaciones, exclusiones, responsabilidades
del cliente
4. Reglas de precio, impuestos, moneda, fechas y aprobador
5. Condiciones de aceptación, cambios, garantías o soporte comprobado
6. Capacidad, requisitos, riesgos y dependencia operativa
7. Versiones: vigencia, sustituciones y comunicación a derivados

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Ficha de compra verificable
2. 01 Cliente/problema y resultado prometido
3. 02 Alcance y entregables medibles
4. 03 Variantes y exclusiones
5. 04 Precio, condiciones y fechas
6. 05 Admisión, ejecución y aceptación
7. 06 Riesgos, garantías, responsables
8. 07 Versiones y referencias

    INSTRUCCIÓN DE PROCEDENCIA: Citar tarifa aprobada, cotización/contrato y
    política; no extrapolar un precio particular como precio general.
    CONEXIONES A VERIFICAR: D03 cataloga y enlaza; D04/X02 entregan; D05 costes;
    X05 acuerdo particular puede prevalecer solo para su ámbito.
    CONTROL DE VIGENCIA: Cambio de alcance, precio, especificación, capacidad,
    garantía: nueva revisión; conservar oferta anterior y acuerdos activos como
    históricos.
    PRUEBA DE UTILIDAD A EJECUTAR: Preparar cotización sin aclaraciones
    inventadas de precio, exclusiones ni condiciones.
    CONTRATO DE EXTRACCIÓN: OFERTA_ID + versión + vigencia + reglas de precio;
    derivados afectados: propuestas, web y procedimientos.

    Si X01 no necesita archivo autónomo según el criterio «Si sólo hay un
    servicio estable con un único precio y la ficha repetirá D03, dejar como
    subsección con ID semántico.», desarrolla la unidad como sección identificada
    dentro del documento de autoridad apropiado y explica por qué. Si sí
    corresponde separar, crea Markdown completo con `doc_id`, `schema_version`,
    `revision`, `editorial_status`, `as_of`, `access`; comentarios estables `<!--
    kb:id=X01-B001 -->` y referencias [F-0001] a fuentes reales. Los IDs no deben
    inventarse como procedencia: crea fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X01 — Prompt completo de actualización

```text
ACTUALIZA X01 — Ficha viva de oferta individual conservando continuidad y
evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X01.
    Especial atención a: Escribe requisitos concretos de compra y aceptación;
    diferencia paquete, licencia, uso interno, piloto y trabajo contratado.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Cambio de alcance, precio,
    especificación, capacidad, garantía: nueva revisión; conservar oferta
    anterior y acuerdos activos como históricos.
    5. Verifica autoridad y destinos afectados: D03 cataloga y enlaza; D04/X02
    entregan; D05 costes; X05 acuerdo particular puede prevalecer solo para su
    ámbito.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Preparar cotización sin aclaraciones
    inventadas de precio, exclusiones ni condiciones.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X02 — Proceso o instrucción de trabajo autónoma

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Permitir repetición o transferencia segura de una operación que tiene decisiones y controles propios.  
**Preguntas que permite responder:** ¿Cuándo empieza y termina?; ¿Quién ejecuta/aprueba?; ¿Qué excepciones bloquean?; ¿Qué evidencia prueba la terminación?.

**Cuándo debe existir:** Crear ante recurrencia, criticidad/riesgo, delegación, cambios de versión o distintos ejecutores.

**Cuándo NO crear archivo independiente:** Si es un paso trivial, raro o puramente creativo y no requiere gobierno independiente, mantener como bloque en D04.

**Entradas y fuentes que deben buscarse:**

- Observación de una ejecución real
- Checklist y evidencia de recepción/entrega
- Casos de fallo
- Decisor/operadores actuales

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- Pide al ejecutor que reconstruya una ejecución real y señale decisiones que no están en la checklist.
- ¿Qué señal obliga a detener el proceso?
- ¿Qué excepción requiere criterio y quién puede autorizarla?
- ¿Qué evidencia demuestra que el proceso terminó correctamente?
- ¿Qué error típico comete un novato siguiendo sólo pasos literales?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Disparador y condición de aplicabilidad
2. Entradas, versiones, permisos y precondiciones
3. Pasos observados y decisiones; distinguir procedimiento obligatorio de recomendación
4. Roles reales, límites de aprobación y escalamiento
5. Resultados/evidencia, criterio de aceptación, almacenamiento de registros
6. Excepciones, contingencias y señales de detenerse
7. Última prueba y cambio contra versión anterior

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Para qué sirve y cuándo aplica
2. 01 Disparador, entradas y precondiciones
3. 02 Flujo principal numerado
4. 03 Puntos de decisión y excepciones
5. 04 Responsabilidades y autorizaciones
6. 05 Comprobaciones de calidad
7. 06 Salida, evidencia y escalamiento
8. 07 Pruebas, incidencias y versión

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Una entrevista sola no demuestra que un SOP sea práctica vigente; pedir corroboración en una ejecución o aprobación.

**Relaciones y autoridad:** D04 mapa macro; D06 autorizaciones; D07 riesgos; X04 evidencia de prueba; X01 reglas de alcance.

**Actualización y conservación histórica:** Tras incidente, modificación de herramienta, revisión de calidad o traspaso; ensayo controlado antes de aprobar cambios críticos.

**Prueba de utilidad empresarial:** Ejecutor distinto al autor sigue pasos sobre caso ficticio e identifica control que impide un error.

**Señales de extracción para agentes:** PROCESO_ID, EVENTO, PASO, PUNTO_DECISIÓN, CONTROL, ROL, EVIDENCIA; preservar versiones, no reescribir episodios.

**Ejemplo sintético (no fuente real):** SINTÉTICO: si cliente no confirma medidas, etapa 3 no permite comprar materiales; excepción requiere autorización escrita.

**Fundamento externo relacionado:** [S09], [S11], [S12], [S33]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X02 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X02 — PROCESO O INSTRUCCIÓN DE TRABAJO AUTÓNOMA
    Objetivo de negocio: Permitir repetición o transferencia segura de una
    operación que tiene decisiones y controles propios.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Observación de una ejecución real
- Checklist y evidencia de recepción/entrega
- Casos de fallo
- Decisor/operadores actuales

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Provee paso a paso cuando la tarea es determinística; para excepciones o
    trabajo de juicio ofrece criterios y un ejemplo decidido.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Disparador y condición de aplicabilidad
2. Entradas, versiones, permisos y precondiciones
3. Pasos observados y decisiones; distinguir procedimiento obligatorio de
recomendación
4. Roles reales, límites de aprobación y escalamiento
5. Resultados/evidencia, criterio de aceptación, almacenamiento de registros
6. Excepciones, contingencias y señales de detenerse
7. Última prueba y cambio contra versión anterior

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Para qué sirve y cuándo aplica
2. 01 Disparador, entradas y precondiciones
3. 02 Flujo principal numerado
4. 03 Puntos de decisión y excepciones
5. 04 Responsabilidades y autorizaciones
6. 05 Comprobaciones de calidad
7. 06 Salida, evidencia y escalamiento
8. 07 Pruebas, incidencias y versión

    INSTRUCCIÓN DE PROCEDENCIA: Una entrevista sola no demuestra que un SOP sea
    práctica vigente; pedir corroboración en una ejecución o aprobación.
    CONEXIONES A VERIFICAR: D04 mapa macro; D06 autorizaciones; D07 riesgos; X04
    evidencia de prueba; X01 reglas de alcance.
    CONTROL DE VIGENCIA: Tras incidente, modificación de herramienta, revisión de
    calidad o traspaso; ensayo controlado antes de aprobar cambios críticos.
    PRUEBA DE UTILIDAD A EJECUTAR: Ejecutor distinto al autor sigue pasos sobre
    caso ficticio e identifica control que impide un error.
    CONTRATO DE EXTRACCIÓN:
    PROCESO_ID/EVENTO/PASO/PUNTO_DECISIÓN/CONTROL/ROL/EVIDENCIA; preservar
    versiones, no reescribir episodios.

    Si X02 no necesita archivo autónomo según el criterio «Si es un paso trivial,
    raro o puramente creativo y no requiere gobierno independiente, mantener como
    bloque en D04.», desarrolla la unidad como sección identificada dentro del
    documento de autoridad apropiado y explica por qué. Si sí corresponde
    separar, crea Markdown completo con `doc_id`, `schema_version`, `revision`,
    `editorial_status`, `as_of`, `access`; comentarios estables `<!--
    kb:id=X02-B001 -->` y referencias [F-0001] a fuentes reales. Los IDs no deben
    inventarse como procedencia: crea fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X02 — Prompt completo de actualización

```text
ACTUALIZA X02 — Proceso o instrucción de trabajo autónoma conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X02.
    Especial atención a: Provee paso a paso cuando la tarea es determinística;
    para excepciones o trabajo de juicio ofrece criterios y un ejemplo decidido.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Tras incidente, modificación de
    herramienta, revisión de calidad o traspaso; ensayo controlado antes de
    aprobar cambios críticos.
    5. Verifica autoridad y destinos afectados: D04 mapa macro; D06
    autorizaciones; D07 riesgos; X04 evidencia de prueba; X01 reglas de alcance.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Ejecutor distinto al autor sigue pasos
    sobre caso ficticio e identifica control que impide un error.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X03 — Ficha de relación con una cuenta o cliente

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Recuperar contexto y compromisos de una relación comercial sin confundir hechos del cliente con segmento de mercado.  
**Preguntas que permite responder:** ¿Quién es el interlocutor autorizado?; ¿Qué se ha ofrecido/contratado?; ¿Qué preferencias están documentadas?; ¿Qué restricción de privacidad aplica?.

**Cuándo debe existir:** Crear sólo si la cuenta acumula interacciones/compromisos que necesitan continuidad fuera del CRM ordinario y existe base legal/autorización.

**Cuándo NO crear archivo independiente:** No crear por cada contacto; si el CRM fiable ya es registro de autoridad y basta una URL segura, conservar referencia al CRM.

**Entradas y fuentes que deben buscarse:**

- CRM, correos autorizados, acuerdos y minutas
- Solicitudes directas y retroalimentación del cliente
- Propuestas con estado y fechas

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué papel real tiene cada interlocutor (usuario, comprador, pagador, aprobador)?
- ¿Qué necesidades fueron expresadas por el cliente y cuáles son interpretación interna?
- ¿Qué promesas o excepciones específicas siguen vigentes para esta cuenta?
- ¿Qué información no debe generalizarse al mercado?
- ¿Qué restricción de acceso/retención/privacidad cambia cómo se conserva la relación?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Identidad empresarial mínima y pseudónimo si corresponde
2. Roles: comprador, pagador, aprobador, usuario, contacto y fuente
3. Cronología de interacciones materiales y condiciones vigentes
4. Necesidades expresadas en contexto, NO diagnósticos psicológicos
5. Estado de oportunidades confirmado, eventos de venta y referencias contractuales
6. Restricciones de privacidad y retención
7. Próximas decisiones y tareas con responsable y fecha

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Relación y restricciones de acceso
2. 01 Actores y autorizaciones
3. 02 Objetivos expresados por el cliente
4. 03 Interacciones relevantes y evidencia
5. 04 Ofertas, acuerdos y estado comercial
6. 05 Preferencias observadas y límites
7. 06 Pendientes, riesgos y próximo contacto
8. 07 Historia, fuente maestra y cierre

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Cada cita/preferencia se asocia a mensaje y fecha; utilización de herramienta no equivale a compra y un prospecto no equivale a cliente contratado.

**Relaciones y autoridad:** D02 usa hallazgos agregados solo con cuidado; D03 estado comercial; X05 compromisos; X04 proyectos; D07 privacidad.

**Actualización y conservación histórica:** Nueva comunicación, cambio de interlocutor, aceptación/cancelación, solicitud de borrado. Minimizar datos y cumplir permisos.

**Prueba de utilidad empresarial:** Retomar una conversación comercial sin confundir promesas realizadas a otro cliente o datos históricos.

**Señales de extracción para agentes:** CUENTA_ID, ROL_INTERLOCUTOR, INTERACCIÓN, OPORTUNIDAD, ESTADO, RESTRICCIÓN; datos sensibles por etiqueta de acceso.

**Ejemplo sintético (no fuente real):** SINTÉTICO: cliente utilizó un prototipo en consultoría pagada: registra uso en proyecto, no adquisición de licencia.

**Fundamento externo relacionado:** [S06], [S07], [S19]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X03 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X03 — FICHA DE RELACIÓN CON UNA CUENTA O CLIENTE
    Objetivo de negocio: Recuperar contexto y compromisos de una relación
    comercial sin confundir hechos del cliente con segmento de mercado.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - CRM, correos autorizados, acuerdos y minutas
- Solicitudes directas y retroalimentación del cliente
- Propuestas con estado y fechas

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Distingue usuario, quien compra y quien autoriza. No sintetices atributos
    generalizables de un único interlocutor.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Identidad empresarial mínima y pseudónimo si corresponde
2. Roles: comprador, pagador, aprobador, usuario, contacto y fuente
3. Cronología de interacciones materiales y condiciones vigentes
4. Necesidades expresadas en contexto, NO diagnósticos psicológicos
5. Estado de oportunidades confirmado, eventos de venta y referencias
contractuales
6. Restricciones de privacidad y retención
7. Próximas decisiones y tareas con responsable y fecha

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Relación y restricciones de acceso
2. 01 Actores y autorizaciones
3. 02 Objetivos expresados por el cliente
4. 03 Interacciones relevantes y evidencia
5. 04 Ofertas, acuerdos y estado comercial
6. 05 Preferencias observadas y límites
7. 06 Pendientes, riesgos y próximo contacto
8. 07 Historia, fuente maestra y cierre

    INSTRUCCIÓN DE PROCEDENCIA: Cada cita/preferencia se asocia a mensaje y
    fecha; utilización de herramienta no equivale a compra y un prospecto no
    equivale a cliente contratado.
    CONEXIONES A VERIFICAR: D02 usa hallazgos agregados solo con cuidado; D03
    estado comercial; X05 compromisos; X04 proyectos; D07 privacidad.
    CONTROL DE VIGENCIA: Nueva comunicación, cambio de interlocutor,
    aceptación/cancelación, solicitud de borrado. Minimizar datos y cumplir
    permisos.
    PRUEBA DE UTILIDAD A EJECUTAR: Retomar una conversación comercial sin
    confundir promesas realizadas a otro cliente o datos históricos.
    CONTRATO DE EXTRACCIÓN:
    CUENTA_ID/ROL_INTERLOCUTOR/INTERACCIÓN/OPORTUNIDAD/ESTADO/RESTRICCIÓN; datos
    sensibles por etiqueta de acceso.

    Si X03 no necesita archivo autónomo según el criterio «No crear por cada
    contacto; si el CRM fiable ya es registro de autoridad y basta una URL
    segura, conservar referencia al CRM.», desarrolla la unidad como sección
    identificada dentro del documento de autoridad apropiado y explica por qué.
    Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=X03-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X03 — Prompt completo de actualización

```text
ACTUALIZA X03 — Ficha de relación con una cuenta o cliente conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X03.
    Especial atención a: Distingue usuario, quien compra y quien autoriza. No
    sintetices atributos generalizables de un único interlocutor.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Nueva comunicación, cambio de
    interlocutor, aceptación/cancelación, solicitud de borrado. Minimizar datos y
    cumplir permisos.
    5. Verifica autoridad y destinos afectados: D02 usa hallazgos agregados solo
    con cuidado; D03 estado comercial; X05 compromisos; X04 proyectos; D07
    privacidad.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Retomar una conversación comercial sin
    confundir promesas realizadas a otro cliente o datos históricos.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X04 — Expediente de proyecto, caso o episodio

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Conservar cronología, contexto, ejecución y aprendizaje específico sin convertirlo automáticamente en política general.  
**Preguntas que permite responder:** ¿Qué se solicitó y cambió?; ¿Qué se hizo y cuándo?; ¿Qué se aceptó o rechazó?; ¿Qué lección tiene alcance limitado?.

**Cuándo debe existir:** Crear cuando una ejecución por cliente/proyecto tiene identidad, fuentes, costes, cambios, privacidad o decisiones propias.

**Cuándo NO crear archivo independiente:** No crear expedientes por cada llamada trivial; un evento simple puede anotarse en CRM/caso existente.

**Entradas y fuentes que deben buscarse:**

- Brief y requerimiento de origen
- Cambios y aprobaciones
- Propuesta/contrato y entregables
- Mensajes de ejecución, costos y cierre
- Observaciones y evidencias del resultado

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué cambió materialmente durante el caso y por qué?
- ¿Qué decisiones/excepciones fueron exclusivas del caso?
- ¿Qué problema detectó el experto y qué señal lo hizo visible?
- ¿Qué resultado observado permite aprender y qué interpretación todavía es hipótesis?
- ¿Qué, si algo, debería promoverse a conocimiento común mediante una decisión separada?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Situación inicial y actores, jurisdicción/permisos pertinentes
2. Línea temporal: fecha, evento, fuente, cambio, efecto
3. Solicitado, propuesto, aceptado, entregado, facturado y cobrado, diferenciados
4. Decisiones y excepciones acotadas al caso
5. Evidencia del resultado, incidencias, limitaciones y cuentas sensibles
6. Lecciones: hecho observado, interpretación, alcance y acción propuesta
7. Referencias a fuentes y derivados; política afectada solo por aprobación separada

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Ficha y confidencialidad del caso
2. 01 Solicitud inicial y alcance
3. 02 Línea temporal de hitos/fuentes
4. 03 Propuesta, acuerdo y cambios
5. 04 Ejecución y evidencias
6. 05 Entrega, cobro y cierre — por separado
7. 06 Problemas, causas e hipótesis
8. 07 Lecciones, alcance y acciones recomendadas
9. 08 Historial y referencias

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Fuentes por hito; no resumir desde memoria si la versión inicial contradice mensaje original; citar revisión comercial y documental.

**Relaciones y autoridad:** D03 condiciones; X01 oferta; X05 acuerdo; D04/X02 aprendizaje propuesto; D05 costos históricos; X07 decisión de institucionalizar.

**Actualización y conservación histórica:** Nuevo cambio, aceptación, factura, devolución, disputa, cierre o reanudación; append-only para eventos, corregir con fe de erratas y rastro.

**Prueba de utilidad empresarial:** Reconstruir «qué se acordó realmente en la fecha X» a partir de fuente original, no del resumen del agente.

**Señales de extracción para agentes:** CASO_ID, EVENTO, FECHA, ALCANCE, ESTADO_COMERCIAL, ESTADO_ENTREGA, ESTADO_COBRO, LECCIÓN; cronología no comprimible.

**Ejemplo sintético (no fuente real):** SINTÉTICO: 03/03 cotización emitida; 05/03 alcance aceptado; 20/03 entrega; 28/03 saldo pagado. No llamar «cobrado» al 05/03.

**Fundamento externo relacionado:** [S09], [S21], [S23], [S24]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X04 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X04 — EXPEDIENTE DE PROYECTO, CASO O EPISODIO
    Objetivo de negocio: Conservar cronología, contexto, ejecución y aprendizaje
    específico sin convertirlo automáticamente en política general.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Brief y requerimiento de origen
- Cambios y aprobaciones
- Propuesta/contrato y entregables
- Mensajes de ejecución, costos y cierre
- Observaciones y evidencias del resultado

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Reconstruye cronología factual con separado «uso», «contratación», «entrega»,
    «facturación» y «pago». Cita qué evidencia soporta cada transición.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Situación inicial y actores, jurisdicción/permisos pertinentes
2. Línea temporal: fecha, evento, fuente, cambio, efecto
3. Solicitado, propuesto, aceptado, entregado, facturado y cobrado,
diferenciados
4. Decisiones y excepciones acotadas al caso
5. Evidencia del resultado, incidencias, limitaciones y cuentas sensibles
6. Lecciones: hecho observado, interpretación, alcance y acción propuesta
7. Referencias a fuentes y derivados; política afectada solo por aprobación
separada

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Ficha y confidencialidad del caso
2. 01 Solicitud inicial y alcance
3. 02 Línea temporal de hitos/fuentes
4. 03 Propuesta, acuerdo y cambios
5. 04 Ejecución y evidencias
6. 05 Entrega, cobro y cierre — por separado
7. 06 Problemas, causas e hipótesis
8. 07 Lecciones, alcance y acciones recomendadas
9. 08 Historial y referencias

    INSTRUCCIÓN DE PROCEDENCIA: Fuentes por hito; no resumir desde memoria si la
    versión inicial contradice mensaje original; citar revisión comercial y
    documental.
    CONEXIONES A VERIFICAR: D03 condiciones; X01 oferta; X05 acuerdo; D04/X02
    aprendizaje propuesto; D05 costos históricos; X07 decisión de
    institucionalizar.
    CONTROL DE VIGENCIA: Nuevo cambio, aceptación, factura, devolución, disputa,
    cierre o reanudación; append-only para eventos, corregir con fe de erratas y
    rastro.
    PRUEBA DE UTILIDAD A EJECUTAR: Reconstruir «qué se acordó realmente en la
    fecha X» a partir de fuente original, no del resumen del agente.
    CONTRATO DE EXTRACCIÓN:
    CASO_ID/EVENTO/FECHA/ALCANCE/ESTADO_COMERCIAL/ESTADO_ENTREGA/ESTADO_COBRO/LECCIÓN;
    cronología no comprimible.

    Si X04 no necesita archivo autónomo según el criterio «No crear expedientes
    por cada llamada trivial; un evento simple puede anotarse en CRM/caso
    existente.», desarrolla la unidad como sección identificada dentro del
    documento de autoridad apropiado y explica por qué. Si sí corresponde
    separar, crea Markdown completo con `doc_id`, `schema_version`, `revision`,
    `editorial_status`, `as_of`, `access`; comentarios estables `<!--
    kb:id=X04-B001 -->` y referencias [F-0001] a fuentes reales. Los IDs no deben
    inventarse como procedencia: crea fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X04 — Prompt completo de actualización

```text
ACTUALIZA X04 — Expediente de proyecto, caso o episodio conservando
continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X04.
    Especial atención a: Reconstruye cronología factual con separado «uso»,
    «contratación», «entrega», «facturación» y «pago». Cita qué evidencia soporta
    cada transición.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Nuevo cambio, aceptación, factura,
    devolución, disputa, cierre o reanudación; append-only para eventos, corregir
    con fe de erratas y rastro.
    5. Verifica autoridad y destinos afectados: D03 condiciones; X01 oferta; X05
    acuerdo; D04/X02 aprendizaje propuesto; D05 costos históricos; X07 decisión
    de institucionalizar.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Reconstruir «qué se acordó realmente en
    la fecha X» a partir de fuente original, no del resumen del agente.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X05 — Acuerdo u obligación autónoma

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Representar obligaciones materiales con texto de autoridad y fechas sin sustituir el documento legal firmado.  
**Preguntas que permite responder:** ¿Quién debe qué a quién?; ¿Desde cuándo y hasta cuándo?; ¿Qué condición modifica/termina?; ¿Qué falta verificar profesionalmente?.

**Cuándo debe existir:** Crear si hay obligación con plazo, contraparte, sensibilidad, renovación, efecto en caja o múltiples documentos derivados.

**Cuándo NO crear archivo independiente:** Obligaciones menores y rutinarias se referencian en D07 o sistema contractual; no duplicar íntegramente contratos sensibles.

**Entradas y fuentes que deben buscarse:**

- Contrato/orden/acta firmada, anexos y modificatorios
- Evidencia de aceptación y comunicaciones formales
- Facturas/pagos/entregas con identificador
- Interpretación de especialista cuando disponible

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué obligaciones son operativamente más importantes y qué fuente exacta las acredita?
- ¿Qué interpretación depende de asesoría profesional y no debe resolver la IA?
- ¿Qué fechas/condiciones cambian el estado de cumplimiento?
- ¿Qué modificación o excepción existe respecto del acuerdo general?
- ¿Qué otros documentos/procesos/caja se ven afectados por este acuerdo?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Partes y objeto, jurisdicción y fuente de autoridad
2. Obligaciones, restricciones, contraprestaciones y fechas
3. Condiciones precedentes, aprobaciones, hitos y remedios contemplados
4. Modificaciones, renovaciones, terminaciones y controversias
5. Estado de cumplimiento basado en evidencias (no deducido)
6. Riesgos y datos restringidos; lectura jurídica por confirmar
7. Enlaces a proyectos, cifras y responsables afectados

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Naturaleza, acceso y fuente contractual
2. 01 Partes y objeto exacto
3. 02 Obligaciones y derechos relevantes
4. 03 Fechas, condiciones y vencimientos
5. 04 Variaciones y documentos relacionados
6. 05 Cumplimiento y evidencias
7. 06 Riesgos, controversias y revisión profesional
8. 07 Histórico de estados y restricciones

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. La interpretación contractual es auxiliar y no reemplaza lectura del texto completo por persona autorizada; cita cláusula o referencia, sin inventarla.

**Relaciones y autoridad:** D07 panorama de obligaciones; D05 flujo de caja; D03/X01 condiciones comerciales; X03 cuenta; X04 ejecución.

**Actualización y conservación histórica:** Firma, modificación, aceptación formal, vencimiento, pago, incumplimiento; conservar documento firmado inmutable y addendas separadas.

**Prueba de utilidad empresarial:** Responder qué vence el próximo mes y qué fuente lo acredita sin inventar derecho u obligación.

**Señales de extracción para agentes:** ACUERDO_ID, PARTE, OBLIGACIÓN, VENCIMIENTO, CONDICIÓN, RESTRICCIÓN, FUENTE; versionado de acuerdos, adendas.

**Ejemplo sintético (no fuente real):** SINTÉTICO: pedido de 80 módulos con anticipo condicionado a aprobación de plano; no deducir que el anticipo es exigible antes de esa condición.

**Fundamento externo relacionado:** [S18], [S13], [S19]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X05 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X05 — ACUERDO U OBLIGACIÓN AUTÓNOMA
    Objetivo de negocio: Representar obligaciones materiales con texto de
    autoridad y fechas sin sustituir el documento legal firmado.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Contrato/orden/acta firmada, anexos y modificatorios
- Evidencia de aceptación y comunicaciones formales
- Facturas/pagos/entregas con identificador
- Interpretación de especialista cuando disponible

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Marca toda cláusula no leída como no verificada; preserva límites de
    autorización y exige revisión jurídica cuando haya interpretación
    conflictiva.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Partes y objeto, jurisdicción y fuente de autoridad
2. Obligaciones, restricciones, contraprestaciones y fechas
3. Condiciones precedentes, aprobaciones, hitos y remedios contemplados
4. Modificaciones, renovaciones, terminaciones y controversias
5. Estado de cumplimiento basado en evidencias (no deducido)
6. Riesgos y datos restringidos; lectura jurídica por confirmar
7. Enlaces a proyectos, cifras y responsables afectados

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Naturaleza, acceso y fuente contractual
2. 01 Partes y objeto exacto
3. 02 Obligaciones y derechos relevantes
4. 03 Fechas, condiciones y vencimientos
5. 04 Variaciones y documentos relacionados
6. 05 Cumplimiento y evidencias
7. 06 Riesgos, controversias y revisión profesional
8. 07 Histórico de estados y restricciones

    INSTRUCCIÓN DE PROCEDENCIA: La interpretación contractual es auxiliar y no
    reemplaza lectura del texto completo por persona autorizada; cita cláusula o
    referencia, sin inventarla.
    CONEXIONES A VERIFICAR: D07 panorama de obligaciones; D05 flujo de caja;
    D03/X01 condiciones comerciales; X03 cuenta; X04 ejecución.
    CONTROL DE VIGENCIA: Firma, modificación, aceptación formal, vencimiento,
    pago, incumplimiento; conservar documento firmado inmutable y addendas
    separadas.
    PRUEBA DE UTILIDAD A EJECUTAR: Responder qué vence el próximo mes y qué
    fuente lo acredita sin inventar derecho u obligación.
    CONTRATO DE EXTRACCIÓN:
    ACUERDO_ID/PARTE/OBLIGACIÓN/VENCIMIENTO/CONDICIÓN/RESTRICCIÓN/FUENTE;
    versionado de acuerdos/adendas.

    Si X05 no necesita archivo autónomo según el criterio «Obligaciones menores y
    rutinarias se referencian en D07 o sistema contractual; no duplicar
    íntegramente contratos sensibles.», desarrolla la unidad como sección
    identificada dentro del documento de autoridad apropiado y explica por qué.
    Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=X05-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X05 — Prompt completo de actualización

```text
ACTUALIZA X05 — Acuerdo u obligación autónoma conservando continuidad y
evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X05.
    Especial atención a: Marca toda cláusula no leída como no verificada;
    preserva límites de autorización y exige revisión jurídica cuando haya
    interpretación conflictiva.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Firma, modificación, aceptación formal,
    vencimiento, pago, incumplimiento; conservar documento firmado inmutable y
    addendas separadas.
    5. Verifica autoridad y destinos afectados: D07 panorama de obligaciones; D05
    flujo de caja; D03/X01 condiciones comerciales; X03 cuenta; X04 ejecución.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Responder qué vence el próximo mes y qué
    fuente lo acredita sin inventar derecho u obligación.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X06 — Recurso, sistema o proveedor crítico

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Asegurar continuidad y comprensión de una dependencia real, sin intentar reproducir inventario o contraseñas.  
**Preguntas que permite responder:** ¿Qué capacidad soporta?; ¿Quién tiene acceso o contrato?; ¿Qué falla afecta la entrega?; ¿Cómo se reemplaza/recupera?.

**Cuándo debe existir:** Crear por dependencia crítica con dueño, sustitución, permisos o historial de incidentes; no por cada artículo del almacén.

**Cuándo NO crear archivo independiente:** Si basta referencia a inventario/ERP/contrato y la dependencia no es material, dejar un enlace controlado en D07.

**Entradas y fuentes que deben buscarse:**

- Contrato/suscripción con proveedor
- Inventario o registro técnico de autoridad
- Política de acceso y respaldo
- Incidentes, pruebas de restauración y responsables

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué capacidad empresarial se pierde si el recurso/sistema/proveedor falla?
- ¿Cuál es la fuente maestra del estado actual y qué no debe duplicarse?
- ¿Quién puede administrar/cambiar/sustituir este recurso?
- ¿Qué límite de capacidad o dependencia suele descubrirse demasiado tarde?
- ¿La recuperación/sustitución está probada o sólo declarada?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Identidad y función empresarial del recurso
2. Sistema de registro: dónde se consulta estado actual
3. Propietario/administrador operativo y permisos sin secretos
4. Dependencias de procesos/ofertas/servicios
5. Límites de capacidad, reemplazo y continuidad
6. Vencimiento, condiciones, ubicación de evidencia y coste cuando material
7. Historial de incidentes, cambios y pruebas de recuperación

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Recurso y criticidad explicada
2. 01 Función y capacidades que habilita
3. 02 Fuente oficial y estado consultable
4. 03 Dependencias y personas autorizadas
5. 04 Límites, costes y vencimientos
6. 05 Sustitución, respaldo y recuperación
7. 06 Incidentes y verificación de continuidad
8. 07 Versiones y referencias

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. No afirmar «hay respaldo» hasta verificar evidencia de restauración, no copiar contraseñas, tokens ni datos sensibles.

**Relaciones y autoridad:** D07 riesgos; D04 y X02 procesos dependientes; D05 gastos; D06 custodios; X05 contratos de suministro.

**Actualización y conservación histórica:** Incidente, sustitución, nuevo control de acceso, cambio de inventario o contrato; actualizar sistema maestro y sólo enlazar su último corte.

**Prueba de utilidad empresarial:** Simular pérdida del sistema/proveedor por 48 horas e identificar impacto, decisión y fuente de restablecimiento.

**Señales de extracción para agentes:** RECURSO_ID, DEPENDENCIA, RESPONSABLE, REGISTRO_MAESTRO, CONTINGENCIA, RESTRICCIÓN; no duplicar inventario.

**Ejemplo sintético (no fuente real):** SINTÉTICO: catálogo de 4,000 productos vive en ERP; ficha crítica sólo referencia el ERP y la integración que bloquea ventas, sin duplicar el catálogo.

**Fundamento externo relacionado:** [S03], [S19], [S33]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X06 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X06 — RECURSO, SISTEMA O PROVEEDOR CRÍTICO
    Objetivo de negocio: Asegurar continuidad y comprensión de una dependencia
    real, sin intentar reproducir inventario o contraseñas.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Contrato/suscripción con proveedor
- Inventario o registro técnico de autoridad
- Política de acceso y respaldo
- Incidentes, pruebas de restauración y responsables

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Identifica la fuente operativa maestra por cada stock/estado y documenta solo
    las dependencias, no copias estáticas de miles de SKUs.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Identidad y función empresarial del recurso
2. Sistema de registro: dónde se consulta estado actual
3. Propietario/administrador operativo y permisos sin secretos
4. Dependencias de procesos/ofertas/servicios
5. Límites de capacidad, reemplazo y continuidad
6. Vencimiento, condiciones, ubicación de evidencia y coste cuando material
7. Historial de incidentes, cambios y pruebas de recuperación

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Recurso y criticidad explicada
2. 01 Función y capacidades que habilita
3. 02 Fuente oficial y estado consultable
4. 03 Dependencias y personas autorizadas
5. 04 Límites, costes y vencimientos
6. 05 Sustitución, respaldo y recuperación
7. 06 Incidentes y verificación de continuidad
8. 07 Versiones y referencias

    INSTRUCCIÓN DE PROCEDENCIA: No afirmar «hay respaldo» hasta verificar
    evidencia de restauración, no copiar contraseñas, tokens ni datos sensibles.
    CONEXIONES A VERIFICAR: D07 riesgos; D04 y X02 procesos dependientes; D05
    gastos; D06 custodios; X05 contratos de suministro.
    CONTROL DE VIGENCIA: Incidente, sustitución, nuevo control de acceso, cambio
    de inventario o contrato; actualizar sistema maestro y sólo enlazar su último
    corte.
    PRUEBA DE UTILIDAD A EJECUTAR: Simular pérdida del sistema/proveedor por 48
    horas e identificar impacto, decisión y fuente de restablecimiento.
    CONTRATO DE EXTRACCIÓN:
    RECURSO_ID/DEPENDENCIA/RESPONSABLE/REGISTRO_MAESTRO/CONTINGENCIA/RESTRICCIÓN;
    no duplicar inventario.

    Si X06 no necesita archivo autónomo según el criterio «Si basta referencia a
    inventario/ERP/contrato y la dependencia no es material, dejar un enlace
    controlado en D07.», desarrolla la unidad como sección identificada dentro
    del documento de autoridad apropiado y explica por qué. Si sí corresponde
    separar, crea Markdown completo con `doc_id`, `schema_version`, `revision`,
    `editorial_status`, `as_of`, `access`; comentarios estables `<!--
    kb:id=X06-B001 -->` y referencias [F-0001] a fuentes reales. Los IDs no deben
    inventarse como procedencia: crea fuentes solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X06 — Prompt completo de actualización

```text
ACTUALIZA X06 — Recurso, sistema o proveedor crítico conservando continuidad
y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X06.
    Especial atención a: Identifica la fuente operativa maestra por cada
    stock/estado y documenta solo las dependencias, no copias estáticas de miles
    de SKUs.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Incidente, sustitución, nuevo control
    de acceso, cambio de inventario o contrato; actualizar sistema maestro y sólo
    enlazar su último corte.
    5. Verifica autoridad y destinos afectados: D07 riesgos; D04 y X02 procesos
    dependientes; D05 gastos; D06 custodios; X05 contratos de suministro.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Simular pérdida del sistema/proveedor
    por 48 horas e identificar impacto, decisión y fuente de restablecimiento.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## X07 — Decisión, experimento o lección con identidad propia

**Naturaleza:** Documento especializado condicional.  
**Propósito:** Preservar razonamiento, evidencia, alternativas y consecuencias de una elección/experimento importante sin confundir aprendizaje con política vigente.  
**Preguntas que permite responder:** ¿Qué se decidió o probó realmente?; ¿Qué alternativas había?; ¿Qué evidencias apoyaron la decisión?; ¿Qué cambiará si los resultados contradicen la hipótesis?.

**Cuándo debe existir:** Crear si el cambio tiene efectos cruzados, controversia, importancia, hipótesis comprobable o historia que deba mantenerse.

**Cuándo NO crear archivo independiente:** No crear ficha por cada microdecisión; registrar decisión menor como entrada fechada en la sección competente de D01/D03/D04.

**Entradas y fuentes que deben buscarse:**

- Acta o aprobación de persona autorizada
- Propuestas/rechazos y criterios
- Experimentos y métricas antes/después
- Casos, fallos, observaciones y fuentes de resultados

**Conocimiento experto a elicitar cuando no esté suficientemente explícito en las fuentes:**

- ¿Qué decisión/hipótesis exacta se está preservando y qué alternativas se consideraron?
- ¿Qué señal/evidencia hizo cambiar de opinión o elegir una opción?
- ¿Qué resultado falsaría la hipótesis o obligaría a revisar la decisión?
- ¿Qué parte es aprendizaje contextual y qué parte podría convertirse en política?
- ¿Qué derivados deben revisarse si cambia esta decisión?

**Criterio de suficiencia para pasar G2/G6:** las respuestas deben producir criterios, señales, trade-offs, excepciones o mecanismos propios del negocio; no basta confirmar nombres, fechas o cantidades.

**Contenido obligatorio desarrollado (no campos vacíos):**

1. Pregunta/decisión precisa, alternativas y supuestos
2. Quién tiene facultad, quién decidió, fecha, alcance y vigencia
3. Evidencia disponible, contradicciones y límites
4. Regla de éxito/fracaso del experimento, medición y fecha de revisión
5. Resultado observado versus interpretación y transferencia posible
6. Contenido que se promueve a política sólo tras aprobación explícita
7. Efectos en documentos y comunicación a usuarios

**Estructura exacta de la clase (encabezados y orden):**

1. 00 Tipo: decisión / experimento / lección
2. 01 Situación y pregunta a resolver
3. 02 Opciones y supuestos
4. 03 Evidencia y contraevidencia
5. 04 Autoridad, decisión o hipótesis
6. 05 Prueba, resultado y alcance de aprendizaje
7. 06 Derivados afectados y acciones
8. 07 Vigencia, revisión e histórico

**Estados de conocimiento y edición:** se aplican por afirmación los cuatro ejes del contrato y el estado de evidencia. Una lección de un caso no gobierna todos los casos; hipótesis no se convierte en decisión por haber sido redactada.

**Relaciones y autoridad:** D01 prioridades, D03 reglas comerciales, D04 procesos, D05 finanzas, X04 caso fuente; el cambio requiere revisión explícita de autoridades.

**Actualización y conservación histórica:** Nuevos resultados, reversión, ampliación de alcance o conflicto: mantener decisión histórica, marcar superseded y crear nueva versión.

**Prueba de utilidad empresarial:** Al recibir un caso contradictorio, localizar la decisión anterior, su evidencia original y si procede revisar o no la regla vigente.

**Señales de extracción para agentes:** DECISIÓN_ID, HIPÓTESIS, ALTERNATIVA, TEST, RESULTADO, EFECTO, DERIVADO, APROBADOR; herencia temporal explícita.

**Ejemplo sintético (no fuente real):** SINTÉTICO: un cliente prefirió entrega en sábado. Eso demuestra una preferencia en un caso, no «todos prefieren sábado».

**Fundamento externo relacionado:** [S01], [S21], [S22], [S23], [S24]. La estructura final es una decisión metodológica propia, no una plantilla publicada por dichas fuentes.

### DES-X07 — Prompt completo de desarrollo

```text
DESARROLLA DOCUMENTO X07 — DECISIÓN, EXPERIMENTO O LECCIÓN CON IDENTIDAD PROPIA
    Objetivo de negocio: Preservar razonamiento, evidencia, alternativas y
    consecuencias de una elección/experimento importante sin confundir
    aprendizaje con política vigente.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    FUENTES A BUSCAR Y RELEER PRIORITARIAMENTE:
    - Acta o aprobación de persona autorizada
- Propuestas/rechazos y criterios
- Experimentos y métricas antes/después
- Casos, fallos, observaciones y fuentes de resultados

    TRABAJO SEMÁNTICO PARTICULAR (NO RECICLES LA PLANTILLA DE OTRA CLASE):
    Diferencia la pregunta/decisión, experimento y aprendizaje; no afirmes
    causalidad si solo tienes correlación o una anécdota.

    DEBES RESOLVER COMO CONTENIDO EMPRESARIAL (NO COMO ENCABEZADOS VACÍOS):
    1. Pregunta/decisión precisa, alternativas y supuestos
2. Quién tiene facultad, quién decidió, fecha, alcance y vigencia
3. Evidencia disponible, contradicciones y límites
4. Regla de éxito/fracaso del experimento, medición y fecha de revisión
5. Resultado observado versus interpretación y transferencia posible
6. Contenido que se promueve a política sólo tras aprobación explícita
7. Efectos en documentos y comunicación a usuarios

    ESTRUCTURA EXACTA DE LAS SECCIONES PARA ESTA CLASE; adapta profundidad, no su
    significado:
    1. 00 Tipo: decisión / experimento / lección
2. 01 Situación y pregunta a resolver
3. 02 Opciones y supuestos
4. 03 Evidencia y contraevidencia
5. 04 Autoridad, decisión o hipótesis
6. 05 Prueba, resultado y alcance de aprendizaje
7. 06 Derivados afectados y acciones
8. 07 Vigencia, revisión e histórico

    INSTRUCCIÓN DE PROCEDENCIA: Una lección de un caso no gobierna todos los
    casos; hipótesis no se convierte en decisión por haber sido redactada.
    CONEXIONES A VERIFICAR: D01 prioridades, D03 reglas comerciales, D04
    procesos, D05 finanzas, X04 caso fuente; el cambio requiere revisión
    explícita de autoridades.
    CONTROL DE VIGENCIA: Nuevos resultados, reversión, ampliación de alcance o
    conflicto: mantener decisión histórica, marcar superseded y crear nueva
    versión.
    PRUEBA DE UTILIDAD A EJECUTAR: Al recibir un caso contradictorio, localizar
    la decisión anterior, su evidencia original y si procede revisar o no la
    regla vigente.
    CONTRATO DE EXTRACCIÓN:
    DECISIÓN_ID/HIPÓTESIS/ALTERNATIVA/TEST/RESULTADO/EFECTO/DERIVADO/APROBADOR;
    herencia temporal explícita.

    Si X07 no necesita archivo autónomo según el criterio «No crear ficha por
    cada microdecisión; registrar decisión menor como entrada fechada en la
    sección competente de D01/D03/D04.», desarrolla la unidad como sección
    identificada dentro del documento de autoridad apropiado y explica por qué.
    Si sí corresponde separar, crea Markdown completo con `doc_id`,
    `schema_version`, `revision`, `editorial_status`, `as_of`, `access`;
    comentarios estables `<!-- kb:id=X07-B001 -->` y referencias [F-0001] a
    fuentes reales. Los IDs no deben inventarse como procedencia: crea fuentes
    solo tras leerlas.

    GATE ANTES DE ENTREGAR: confirma G1–G7. Si falla G2 o G6, NO entregues una
    pseudo-versión final: devuelve el avance de descubrimiento, los huecos K1/K2/K3
    y ejecuta la siguiente ronda de elicitación o recuperación necesaria.

    ENTREGA CUANDO PASE EL GATE: (1) documento empresarial desarrollado e
    inteligible sin hablar de estas instrucciones, (2) tabla privada/control de
    afirmaciones importantes: ID, estado, fecha, fuente, alcance, (3) pendientes
    concretos, (4) impactos transversales, (5) resultado de la prueba de utilidad,
    (6) evidencia de particularidad: al menos tres criterios/señales/trade-offs o
    excepciones que seguirían siendo propios de esta empresa si se ocultaran
    nombres, clientes, fechas y montos.
```

### ACT-X07 — Prompt completo de actualización

```text
ACTUALIZA X07 — Decisión, experimento o lección con identidad propia
conservando continuidad y evidencia.

    REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

    1. Recupera la versión exacta y sus fuentes (no solo su resumen); identifica
    `doc_id`, `revision`, IDs de bloques, campo de autoridad, fecha de evento y
    fecha de registro.
    2. Extrae del material nuevo los cambios que afectan ESPECÍFICAMENTE X07.
    Especial atención a: Diferencia la pregunta/decisión, experimento y
    aprendizaje; no afirmes causalidad si solo tienes correlación o una anécdota.
    3. Contrasta hecho/propuesta/aprobación/histórico y conserva intactos bloques
    ajenos; no generes secciones de relleno. Si la fuente contradice el
    documento, relee origen y registra conflicto.
    4. Regla de actualización específica: Nuevos resultados, reversión,
    ampliación de alcance o conflicto: mantener decisión histórica, marcar
    superseded y crear nueva versión.
    5. Verifica autoridad y destinos afectados: D01 prioridades, D03 reglas
    comerciales, D04 procesos, D05 finanzas, X04 caso fuente; el cambio requiere
    revisión explícita de autoridades.
    6. Conserva IDs de las afirmaciones cuyo significado siga intacto; si una
    afirmación se revoca, añade valid_to y supersedes sin borrar prueba anterior.
    Renueva solo los bloques materialmente cambiados y el índice de fuentes.
    7. Ejecuta de nuevo prueba práctica: Al recibir un caso contradictorio,
    localizar la decisión anterior, su evidencia original y si procede revisar o
    no la regla vigente.

    ENTREGA: documento actualizado completo o cambios versionados si no está
    permitido escribir; diferencias exactas, fuentes nuevas, estado
    editorial/cobertura/evidencia/vigencia de piezas cambiadas y cola de
    derivados. No proclames cambios guardados si no hubo escritura verificable.
```

## Ejemplo aplicado de una fuente transversal

## Ejemplo sintético de extremo a extremo: una fuente, varias consecuencias

> **Empresa ficticia:** Brisa Modular, fabrica módulos para exposición y ofrece instalación como servicio adicional. Los datos no corresponden a ninguna empresa ni usuario real.

**Entrada F-0100: llamada autorizada del 18/10/2026.** El interlocutor pregunta por entrega en sábado, comenta una posible tarifa adicional de MXN 4,000, señala que el equipo no cubre siempre fines de semana y solicita saber si pueden probarlo en dos trabajos. Este resumen no significa que exista contrato ni política nueva.

**Captura correcta, sin perder nada:**

- D02: observación acotada a una conversación: interés por sábado. No «preferencia del mercado».
- D03 y X01: tarifa adicional mencionada como **propuesta por validar**, no precio vigente.
- D04: nueva variante de entrega en revisión, todavía no SOP.
- D06: capacidad no acreditada; falta verificar operador disponible y facultad de aprobar horas extra.
- D07: riesgo de incumplimiento por falta de personal/transportista.
- X07: experimento opcional con dos entregas y criterios de éxito definidos antes.
- D05: escenario económico solo si contamos costos, cobertura, impuestos y método de cálculo; si faltan, queda pendiente.

**No se copia F-0100 siete veces:** CONTROL conserva una fuente con ID y cada bloque documenta su aportación y su estado. Las propuestas requieren aprobación. En el Paso 2, una pregunta sobre tarifa de sábado debe responder «en discusión» y localizar F-0100; no se permite concluir que el cliente ya la contrató.

### Ejemplo pequeño de D03, bloque humano + ancla de extracción

```markdown
---
doc_id: D03
schema_version: '0.9'
revision: '1.1'
editorial_status: 'en_revision'
as_of: '2026-10-25'
access: 'interno'
---
# Portafolio y sistema comercial de Brisa Modular
## 02 Promesa, alcance y exclusiones por modalidad
<!-- kb:id=D03-B004 -->
La instalación en domicilio se cotiza por separado del módulo.
La posibilidad de entregas en sábado es una propuesta no aprobada.
Fuente: [F-0100]. La tarifa de MXN 4,000 no debe mostrarse como vigente.
## Fuentes y límites
- [F-0100]: llamada del 18/10/2026; verificar transcripción original.
```

La captura narrativa y el comentario de bloque son diferentes: el cliente ve el texto comercial, un agente puede localizar `D03-B004` y resolver su estado en `manifest.json`. Este ejemplo **no debe publicarse** ni usarse como regla real; ilustra el diseño de fuentes/estados.

## Biblioteca de prompts de coordinación (íntegros)

**Para empezar, copie únicamente P00.** Los demás están disponibles para reiniciar una etapa, auditar, corregir o hacer la entrega en otra IA. Los 28 prompts de desarrollo/actualización ya aparecen completos dentro de sus fichas anteriores.

## P00 — Inicio y orquestador del Paso 1

```text
Actúa como director metodológico, analista de conocimiento empresarial y entrevistador de conocimiento experto.
Quiero construir documentación empresarial útil hoy y preparada para un futuro traspaso a Obsidian/agentes. NO diseñes ahora la bóveda.

AUTORIDAD: usa esta guía completa y las fichas D01–D07/X01–X07 como especificación. No simplifiques el contenido obligatorio ni inventes otra taxonomía.

PRINCIPIO CENTRAL:
RECUPERAR -> CLASIFICAR HUECOS K1/K2/K3/K4 -> ELICITAR K1 -> PASAR G1–G7 -> REDACTAR -> P03 -> VERSIONAR -> HANDOFF.
No redactes un D/X final sólo porque encontraste archivos relacionados.

FASE 0 — CAPACIDAD Y ALCANCE
- Identifica negocio, fuentes visibles, conexiones efectivas y sistemas de registro.
- No confundas «sé que existe» con «puedo leerlo».

FASE 1 — RECUPERACIÓN (P01)
- Lee primero y registra una vez cada fuente.
- Extrae hechos, decisiones, criterios explícitos, casos, procesos, cifras, excepciones y cambios.
- Produce mapa de preguntas ya respondidas; no vuelvas a preguntarlas.

FASE 1B — HUECOS Y AUTORIDAD (P01B)
Clasifica cada hueco:
K1 experto lo sabe; K2 vive en sistema/documento; K3 nadie lo sabe todavía; K4 no hace falta ahora.
Aplica la matriz de autoridad por tipo de conocimiento.

FASE 1C — ELICITACIÓN EXPERTA (P01C)
Para K1 realiza rondas de máximo cinco preguntas, ligadas a contenido obligatorio concreto.
Usa episodios reales, señales, comparación, contrafactuales, errores, excepciones y trade-offs.
No entrevistes al dueño sobre cifras o documentos K2 que deben recuperarse de una fuente.

FASE 2 — UNIDAD DOCUMENTAL (P02)
Decide qué D/X trabajar y si requiere archivo autónomo según utilidad, ciclo, autoridad, permisos, historia y consulta.

FASE 3 — GATE Y DESARROLLO
Antes de DES-[ID], verifica G1–G7. Si falla G2 o G6, vuelve a P01C; no generes un documento defensivo lleno de ausencias.
Si pasa, ejecuta íntegramente el DES-[ID] de la guía: contenido obligatorio, estructura exacta, relaciones, actualización, prueba y extracción.

FASE 4 — REVISIÓN (P03)
Prueba fuentes, autoridad, vigencia, criterio experto, particularidad y utilidad.
No marques no-genericidad porque aparezcan clientes, cantidades o fechas.

FASES 5–7
Versiona, procesa cambios con P04–P07 y cierra con P08/P09 sólo después de que los documentos pasen los gates y pruebas.

PRIMERA RESPUESTA:
(a) negocio y fuentes realmente leídas; (b) qué ya sabes; (c) mapa inicial K1/K2/K3/K4; (d) documento prioritario y por qué; (e) primera ronda P01C si hay K1; (f) siguiente operación concreta.
Después continúa ejecutando. No termines en un diagnóstico.
```

## P01 — Inventario y recuperación de fuentes

```text
Estás ejecutando recuperación, no una entrevista genérica.
1. Delimita y LEE fuentes autorizadas existentes: archivos, conversaciones accesibles, contratos, propuestas, CRM/correo si la conexión existe, sistemas de registro.
2. Registra cada fuente útil con ID persistente F-0001..., nombre, tipo, fecha efectiva, fecha de captura, localizador verificable, permisos, alcance y estado de lectura.
3. De cada fuente leída extrae hechos, episodios, decisiones, criterios explícitos, compromisos, métricas, cambios, excepciones y dudas. Agrupa por asunto, no por D/X prefijado.
4. Contrasta reciente/antiguo y autoridad; no votes por mayoría ni uses «archivo más nuevo» como regla automática.
5. Marca preguntas que ya pueden responderse y NO deben volver a preguntarse.
6. No conviertas ausencia documental en ausencia de conocimiento: envía los huecos a P01B.
SALIDA: registro de fuentes + mapa pregunta→evidencia + contradicciones + conocimiento explícito ya recuperado.
```

## P01B — Mapa de huecos y autoridad

```text
Recibiste el inventario P01. Para cada pregunta material aún incompleta clasifica:
K1 = el dueño/experto probablemente conoce el criterio o decisión aunque no esté escrito.
K2 = la respuesta debe venir de un sistema/documento/comprobante/cliente/fuente externa concreta.
K3 = nadie tiene todavía una respuesta suficiente; es hipótesis, investigación o decisión pendiente.
K4 = no es necesaria para la tarea/documento actual.

Para cada hueco indica: pregunta, clase K, autoridad correcta, por qué importa, D/X afectado, acción siguiente.
Usa la matriz de autoridad: estrategia/criterio puede tener al decisor como fuente primaria; transacción necesita sistema; voz de mercado necesita clientes/datos; obligación legal necesita contrato/norma/asesoría.
No uses K1 para sustituir un K2 ni pidas al dueño recordar un K2 de memoria.
SALIDA: MAPA_K1_K2_K3_K4 + lista K1 priorizada para P01C + solicitudes concretas K2 + K3/K4 no bloqueantes.
```

## P01C — Elicitación experta adaptativa

```text
Tu objetivo es convertir conocimiento tácito K1 en conocimiento explícito, NO entrevistar toda la empresa desde cero.
1. Relee antes el contenido obligatorio y la sección «Conocimiento experto a elicitar» del D/X objetivo.
2. Elige máximo CINCO preguntas de mayor valor que completen criterios, señales, trade-offs, excepciones o decisiones materiales.
3. Prefiere preguntas de episodio, contraste, señal, error, excepción, contrafactual y transferencia. Evita «¿cuál es tu misión?» si puedes preguntar por una decisión real.
4. Después de cada respuesta separa: decisión/criterio del experto, ejemplo, excepción, alcance y cualquier K2/K3 descubierto.
5. Contrasta con casos/documentos disponibles cuando corresponda. No invalidez un criterio interno sólo porque no sea una preferencia demostrada del mercado.
6. Resume lo entendido en lenguaje concreto y pregunta corrección sólo si cambia el significado.
7. Reevalúa G1–G7. Si G2/G6 siguen débiles, diseña la siguiente ronda; si pasan, devuelve autorización metodológica para ejecutar DES-[ID].
SALIDA: conocimiento experto estructurado + fuentes/atribución + límites + gate actualizado + cola transversal.
```

## P02 — Elegir unidad documental y descomposición

```text
Recibiste P01 + P01B y, cuando corresponda, P01C. No crees archivos por cada tema.
Evalúa cada candidato como bloque o documento autónomo: (1) versión/fecha propias, (2) autoridad/aprobador distinto, (3) sensibilidad diferente, (4) consulta independiente, (5) ciclo de vida diferente, (6) historia/evidencia propia, (7) reutilización.
Si una ficha autónoma sólo repetiría el documento mayor, descártala.

ANTES DE AUTORIZAR REDACCIÓN FINAL comprueba G1–G7. Un documento con fuentes abundantes pero sin criterio experto material o sin particularidad NO está listo.

Devuelve: unidad/identidad, dónde vive, autoridad, por qué dividir/no dividir, relaciones, documento/bloque propuesto, riesgo de duplicación, estado G1–G7 y siguiente acción si algún gate falla.
```

## P03 — Revisión editorial, semántica y de utilidad

```text
Audita un documento empresarial completo y sus fuentes. No premies estructura o trazabilidad si el documento todavía no explica la empresa.
A) fuente→documento: hechos y matices materiales.
B) documento→fuente/autoridad: cada afirmación usa el tipo de autoridad correcto.
C) cobertura: responde lo que la ficha promete, independiente de aprobación editorial.
D) vigencia: actual/histórico/propuesta/hipótesis/conflicto.
E) autoridad: lugar principal por asunto+entidad+contexto+periodo.
F) transversalidad: impactos en otros D/X.
G) legibilidad: un lector nuevo entiende cómo funciona esta parte de la empresa.
H) prueba funcional: ejecuta la tarea empresarial de la ficha.
I) criterio experto: identifica las señales, decisiones, trade-offs, excepciones o mecanismos que el experto aportó; si faltan, falla G2.
J) particularidad/no-genericidad: oculta mentalmente nombres, clientes, fechas y montos. Si el resto podría pertenecer a casi cualquier empresa del sector, falla G6. Exige al menos tres elementos de criterio/mecanismo/elección propios cuando la clase lo permita.
K) equilibrio empresa/CONTROL: el cuerpo no puede convertirse en un reporte de lo que la IA no pudo demostrar.

Un fallo G/H/I/J material bloquea aceptación. Vuelve a P01C, K2 o al DES según la causa; no maquilles el texto.
INFORME: errores por gravedad, causa (fuente/K1/K2/K3/síntesis), corrección, derivados afectados y retest.
```

## P04 — Corrección sustantiva y propagación

```text
El propietario dijo «esto está mal» o detectaste contradicción. Trata la
corrección como una investigación focalizada, no un parche textual.
REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

1. Expresa en una línea cuál afirmación específica fue cuestionada, su
bloque/ID, asunto, vigencia y fuente original.
2. Recupera y RELEE fuentes primarias relacionadas y las contrapuestas. Si
faltan, señala exactamente cuáles.
3. Reconstruye qué era verdadero antes, qué se propuso, qué fue aprobado, qué
está vigente y para qué caso/alcance.
4. Corrige el bloque y sus referencias conservando `doc_id`, `block_id` y la
historia. Cuando cambió semántica, registra versión/reemplazo sin borrar el
anterior.
5. Consulta relaciones inversas y produce lista de derivados: oferta,
propuesta al cliente, SOP, cifra, acuerdo, expediente, documento de marca,
claim público, etc. Marca cada uno `actualizado`, `en_revision` o
`no_afectado` con razón.
6. Ejecuta prueba negativa: una consulta sobre el estado ANTERIOR debe
recuperar el histórico; una consulta de HOY debe recuperar lo vigente.
Rechaza cualquier resultado que transfiera la regla de un cliente a todos.

SALIDA: (i) diagnóstico fuente→error, (ii) documento corregido íntegro o
bloque con contexto si no autorizado a reescribir, (iii) diferencias, (iv)
impacto en derivados, (v) lo que aún requiere aprobación.
```

## P05 — Actualización periódica sin rehacer todo

```text
Actualiza documentos empresariales existentes a partir de nuevas fuentes
verificadas y del manifest actual; no reescribas desde cero.
REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

Recupera versión canónica y fuente antes de editar. Resume delta entre
registro previo y nuevo; distingue cuándo ocurrió el cambio (`valid_from`) y
cuándo se supo (`recorded_at`). Identifica asunto/entidad/alcance de cada
delta; si son varios, procesa una vez la fuente y vincula múltiples bloques.
Preserva documento y bloques no afectados, conserva historia, incrementa
revisión según significado y corrige derivados con autoridad. Recalcula
cobertura afectada y vuelve a probar una tarea real de negocio. Si hay
conflicto, mantén ambas versiones visibles como conflicto hasta resolver; no
uses «último archivo» como desempate automático.

SALIDA: changelog por bloque, revisiones, fuentes y permisos, estado
editorial/cobertura/evidencia/vigencia, cola transversal y prueba de
regresión.
```

## P06 — Procesar conversación, audio o archivo nuevo

```text
Tengo una nueva conversación, audio, transcripción, presentación, Excel,
acuerdo o material. Ingresa el material SOLO si realmente está adjunto o
accesible por una conexión autorizada.
REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

1. Registra origen con ID, fecha de evento, captura, localizador, nivel de
privacidad y calidad (transcripción editada/no editada, si aplica). Nunca
trates transcripción de audio como aprobación jurídica.
2. Reconstruye episodios y afirmaciones atómicas: quién
dijo/decidió/solicitó/usó/contrató/entregó/facturó/cobró; cantidades,
monedas, unidades, fechas y condiciones. Separa interpretación de cita.
3. Detecta a cuáles unidades/documentos impacta, aunque pertenezcan a otro
tema de trabajo, sin duplicar el archivo ni pegar la conversación en varios
lugares.
4. Compara con autoridad vigente y ubica resultados como `confirmacion`,
`correccion`, `nueva_propuesta`, `nuevo_hecho`, `conflicto` o `no_aplicable`.
5. Actualiza de forma conservadora; no publiques cambios a clientes ni
cambies contratos, precios o políticas sin autorización y fuente.
6. Devuelve registro de nuevo conocimiento, tabla de impactos por documento,
referencias, máximo tres preguntas y los cambios preparados o hechos
realmente.

Si el archivo es PDF/imágenes, señala si pudiste ver sus partes visuales; no
inventes lectura. Si está truncado o protegido, no lo marques «leído
completo».
```

## P07 — Reanudar en otra conversación o IA

```text
Quiero continuar una documentación ya empezada. No confíes en el resumen que
te traiga como autoridad última.
REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

Lee el manifest, registro de fuentes y documentos canónicos realmente
disponibles; verifica versiones y checksums si existen; elige 2–4
afirmaciones materiales y vuelve a su fuente. Compara registro del último
cierre con archivo actual para detectar revisiones o desacuerdos. Identifica
compromisos pendientes y qué puede hacerse con fuentes actuales. Si hay
faltantes de acceso, no repitas toda la entrevista: pide solo el documento
fuente preciso o permite continuar en piezas independientes.

Devuelve: versiones observadas, divergencias con resumen anterior, trabajo
reanudable, 1–3 bloqueos, siguiente tarea empresarial verificable. No
presupongas que una aplicación comparte archivos o memorias con otra.
```

## P08 — Cierre del Paso 1 y aceptación del dueño

```text
Audita el Paso 1 como sistema de conocimiento empresarial, no como colección de archivos.
Comprueba C01–C11 y E01–E16, añadiendo estos gates de aceptación:
- Ningún D principal puede aceptarse si falla G2 o G6.
- C03 NO GENERICIDAD no se satisface con nombres, clientes, cantidades o fechas. Debe existir criterio, mecanismo, señal, trade-off, regla de excepción o vocabulario propio que sobreviva al ocultar esos datos.
- C01 UTILIDAD exige que el documento permita a una persona comprender y actuar, no sólo detenerse por falta de evidencia.
- C09 USABILIDAD incluye una revisión humana del significado cuando el piloto lo permita; una revisión de IA no sustituye al dueño.

Ejecuta como mínimo: cotizar, delegar, decidir con información económica, recuperar acuerdo/decisión a una fecha, incorporar fuente transversal y explicar una decisión del negocio desde criterio experto + fuente adecuada.
Para cada D/X reporta G1–G7, P03 A–K, reservas K2/K3 y prueba funcional.
Nunca declares completo por número de archivos, schema válido o citas correctas.
```

## P09 — Preparar el handoff al Paso 2

```text
Prepara una entrega agnóstica de harness para que otro agente pueda construir
después un cerebro empresarial en Obsidian. NO diseñes todavía carpetas,
grafos o plugins definitivos.
REGLAS NO NEGOCIABLES:
- Antes de preguntar, identifica y LEE las fuentes sustantivas disponibles en
esta conversación o en conexiones expresamente accesibles y autorizadas.
Enumera cuáles leíste y cuáles no puedes abrir; jamás finjas acceso a
memorias, otras conversaciones, correos o carpetas.
- No des por correcto un resumen de IA anterior si una fuente primaria lo
contradice. Al detectar laguna o choque, vuelve al mensaje, contrato, tabla,
audio transcrito o archivo original; identifica fecha y localizador.
- Distingue exactamente: hecho observado, testimonio, decisión aprobada,
propuesta, hipótesis, pendiente, desconocido, conflicto e histórico.
Editorial, cobertura, evidencia y vigencia son ejes distintos.
- No conviertas uso de una herramienta en compra de ese producto; no
conviertas una cotización en contrato, un caso en una política, un pronóstico
en un resultado, o un cargo sugerido en un área existente.
- Para afirmaciones relevantes, vincula ID de fuente una sola vez en CONTROL
y referencia ese ID en los bloques afectados. Captura hallazgos transversales
aunque pertenezcan a otros documentos: agrégalos a «cola de impactos» sin
duplicar su texto ni cambiar arbitrariamente la sesión.
- No me interrogues acerca de lo ya documentado. Antes de preguntar clasifica
cada hueco: K1 (lo sabe el experto), K2 (debe venir de sistema/documento),
K3 (nadie lo sabe todavía) o K4 (no es necesario ahora).
- Para K1, formula una ronda adaptativa de máximo CINCO preguntas vinculadas al
contenido obligatorio de esta clase. Usa episodios reales, señales, contrastes,
excepciones, errores y trade-offs; no preguntas abstractas que sólo produzcan
frases corporativas. Para K2 pide/localiza la fuente exacta. Para K3 conserva
hipótesis/pendiente. K4 no bloquea.
- La declaración del dueño/decisor autorizado puede ser fuente primaria de una
decisión, prioridad, política interna o criterio profesional dentro de su
facultad. No exijas evidencia de mercado para demostrar qué decidió la empresa;
pero no uses testimonio para certificar pagos, preferencias generales del
mercado, obligaciones legales u otros hechos cuya autoridad corresponde a un
sistema, cliente o fuente externa.
- Redacta conocimiento empresarial concreto para un lector nuevo; separa la
auditoría detallada en CONTROL. No dejes plantillas vacías ni rellenes secciones
con una sucesión de «no se recuperó/no se acredita». Si el hueco es K1, elicita;
si es K2, busca/pide la fuente; si es K3, delimítalo brevemente y continúa.
- No declares el documento desarrollado si falla G2 (criterio experto) o G6
(particularidad empresarial). Nombres, fechas, clientes y montos reales no
bastan para superar G6.
- No envíes comunicaciones externas, no publiques, no modifiques archivos
canónicos fuera del ámbito aprobado, no incluyas secretos ni datos personales
innecesarios. Si no puedes escribir archivos, devuelve contenido Markdown
completo para guardar, no digas que lo guardaste.
- Los identificadores, versiones, referencias y metadatos técnicos los
administras tú. El propietario revisa significado y autoriza decisiones, no
escribe YAML.

Lee documentación canónica aprobada y/o parcialmente suficiente, CONTROL y
fuentes accesibles. Genera `manifest.json` conforme al
Contrato_Traspaso_Obsidian_Agentes_vNext.md y al JSON Schema suministrado.
Incluye documentos, versiones, cobertura por pregunta, cuatro ejes de estado,
fuentes y locators, IDs estables de bloques, autoridad por asunto/alcance,
entidades con identidad propia, relaciones tipadas, historiales,
restricciones, permisos, pendientes y tests de recuperación. Comprueba
integridad referencial, unicidad, caminos relativos seguros, tipos/estados
válidos, fechas y ausencia de dos autoridades vigentes incompatibles.
Reconciliación semántica y permisos requieren revisión humana aunque el JSON
pase schema.

Realiza consultas de aceptación («precio vigente oferta X», «qué se firmó en
fecha Y», «caso que originó regla Z»), y entrega evidencia `consulta → bloque
→ fuente exacta`. No marques listo para ingesta si se perdieron fuentes,
vigencias o relaciones. Reporta limitaciones y qué no debe migrar por
restricción.
```

## Cómo se verifica que no vuelve a fallar

Pruebas mínimas del sistema sobre información autorizada: (1) cotizar sin inventar precio/alcance/impuestos; (2) decidir qué es delegable ante ausencia del dueño; (3) evaluar escenario de caja sin llamar «real» a un pronóstico; (4) reconstruir por fecha qué se acordó en un caso y qué cambió; (5) incorporar una conversación transversal sin duplicar fuente; (6) responder una pregunta desde un bloque con fuente original y permiso correcto. Un error material bloquea la aceptación de esa parte. Las pruebas conceptuales de seis PyME se detallan en el Informe.

**Revisión de los 16 errores históricos, en lenguaje cotidiano:** comprobar cobertura sin contar archivos (E01), separación por identidad (E02), estructuras especializadas (E03), estados independientes (E04), captura cruzada (E05), relectura de originales (E06), uso ≠ compra (E07), caso ≠ regla (E08), histórico ≠ actual (E09), propagación de correcciones (E10), negocio antes que parser (E11), consulta recuperable ≠ solo link (E12), documento de negocio ≠ informe del asistente (E13), valor parcial honesto (E14), recuperar antes de preguntar (E15), y flujo real más allá de un mega-prompt (E16).

Al cierre se revisan C01–C11: utilidad, cobertura, particularidad, extraibilidad, evolución, fechas, evidencia, autoridad, usabilidad, portabilidad y transferencia al Paso 2. **Particularidad exige criterio propio, no sólo datos reales del negocio; utilidad exige comprensión/acción, no únicamente prudencia documental.** Un resultado «aprobado con reservas» explica sus reservas, no oculta los datos faltantes.

## Contrato de entrega al Paso 2: lo indispensable

La entrega contiene: (a) documentos Markdown de negocio, (b) `CONTROL` de fuentes, cobertura, pendientes y control de cambios, (c) `manifest.json` con documentos, revisiones, IDs de bloque, estados, autoridad, fuentes, permisos, históricos y relaciones, (d) un JSON Schema y validador de referencias, (e) consultas de recuperación que prueben `pregunta→bloque→fuente`. La especificación exacta está en `Contrato_Traspaso_Obsidian_Agentes_vNext.md` y se entrega un JSON sintético de ejemplo más un validador.

El agente futuro **NO recibe** acceso implícito al correo, cuentas, clientes o secretos; las fuentes restringidas deberán entregarse mediante permiso y contenedor autorizados o referenciarse sin contenido. La aprobación del handoff no equivale a implementar el sistema Obsidian. La arquitectura física de la bóveda queda expresamente fuera del alcance de esta fase.

## Preguntas frecuentes y límites de uso

## Problemas comunes y decisiones recomendadas

**¿Y si mi negocio tiene solo una persona?** Documenta funciones, permisos, sustituciones y dependencia real. No inventes dirección financiera, recursos humanos ni un organigrama. D06 puede ser una sección en dossier.

**¿Y si tengo cientos de clientes o productos?** Conserva la fuente maestra en CRM/ERP. Documenta reglas y excepciones con identidad; solo crea expediente X03/X01 cuando aporte historia, autoridad, restricciones o decisiones que el sistema maestro no explica. No exportes datos privados por comodidad.

**¿Y si el asistente no puede leer mis chats anteriores?** El prompt no le concede poderes. Comparte archivos relevantes o exportaciones de conversaciones con consentimiento; pide inventario explícito de lo realmente leído y avances parciales. Un resumen no es prueba suficiente al aparecer conflicto.

**¿Y si la empresa no conoce márgenes?** D05 describe mecanismo económico conocido, distingue costes faltantes y bloquea la conclusión sobre margen. No inventa cifras para «completar» una plantilla.

**¿Qué pasa cuando apruebo un párrafo?** Cambia editorial a aprobado de ese bloque. Evidencia, cobertura y vigencia se evalúan por separado. No des por cerrado todo D01 porque aprobaste su primera página.

**¿Puede IA tomar una experiencia y generalizarla?** Puede proponer un patrón o hipótesis sustentada. Convertirlo en política requiere X07 o aprobación equivalente y prueba de alcance. Un caso conserva su naturaleza contextual.

**¿Dónde van mi marca, contratos, datos, tecnología y aprendizaje?** No son olvidados ni obligatoriamente carpetas. D02 trata percepción/claims; D03 promesas; X05 obligaciones contractuales; D07 riesgos/privacidad/sistemas; X06 dependencias; X04/X07 casos, hipótesis y decisiones. El mapa de cobertura comprueba lo pertinente sin fabricar un departamento.

**¿Qué significa «portátil»?** Que otra IA pueda recibir Markdown y JSON con fuentes/IDs/estados y reconstruir consultas con evidencia. Portabilidad no equivale a que las conexiones, permisos o historiales sean compartidos automáticamente.

## Apéndice: fuentes verificadas y trazabilidad

- **[S01] Porter, M.E. (1996) — What Is Strategy?.** HBR, texto en sitio. https://hbr.org/1996/11/what-is-strategy
  - Uso aquí: Separar posición competitiva, renuncias, configuración de actividades y mejora operativa. Límites: La lectura en línea no equivale a prueba empírica propia.
- **[S02] Kaplan, R.S. y Norton, D.P. (1992) — The Balanced Scorecard—Measures That Drive Performance.** HBR, artículo original. https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2
  - Uso aquí: Relacionar métricas financieras con capacidad operativa, clientes y aprendizaje, sin imponer cuatro cuadros. Límites: Modelo diseñado para medición gerencial, posible burocracia PyME.
- **[S03] Ross, J.W. (2005), MIT CISR — Forget Strategy: Focus IT on Your Operating Model.** MIT, briefing original. https://cisr.mit.edu/publication/2005_12_3C_OperatingModels
  - Uso aquí: Separar coherencia de procesos y estándares de decisiones tecnológicas. Límites: Marco de arquitectura empresarial sobredimensionado para ciertas PyME.
- **[S04] Osterwalder et al., Strategyzer — Business Model Canvas.** Fuente del framework. https://www.strategyzer.com/library/the-business-model-canvas
  - Uso aquí: Usar nueve componentes para contrastar coherencia, no un canvas como documento final. Límites: Representación estática no sustituye pruebas ni decisiones.
- **[S05] Strategyzer — Value Proposition Canvas.** Fuente del framework. https://www.strategyzer.com/library/the-value-proposition-canvas
  - Uso aquí: Distinguir trabajos, fricciones, ganancias y promesa validada. Límites: Hipótesis no equivalen a demanda demostrada.
- **[S06] Christensen, Hall, Dillon y Duncan (2016) — Know Your Customers’ Jobs to Be Done.** HBR, artículo original. https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
  - Uso aquí: Describir episodios de elección y circunstancias, no personas imaginadas. Límites: Marco interpretativo: exige entrevistas situadas y triangulación.
- **[S07] Blank, S. (2008) — The Customer Development Process.** Stanford eCorner, transcripción. https://ecorner.stanford.edu/wp-content/uploads/sites/2/2008/10/2058.pdf
  - Uso aquí: Separar hipótesis de clientes de evidencia observada. Límites: Enfocado en descubrimiento de clientes; no siempre escala de muestra.
- **[S08] Keller, K.L. (1993) — Conceptualizing, Measuring, and Managing Customer-Based Brand Equity.** Journal of Marketing, abstract editorial. https://journals.sagepub.com/doi/10.1177/002224299305700101
  - Uso aquí: Separar asociaciones/claims de marca y evidencia del cliente. Límites: Acceso a resumen y metadatos, no a análisis completo de artículo bajo licencia.
- **[S09] Shostack, G.L. (1984) — Designing Services That Deliver.** HBR, original. https://hbr.org/1984/01/designing-services-that-deliver
  - Uso aquí: Modelar experiencia de cliente, momentos de verdad y puntos de falla. Límites: Particularmente servicios; no sustituye procesos internos de producto.
- **[S10] APQC — Process Classification Framework, cross-industry.** APQC, estándar/taxonomía oficial. https://www.apqc.org/process-frameworks
  - Uso aquí: Inventario de capacidades para detectar omisiones, no lista obligatoria de procesos. Límites: Taxonomía genérica no dice cómo opera una PyME concreta.
- **[S11] Object Management Group (2014) — BPMN 2.0.2.** OMG, especificación oficial. https://www.omg.org/spec/BPMN/2.0.2
  - Uso aquí: Distinguir actividades, eventos, responsables y decisiones; usar diagramas sólo si aportan. Límites: Notación formal requiere formación y mantenimiento.
- **[S12] ISO/TC 176 — The Process Approach in ISO 9001:2015.** ISO, orientación oficial. https://www.iso.org/iso/iso9001_2015_process_approach.pdf
  - Uso aquí: Capturar entradas, salidas, control, seguimiento y mejora proporcional. Límites: No implica certificar a la empresa ni redactar un SOP para todo.
- **[S13] IASB / IFRS Foundation (2025) — IFRS for SMEs Accounting Standard, third edition.** Fuente normativa primaria. https://www.ifrs.org/news-and-events/news/2025/03/march-2025-ifrs-for-smes-accounting-standard-update/
  - Uso aquí: Separar reconocimiento contable de modelos gerenciales y proyecciones. Límites: No se presume obligatoria en ninguna jurisdicción; vigencia/aplicación local requieren profesional.
- **[S14] IASB / IFRS Foundation (2025) — Revised IFRS Practice Statement 1: Management Commentary.** Fuente institucional primaria. https://www.ifrs.org/issued-standards/list-of-standards/management-commentary-practice-statement/
  - Uso aquí: Exigir relato conectado de modelo, recursos, riesgos y capacidad de generar efectivo. Límites: Guía orientada a reportes para inversionistas; no requisito PyME.
- **[S15] U.S. SBA — Manage your business — finances.** Organismo público de PyME. https://www.sba.gov/counseling/manage-your-business/
  - Uso aquí: Separar efectivo, saldos, cuentas por cobrar/pagar y registro real. Límites: Guía de EE.UU.; no sustituye normativa fiscal local.
- **[S16] Galbraith, J. — Star Model.** Autor original. https://jaygalbraith.com/services/star-model/
  - Uso aquí: Relaciones entre estrategia, estructura, procesos, incentivos y personas. Límites: No obliga a organigrama formal; puede sobredimensionarse.
- **[S17] Rogers, P. y Blenko, M. (2006) — Who Has the D?.** HBR, artículo original. https://hbr.org/2006/01/who-has-the-d-how-clear-decision-roles-enhance-organizational-performance
  - Uso aquí: Registrar quién propone, decide, ejecuta y revisa decisiones de alto impacto. Límites: RAPID completo puede ser excesivo para tres personas.
- **[S18] COSO (2017) — Enterprise Risk Management—Integrating with Strategy and Performance.** Organismo del marco. https://www.coso.org/enterprise-risk-management
  - Uso aquí: Conectar riesgos con decisiones, objetivos, respuesta y monitoreo. Límites: Marco complejo de enterprise risk management, simplificar para PyME.
- **[S19] NIST (2024) — Cybersecurity Framework 2.0: Small Business Quick-Start Guide.** Guía gubernamental primaria. https://www.nist.gov/publications/nist-cybersecurity-framework-20-small-business-quick-start-guide
  - Uso aquí: Registrar dependencias críticas, accesos, respaldos, respuesta y continuidad. Límites: Riesgo cibernético es sólo una clase de riesgo.
- **[S20] Nonaka, I. (2007; obra previa 1991) — The Knowledge-Creating Company.** HBR, artículo del autor. https://hbr.org/2007/07/the-knowledge-creating-company
  - Uso aquí: Hacer explícitos criterios y experiencias sin fingir que todo saber tácito cabe en fichas. Límites: No todo aprendizaje se captura sólo por escritura.
- **[S21] Argyris, C. (1977) — Double Loop Learning in Organizations.** HBR, original. https://hbr.org/1977/09/double-loop-learning-in-organizations
  - Uso aquí: Revisar supuestos y políticas, no solo corregir ejecuciones. Límites: No equivale a que un caso aislado cambie una política.
- **[S22] APQC (2023) — Knowledge Flow Process.** Marco institucional. https://www.apqc.org/resource-library/resource-listing/apqcs-knowledge-flow-process-framework
  - Uso aquí: Crear, identificar, recolectar, revisar, compartir, acceder y utilizar. Límites: Ciclo describe actividades, no formato documental ni prueba de impacto.
- **[S23] National Wildfire Coordinating Group — After Action Reviews: four questions.** Práctica institucional adaptada del ejército. https://www-nwcg.fs2c.usda.gov/wfldp/toolbox/aars
  - Uso aquí: Comparar intención, resultado, explicación y mejora con evidencia. Límites: Sesgo retrospectivo si no se retienen evidencias.
- **[S24] Project Management Institute — Applying lessons learned.** Asociación profesional, artículo. https://www.pmi.org/learning/library/applying-lessons-learned-implement-project-8344
  - Uso aquí: Separar capturar de aplicar lecciones en casos nuevos. Límites: Artículo de practitioner, no evaluación experimental comparativa.
- **[S25] ISO (2018) — ISO 30401:2018 Knowledge management systems—Requirements.** Referencia normativa oficial. https://www.iso.org/standard/68683.html
  - Uso aquí: Revisión, mejora y mantenimiento del conocimiento como práctica recurrente. Límites: Texto integral bajo licencia; edición en revisión en 2026, no presuponer certificación.
- **[S26] W3C (2013) — PROV-O: The PROV Ontology.** Recomendación W3C. https://www.w3.org/TR/prov-o/
  - Uso aquí: Separar entidades, actividades, agentes y derivaciones para trazabilidad. Límites: No implementar OWL/RDF completo en una PyME.
- **[S27] OASIS — DITA: What are topics?.** Especificación conceptual. https://docs.oasis-open.org/dita/v1.0/archspec/topics.html
  - Uso aquí: Unidad semántica autocontenida y reutilizable no equivale a archivo físico. Límites: No introducir XML/DITA como formato obligatorio.
- **[S28] Obsidian — Properties.** Ayuda oficial vigente. https://obsidian.md/help/properties
  - Uso aquí: YAML posible en Paso 2, no imponer campos técnicos al dueño. Límites: Propiedades son de notas, no semántica empresarial.
- **[S29] Obsidian — Internal links and block references.** Ayuda oficial vigente. https://obsidian.md/help/links
  - Uso aquí: IDs de bloque Obsidian no son Markdown estándar ni unidad de autoridad. Límites: No utilizar ^id de Obsidian como ID primario portable.
- **[S30] OpenAI — Custom instructions with AGENTS.md.** Documentación oficial de Codex. https://learn.chatgpt.com/docs/agent-configuration/agents-md
  - Uso aquí: Instrucciones del agente viven aparte del contenido empresarial. Límites: Codex no garantiza acceso a fuentes remotas sin permisos/herramientas.
- **[S31] JSON Schema — JSON Schema 2020-12 specification.** Especificación abierta. https://json-schema.org/specification
  - Uso aquí: Validar manifest de traspaso con reglas de estructura. Límites: Schema valida estructura, no veracidad ni recuperación semántica.
- **[S32] U.S. SBA — Plan your business.** Guía pública. https://www.sba.gov/counseling/plan-your-business/
  - Uso aquí: Revisar relaciones entre mercado, operación, finanzas y personas. Límites: Plan de negocios típico es demasiado estático y orientado a financiación.
- **[S33] APQC — Knowledge management approaches.** Marco institucional. https://www.apqc.org/expertise/knowledge-management/km-approaches
  - Uso aquí: Escoger entre documentación y transferencia oral/asistida según naturaleza del saber. Límites: Captura escrita no resuelve por sí sola competencias tácitas.
- **[S34] Peter Fader y Sarah Toms (2018), Wharton — The Customer Centricity Playbook.** Fuente institucional de autores. https://leadershipcenter.wharton.upenn.edu/books/the-customer-centricity-playbook/
  - Uso aquí: No tratar a todos los clientes como monolito; documentar diferencias observadas y valor económico cuando pueda medirse. Límites: No exigir CLV ni inventar segmentos cuando los datos son insuficientes.
- **[S35] Alexander Chernev y Philip Kotler (2023), Kellogg — Kellogg on Marketing, 3rd ed., cap. 2.** Índice y sinopsis editorial de obra original. https://www.oreilly.com/library/view/kellogg-on-marketing/9781119906247/c02.xhtml
  - Uso aquí: Distinguir decisiones de mercado y valor de ejecución táctica y controles. Límites: Acceso al índice/sinopsis, no a texto íntegro bajo licencia.
- **[S36] Jensen, R.J. y Szulanski, G. (2007), INSEAD — Template Use and the Effectiveness of Knowledge Transfer.** Artículo académico, resumen INFORMS e INSEAD. https://doi.org/10.1287/mnsc.1070.0740
  - Uso aquí: Ejemplos de ejecución verificables pueden ayudar a transferir procedimientos cuando el contexto está controlado. Límites: Estudio de transferencia de prácticas de gran corporación; no justifica plantilla universal para todos los documentos empresariales.


Las fuentes externas sostienen principios y comparaciones, no garantizan por sí solas el diseño resultante ni autorizan copiar contenido licenciado. Para decisiones metodológicas, alternativas rechazadas y limitaciones por fuente, consulte `Informe_de_Investigacion_y_Decisiones.md` y `Matriz_Fuentes_Frameworks_Documentos.csv`.


---

**Estado de esta guía:** candidata bien fundamentada y validada conceptualmente con escenarios sintéticos; requiere piloto real y pruebas de ingestión multi-harness para llamarse definitiva.
