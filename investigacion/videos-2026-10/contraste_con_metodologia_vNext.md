# Continuidad obligatoria con la metodología de documentación empresarial vNext-1.0R

**Componentes publicados de referencia:**
- `metodologia/vNext-1.0R/`, guía y catálogo canónico.
- `contratos/vNext-0.9/Contrato_Traspaso_vNext.md`, versión 0.9: interfaz Paso 1→Paso 2; **no** bóveda física.
- `investigacion/diseno-D0.1/02_Capacidades_y_Cobertura.md`: criterios de diseño RQ-001 a RQ-030.

## Principios que ya existían y no debemos reiniciar

1. **Paso 1** recupera conocimiento de la empresa, fuentes y criterio experto con IA. **Paso 2** lo convierte en un cerebro navegable, consultable, actualizable y reutilizable; los tutoriales pertenecen a investigación para el Paso 2, no invalidan el Paso 1.
2. Los D01–D07 son familias de cobertura; los X01–X07 son expedientes condicionales. **No** equivalen a catorce archivos automáticos ni a una lista de catorce carpetas. No volver a 45/64 activos obligatorios.
3. El método K1–K4 separa juicio del experto, hechos de sistemas, conocimiento no disponible y contenido no necesario en la tarea. Una vista de tareas no sustituye esas fuentes.
4. Estados independientes: editorial, cobertura por pregunta, estado de cada afirmación y vigencia, más clase de evidencia, permisos y restricciones. No usar un único `status` genérico para todo.
5. Autoridad por asunto + entidad + contexto + fecha + origen + ámbito. No resolver mediante archivo más reciente ni el dashboard de quien tomó notas.
6. Un `doc_id` y un `block_id` deben sobrevivir al cambio de nombre/ruta; una relación tipada conserva procedencia. La decisión sobre wikilinks, Bases o plugin se toma posteriormente.
7. El contrato exige pruebas de estructura, referencias, semántica, tiempo, permisos, recuperación y reanudación; instalar Obsidian o visualizar Graph no es cumplirlas.

## Qué agrega la investigación de videos, sin competir con lo anterior

| Nuevo patrón práctico | Evidencia | Posible relación con vNext | Decisión pendiente |
|---|---|---|---|
| Primer dashboard simple | VID-002/H-010 a H-011, VID-005 | Vista de acceso a D01–D07 y X activos | Interfaz de inicio, no estructura de datos |
| Tareas con fecha de ejecución y vencimiento | VID-001/H-004 | D04/X04 y compromisos, no D05 contabilidad | Modelo de tarea, plan y obligación |
| Reunión alimenta proyecto y subproyecto | VID-003/H-021 a H-023 | X04 (caso/episodio), X03 (cuenta) | Umbral para crear entidad reunión independiente |
| Responsable y participante no son la misma relación | VID-003/H-022 a H-023 | D06, X03/X04 | Roles y autoridad según contexto |
| Contexto de agentes y skills | VID-004/H-035 a H-037 | Contrato Paso 2, `restrictions`, `retrieval_tests` | Abstracción portátil a chats/agentes |
| Propuesta IA va a revisión | VID-004/H-030 | Cuatro ejes y gates de autoridad | Implementación concreta de revisión autorizada |
| Vistas y plugins sobre Markdown | VID-001, VID-005 | Vista derivada del conocimiento | Estrategia de compatibilidad/migración |

## Prueba crítica de continuidad

Una nueva sesión con Codex debe poder recibir documentación de Paso 1 y reconstruir una respuesta como: «¿Cuál es la oferta vigente, qué condiciones aplican a esta cuenta, cuál fue la excepción firmada y qué cambió ayer?». Para hacerlo debe respetar `authorities`, `sources`, `blocks`, `restrictions`, `valid_from/valid_to`, `recorded_at` y la política de acceso. Los tutoriales facilitan navegación, pero **ninguno** prueba esa consulta.

**Resultado de esta revisión:** propuesta de continuidad, pendiente de revisión/aceptación del usuario. Ningún archivo vNext fue editado.
