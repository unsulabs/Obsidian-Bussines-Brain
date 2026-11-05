# Catálogo de documentos canónicos — vNext-1.0R — vNext

**Versión:** vNext-0.9 — candidata para validación práctica.  
**Lectura correcta:** hay **14 clases semánticas** y **cero obligación** de que sean catorce archivos; siete familias cubren funciones esenciales y siete tipos de expedientes solo existen si su identidad lo exige. No es un plan de carpetas Obsidian.


## Adenda de adquisición de conocimiento tras el piloto

Este catálogo **no cambia** las clases ni sus contenidos investigados. Antes de declarar una clase desarrollada, aplicar K1/K2/K3/K4 y G1–G7 de la guía vNext-1.0R. En particular, las fuentes documentales no sustituyen el criterio del experto cuando la clase exige decisiones, señales o trade-offs; y el testimonio del experto no sustituye un sistema de registro cuando la clase exige un hecho transaccional o externo.

## Cómo decidir número de archivos sin decidir antes el negocio

**Primero** reconstruir preguntas del negocio y fuentes. **Después** seleccionar la autoridad de cada asunto. **Finalmente** decidir si bloque o documento con base en identidad, vigencia, dueño de aprobación, privacidad, historia, frecuencia de actualización, consulta y reutilización. Heurística: dos señales justifican evaluar separación; una obligación o restricción crítica puede bastar. Si el archivo creado sería una copia del documento mayor, no crearlo. No separar por función ni por nombre de framework.

Una empresa puede llevar D01–D07 en secciones diferenciadas de un *dossier* inicial mientras aprende; al aparecer múltiples precios/contratos/casos, nacen X01–X07 independientes y se referencian sin copiar su autoridad. Un documento de familia sigue teniendo su estructura de secciones, incluso si vive dentro de dossier. Todos los IDs semánticos permanecen estables frente al traslado de archivo.

## Tabla de clases

| ID | Clase | Forma | ¿Autónomo? |
|---|---|---|---|
| D01 | Dirección, modelo de negocio y límites estratégicos | Familia principal | No requiere archivo independiente si no hay más de un modelo de negocio, ciclos de revisión diferentes o decisiones estratégicas complejas. |
| D02 | Conocimiento del mercado, clientes y marca | Familia principal | Puede quedar integrado con D03 si solo hay una audiencia y dos o tres observaciones verificadas; no inventar buyer personas por ausencia de datos. |
| D03 | Portafolio y sistema comercial | Familia principal | No separar comercial y ofertas si cambiar cualquiera no ocasiona revisiones en agendas/usuarios distintos; abrir X01 por autonomía real. |
| D04 | Ejecución, experiencia y calidad | Familia principal | No crear un SOP por cada actividad; si la tarea cambia siempre y depende de criterio experto, documentar decisiones y ejemplos más que pasos rígidos. |
| D05 | Economía, caja y criterios financieros | Familia principal | Puede ser sección breve mientras no existan varias unidades económicas, financiamiento o múltiples responsables; estados financieros permanecen en sistema fuente. |
| D06 | Personas reales, responsabilidades y facultades | Familia principal | No necesita organigrama/archivo separado si hay una sola persona y pocas responsabilidades; nunca inventar CFO, departamento o junta. |
| D07 | Riesgos, compromisos y dependencias críticas | Familia principal | Puede integrarse como sección si sólo existen pocas dependencias controladas; no elaborar evaluación legal/regulatoria ficticia. |
| X01 | Ficha viva de oferta individual | Documento especializado condicional | Si sólo hay un servicio estable con un único precio y la ficha repetirá D03, dejar como subsección con ID semántico. |
| X02 | Proceso o instrucción de trabajo autónoma | Documento especializado condicional | Si es un paso trivial, raro o puramente creativo y no requiere gobierno independiente, mantener como bloque en D04. |
| X03 | Ficha de relación con una cuenta o cliente | Documento especializado condicional | No crear por cada contacto; si el CRM fiable ya es registro de autoridad y basta una URL segura, conservar referencia al CRM. |
| X04 | Expediente de proyecto, caso o episodio | Documento especializado condicional | No crear expedientes por cada llamada trivial; un evento simple puede anotarse en CRM/caso existente. |
| X05 | Acuerdo u obligación autónoma | Documento especializado condicional | Obligaciones menores y rutinarias se referencian en D07 o sistema contractual; no duplicar íntegramente contratos sensibles. |
| X06 | Recurso, sistema o proveedor crítico | Documento especializado condicional | Si basta referencia a inventario/ERP/contrato y la dependencia no es material, dejar un enlace controlado en D07. |
| X07 | Decisión, experimento o lección con identidad propia | Documento especializado condicional | No crear ficha por cada microdecisión; registrar decisión menor como entrada fechada en la sección competente de D01/D03/D04. |

