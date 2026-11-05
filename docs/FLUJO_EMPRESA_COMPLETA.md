# Flujo de conocimiento para una empresa completa

**Estado:** contrato de trabajo candidato para pilotos. Complementa vNext-1.0R, el catálogo D01–D07/X01–X07 y la especificación de red 0.4. No constituye una plantilla empresarial universal ni implica que todas las fuentes estén disponibles.

## Resultado buscado

El dueño entrega a Codex el repositorio y una tarea empresarial. Codex prepara una bóveda privada, recupera fuentes autorizadas, extrae criterio, cataloga afirmaciones, redacta piezas con autoridad y las usa para decidir, vender, operar, delegar, cuidar caja y aprender. Una nota sólo cuenta como avance si otra sesión puede localizarla, distinguir su estado y utilizarla correctamente en una tarea. El dueño no tiene que diseñar carpetas, YAML ni un organigrama ficticio.

## Dos puntos de entrada

- **Empresa nueva:** `ce-instalacion` comprueba equipo, permiso y destino; crea instancia fuera de Git, abre Inicio/Bases; `ce-desarrollo-empresa` inicia el mapa de cobertura. La instalación no equivale a empresa documentada.
- **Instancia existente:** conserva IDs, fuentes, notas, versiones y personalizaciones; lee estado y continuidad, vuelve al original pertinente, detecta huecos por tarea y continúa. Nunca reejecutar `crear` ni importar automáticamente las plantillas.

Si el dueño prioriza **completar el producto antes de intervenir la instancia activa**, el orden es producto general → pruebas con empresa ficticia y copia aislada autorizada → paquete sin datos privados → conciliación de la bóveda activa → tareas y aceptación del dueño. El paquete y la copia prueban código, estructura y parte de la recuperación; no certifican Obsidian GUI ni fidelidad empresarial aceptada. La distinción metodológica entre conocimiento útil para personas y representación en bóveda es una exigencia del contenido, no una entrevista o entrega duplicada obligatoria.

## 1. Orientación y adquisición

Preguntar primero qué decisión o trabajo quiere mejorar la persona, cómo funciona hoy y qué ya existe. Recuperar sólo fuentes admisibles y autorizadas: conversaciones originales, personas que ejecutan, propuestas/acuerdos, registros operativos, CRM, caja, materiales de marca, mediciones y sistemas fuente según aplique. Registrar ubicación estable, permiso, sensibilidad, fecha del hecho y lectura completa/parcial. Si hay conflicto, conservar ambas versiones y su ámbito. No copiar indiscriminadamente originales a Git ni a la bóveda.

Para cada hallazgo, clasificar: declaración del decisor, criterio del ejecutor, hecho del sistema, observación de cliente, inferencia del agente o hipótesis. Separar `usado`, `ofrecido`, `cotizado`, `aceptado`, `contratado`, `entregado`, `facturado` y `cobrado`. Si falta el registro correspondiente, escribir `no acreditado` o `dato no disponible`, nunca `0`: la ausencia de evidencia no demuestra un valor cero. Aplicar K1/K2/K3/K4 antes de preguntar y dejar en plan o CONTROL un rastro breve para cada necesidad material: clase, fuente leída o pendiente y próxima acción. La clasificación sirve a la tarea y no requiere cuatro casillas por documento; máximo dos preguntas K1 por ronda sustantiva si cambian la pieza actual.

## 2. Mapa de cobertura por tarea, no siete archivos forzosos

| Familia | Uso que debe permitir | Fuentes orientativas y prueba |
| --- | --- | --- |
| D01 Dirección | Elegir entre oportunidades y explicar renuncias | Dueño/decisiones; comparar dos oportunidades reales |
| D02 Mercado, clientes y marca | Preparar conversación y mensaje para una situación observada | Voz de clientes, episodios, CRM, activos aprobados; no inventar segmentos |
| D03 Portafolio y comercial | Saber qué ofrecer y qué condición se puede cotizar hoy | Oferta con aprobador/vigencia y propuestas; no generalizar precio particular |
| D04 Ejecución y calidad | Hacer y transferir un trabajo con excepciones y aceptación | Ejecutor, proceso, proyectos; probar una tarea y una excepción |
| D05 Economía y caja | Decidir precio/capacidad con costos y flujo sustentados | Contabilidad, bancos, costos; no confundir cotización con cobro |
| D06 Personas y facultades | Saber quién decide, ejecuta y autoriza | Personas reales, delegación, acuerdos; no crear puestos ficticios |
| D07 Riesgos y compromisos | Actuar ante dependencia, permiso u obligación material | Contrato, norma, incidente, proveedor; distinguir riesgo de obligación |

