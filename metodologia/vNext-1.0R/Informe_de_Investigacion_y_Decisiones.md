# Informe de investigación y decisiones — Paso 1: documentación empresarial con IA

**Edición:** vNext-0.9 — candidata para validación práctica  
**Fecha de consulta y corte:** 25 de octubre de 2026  
**Objeto:** diseñar el conocimiento empresarial útil para PyME y su traspaso documental portable, sin definir todavía la bóveda Obsidian.  
**Autoría de síntesis y diseño:** análisis metodológico asistido por IA; **no** equivale a validación académica por pares ni prueba piloto de campo.

## 1. Alcance y valoración honesta de la investigación anterior

El archivo de referencia DR-BRIEF-1.0 fue leído completo. El resumen entregado por la ejecución previa de Deep Research repetía esencialmente el brief y no adjuntó archivos ni evidencias bibliográficas rastreables. Por tanto, no se utilizó como autoridad metodológica. Este trabajo reconstruye los hallazgos con fuentes institucionales y originales verificadas públicamente. **Limitación importante:** varios artículos de HBR y normas ISO presentan solo resúmenes o acceso parcial; no alegamos haber consultado contenido licenciado no disponible. Tampoco se realizó estudio empírico propio con PyME reales; las seis pruebas son simulaciones adversariales conceptuales.

## 2. Evidencia externa, inferencia, decisión e hipótesis

- **[EVIDENCIA EXTERNA]** Un autor/organismo afirma o formaliza un principio; se cita fuente concreta con URL y se especifica cuál parte respalda la decisión.
- **[INFERENCIA]** Síntesis razonada entre marcos/errores del brief; no atribuir al autor un diseño particular que no propuso.
- **[DECISIÓN DE DISEÑO]** Convención elegida por equilibrio de valor, mantenimiento, control de versiones y portabilidad; puede cambiar con un piloto.
- **[HIPÓTESIS PENDIENTE]** Necesita pruebas con empresas reales, nuevas conversaciones, parsers alternativos y portabilidad cross-model para aceptarse.

## 3. Antes de documentos: mapa de necesidades de conocimiento

El mapa siguiente se construyó **antes** de decidir archivos; cubre preguntas operativas y decisiones, no departamentos.

| Necesidad | Pregunta de uso real | Lugar semántico candidato | Fuentes clave |
|---|---|---|---|
| Necesidad y propósito | ¿Qué problema resuelve y dónde gana/pierde valor? | D01 | S01 S04 S14 |
| Clientes y contexto | ¿Quién usa, paga y decide y en qué situación? | D02 | S05 S06 S07 |
| Promesa verificable | ¿Qué se vende y cuáles son exclusiones? | D03 X01 | S04 S05 S07 |
| Captación y conversión | ¿Cómo llega una demanda hasta un acuerdo? | D03 X03 | S32 S07 |
| Experiencia y entrega | ¿Qué secuencia, contingencia y aceptación funcionan? | D04 X02 X04 | S09 S10 S12 |
| Economía por unidad | ¿Qué cobra, cuesta y deja cada modalidad? | D05 X01 | S13 S15 |
| Liquidez y compromisos | ¿Qué entra y sale de caja y en qué fecha? | D05 X05 | S13 S15 |
| Quién decide | ¿Quién puede autorizar promesas/gasto/excepciones? | D06 X07 | S16 S17 |
| Capacidad y continuidad | ¿Qué falla al faltar persona, sistema, activo o proveedor? | D06 D07 X06 | S03 S19 |
| Obligaciones | ¿A qué se comprometió la empresa, con qué límites? | D07 X05 | S18 S19 |
| Información sensible | ¿Quién puede acceder, conservar y compartir? | D07 X03 X05 | S19 S25 |
| Aprendizaje | ¿Qué pasó, qué se aprendió, qué política sí se aprobó? | X04 X07 D01 D04 | S20 S21 S22 S23 |
| Temporalidad | ¿Qué era verdad antes, qué es vigente y qué se está probando? | TODOS | S22 S26 |
| Recuperación/autoridad | ¿Dónde está la fuente y quién prevalece si hay conflicto? | TODOS TRASPASO | S26 S27 S31 |