## Estados, procedencia y autoridad

**Cuatro ejes independientes, nunca un estado único:**

1. **Editorial:** `borrador` / `en_revision` / `aprobado` / `retirado`. Indica quién revisó la redacción, no que toda la materia está completa.
2. **Cobertura por pregunta:** `sin_fuente` / `parcial` / `suficiente_para_tarea` / `no_aplica` (con justificación). En cuanto cambie una tarea o contexto puede cambiar la suficiencia.
3. **Conocimiento de cada afirmación:** `hecho_observado` / `decision_aprobada` / `propuesta` / `hipotesis` / `historico` / `pendiente` / `desconocido` / `conflicto`. No se deduce la certeza de la confianza retórica de la IA.
4. **Vigencia temporal:** `vigente` / `futuro` / `superseded` / `caducado` / `sin_verificar`, con `valid_from`, `valid_to` cuando se conoce. Además guardar `recorded_at` para separar fecha de ocurrencia de fecha en que se registró.

La **clase de soporte** es independiente: `documental_directo`, `testimonio_atribuido`, `observacion`, `derivado_calculado`, `sin_fuente`, `fuentes_en_conflicto`. Una decisión puede estar aprobada pero apoyarse en una hipótesis no validada. Un precio aprobado puede ser histórico. Una sección editada puede mantener cobertura insuficiente. Registrar sensibilidad (`interno`, `confidencial`, `restringido`) y acceso por unidad; no exponer datos porque el PDF se vea bonito.
**Regla operativa de autoridad:** una afirmación no tiene autoridad global: se resuelve por *asunto + entidad + contexto + vigencia + fuente + ámbito*. Para un cliente y proyecto concreto, un acuerdo aceptado puede prevalecer sobre una condición comercial general para ese alcance, pero no convierte la excepción en política universal. Para datos de caja mandan transacciones registradas/conciliadas, no un PDF presupuestal. Para intención estratégica manda el decisor autorizado; para preferencias de clientes la evidencia observada y su muestra; para leyes, la fuente normativa y asesoría aplicable, no una propuesta de IA.

**Una sola autoridad por asunto y contexto:** si X01 gobierna el precio específico de una oferta, D03 no copia su valor como regla alternativa: enlaza la ficha y muestra una síntesis *no autoritativa*. Si no existe X01, la subsección versionada de D03 es autoridad. Si X05 gobierna contrato particular, D03/X01 no lo sobreescriben. Lo que una fuente demuestra y su alcance prevalecen sobre resúmenes posteriores.

**Separación de hechos comerciales:** `usado` ≠ `ofrecido` ≠ `cotizado` ≠ `aceptado` ≠ `contratado` ≠ `entregado` ≠ `facturado` ≠ `cobrado`. Son eventos distintos que requieren evidencia diferente. `Autorizado para usar material` tampoco significa `autorizado para compartirlo fuera del equipo`.

