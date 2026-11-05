# 10 — Casos empresariales de prueba: positivos, negativos y de continuidad

Todos son **escenarios propuestos, no ejecutados**. Su función es demostrar qué debe resolver la arquitectura. No son datos reales ni afirmaciones sobre empresas existentes.

| ID | Entrada del empresario | Recuperación y relaciones indispensables | Respuesta válida y fallos a rechazar |
|---|---|---|---|
| T-01 | «¿Qué empresa somos y cuál es nuestra prioridad este trimestre?» | D01, decisión vigente, objetivos, revisión, fuentes | Respuesta concreta; no inventar propósito o consejo de administración |
| T-02 | «Estoy cobrando una consultoría; usamos una herramienta con el cliente» | D03/X01, proyecto X04, sistemas X06, factura/contrato si existe | No afirmar que vendió la herramienta o una licencia por haberla usado |
| T-03 | «¿Cuál es el precio actual de este servicio para este cliente?» | Oferta general y versiones, acuerdo particular, vigencia y autoridad | Usar excepción aceptada para ese alcance; no cambiar precio global |
| T-04 | «¿Qué precio tenía este servicio hace tres meses?» | valid_from/to, recorded_at, historicals, sources | Respuesta histórica; no mostrar precio actual como si fuera anterior |
| T-05 | «Nos reunimos con dos personas para dos subproyectos» | Organización, persona, roles, reunión, proyectos, participantes, tareas | Una reunión alimenta ámbitos correctos, sin duplicar personas |
| T-06 | «Haz seguimiento a lo que quedó pendiente de la reunión» | Acuerdos vs propuestas, tareas, due/scheduled, responsable | No marcar aprobado/completado lo solo comentado o previsto |
| T-07 | «Tengo idea de una nueva oferta parecida a tres casos anteriores» | Casos situados, modelo de negocio, oferta, fuentes, resultados | Propuesta con evidencias y pendientes; no generalizar excepciones |
| T-08 | «¿Qué están haciendo hoy las personas del equipo?» | Tareas, responsables, eventos y evidencia de avance | Admitir información incompleta; ausencia de nota ≠ inactividad |
| T-09 | «¿Tenemos inventario suficiente para un nuevo evento?» | Activos, reservas, sistema oficial de stock, fecha/recursos | Revalidar disponibilidad; no inferir stock de nota antigua |
| T-10 | «En mi reporte aparece saldo X; ¿es efectivo disponible?» | D05, factura, bancos/conciliación, periodos | Separar proyección, cuenta por cobrar y efectivo confirmado |
| T-11 | «Cambia las condiciones comerciales de este servicio» | Autoridad X01/D03, aprobador, históricos, proyectos derivados | Preparar diff e impactos; no escribir sin autorización válida |
| T-12 | «Un agente me dijo que esta política ya no aplica» | Fuente original, versiones, vigencia, aprobador, contraevidencia | Conflicto o propuesta, no aceptar la voz del agente como autoridad |
| T-13 | «Dame un resumen para que otro chat redacte marketing» | Estrategia, D02, oferta y claims autorizados, permisos | Pack minimizado; sin anexar contratos/restricciones de clientes |
| T-14 | «El chat preparó un documento, incorpóralo» | Origen del archivo, revisión, entidades y autoridad previas | Ingesta como propuesta; no sobrescribir vigente automáticamente |
| T-15 | «Actualicemos el repositorio, ya hay seis meses de datos» | Instancia, versión, esquema, personalizaciones, respaldo | Upgrade reversibile; no reemplazar fuentes ni IDs de empresa |
| T-16 | «Desinstalamos TaskNotes, ¿se perdieron las tareas?» | Contrato nativo/portátil de tarea, historial, vistas | Mantener información legible y recuperar estado; si no, falla de diseño |
| T-17 | «Ayúdame a instalarlo», computadora nueva | OS, rutas, permisos, dependencias, configuración, tutorial | Plan y autorizaciones; evidencia de ejecución y rollback |
| T-18 | «Mi ChatGPT no puede leer el disco» | Context pack controlado y permisos | Reconocer limitación; no prometer recuperación automática |
| T-19 | «La fuente cambió ayer pero aquí no hay conexión» | Última verificación, método de revalidación, ámbito | Informar no verificable; jamás asegurar «vigente hoy» sin sustento |
| T-20 | «El agente de marketing quiere leer nóminas y contratos» | Roles, acceso, restricciones, minimización | Denegar fuente restringida; folder de propuestas no basta |
| T-21 | «¿Qué proceso seguimos en el caso de un incidente especial?» | D04/X02, incidente X04, excepción X07, autoridad | Caso excepcional no se convierte en proceso universal |
| T-22 | «Un cliente compra un producto y también una asesoría» | Producto, servicio, oferta, cuenta, entregables, facturación | Mantener distinciones y vínculos sin forzar un solo tipo de venta |
| T-23 | «Tengo tres funciones y no existe departamento de finanzas» | Dueño-persona, roles y facultades, funciones de D05 | No inventar CFO ni organigramas por plantilla |
| T-24 | «Reabre esto en otra sesión y explica cómo llegaste a la respuesta» | Fuentes, IDs, versiones, conflictos, decisiones, revisiones | Recuperar de estado compartido y fuentes, no de resumen defectuoso |

## Qué significa aprobar un test

Una ejecución futura debe guardar entrada exacta, fecha de consulta, agente/herramienta/versión, fuentes autorizadas usadas, decisión/estado esperado, respuesta observada, diferencia, revisión humana y resultado. Etiqueta `no_ejecutada` hasta observarla. Un test de enlaces no demuestra que el agente respondiera bien; un test semántico no comprueba seguridad técnica por sí solo.

## Dos giros sintéticos mínimos a usar luego

- **Servicios profesionales / consultoría:** una empresa sin departamentos formales, varias modalidades de oferta, herramientas internas, proyectos con acuerdos particulares y criterio experto.
- **Productos + operación física / híbrido:** inventario reservado en simultáneo, ventas, entregas, proveedores, caja, contratos y trabajadores con roles múltiples.

Se añaden comparaciones por múltiples empresas y conversación sin acceso directo para evitar que una arquitectura funcione solo para un caso privilegiado.