**[INFERENCIA]** Las necesidades abarcan estrategia, demanda, oferta, entregas, economía, facultades, obligaciones y aprendizaje. La información transversal (p. ej. una promesa que genera costo/riesgo) no se divide según el nombre del departamento que la mencionó. La clasificación de APQC sirve para detectar brechas, no para imponer procesos que no existen [S10]. El modelo de caja narrativa IFRS une modelo, riesgo, recursos, estrategias y resultados [S14], pero no obliga a preparar reportes de inversionistas.

## 4. Comparación de escuelas metodológicas y tensiones reales

| Tensión | Fuente y aporte | Límite/aparente contradicción | Elección y prueba |
|---|---|---|---|
| Estrategia vs eficiencia | Porter [S01] exige decisiones y renuncias; MIT CISR [S03] pide integración/estandarización operativa | La primera habla de elección; la segunda del sistema repetible | D01 declara renuncias y D04 procesos, unidos por relación explícita; se prueba con una oportunidad incompatible. |
| Canvas vs expediente vivo | Strategyzer [S04,S05] muestra coherencia y problemas del cliente | Canvas no conserva contratos, fechas ni pruebas en profundidad | Canvas es herramienta auxiliar, no documento canónico obligatorio; D01–D03 registran fuentes y estados. |
| JTBD vs segmentación | Christensen [S06] favorece circunstancias/trabajos; Keller [S08] analiza asociaciones de marca; Wharton [S34] describe heterogeneidad y CLV; Kellogg [S35] diferencia marketing estratégico del táctico | Un episodio no prueba un segmento; CLV requiere datos; índice de obra no prueba toda la metodología | D02 exige episodio, alcance y muestra antes de generalizar; segmentación, percepción y aspiración permanecen distintas. |
| Lista de procesos vs flujo observado | APQC [S10] clasifica, Shostack [S09] identifica fallas del servicio, ISO [S12] controla procesos | Taxonomía no detalla el flujo real y BPMN [S11] podría ser excesivo | D04 produce mapa narrativo real, X02 SOP sólo bajo disparador de riesgo/delegación; BPMN es opcional. |
| Indicadores estratégicos vs contabilidad | Balanced Scorecard [S02] amplía rendimiento; IFRS [S13] regula estados y SBA [S15] enfatiza flujo de efectivo | Objetivos y métricas no son asientos contables, presupuesto no es resultado | D05 etiqueta periodo, unidad, método y real/escenario; no duplica ERP/contabilidad. |
| Organigrama vs facultades reales | Galbraith [S16] conecta decisiones/personas/procesos; RAPID [S17] aclara decisión | Una PyME con fundador y apoyos externos no tiene jerarquía corporativa | D06 describe funciones y límites existentes; se prueba con ausencia del fundador. |
| Gestión de riesgo integral vs simplicidad | COSO [S18] une estrategia y riesgo; NIST [S19] adapta ciberseguridad a PyME | ERM completo es burocrático y ciberseguridad no es todo el riesgo | D07 prioriza exposición material y continuidad comprobada, sin matriz ficticia de 5x5. |
| Lección vs política | Argyris [S21] revisa supuestos, AAR [S23] ordena reflexión y PMI [S24] busca aplicar lecciones | Caso único puede no ser representativo | X04 guarda evidencia acotada; X07 requiere decisión autorizada para transformar una lección en política. |
| Plantillas que ayudan vs plantillas que vacían contexto | Jensen y Szulanski [S36] analizaron transferencia de prácticas con ejemplos operativos probados | El resultado se refiere a transferencia de rutinas, no a imponer idénticos encabezados a estrategia, marca y acuerdos | X02 incorpora ejemplo ejecutado y controles; D01–D07 preservan estructuras distintas; se comprueba que el dueño puede ejecutar, no solo rellenar. |
| Documento humano vs documento machine-readable | DITA [S27] favorece unidades autocontenidas; PROV [S26] aporta procedencia; Obsidian [S28,S29] ofrece propiedades/links | XML/OWL/propiedades específicas pueden invadir la semántica y bloquear portabilidad | Markdown humano + IDs de bloques estables + refs de fuente + manifest JSON externo, sin DITA/PROV completos. |
| Publicar rápido vs confiar en contenido | APQC Knowledge Flow [S22] pide revisión y uso; ISO 30401 [S25] mantenimiento | Obligar perfección impide que el dueño obtenga utilidad | Entrega parcial con estados honestos y tareas probadas; nunca homologar editorial y cobertura. |