## Especificación exacta, utilidad y pruebas

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- Compara oportunidades reales aceptadas y rechazadas: ¿qué señales hacen que una oportunidad sí encaje o no?
- ¿Qué trabajo puede pagar bien pero deliberadamente no quiere la empresa, y por qué?
- ¿Qué prioriza cuando precio, capacidad, reputación, calidad y tiempo chocan?
- ¿Qué actividad o combinación de capacidades considera difícil de copiar y por qué?
- ¿Qué quiere construir o dejar de hacer en los próximos periodos, y qué evidencia cambiaría esa decisión?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- Compara clientes excelentes y problemáticos: ¿qué señales aparecen antes de contratar?
- ¿Qué pregunta, comportamiento o circunstancia revela mejor el trabajo que el cliente intenta resolver?
- ¿Qué objeciones son literales y cuáles suelen esconder otra preocupación?
- ¿Qué promesa o claim nunca haría la empresa aunque ayudara a vender?
- ¿Qué creencia sobre clientes ha cambiado después de experiencias reales?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Cómo construye la empresa un precio cuando el trabajo no coincide con una oferta estándar?
- ¿Qué componentes, costos, condiciones o exclusiones nunca deben omitirse al cotizar?
- ¿Cuándo conviene precio global, desglose, módulo, paquete o cotización personalizada?
- ¿Qué excepción comercial puede autorizar cada persona y cuál necesita otra aprobación?
- ¿Qué señales indican que una propuesta todavía no está lista para enviarse?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- Reconstruye un trabajo real difícil desde confirmación hasta cierre: ¿dónde hubo decisiones críticas?
- ¿Qué señal temprana permite anticipar que la entrega puede salir mal?
- ¿Qué parte puede seguir una checklist y qué parte exige juicio experto?
- ¿Qué error es costoso/difícil de corregir y qué control lo evita?
- ¿Qué significa «terminado» o «aceptado» para la empresa en la práctica?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Cómo estima el experto si un trabajo vale la pena antes de tener todos los costos cerrados?
- ¿Qué costos o consumos suele olvidar una persona que no conoce bien el negocio?
- ¿Cuándo un proyecto grande puede ser peor negocio que uno pequeño?
- ¿Qué criterio usa para anticipos, descuentos, crédito, compras o gastos extraordinarios?
- ¿Qué cifra o señal mira primero al tomar una decisión económica y qué limitaciones reconoce?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- Si el fundador/dueño falta varios días, ¿qué puede seguir y qué se detiene realmente?
- ¿Qué decisiones sólo puede tomar hoy una persona específica y por qué?
- ¿Qué tarea podría delegarse si se explicitara mejor el criterio experto?
- ¿Qué conocimiento crítico vive en la cabeza de una persona y cómo se reconoce que alguien ya lo aprendió?
- ¿Qué diferencia existe entre ejecutar una tarea y tener facultad para comprometer a la empresa?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué problema real ha causado más daño, retrabajo, pérdida de dinero o riesgo reputacional?
- ¿Qué dependencia dejaría a la empresa sin poder entregar si falla mañana?
- ¿Qué riesgo acepta deliberadamente y cuál nunca aceptaría?
- ¿Qué control o respaldo se da por supuesto pero no se ha probado de extremo a extremo?
- ¿Qué compromisos, permisos o revisiones requieren fuente contractual/profesional en vez de criterio interno?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué debe poder entender el comprador sin conversación adicional para contratar esta oferta?
- ¿Qué parte del alcance cambia más y cuál nunca debe quedar implícita?
- ¿Cómo se construye o autoriza el precio de esta oferta y qué excepciones existen?
- ¿Qué condición hace que la oferta no sea adecuada para un cliente/caso?
- ¿Qué criterio de aceptación/soporte/garantía es realmente aplicable?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- Pide al ejecutor que reconstruya una ejecución real y señale decisiones que no están en la checklist.
- ¿Qué señal obliga a detener el proceso?
- ¿Qué excepción requiere criterio y quién puede autorizarla?
- ¿Qué evidencia demuestra que el proceso terminó correctamente?
- ¿Qué error típico comete un novato siguiendo sólo pasos literales?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué papel real tiene cada interlocutor (usuario, comprador, pagador, aprobador)?
- ¿Qué necesidades fueron expresadas por el cliente y cuáles son interpretación interna?
- ¿Qué promesas o excepciones específicas siguen vigentes para esta cuenta?
- ¿Qué información no debe generalizarse al mercado?
- ¿Qué restricción de acceso/retención/privacidad cambia cómo se conserva la relación?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué cambió materialmente durante el caso y por qué?
- ¿Qué decisiones/excepciones fueron exclusivas del caso?
- ¿Qué problema detectó el experto y qué señal lo hizo visible?
- ¿Qué resultado observado permite aprender y qué interpretación todavía es hipótesis?
- ¿Qué, si algo, debería promoverse a conocimiento común mediante una decisión separada?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué obligaciones son operativamente más importantes y qué fuente exacta las acredita?
- ¿Qué interpretación depende de asesoría profesional y no debe resolver la IA?
- ¿Qué fechas/condiciones cambian el estado de cumplimiento?
- ¿Qué modificación o excepción existe respecto del acuerdo general?
- ¿Qué otros documentos/procesos/caja se ven afectados por este acuerdo?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué capacidad empresarial se pierde si el recurso/sistema/proveedor falla?
- ¿Cuál es la fuente maestra del estado actual y qué no debe duplicarse?
- ¿Quién puede administrar/cambiar/sustituir este recurso?
- ¿Qué límite de capacidad o dependencia suele descubrirse demasiado tarde?
- ¿La recuperación/sustitución está probada o sólo declarada?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

**Conocimiento experto a elicitar cuando no esté suficientemente explícito:**

- ¿Qué decisión/hipótesis exacta se está preservando y qué alternativas se consideraron?
- ¿Qué señal/evidencia hizo cambiar de opinión o elegir una opción?
- ¿Qué resultado falsaría la hipótesis o obligaría a revisar la decisión?
- ¿Qué parte es aprendizaje contextual y qué parte podría convertirse en política?
- ¿Qué derivados deben revisarse si cambia esta decisión?

**Gate:** no declarar la clase desarrollada si falla G2 o G6.

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

## Localización de los prompts completos

Cada clase anterior tiene su propio prompt `DES-[ID]` y `ACT-[ID]`. Todos están íntegros, no abreviados, en `Biblioteca_Prompts_vNext.md` y repetidos completos en la guía PDF/Markdown. El dueño no tiene que ejecutarlos manualmente: P00 orquesta el flujo.
