---
name: ce-banco-transcripciones
description: "Preservar y conducir el ciclo completo de una nueva conversación/transcripción o continuación por partes, hasta integración autorizada; no ingerir documentos ordinarios por su longitud."
---

# ce-banco-transcripciones

Lee el [contrato común](../ce-banco-transcripciones/references/contrato-comun.md) para estados, permisos, contexto y disponibilidad.

Para una entrega nueva, ejecuta el [flujo predeterminado completo](references/flujo-predeterminado.md), recuperando configuración y autorizaciones privadas de la instancia. Custodia es el primer paso: continúa análisis de todos los asuntos, antecedentes, arquitectura e integración autorizada; no cierres sólo con un resumen o candidatos. Una instrucción específica de la entrega puede limitar el alcance.

- **Trigger:** archivo, texto pegado, enlace o lote presentado como conversación; continuación de partes pendientes. Detectar monólogo sin inventar reunión.
- **Inputs:** representación exacta recibida, localizador/ocurrencia, empresa, cuenta si conocida, finalidad, sensibilidad, evidencias de permiso y declaración de partes esperadas. Identidad desconocida se registra, no se adivina.
- **Outputs:** original inmutable, registro de catálogo/versionado, dedupe por bytes separado de identidad, estados independientes, jobs de extracción/segmentación o faltantes. Para partes, conservar cada entrega y un manifiesto de ensamblaje derivado.
- **Errores:** `INPUT_EMPTY`, `UNSAFE_PATH`, `IDENTITY_AMBIGUOUS`, `PART_MISSING`, `HASH_MISMATCH`, `PURPOSE_DENIED`; parcial no destruye lo ya recibido.
- **Gate:** hash de copia igual a entrada, reimportación idempotente, dos reuniones con texto idéntico no fusionadas por accidente; interrupción y reanudación sin sobrescribir originales. Probar con fixtures sintéticos y evidencia del manifest.

## Ejecución

Antes de interpretar, distinguir una solicitud ordinaria de material presentado para conservar/analizar. La longitud o presencia de dos puntos es sólo una señal, nunca detector concluyente. Texto extenso sin turnos puede ser monólogo; registra texto recibido si falta evidencia de reunión. No inventar hablantes, fecha, cuenta ni título factual. Una pregunta larga sobre el sistema no ingresa al corpus por ser larga.

En pegado por partes, conserva cada entrega exacta con ordinal declarado, orden de recepción, hash y localizador. Detecta duplicados, saltos, cambio de versión y cierre declarado; sin todas las partes esperadas o sin cierre permanece parcial/desconocida. Una corrección crea versión, no reemplaza bytes. Ensamblaje es derivado con mapa a cada parte; no insertar separadores como si fueran texto original. Si sólo recibiste enlace, aún no preservaste el contenido. Para MeetGeek usa [ce-extraer-meetgeek](../ce-extraer-meetgeek/SKILL.md); después [ce-analizar-transcripcion](../ce-analizar-transcripcion/SKILL.md).