**La matriz CSV anexa** amplía estos contrastes a todas las fuentes, con influencia en cada tipo de documento. Se rechazó convertir el prestigio de una escuela en un argumento; se priorizaron trabajos originales de HBR/MIT/Stanford, instituciones y normas pertinentes, sin reclamar que todas las escuelas recomendadas fueron investigadas con la misma profundidad.

## 5. Unidades semánticas y criterio de identidad

Los conceptos principales no corresponden uno a uno a archivos físicos:

| Unidad | Grano | Criterio / advertencia | Autoridad inicial |
|---|---|---|---|
| Empresa / línea | Entidad | Identidad legal/comercial y régimen del modelo, no archivo por cada división inventada | D01 |
| Segmento | Concepto condicional | Criterio observable y al menos episodio; separar solo si decisiones/mantenimiento distintos | D02 |
| Actor / rol | Entidad cuando tiene facultades | Identificar pagador, comprador, usuario, aprobador sin crear jerarquía | D02 D06 X03 |
| Trabajo / necesidad | Afirmación contextual | Contexto y episodios; no inferir universalidad | D02 |
| Oferta | Entidad si cotizable/versionable | Autonomía si precio/alcance/reglas tienen revisión independiente | D03 X01 |
| Precio | Afirmación temporal | Una sola autoridad por modalidad/segmento/vigencia y moneda | D03 X01 |
| Claim / promesa | Afirmación verificable | Estado publicable, alcance, evidencia/fecha | D02 D03 |
| Proceso | Entidad si delegable/recurrente | Inicio, salida, responsable, decisiones; no todo es SOP | D04 X02 |
| Paso / control | Bloque | Normalmente anidado dentro del proceso, evidencia de aplicación | D04 X02 |
| Proyecto / caso | Entidad contextual | Historia, cambios, evidencias, permisos y cobro propios | X04 |
| Cuenta | Entidad solo si autónoma | CRM autoridad si existe; no duplicar PII | X03 |
| Obligación / contrato | Entidad por exigibilidad | Vigencia, partes, consecuencias y fuente firmada | D07 X05 |
| Métrica / cifra | Afirmación con medida | Unidad, fórmula, periodo, corte, fuente, naturaleza real/estimada | D05 |
| Objetivo | Afirmación temporal | Meta, responsable de decidir, horizonte y resultado observable | D01 |
| Decisión | Entidad según materialidad | Alternativas, autoridad, fecha, efectos; no cada microdecisión | D01 X07 |
| Hipótesis | Afirmación refutable | Predicción/test, alcance; no promocionar automáticamente | D02 X07 |
| Riesgo | Afirmación evaluable | Evento, afectación, control y responsable | D07 |
| Recurso / sistema | Entidad si crítico | Fuente maestra, dependencia, recovery, acceso, fechas | D07 X06 |
| Fuente / evidencia | Entidad de procedencia | Origen, locator, checksum si viable, fecha y permiso; registrar una vez | CONTROL / TRASPASO |
| Aprendizaje | Afirmación con alcance | Episodio y evidencia + autoridad para generalizar | X04 X07 |
| Relación | Arista explícita | tipo/verbo, sujeto y objeto, vigencia, origen | TRASPASO |
| Restricción | Atributo + control | Sensibilidad y permisos prevalecen sobre facilidad de búsqueda | D07 TRASPASO |

**[DECISIÓN DE DISEÑO] Regla de promoción a documento propio.** Una unidad empieza como bloque o subsección bajo una autoridad por asunto. Se separa si necesita identidad y versión propias para operar, si presenta autoridad/ciclo de cambio diferente, sensibilidad, expediente/cronología, múltiples referencias o consultas independientes. Como atajo práctico se propone analizar siete criterios y requerir normalmente **dos señales**, salvo obligaciones o privacidad que pueden justificar separación inmediata. El umbral de dos es **hipótesis de usabilidad**, no resultado de un estudio estadístico: ajustar en piloto.

**Ejemplo semántico clave:** un descuento aprobado a un cliente se incorpora al expediente de oferta/cliente con su alcance; no cambia el precio general. Una queja del cliente alimenta X04 y D02 como fuente compartida, sin convertir automáticamente la experiencia en regla comercial.

## 6. Catálogo derivado, no universal

