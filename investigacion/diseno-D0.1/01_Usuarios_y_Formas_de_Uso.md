# 01 — Usuarios y formas de uso (diseño de experiencia, no interfaz aprobada)

## Persona principal: propietario multitarea de negocio

Dirige su empresa, conoce partes de la operación a profundidad, tiene conocimiento disperso y delega mediante IA lo que antes hacía con colaboradores o herramientas aisladas. Es experto en el negocio, **no necesariamente en tecnología**. Puede operar productos y servicios simultáneamente, manejar excepciones comerciales y tener documentos incompletos. No desea responder cuestionarios extensos sobre lo que ya explicó en chats u otros sistemas.

## Personas adyacentes, no confundidas con el propietario

- **Copropietario o decisor:** puede compartir responsabilidades sin compartir todas las facultades de aprobación.
- **Empleado/colaborador que ejecuta:** conoce detalles de práctica, calidad y excepciones; su testimonio no necesariamente autoriza políticas.
- **Consultor/implementador:** instala/configura para una empresa distinta; no adquiere automáticamente acceso a datos sensibles.
- **Agente/chat de IA:** instrumento, con capacidades y permisos reales distintos; no equivale a una persona jurídica ni a un empleado autorizado.

## Seis modos de usar el producto

| Modo | Punto de entrada | Propósito | Qué debe comprobar el sistema |
|---|---|---|---|
| M1 — Instalación asistida | Tutorial → repo → Codex | Configurar sin conocimientos técnicos | Entorno, permisos, privacidad, respaldo, resultado real y reversión |
| M2 — Conversación cotidiana | Chat/agente | Preguntar, orientar, iniciar un trabajo | Contexto suficiente, fuente de autoridad, acceso y límite de herramientas |
| M3 — Navegación visual | Obsidian Inicio/Bases/links | Ubicar ofertas, proyectos, áreas y pendientes | Vistas derivadas, información no duplicada y enlaces válidos |
| M4 — Trabajo y seguimiento | Proyecto/tarea/reunión | Registrar ejecución, tiempo, responsables y acuerdos | Separar planeación, evento, aprobación y resultado |
| M5 — Cambio de negocio | Oferta, proceso, estrategia | Evolucionar condiciones, metodología o productos | Impactos, versiones, fuentes, aprobaciones y vigencia |
| M6 — Intercambio entre asistentes | Codex/Claude/chat sencillo | Portar contexto y devolver entregables | Paquete mínimo, restricciones, referencias, revisión y reintegración |

## Recorrido A — De cero a primera respuesta útil

1. Dueño encuentra video/tutoría; descarga o clona el repositorio y pide «ayúdame a instalarlo».
2. Asistente inspecciona sistema operativo, dependencias, carpeta elegida y permisos reales **sin cambios automáticos silenciosos**.
3. Muestra plan de instalación y solicita autorización para escribir/instalar. Distingue código distribuido de bóveda privada de empresa.
4. Pregunta qué fuentes existentes se pueden consultar y detecta qué ya está documentado. Evalúa K1–K4.
5. Crea una experiencia inicial simple con identidad/proyecto o pregunta útil, y deja claro qué es parcial.
6. Demuestra al dueño una consulta real con fuentes y un cambio propuesto sin modificar autoridad automáticamente.
7. Entrega verificación, respaldo, límites, manual de continuidad y modo seguro de actualización.

**Resultado de aceptación:** propietario no técnico puede reencontrar y continuar un dato conocido sin repetir toda la entrevista; lo que no se pudo verificar aparece como pendiente.

## Recorrido B — Una nueva oferta basada en trabajo anterior

El dueño pregunta: «Quiero lanzar una consultoría combinada con herramientas que ya usamos». El sistema recupera estrategia, portafolio, casos, procesos, evidencia comercial y capacidad operativa. Distingue que **usar una herramienta para prestar consultoría no la convierte en una licencia vendida**. Propone oferta, condiciones, dependencias y plan; pide autorización comercial antes de publicarla o presentarla como vigente.

## Recorrido C — Una pregunta sencilla que cruza departamentos

«¿Qué debemos entregar a este cliente el viernes y quién lo aprobó?». Respuesta compuesta desde acuerdo vigente para ese cliente, proyecto, tareas, decisiones, personas autorizadas y calendario operativo. Debe distinguir fecha de trabajo de fecha de entrega, y no convertir el plan en ejecución verificada.

## Recorrido D — Aprendizaje desde la operación

Una reunión produce cambios de alcance, seguimiento y nuevo conocimiento. El sistema preserva acta/episodio y origen; enlaza proyecto, cliente, participantes y tareas, y **propone** cambios a una política general solo si el episodio tiene relevancia sustentada. No reescribe las reglas por una sola anécdota.

## Recorrido E — Uso desde chat sin agente instalado

Un chat sin acceso al disco recibe un paquete autorizado con resumen, fuentes y límites, produce recomendaciones o un archivo de cambios, y el dueño lo entrega de vuelta a Codex. El sistema no supone que ese chat vio documentos que no se le compartieron, ni que puede escribir en Obsidian.

## Diseño de experiencia que permanece abierto

- ¿Primera pantalla Obsidian, chat conversacional, híbrido o asistente guiado?
- ¿Cuánta configuración/entrevista hace el propietario antes de una primera consulta útil?
- ¿Qué puede instalarse y funcionar sin internet o sin cuenta en servicios externos?
- ¿Cómo se diferencian vistas de propietario, ejecutor y tercero sin simular seguridad con carpetas?
- ¿Cómo evitar que la complejidad de los agentes se transforme en trabajo técnico para el dueño?

**Inspiración, no obligación:** la simplicidad inicial de VID-002 y VID-005 puede convivir con profundidad empresarial que no se ve de inicio. No convertir su estructura de tres carpetas en restricción universal.
