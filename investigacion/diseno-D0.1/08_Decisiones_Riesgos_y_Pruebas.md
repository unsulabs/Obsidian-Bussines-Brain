# 08 — Registro de decisiones abiertas, riesgos y pruebas

**Ninguna** de las alternativas técnicas aquí está aprobada. El propietario aprobó el proceso de consolidación, no sus decisiones futuras. No cerrar preguntas por conveniencia de programación.

## Decisiones pendientes (orden por dependencia, no por urgencia personal)

| ID | Decisión | Alternativas de análisis | Prueba o evidencia exigida |
|---|---|---|---|
| DEC-01 | Experiencia inicial del propietario | Chat guiado / Obsidian Inicio / híbrido | Persona sin experiencia configura y encuentra primera respuesta sin intervención experta |
| DEC-02 | Representación de entidades | Nota / bloque / registro externo / híbrido | Mismo cliente en tres roles y dos proyectos; no duplicar ni perder historia |
| DEC-03 | Ontología y relaciones | Properties tipadas / índice semántico / otro modelo | `contrata` ≠ `participa` ≠ `paga`; fuente y recuperación correctas |
| DEC-04 | Autoridad en sistemas externos | Referencia federada / réplica controlada / dato local | Contrato distinto de oferta y finanzas con corte temporal |
| DEC-05 | Motor de vigencia | Fechas/estado explícito / revalidación periódica / combinación | Precio caducado, acuerdo posterior y fuente inaccesible |
| DEC-06 | Edición y cambios | Borradores / diffs / registro de eventos / versionado de dominio | Dos editores, conflicto y rollback sin pérdida |
| DEC-07 | Permisos por agente | Separación OS/directorios / scopes de herramientas / infraestructura aislada | Agente sin permiso no lee ni escribe bloque restringido |
| DEC-08 | Contrato de tareas | Checkbox / TaskNotes / sistema externo / dual | Programado vs vencimiento; desinstalar plugin y consultar tareas |
| DEC-09 | Vistas Obsidian | Core nativo / plugin / híbrido | Comparar carga, mantenimiento y uso cotidiano |
| DEC-10 | Plantillas adaptativas | Clases especializadas / diálogo IA / mezclas | Producto, consultoría y empresa híbrida con estructura pertinente |
| DEC-11 | Paquetes para agentes | Export estático / consulta dinámica / herramienta local | Mismo caso por Codex, Claude y chat sin disco |
| DEC-12 | Instrucciones y skills | Archivos por harness / adaptador común / generador | Pruebas por harness, sin asumir sintaxis universal |
| DEC-13 | Instalación y permisos | Script guiado / comando Codex / asistente híbrido | Prueba limpia, consentimiento granular y error reproducible |
| DEC-14 | Integración de datos | Referencia / copia selectiva / sincronización | Sin fuga de datos ni doble autoridad; reconexión y revocación |
| DEC-15 | Versiones del producto | Core fijo + instancia / módulos y migraciones | Upgrade, rollback, recuperación, compatibilidad con extensiones |
| DEC-16 | Respaldo/sincronización | Git privado / Obsidian Sync / sistema archivo / mixto | Restauración completa sin subir secretos ni conflictos |
| DEC-17 | Criterio de cobertura | Preguntas por dominio / escenarios / matriz de evidencia | Empresa sin finanzas maduras y otra con muchos proyectos |
| DEC-18 | Umbral de autonomía | Riesgo, permisos, historia, consulta frecuente | Evitar nota por cada mención o todo dentro de una nota monolítica |
| DEC-19 | Métricas de utilidad | Tiempo a primera respuesta / precisión / continuidad / esfuerzo | Test de dueño no técnico y recuperación semántica adversarial |
| DEC-20 | Política de terceros | Solo oficial y nativo / plugins curados / catálogo opcional | Licencia, mantenimiento, seguridad, desconexión de plugin |

## Riesgos que no resuelven los videos

| Riesgo | Qué lo hace crítico | Mitigación a investigar |
|---|---|---|
| Falsa vigencia | Enlace reciente a nota antigua parece autorización actual | Fuente/ámbito/tiempo y etiqueta de revalidación |
| Falsa seguridad | Carpeta privada dentro de bóveda escribible por agente | Restricciones reales de herramientas, OS e identidad |
| Complejidad inútil | Demasiados tipos obligatorios para empresa pequeña | Onboarding progresivo, vistas por necesidad |
| Fragmentación excesiva | Nota por cada tarea/idea/episodio | Umbral de identidad y reglas de agrupación |
| Dependencia de plugin | Dejar de leer tareas sin TaskNotes | Formato durable, exportación y prueba de retiro |
| Fabricación del negocio | IA rellena departamentos, cifras, clientes y políticas | K1–K4, puertas de evidencia y aprobación |
| Mezcla de instancias | Demo/consultor/cliente comparten archivos | Aislamiento de datos y pruebas multitenancy |
| Actualización destructiva | Upgrade sobrescribe fuentes o personalizaciones | Migración reversible + snapshots + pruebas |
| Deriva semántica | Un resumen o skill sobrescribe acuerdo previo | Propuestas con diff y contraste contra fuentes |
| Brecha de privacidad | Copia de fuentes a packs externos sin autorización | Minimización, scopes, registro de destinatario |
| Confusión de resultados | Registro de tarea completada parece factura cobrada | Eventos y autoridad por dominio separadas |

## Gates de aceptación que deben sostener el proyecto

Se conservan **V1–V7 del contrato vNext**: estructura, integridad referencial, auditoría semántica, temporalidad, permisos, recuperación y reanudación. Para el repositorio instalable añadir pruebas específicas **no ejecutadas**:

- **G-INST**: propietario novato y equipo limpio, con autorización y rollback.
- **G-PLUG**: instalación, versión, dependencia y retiro de plugin sin pérdida de datos.
- **G-AGENT**: mismo caso en al menos dos agentes reales y una modalidad sin acceso directo.
- **G-CROSS**: empresa de productos y empresa de servicios/híbrida sin campos impropios.
- **G-SAFE**: fuente restringida, separación entre empresas y denegación de escritura no autorizada.
- **G-CHANGE**: cambio vigente + historial + derivados + consulta histórica.
- **G-SOURCE**: una fuente externa que cambió o es inaccesible no se da por vigente.

`NO_EJECUTADO` es un estado honesto: ninguno de estos gates se certifica por redactar este expediente.

## Regla de cierre de una decisión

Registrar: pregunta exacta; alternativas; evidencia primaria y secundaria; impacto en usuario; pros y contras; compatibilidad; prueba observada; riesgos; persona autorizada; decisión fechada; estado (`abierta`, `aprobada`, `rechazada`, `aplazada`) y condición para revisarla. Una aprobación general del proyecto no cierra DEC-01…DEC-20.