El diseño distingue **siete familias de explicación del negocio** y **siete tipos de expediente autónomo condicional**. Esta cifra es una consecuencia de agrupar preguntas por su uso y autoridad; **no** se recomienda crear catorce archivos a todas las empresas. Una microempresa puede comenzar con un dossier y tres anexos; una PyME con actividades distintas puede requerir decenas de expedientes de casos, ofertas y acuerdos sin multiplicar familias. Cada familia tiene una estructura especializada, no la plantilla genérica de un capítulo.

| ID | Clase | Identidad | Motivo del corte |
|---|---|---|---|
| D01 | Dirección, modelo de negocio y límites estratégicos | Familia principal | Siempre debe estar cubierto; puede ser una sección integrada en el dossier inicial cuando la empresa es muy pequeña. |
| D02 | Conocimiento del mercado, clientes y marca | Familia principal | Siempre existe cobertura mínima de clientes o usuarios; la separación física crece con heterogeneidad de segmentos y datos de investigación. |
| D03 | Portafolio y sistema comercial | Familia principal | Siempre que haya ventas o compromisos comerciales; si la empresa sólo tiene una oferta estable y pocos canales, puede vivir dentro de un dossier. |
| D04 | Ejecución, experiencia y calidad | Familia principal | Siempre que se realice una entrega; puede ser sección breve o ampliarse a mapa de procesos y X02 por independencia. |
| D05 | Economía, caja y criterios financieros | Familia principal | Debe cubrirse siempre: al menos mecánica de ingresos, principales costos, compromisos y regla de caja. |
| D06 | Personas reales, responsabilidades y facultades | Familia principal | Siempre que haya al menos un operador y decisiones; puede ser una sección reducida de roles reales para una empresa unipersonal. |
| D07 | Riesgos, compromisos y dependencias críticas | Familia principal | Siempre debe existir cobertura mínima de riesgos materiales y continuidad; profundidad proporcional a la exposición. |
| X01 | Ficha viva de oferta individual | Documento especializado condicional | Crear cuando la oferta tiene precio/alcance/versiones distintas, ventas recurrentes, responsable o aprobación separados. |
| X02 | Proceso o instrucción de trabajo autónoma | Documento especializado condicional | Crear ante recurrencia, criticidad/riesgo, delegación, cambios de versión o distintos ejecutores. |
| X03 | Ficha de relación con una cuenta o cliente | Documento especializado condicional | Crear sólo si la cuenta acumula interacciones/compromisos que necesitan continuidad fuera del CRM ordinario y existe base legal/autorización. |
| X04 | Expediente de proyecto, caso o episodio | Documento especializado condicional | Crear cuando una ejecución por cliente/proyecto tiene identidad, fuentes, costes, cambios, privacidad o decisiones propias. |
| X05 | Acuerdo u obligación autónoma | Documento especializado condicional | Crear si hay obligación con plazo, contraparte, sensibilidad, renovación, efecto en caja o múltiples documentos derivados. |
| X06 | Recurso, sistema o proveedor crítico | Documento especializado condicional | Crear por dependencia crítica con dueño, sustitución, permisos o historial de incidentes; no por cada artículo del almacén. |
| X07 | Decisión, experimento o lección con identidad propia | Documento especializado condicional | Crear si el cambio tiene efectos cruzados, controversia, importancia, hipótesis comprobable o historia que deba mantenerse. |

**[INFERENCIA]** Esta propuesta reformula H1–H7 del brief: H1 (dossier integrado con expedientes necesarios), H2 (casos por historia/permisos), H3 (dominios como checklist no carpetas), H4 (procedencia fuera de prosa), H5 (pruebas por tarea), H6 (unidades semánticas > carpetas) y H7 (JSON ligero y validable). Se conserva la intención pero ninguna hipótesis queda probada empíricamente. D01–D07 no son departamentos, ni bloques obligatoriamente separados; X01–X07 solo nacen por motivo justificado.

## 7. Decisiones de soporte humano + agente

