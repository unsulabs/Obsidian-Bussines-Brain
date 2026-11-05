# 00 — Alcance, principios y frontera de la aprobación

## Problema de producto

En un negocio, especialmente cuando una o pocas personas concentran varias funciones, el conocimiento empresarial está disperso entre conversaciones de IA, documentos, hojas, correos, archivos de operación, herramientas y experiencia tácita. La dificultad no es solo almacenar: es **saber qué existe, qué significa, qué está vigente, de dónde proviene, qué está permitido hacer y cómo aprovecharlo para trabajar**.

## Resultado buscado

Un **repositorio maestro reutilizable en GitHub**, preparado para que un propietario no técnico pueda dárselo a Codex u otro asistente y recibir acompañamiento para instalar/configurar **una instancia privada de su empresa**. Su información podrá consultarse, relacionarse, desarrollarse y actualizarse con ayuda de agentes o chats; Obsidian será una interfaz de conocimiento, no una autoridad universal por ser la aplicación de visualización.

## Usuarios y restricciones reales

- Propietario/copropietarios de negocios, emprendimientos y actividades de autoempleo, sin restricción de país; una persona puede asumir dirección, ventas, compras, operaciones, finanzas y atención a clientes.
- Personas sin conocimientos de terminal, Markdown, YAML, Git o modelos de datos: la instalación debe explicarse conversacionalmente, con evidencia y reversibilidad.
- Empresas de servicios, productos, consultoría, híbridas o por proyectos, con o sin departamentos formales, CRM, ERP o procesos maduros.
- Agentes con capacidades muy diferentes: Codex con archivos y ejecución; Claude Code con sus propias convenciones; un chat sin herramientas que requiere exportación/importación explícita. No se presupone conectividad ni permisos.

## Cuatro niveles de diseño a mantener separados

1. **Visión de producto y experiencia humana:** propósitos, perfiles, modos de acceso, resultados útiles.
2. **Capacidades empresariales y operativas:** acciones, respuestas, flujos y aceptación.
3. **Semántica del conocimiento:** identidades, relaciones, autoridad, vigencia, procedencia, restricciones y evolución.
4. **Implementación técnica:** GitHub, Obsidian, plugins, agentes, motores, conectores, despliegue y mantenimiento.

Un diagrama que junte estos niveles puede orientar, pero no sustituye sus contratos ni pruebas.

## Principios conservados de vNext-1.0R y su contrato 0.9

- **Dos pasos:** primero desarrollar documentación empresarial útil con IA; después organizarla y operarla en un cerebro. El segundo paso no obliga a rehacer el primero.
- **D01–D07** son siete familias semánticas de cobertura; **X01–X07** son expedientes opcionales por necesidad de identidad. No significan catorce carpetas ni catorce archivos obligatorios.
- **K1–K4**: K1 criterio tácito del experto (preguntar de manera adaptativa); K2 hecho con autoridad en fuente/sistema (consultar documento o servicio); K3 desconocido todavía (marcarlo); K4 innecesario para la tarea actual (no bloquear).
- Una unidad se separa por identidad, historial, vigencia, permisos, consulta, autoridad y reutilización, no por nombre de departamento.
- Distinguir estados de revisión editorial, cobertura por pregunta, conocimiento de afirmaciones, vigencia temporal y clase de evidencia.
- No confundir `usado`, `ofrecido`, `cotizado`, `aceptado`, `contratado`, `entregado`, `facturado` y `cobrado`.
- Una experiencia individual no se convierte automáticamente en regla empresarial. Un agente no inventa acuerdos, precios, cargos ni autorizaciones.
- Un enlace de Obsidian ayuda a navegar; la recuperación correcta necesita pregunta, contexto, autoridad, evidencia, tiempo, permisos y prueba.

## Qué significa «siempre vigente» de forma verificable

No podemos garantizar información en tiempo real solo por almacenar Markdown. Aspiramos a **vigencia gestionada**: señalar cuál es el registro de autoridad para cada asunto y ámbito, fecha/condición de validez, última comprobación, método de revalidación, discrepancias y responsables. En fuentes que puedan cambiar externamente, devolver `requiere_revalidacion` o incertidumbre si no hay acceso actual y nunca presentar un caché viejo como verdad confirmada.

## Fuera de alcance por ahora

- Crear o modificar la instancia real de una compañía.
- Publicar GitHub, instalar plugins, dar permisos a conectores o configurar agentes reales.
- Dar por aprobadas carpetas del Core v0.1, cualquier plugin o una ontología técnica.
- Convertir Obsidian en ERP, sistema contable, CRM autoritativo por defecto o sistema de autorización multiusuario.
- Redistribuir contenido propietario de videos, plugins o templates sin revisar licencias.

## Protocolo de decisiones

| Etiqueta | Significado |
|---|---|
| `REQUISITO_DECLARADO` | El propietario expresó un objetivo; está abierto a precisión. |
| `HEREDADO_DOCUMENTADO` | Existe en vNext / contrato o investigación anterior; su cumplimiento práctico se verifica aparte. |
| `HALLAZGO_EXTERNO` | Observado en transcripción o fuente; no aprobado para instalar. |
| `HIPOTESIS_DISENO` | Alternativa que requiere contraste y prueba. |
| `DECISION_APROBADA` | El propietario aprobó explícitamente un alcance o alternativa concreta. |
| `NO_PROBADO` | No hay ejecución real ni evidencia suficiente. |

**Única aprobación registrada en esta fecha:** proceder con consolidación integral **antes** de decidir arquitectura e implementación. Todo lo demás conserva su propio estado.
