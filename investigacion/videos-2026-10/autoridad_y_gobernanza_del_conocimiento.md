# Autoridad del conocimiento y permisos: contrato funcional a estudiar

Este documento **no rediseña** el contrato vNext: traduce sus obligaciones a preguntas y casos que los videos no resolvieron.

## Distinciones no negociables antes de escoger plugins

- **Lugar de almacenamiento ≠ autoridad.** Una nota puede mostrar la tarifa de un servicio pero la tarifa vigente puede tener autoridad en un registro comercial específico con fecha efectiva; no duplicar condiciones en cinco pantallas editables.
- **Enlace ≠ relación semántica.** Una persona citada en una reunión no es por ello la responsable de todas sus tareas. Un instrumento de IA utilizado para prestar un servicio no se convierte en producto vendido por ese solo uso.
- **Fecha de edición ≠ fecha efectiva.** Una nota corregida hoy puede declarar que una condición cambió hace semanas. Mantener fecha válida y fecha de registro.
- **Resumen ≠ transacción.** Una nota sobre un pago recibido no sustituye banco/ERP/contabilidad ni evidencia de conciliación.
- **Propuesta del agente ≠ decisión autorizada.** Un agente puede recomendar, elaborar borrador y explicar impacto; las aprobaciones deben relacionarse con responsable/ámbito y registrarse.
- **Carpeta para inbox ≠ permiso.** Si un proceso o plugin tiene acceso completo a la bóveda, puede sobreescribir contenidos. Se necesitan controles de acceso reales, revisión previa y mecanismos de rollback.

## Ejercicio sintético de control por asunto

**Escenario:** Una empresa ofrece consultoría y software. El precio publicado del paquete de consultoría se revisó el 01/10, pero un contrato firmado del cliente A contiene una excepción vigente hasta diciembre. Ayer un agente generó una propuesta de nueva tarifa. Además, el cliente usa una herramienta de IA durante la consultoría, sin haber contratado licencia de esa herramienta.

Consultas que el sistema debe resolver sin contradicción:

1. ¿Cuál es el precio general aplicable hoy? Respuesta respaldada por la autoridad comercial **vigente** y fecha de validez.
2. ¿Qué precio se aplica a cliente A? Respuesta respaldada por el contrato/ámbito particular y su vigencia, sin reescribir tarifa general.
3. ¿La recomendación de ayer ya cambió el precio? **No**, salvo aprobación explícita y transición registrada.
4. ¿El cliente contrató software porque lo utilizó? **No se puede inferir**; separar usado, ofrecido, aceptado, contratado, facturado y cobrado.
5. ¿Qué documentos derivados conviene revisar tras aprobar un cambio? Identificar referencias, propuestas y comunicaciones de precio potencialmente afectadas.
6. ¿Puede un agente de marketing ver el anexo confidencial del contrato? Solo si está autorizado y conectado al sistema de la fuente, no porque haya un link en Obsidian.
7. ¿Cuál era el precio general el 30/09? Consulta histórica con fechas efectivas, no con modificación del archivo.

## Candidatos de solución, no selección

**A. Autoridad declarativa** en manifiesto/relaciones semánticas y fuentes oficiales enlazadas. **B. Autoridad federada** consultando CRM, contabilidad o contratos vivos. **C. Enfoque híbrido**, conservando en Markdown la explicación/versionado y consultando hechos transaccionales solo en sistemas de registro. Evaluar riesgo offline, caducidad, conectividad, responsabilidades y mantenimiento.

## Controles de escritura y salida a estudiar

- Ingesta de documentos, conversaciones o video a zona de revisión; extracción con fuente, fecha y ámbito.
- Diff con cambios propuestos y afectados; validación contra autoridad existente.
- Identificación de permisos por entidad y bloque cuando haga falta.
- Aprobación humana en reglas comerciales, contratos, prioridades o difusión externa; rollback verificable.
- Respuesta del agente con `fuente`, `válido_para`, `fecha`, `estado`, `limite` y solicitud de confirmación cuando exista conflicto.
- Logs de quién propuso, autorizó y materializó el cambio, sin incluir secretos.

**No se implementa ni presupone verificado ninguno de estos controles.** Vinculado a RQ-006, 013, 016–018, 024–027 y al contrato vNext.