| Opción | Ventaja | Desventaja | Tratamiento |
|---|---|---|---|
| Markdown libre | Excelente lectura | Se pierden estados, versionado y autoridad | Insuficiente solo |
| Frontmatter rico | Consultas y filtros | Costoso, frágil y técnico para dueño | **Mínimo de seis claves**, autogenerado |
| Encabezados semánticos estables | Legible, navegable, estable | Renombres rompen referencias si se usa título como ID | **Sí**, con ID de bloque independiente |
| Block IDs estilo Obsidian `^id` | Links dentro de Obsidian | No es sintaxis portable estándar [S29] | **No** como identidad primaria |
| Tablas homogéneas | Útiles para precios/cronologías/métricas | Hacen ilegibles estrategia y narración | Sólo donde corresponden a la función |
| Bloques de procedencia junto a cada oración | Máxima pista de fuente | Rompen lectura y mantenimiento | Referencias discretas más índice único |
| Metadata separada sin IDs en texto | No contamina prosa | Un parser necesita adivinar qué bloque corresponde | Descartado solo |
| Manifest JSON junto al Markdown | Estados, relaciones, permisos, validación | Riesgo de desincronizar | **Sí**, regenerar y validar en cada entrega |
| DITA XML / PROV RDF completos | Especificaciones profundas | Coste alto y aprendizaje técnico | Adopción de PRINCIPIOS, no formato |

**[DECISIÓN DE DISEÑO] Combinación mínima robusta:** cabecera breve autogenerada + estructura humana especializada + comentarios `kb:id` para unidades críticas + referencias discretas de fuentes + registro maestro de fuentes + `manifest.json` generado y validado al cierre. Más estructura debe justificar un fallo concreto de recuperación. Los bloqueos de acceso se aplican antes de indexación y exportación. XML/RDF, Obsidian YAML extensivo y bases de datos se reservan para el futuro Paso 2, sin obligación de implantarlos.

## 8. Estados, autoridad y temporalidad

**Cuatro ejes independientes, nunca un estado único:**

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
## 9. Pruebas conceptuales adversariales: seis PyME

| Perfil | Situación | Riesgo buscado | Corrección diseñada | Prueba de aceptación |
|---|---|---|---|---|
| Servicios profesionales pequeños | Consultoría de dos socios con asistente interno no vendido. | Riesgo E07: confundir herramienta usada con producto comprado; cada engagement tiene factura y términos. | D03 clasifica consultoría como contratada, asistente como herramienta; X04 registra episodios; D05 cobra por hitos. | No crear X01 por asistente sin oferta comercial. Pasa si una propuesta refleja alcance y fee correcto. |
| Fabricación y venta de productos | Taller de sillas con 6 variantes, lotes, mermas y catálogo en ERP. | Riesgo duplicar SKU/inventario y confundir precio publicado con costo de producción. | D03 sólo catálogo navegable; X01 para variante con reglas distintas, D05 costos por lote, X06 ERP crítico. | Pasa si una consulta de stock remite al ERP vigente, no a copia documental. |
| Híbrida producto-servicio | Vende equipos y además instalación con alcance opcional. | Riesgo tomar instalación como incluida en el equipo o doble contar ingresos. | X01 separa precio de equipo e instalación; D04 proceso de aceptación; D05 driver de mano de obra. | Pasa si cotización deja instalación fuera cuando no se contrata. |
| Dependencia del fundador | Negocio atendido por una sola persona; familia cubre urgencias. | Riesgo crear organigrama ficticio y descuidar secretos/continuidad. | D06 usa funciones y límites de sustitución, D07 ubica dependencia y accesos; D01 conserva decisiones. | Pasa si la sustitución se sabe detener en gastos no autorizados. |
| Varios equipos y funciones | PyME con ventas, logística, compras y personal externo. | Riesgo aprobaciones y fuentes paralelas compitiendo por autoridad. | D06 matriz de decisión real, D04 traspasos, D05 origen de datos, X02 solo procesos críticos. | Pasa si descuento grande identifica aprobador y mantiene versión de cotización. |
| Proyectos por cliente | Decoración de eventos con revisiones de alcance, rentas y cierre. | Riesgo histórico sobrescrito por documento comercial reciente y lección promovida a regla. | X04 cronología + fuente, X05 acuerdo, D03 modalidades, X07 decisión de generalizar, D05 cobro por evento. | Pasa si responde «¿qué se acordó el día X?» con evidencia y versión correctas. |

**Resultado**: no se detectó una ausencia semántica fatal en los escenarios sintéticos una vez añadidas las reglas de autoridad y traspaso; sí quedan **riesgos abiertos** sobre volumen real, permisos, transcripciones incompletas, parsing entre modelos y coste humano de mantener los índices. Son simulaciones razonadas, NO validación experimental o prueba de funcionamiento en conectores reales. No afirmar tasa de éxito.

### Experimento de transversalidad sobre una fuente compartida

