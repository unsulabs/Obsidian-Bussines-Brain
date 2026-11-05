---
name: ce-revisar-antecedentes
description: "nueva fuente, categoría/alias, corrección, cambio de vigencia/permiso, idea retomada o fallo de respuesta."
---

# ce-revisar-antecedentes

Lee el [contrato común](../ce-banco-transcripciones/references/contrato-comun.md) para estados, permisos, contexto y disponibilidad.

- **Trigger:** nueva fuente, categoría/alias, corrección, cambio de vigencia/permiso, idea retomada o fallo de respuesta.
- **Inputs:** evento versionado, universo elegible del catálogo, índice con watermark, análisis nuevo y contexto canónico. Leer candidatos con vecinos; ampliar a conversación completa cuando afecte significado.
- **Outputs:** relaciones candidatas con dos extremos citados, conflictos, dependencias/impactos, propuestas de actualización, cursor de barrido y lista explícita de pendientes/inaccesibles.
- **Errores:** `INDEX_STALE`, `ANTECEDENT_UNAVAILABLE`, `SCOPE_MISMATCH`, `UNSUPPORTED_PREDICATE`, `SWEEP_INCOMPLETE`. Buscar sin resultados no prueba inexistencia.
- **Gate:** una categoría nueva encuentra un antecedente antiguo sin compartir vocabulario exacto en el ensayo diseñado; conflicto queda abierto si no hay autoridad para resolver. Sólo afirmar barrido completo cuando cada entrada del snapshot tenga resultado; nuevas entradas abren delta.

## Ejecución

Construye universo elegible por empresa, finalidad, audiencia, sensibilidad y permisos actuales antes de recuperar texto. Incluye investigación, fuentes y asuntos secundarios, no sólo D/X o títulos. Busca términos/alias/contextos, lee pasajes vecinos y amplía a original completo cuando cambie significado. FTS y coincidencias literales son candidatos, no juicio semántico ni prueba de exhaustividad.

Cada relación requiere pasajes originales verificados de ambos extremos, dirección, ámbito, tiempo, predicado, razón y estado editorial. No convertir coincidencia temática en causalidad, ni fecha reciente en autoridad. Contradicción queda abierta hasta decisión autorizada; retoma/precisa permanecen propuestas privadas si el vocabulario de destino no los admite.

Retomar cursor por TR-ID y snapshot con resultado por entrada; entradas posteriores forman delta. No afirmar barrido completo mientras haya pendientes. Propaga corrección/revocación/rechazo a dependientes registrados y marca desconocidos: no reintroducir redacción rechazada desde resúmenes, web o citas circulares. Usa [ce-cambios](../ce-cambios/SKILL.md) sólo para cambios editoriales con interfaz comprobada.
