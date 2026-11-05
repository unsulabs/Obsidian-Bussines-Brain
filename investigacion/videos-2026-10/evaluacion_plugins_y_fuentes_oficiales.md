# Evaluación preliminar de Obsidian y plugins a partir de los videos

**Corte:** 27/10/2026. Se utilizaron páginas oficiales y repositorio público; no hay prueba de instalación en el entorno del usuario.

| Herramienta o función | Función útil | Fuente primaria de verificación | Estado para nuestro producto |
|---|---|---|---|
| Obsidian Markdown + Properties | Metadatos de notas, búsqueda, enlaces | https://obsidian.md/help/properties | Capacidad nativa documentada; diseño semántico pendiente |
| Bases (core) | Vistas filtrables, editables y agrupadas de propiedades, archivos `.base` | https://obsidian.md/help/bases | Prioridad de evaluación antes de plugins de consulta redundantes |
| Backlinks / Unlinked mentions | Menciones entrantes y posibles enlaces | https://obsidian.md/help/plugins/backlinks | Navegación, NO integridad semántica |
| Graph (core) | Red de enlaces entre notas | https://obsidian.md/help/plugins/graph | Visualización, NO relaciones tipadas validadas |
| Templates / Daily notes / Bookmarks | Captura repetible, continuidad y navegación | https://obsidian.md/help/plugins | Candidatos nativos; probar sin crear notas ficticias |
| **TaskNotes** (tercero) | Tareas como notas, Bases, kanban, agenda, calendario, tiempo, Pomodoro, optional API | https://github.com/callumalpass/tasknotes · https://tasknotes.dev/obsidian/ | Candidato opcional para tareas; no para todo el cerebro |
| Dataview (tercero) | Consultas/visualizaciones de datos de notas | VID-005 4:17; **no** se ha auditado implementación/versiones | Diferido; probar Bases antes |
| Archivos `CLAUDE.md`, `memory.md`, skills (ejemplo) | Contexto para asistente Claude | VID-004 18:48–25:19 | Patrón adaptable, **no** contrato portable automático |

## Comprobación reciente importante: TaskNotes

El tutorial VID-001 se publicó en septiembre de 2025. La documentación del producto actualmente identifica **TaskNotes 4.14.0** como versión estable, requiere Obsidian **1.12.2+** y Bases habilitado (https://tasknotes.dev/obsidian/). El plugin guarda las tareas como Markdown+YAML y define vistas mediante `.base`, según repositorio https://github.com/callumalpass/tasknotes. Tiene licencia MIT declarada por su repositorio, pero **la revisión legal del uso/distribución de cada componente** sigue pendiente. Las cifras de versión cambian: fijarlas solo en un informe con fecha de corte, no en instrucciones eternas de instalación.

El video muestra configuraciones que pueden diferir de la versión 4.14 actual. Nunca construir un instalador basándose exclusivamente en los botones de un tutorial antiguo.

### Punto de seguridad (alta prioridad)

Obsidian advierte que plugins de comunidad pueden acceder a archivos, internet e instalar programas; no tienen una separación fiable de permisos por plugin: https://obsidian.md/help/plugin-security. Esto **impide confiar** en un plugin de la bóveda como aislamiento técnico de documentos de clientes o secretos.

TaskNotes ofrece una API HTTP opcional, deshabilitada inicialmente y con autenticación documentada, pero la propia documentación técnica tiene advertencias de CORS, HTTP sin TLS y alcance de escucha que exigen pruebas específicas: https://tasknotes.dev/HTTP_API/. No habilitar API ni MCP por defecto y no suponer que basta con tener un token para una exposición segura. Tampoco permitir sincronización o apps asociadas sin revisar su tratamiento de datos.

## Lo que faltaría para decidir instalar una dependencia

1. ¿Resuelve una necesidad que la funcionalidad nativa no puede cubrir satisfactoriamente?
2. ¿Las entidades básicas siguen siendo legibles/editables si se desinstala?
3. ¿Mantiene licencia y actualizaciones compatibles con versiones del sistema del usuario?
4. ¿Es instalable y reversible con un dueño no técnico y un agente en modo guiado?
5. ¿Puede leer o enviar información confidencial fuera de la bóveda?
6. ¿La extensión administra autoridad de negocio o solo visualiza un registro? No dejarla dominar la fuente de verdad.
7. ¿Qué ocurre con varias empresas, múltiples equipos, cambios de schema y un cierre inesperado?
8. ¿La prueba con Codex verifica funcionamiento real y recuperación de datos con referencias, no solamente apertura de interfaz?

**Ningún plugin queda aprobado ni instalado por este análisis.**