**Episodio 100 % sintético (no dato de ningún cliente):** una llamada del 18-10-2026 trata (a) deseo de entrega un sábado, (b) una posible tarifa especial, (c) falta de operador en fines de semana, (d) riesgo de retraso y (e) voluntad del dueño de ensayar dos entregas. Se registra **una sola fuente F-0100** y cinco **aportaciones**: D02 = preferencia observada en una relación, D03/X01 = tarifa **propuesta**, D04 = excepción de entrega, D06 = capacidad limitada, D07 = riesgo y X07 = experimento, todos citando F-0100. Nada se vuelve política aprobada sin acto autorizado y nueva fuente. D05 solo incorpora escenario de coste si hay fórmula y fuentes suficientes; no calcula margen imaginario.

### Defectos identificados durante esta revisión y correcciones realizadas

- **Duplicidad D03/X01**: inicialmente ambos podían asumir precio como autoridad. Corregido: D03 es índice/política general y X01 autoridad por oferta cuando existe, D03 enlaza.
- **Contrato vs política general**: corregido alcance de X05 como autoridad específica solo para el acuerdo y tiempo, sin globalizar excepción.
- **Aprendizaje automático**: corregido gate X04→X07→documento de política por decisión autorizada.
- **Riesgo de exposición de cuentas**: corregido X03 con minimización, control de acceso y CRM como sistema maestro donde exista.
- **Vínculos incapaces de demostrar recuperación**: se añadió `retrieval_tests` con consulta→bloque→fuente, además de `relationships`.
- **Fechas ambiguas**: se diferenciaron `valid_from` y `recorded_at` para reversiones y correcciones retroactivas.

## 10. Auditoría retrospectiva: 16 errores E01–E16

| ID | Fallo del brief | Salvaguarda | Estado de revisión |
|---|---|---|---|
| E01 | Cobertura ≠ número de archivos | Cobertura por preguntas, pruebas y mapa de unidades; no meta cuantitativa de documentos. | Corregido en diseño; sin prueba piloto |
| E02 | Tema ≠ archivo | Reglas explícitas de promoción de bloque a documento con identidad y versión. | Corregido en diseño; sin prueba piloto |
| E03 | Plantilla genérica | 14 estructuras de contenido diferenciadas, pruebas específicas y prompts por especialidad. | Corregido en diseño; sin prueba piloto |
| E04 | Aprobación ≠ cobertura | Cuatro ejes independientes: editorial, cobertura, evidencia y vigencia. | Corregido en diseño; sin prueba piloto |
| E05 | Transversalidad perdida | Un ID de fuente alimenta múltiples bloques sin repetir texto ni cambiar la agenda. | Corregido en diseño; sin prueba piloto |
| E06 | Resumen erróneo | Ante conflicto releer fuente sustantiva, registrar fe de erratas y no confiar en bitácora. | Corregido en diseño; sin prueba piloto |
| E07 | Uso ≠ compra | Estados separados uso/venta/aceptación/factura/entrega y evidencia distinta. | Corregido en diseño; sin prueba piloto |
| E08 | Caso ≠ norma | Aprendizaje conserva alcance y gate de decisión autorizada para generalizar. | Corregido en diseño; sin prueba piloto |
| E09 | Histórico ≠ vigente | Fecha de validez, sucesión/reemplazo y dos líneas temporales: afirmación y registro. | Corregido en diseño; sin prueba piloto |
| E10 | Corrección con propagación | Índice de relaciones/derivados, cola de cambio y verificación de impacto. | Corregido en diseño; sin prueba piloto |
| E11 | Parser dicta semántica | Tipos semánticos de negocio independientes del JSON y de Obsidian. | Corregido en diseño; sin prueba piloto |
| E12 | Enlace ≠ recuperar | Pruebas de búsqueda con preguntas y evidencia recuperada, no solo enlaces. | Corregido en diseño; sin prueba piloto |
| E13 | Documento empresarial ≠ informe IA | Texto de negocio separado de CONTROL, manifest y notas de auditoría. | Corregido en diseño; sin prueba piloto |
| E14 | Perfección bloquea utilidad | Publicación parcial honesta con pendientes, conflictos y riesgos explícitos. | Corregido en diseño; sin prueba piloto |
| E15 | Preguntar lo sabido | Inventario/relectura precede 1–3 preguntas prioritarias por ronda. | Corregido en diseño; sin prueba piloto |
| E16 | Mega-prompt ≠ método | Orquestador por etapas, estados/gates, prompts especializados opcionales. | Corregido en diseño; sin prueba piloto |