Cada familia puede quedar `sin_fuente`, `parcial`, `suficiente_para_tarea` o `no_aplica` con razón y tarea. `Suficiente` cambia si cambia la decisión. El mapa de cobertura lista enlaces a lo ya existente y la siguiente prioridad; no crea documentos vacíos ni bloquea trabajo útil hasta completar siete familias.

## 3. Distribuir y desarrollar

Cuando una conversación mezcle asuntos, usar `ce-arquitectura-conocimiento` y `plan-conocimiento` en sólo lectura. Para cada afirmación escoger un dueño canónico: fuente, bloque D, expediente X o nota tipada. Separar ofertas, servicios, procesos, proyectos, casos, reuniones, decisiones, tareas y recursos por identidad y mantenimiento; no por cada sustantivo. Los D/X sintetizan y enlazan sin duplicar precios, obligaciones o procedimientos que cambian por separado. Proponer relaciones tipadas con ámbito/fuente; un enlace no demuestra contratación.

Con `ce-documentacion`, producir texto empresarial con situación, mecanismo, decisiones, ejemplo, excepciones y uso. CONTROL separado conserva procedencia, estado, vigencia, permisos y preguntas que alteran una decisión. Revisión humana comprueba que el texto representa el negocio y sirve para hacer algo. Guardar en borrador o `en_revision`; para cambiar algo previamente autorizado usar diff, SHA, respaldo, impacto y decisión.

## 4. De conocimiento a trabajo repetible

Cada capacidad tiene un ciclo: **fuentes y criterios aprobados → tarea concreta → borrador/acción propuesta → revisión del dueño → corrección localizada → historial → siguiente ejecución**. La corrección se registra con fecha, fuente y alcance; no se convierte una preferencia casual en regla universal. Una segunda sesión recupera el original y el criterio vigente y explica por qué cambió. `continuidad` orienta, nunca reemplaza fuentes.

Para trabajo recurrente, definir disparador, fuentes accesibles, producto de salida, límite de búsquedas/tiempo, persona que revisa, presupuesto y condición para detener. Si el entorno dispone de tareas programadas, sólo configurarlas cuando el dueño pida programación y apruebe destino, frecuencia, acceso y costo. Sin esa capacidad, dejar una receta manual. Ningún borrador se publica, envía o cambia permisos por sí solo.

## 5. Marketing integrado con el resto de la empresa

Activar `docs/MARKETING_EMPRESARIAL.md` para marca, mensajes, investigación, contenido, campañas o demanda. Marketing toma hechos de D01, audiencia y lenguaje de D02, promesas y condiciones vigentes de D03, capacidad de entrega de D04 y restricciones/costos de D05–D07. Devuelve preguntas de clientes, hipótesis y resultados a esas familias con fuente y fecha. Una guía visual o brand kit aprobado ayuda a la coherencia, pero no acredita demanda, ventas ni desempeño. El flujo produce ideas originales y borradores revisables, no una fábrica automática de publicaciones.

## 6. Comprobación y cierre de una ronda

Comprobar `estado` y `validar`; navegar en GUI cuando se pueda; recuperar una respuesta por ámbito, fecha y fuente; hacer una pregunta negativa que deba conservar incertidumbre. Registrar qué archivo/ID cambió, qué tarea resolvió, qué decisión confirmó el dueño y qué queda abierto. Un informe de integridad no sustituye la prueba de utilidad. El producto multiempresa exige además segunda instalación y aislamiento de datos.
