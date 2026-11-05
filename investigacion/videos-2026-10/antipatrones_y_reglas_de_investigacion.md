# Antipatrones evidenciados o sugeridos por el análisis

| Antipatrón | Fuente o situación | Prueba de mitigación por diseñar |
|---|---|---|
| Convertir estructura inicial de 3 carpetas en ontología universal | VID-002 y VID-005 | Dos empresas con modelos y permisos distintos acceden a un Inicio igualmente sencillo |
| Tratar dos videos casi idénticos de un canal como prueba independiente | VID-002 + VID-005 | Matriz agrupa coincidencias por origen |
| Asociar por nombres iguales | VID-003 `related`, VID-004 grafo | Tipos de vínculo y entidades inequívocas; negativos de falso positivo |
| Asumir que la nota más reciente siempre tiene autoridad | Falta en cinco videos | Consulta histórica y excepciones contractuales |
| Convertir una bitácora en una tarea o viceversa | VID-003 usa checkbox para logs | Evento no se vuelve completado por marcar casilla |
| Deducir facturación de un temporizador | VID-001 | Tiempo tracked ≠ billable ≠ facturado ≠ cobrado |
| Considerar que un agente entiende por leer wikilinks | VID-004 | Benchmark de preguntas y pruebas con casos negativos |
| Escribir notas de IA directamente como política | VID-004 inbox | Propuesta, diff, permisos y aprobación separadas |
| Saturar cada nueva nota con mismo formato o demasiado detalle | VID-001 rechazo a plantilla única | Plantillas por función, evidencia y estado de aplicación |
| Afirmar que no se trabajó porque no hay registro | VID-004 reflexión sobre notas diarias | Análisis revela cobertura/fecha del período y dato faltante |
| Instalar plugins por tutorial sin verificar versiones | VID-001/TaskNotes | Versiones verificadas, compatibilidad, rollback, función nativa alternativa |
| Capturar gustos personales por conveniencia social | VID-003 CRM social | Datos mínimos, propósito y autorización; no incluir por defecto |
| Suponer que carpeta local define permisos | VID-004 inbox; Obsidian plugins | Prueba de escritura fallida y exposición no autorizada |
| Confundir la herramienta de una consultoría con la oferta contratada | Necesidad del usuario | Casos `usado` vs `contratado` con evidencia distinta |
| Embellecer graph pero no probar recuperación | Todos los ejemplos | Pruebas de consulta con autoridades, fuentes y límites |