## 11. Aceptación C01–C11

| ID | Criterio | Prueba | Estado honesto |
|---|---|---|---|
| C01 | Utilidad real | Propuesta, delegación, decisión y recuperación de un acuerdo en casos sintéticos | Especificada; pendiente de piloto real |
| C02 | Cobertura | Mapa de necesidades + ausencias importantes marcadas sin inventar | Especificada; pendiente de piloto real |
| C03 | No genericidad | Rechaza párrafos sustituibles por nombre de cualquier empresa | Especificada; pendiente de piloto real |
| C04 | Extraibilidad | Bloques identificables con tipos, fechas, fuente y relaciones | Especificada; pendiente de piloto real |
| C05 | Evolución | Cambio distribuido mantiene fuentes e histórico | Especificada; pendiente de piloto real |
| C06 | Temporalidad | Consulta antes/después devuelve versión que estaba vigente | Especificada; pendiente de piloto real |
| C07 | Evidencia | No asciende caso ni conjetura sin aprobación | Especificada; pendiente de piloto real |
| C08 | No duplicación | Una autoridad por asunto/alcance/periodo | Especificada; pendiente de piloto real |
| C09 | Usabilidad | Un prompt de inicio, dueño valida decisiones semánticas, no YAML | Especificada; pendiente de piloto real |
| C10 | Portabilidad | Markdown/JSON/CSV estándar; sin IDs Obsidian obligatorios | Especificada; pendiente de piloto real |
| C11 | Traspaso | Paquete versionado, validación estructural y preguntas de recuperación | Especificada; pendiente de piloto real |

## 12. Alternativas descartadas y límites

**Descartadas:** 64 fichas, 45 formularios, un archivo obligatorio por capítulo, toda la empresa en un archivo sin bloques, un documento por cada minievento, un BPMN obligatorio, una ontology OWL/RDF completa, metadatos que el dueño escriba manualmente, confiar solo en snippets de IA, una sola etiqueta «aprobado» como calidad, medir cobertura por número de archivos, normalizar casos únicos como políticas. Se descartan por incompatibilidad con la necesidad de uso y riesgos históricos, no porque los frameworks sean intrínsecamente malos.

**Limitaciones externas:** este análisis consultó material oficial, textos abiertos y resúmenes editoriales cuando los textos completos no eran accesibles; las fuentes no demuestran experimentalmente que nuestra combinación de formatos sea superior. No se efectuó ensayo aleatorizado, análisis formal de coste por usuario ni certificación de normas. El marco de fuentes es principalmente internacional; aplicación fiscal, laboral, contractual y de protección de datos en cada jurisdicción debe revisarse por especialista según jurisdicción y situación real. En particular, NIIF para las PYMES no se declara normativa obligatoria universal.

**Limitaciones técnicas:** la documentación oficial de Obsidian confirma las propiedades y los links `^` propios del producto [S28,S29]; la documentación de Codex explica reglas AGENTS.md [S30], pero no demuestra que todas las aplicaciones de IA tengan acceso a historiales, adjuntos o el mismo comportamiento. Manifest JSON válido significa estructura correcta, no comprensión semántica, actualidad de precios o permisos efectivos. No se probó ingestión real multi-harness en esta entrega.

**Próximos tests empíricos recomendados:** 6 pequeñas empresas con distinta tipología; un usuario sin formación técnica que ejecute solo P00; prueba ciega de cotización con borrador/contrato; corrección que modifica 4 documentos; una reanudación cross-model; privacidad sobre cuenta restringida; extracción por dos parsers, con medida de precisión de citas y tasas de errores materiales (no «evaluación subjetiva de completitud»). Para aprobar v1.0 serían necesarias actas de esos tests, casos negativos y correcciones.

## 13. Hipótesis y decisión de cierre

**Conclusión del diseño:** elegir **explicaciones empresariales operables** antes que una carpeta perfecta y garantizar identidad, procedencia, estados y temporalidad sin obligar al dueño a gestionar YAML. Se sostiene por convergencia de estrategia, flujo de conocimiento, process management y autoría estructurada [S01,S03,S10,S22,S26,S27]. **No está probado** que siete familias y siete tipos condicionales sean la configuración óptima universal; se propone como candidata escalable que debe ser refutada o mejorada en pruebas reales.

## 14. Fuentes consultadas, relevancia y límites de acceso

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

