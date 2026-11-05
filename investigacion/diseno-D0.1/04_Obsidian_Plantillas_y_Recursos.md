# 04 — Obsidian, vistas, plantillas adaptativas y recursos externos

**Naturaleza:** estudio de integración, no stack aprobado. Se distingue la **experiencia visible** de la **representación confiable del conocimiento**.

## Aportación documentada de las transcripciones

| Fuente | Técnica observada en la transcripción | Valor que puede rescatarse | Cuidado o límite |
|---|---|---|---|
| [VID-001 1:26–8:12](https://www.youtube.com/watch?v=vihPqFnM0dU&t=86s) | TaskNotes; tarea como nota, atributos, fecha de trabajo distinta de fecha de vencimiento | Operación de proyectos, recordatorios y tiempo | Plugin opcional, no autoridad comercial o financiera |
| [VID-001 12:00–25:34](https://www.youtube.com/watch?v=vihPqFnM0dU&t=720s) | Agenda, calendario, Kanban, filtros, tracking y Pomodoro | Vistas funcionales para quien ejerce varios roles | Versiones/dependencias del tutorial deben reconfirmarse |
| [VID-002 0:00–3:26](https://www.youtube.com/watch?v=uclyVDxJeeY) y [VID-005 0:00–2:10](https://www.youtube.com/watch?v=pJSWJaLQtG4) | Dashboard, proyectos y biblioteca de recursos en entrada simple | Reducir carga inicial para dueño no técnico | Dos videos similares del mismo canal; no prueban tres carpetas universales |
| [VID-003 2:09–20:48](https://www.youtube.com/watch?v=Fzy6BmHWNRQ&t=129s) | Proyecto padre/hijos, empresa, reunión, personas, tareas y notas de trabajo | Relación contextual recuperable, expedientes operativos | `up` y `related` no definen tipo de vínculo, autoridad ni permisos |
| [VID-003 25:29–32:20](https://www.youtube.com/watch?v=Fzy6BmHWNRQ&t=1529s) | Continuidad desde diario a proyectos y bookmarks | Encontrar conocimiento por episodio, no solo carpeta | Uso indiscriminado de diarios puede fragmentar fuentes |
| [VID-004 3:54–18:17](https://www.youtube.com/watch?v=w1r4ItfXNh0&t=234s) | Estrategia enlazada con notas diarias, MOCs y revisión periódica | Interrogar progreso y coherencia entre estrategia y ejecución | La ausencia de nota no demuestra que no hubo trabajo |
| [VID-004 8:48–9:34](https://www.youtube.com/watch?v=w1r4ItfXNh0&t=528s) | Bandeja de sugerencias para agentes en lugar de cambios directos | Revisiones humanas y separación de propuestas | La carpeta no es seguridad técnica por sí sola |
| [VID-004 18:48–27:30](https://www.youtube.com/watch?v=w1r4ItfXNh0&t=1128s) | Archivo de instrucciones, memoria ligera, skill de revisión CEO | Contexto y rutinas específicas para IA | Convenciones CLAUDE.md no son universalmente compatibles |

**Nivel de evidencia:** transcripción extraída con marcas de tiempo; no audición visual de cada configuración, ni reproducción de plugins sobre máquinas destino.

## Capacidades oficiales Obsidian a estudiar

| Tecnología | Función aspirada en el producto | Regla de independencia |
|---|---|---|
| Markdown y archivos locales | Contenido duradero y portable | No cargar secretos en texto libre |
| Properties | Metadatos tipados y filtros | ID y significado no dependen del título/ruta |
| Bases | Vistas y consultas de notas/properties | Una vista no sustituye el sistema fuente |
| Wikilinks y Backlinks | Navegación bidireccional | Un link no implica relación tipada aprobada |
| Graph | Explorar red de enlaces | No se debe confundir estética del grafo con recuperación confiable |
| Canvas | Representar escenarios o mapas | Usar vista derivada, no duplicar verdades |
| Templates | Repetir estructura adecuada por tipo | No introducir encabezados idénticos en toda clase documental |
| Search / Bookmarks / Daily notes | Acceso rápido y continuidad | Preferir recuperabilidad por pregunta, no solo palabra clave |

Fuentes oficiales para verificación técnica al diseñar: [Obsidian Help](https://help.obsidian.md/), [Obsidian Developer Docs](https://docs.obsidian.md/Home). La disponibilidad y semántica concreta se confirmarán contra versiones actuales antes de implementar.

## Evaluación de plugins (TaskNotes y otros)

Antes de recomendar o empaquetar un complemento:

1. Confirmar nombre exacto, repositorio original, autor, licencia, versiones, dependencias y compatibilidad con el Obsidian objetivo.
2. Identificar qué datos lee/escribe, qué privilegios requiere, si registra en formato portable y cómo se recupera información sin él.
3. Comparar capacidad nativa, solución existente y código propio con el mismo caso práctico.
4. Comprobar instalación, operación, desinstalación, backups, migración y errores en máquina de prueba.
5. Explicar al dueño por qué se incorpora, qué valor añade y qué ocurre si falla o deja de mantenerse.

**Candidato destacado:** TaskNotes para tareas/agenda/tiempo. **No aprobado** todavía; contrato propio de tarea y exportación agnóstica deben discutirse primero. **Evitar** duplicar sistemas de tareas y contextos sin un mecanismo de conciliación.

## Plantillas adaptativas: diseño por clases, no formulario universal

Una plantilla adaptativa debe responder, para cada operación:

- **Qué clase de conocimiento se está creando** y cómo distinguirla de otra cercana.
- **Cuándo hay identidad independiente** (nota, bloque o referencia a sistema externo).
- **Qué datos ya existen** y dónde están las fuentes; aplicar K1–K4 antes de preguntar.
- **Qué propiedades mínimas son realmente necesarias** para esa clase, qué es opcional y qué no aplica.
- **Qué relaciones son posibles** y por qué, con fuente/contexto.
- **Qué reglas requieren autoridad** y cómo separar propuesta de aprobación.
- **Qué preguntas debe poder responder** y qué falta para considerarlo suficiente.
- **Qué cambia si la empresa tiene productos, consultorías, servicios, proyectos o mezcla**.

Ejemplos para pruebas de adaptación:

- **Nueva oferta de consultoría:** alcance, modalidad, condiciones, exclusiones, criterios, aprobador comercial; la herramienta utilizada se registra como dependencia, no se factura automáticamente como licencia.
- **Reunión en proyecto:** fecha, participantes y roles, acuerdos propuestos, decisiones efectivamente aprobadas, acciones, prueba, relación con uno o más proyectos.
- **Incidente de entrega:** proyecto, actividad, evidencia, impacto, acción correctiva, posible mejora a procedimiento. Una incidencia no crea política por defecto.
- **Decisión estratégica:** alternativas, renuncia, facultad, fecha de vigencia, efecto, revisión; no exige igual estructura que un contrato.

## Vistas iniciales (candidatos de diseño, no carpetas)

**Mínimo del primer día:** identidad de empresa, una pregunta útil, lo que está activo y pendientes de incorporación. **Con el crecimiento:** dirección, negocio/ofertas, cliente/oportunidad, proyecto/tarea, recursos, finanzas, decisiones, fuentes y herramientas; rutas de navegación generadas desde lo que realmente exista, sin mostrar decenas de paneles vacíos.

## Antipatrones específicos

- Instalar 20 plugins por atractivo visual y convertirlos en requisitos de entrada.
- Usar un campo `status` universal en vez de estados específicos y cuatro ejes del contrato.
- Una carpeta por cada departamento (o una nota por cada concepto) por simetría.
- Importar una bóveda comercial de terceros sin revisar licencia, contenido de prueba y seguridad.
- Confundir la búsqueda Graph con un grafo semántico probado.
- Convertir el diario privado del propietario en fuente autoritativa sobre finanzas o contratos.
