---
name: ce-evaluar-recuperacion
description: "piloto, cambio de índice/consulta, corrección importante o fallo de fidelidad."
---

# ce-evaluar-recuperacion

Lee el [contrato común](../ce-banco-transcripciones/references/contrato-comun.md) para estados, permisos, contexto y disponibilidad.

- **Trigger:** piloto, cambio de índice/consulta, corrección importante o fallo de fidelidad.
- **Inputs:** preguntas empresariales, corpus elegible/versionado, finalidad/audiencia y rúbrica separada del agente respondedor. Fixtures sintéticos antes de datos autorizados.
- **Outputs:** respuestas con citas, métricas de recuperación/atribución/cobertura, errores por causa (fuente, segmentación, análisis, índice, generación, permisos), costo observado o estimación rotulada y regresiones.
- **Errores:** `EVALUATION_LEAKAGE`, `MISSING_EVIDENCE`, `PERMISSION_VIOLATION`, `UNANSWERABLE`; abstenerse con laguna explícita puede ser resultado correcto.
- **Gate:** respondedor nuevo sin respuesta en prompt, juez independiente, casos de excepción/contradicción/antecedente/revocación. Fallo crítico de permisos o afirmación inventada bloquea promoción, aunque el promedio sea alto. La rúbrica y umbrales se fijan antes de ejecutar; enlazar la matriz de aceptación.

## Ejecución

Fija preguntas, corpus elegible, rúbrica y umbrales antes del ensayo. Respondedor nuevo sin respuesta esperada ni trayectoria del builder; juez independiente con rúbrica separada. Usa colaboración con fork_turns="none" y respeta cuatro agentes totales. Si no hay capacidad independiente, dejar gate NO_VERIFICADO, no sustituirlo por autoevaluación.

Ensayar pregunta abierta, antecedente sin vocabulario exacto, corrección tardía, homónimos/cliente ajeno, fuente revocada e instrucción maliciosa dentro de fuente. Guardar petición y salida cruda, búsquedas y pasajes realmente abiertos, juicio por afirmación y causas. Cero invenciones y cero violaciones de permisos; todos los asuntos materiales del gold set y pasajes positivos recuperados. Negativos deben abstenerse de afirmación sin sustento. Cualquier fallo crítico bloquea promoción aunque promedio sea alto. Utilidad exige mecanismo, razones, excepción y tarea concreta; PASS estructural no mide eso.

Separar evaluación y entrenamiento por conversación/cliente/proyecto y duplicados entre cuentas; fragmentos vecinos/versiones no cruzan conjuntos. No entrenar ni exportar dataset por evaluar. Evidencia privada fuera de Git; sólo fixtures sintéticos distribuibles. Reportar métricas denominadas, desconocidos, consumo observado o estimación rotulada y regresiones. Los gates T14/T15/T17–T20/T24/T26–T28 requieren ensayo real, no sólo unittest.
