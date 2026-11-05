# 09 — Programa para continuar por bloques sin imponer arquitectura

La siguiente etapa **no es programar más software**: es consolidar, comprobar y aprobar decisiones documentadas de diseño. Se avanza por dependencias, pero pueden incorporarse nuevos recursos en cualquier momento.

## Bloque C0 — Inventario y continuidad (este corte)

**Entradas:** criterios de diseño RQ-001–RQ-030, metodología vNext-1.0R, contrato 0.9, kit de videos v0.2 y prototipo Core v0.1.

**Realizado:** lectura de material disponible, síntesis de alcances, mapa de capacidades, semántica conceptual, registro de activos/decisiones, propuesta de pruebas. **Pendiente:** que el propietario revise si hay omisiones o interpretaciones incorrectas.

## Bloque C1 — Problemas, usuarios y capacidades (siguiente revisión)

Revisar con el propietario **todo el mapa**, no forzar a elegir solo un rol o un caso. Organizar modos de uso, tareas, responsabilidades y valor esperado. Buscar contradicciones y requisitos olvidados (por ejemplo proveedores, entregables comerciales, control de permisos). Salida: matriz de capacidades **revisada**, no diseño de carpetas.

**Gate:** cada capacidad relevante tiene una pregunta/acción empresarial y al menos un escenario para comprobarla.

## Bloque C2 — Entidades, significado y autoridad

Contrastar cada pareja difícil (oferta/producto; consultoría/herramienta; proyecto/servicio; reunión/decisión; factura/pago; CRM/cliente; caso/política). Para cada tipo requerido, decidir identidad, historia, propiedades mínimas, relaciones permitidas, fuente competente, ámbito, temporalidad, permisos y preguntas. No introducir tipos por estética.

**Gate:** un mismo hecho se recupera correctamente desde varias preguntas y fechas sin duplicar autoridad.

## Bloque C3 — Uso real y representación técnica comparada

Con casos y modelo semántico suficientemente claros, evaluar estructura de bóveda, vistas, Bases, Templates, TaskNotes, plugins, instrucciones por harness, mecanismos de indexación e intercambios con servicios externos. Comparar nativo vs plugin vs implementación propia con costos, licencias y portabilidad.

**Gate:** alternativas con experimentos observables, sin dar por aprobada una demo sintética.

## Bloque C4 — Instalación, seguridad, evolución y aceptación

Diseñar recorrido end-to-end para dueño novato (video tutorial → repositorio → Codex → instancia privada → primera respuesta con fuentes), permisos, respaldos, recuperación, migraciones y pruebas multiagente/multigiro. Entrega esperada: especificación integral apta para implementación **si se aprueba**.

**Gate:** criterios medibles y negativos; qué falla, qué no se sabe, cómo se revierte, quién decide.

## Bloque C5 — Implementación posterior (requiere autorización separada)

No iniciar hasta aprobar contratos de diseño prioritarios. Reutilizar el Core v0.1 solo tras auditoría de compatibilidad; implementación incremental con pruebas, no reconstrucción genérica ni instalación masiva de plugins.

## Ciclo para recursos nuevos

En cualquiera de C1–C4, un video/template/repositorio adicional entra por `06_Incorporacion_de_Activos.md`; se contrastan hallazgos con RQ/CAP/DEC y casos, se proponen cambios al expediente y se conserva historial de interpretaciones. **Agregar información no reinicia el proyecto**.

## Producto del cierre de consolidación (no de este corte)

1. Narrativa de producto y personas/uso aprobadas.
2. Mapa de capacidades/escenarios con cobertura auditada.
3. Especificación semántica empresarial y fuentes de autoridad por dominio.
4. Contrato portable Paso 1→Paso 2 enriquecido si la evidencia lo exige, sin perder compatibilidad.
5. Comparación técnica de Obsidian/plugins/agentes y decisión de composición justificada.
6. Protocolo de instalación y actualización probado en ambiente de ensayo.
7. Criterios y casos de aceptación que distinguen lo estructural de lo semántico.
8. Ruta de implementación y cierre formal de decisiones.

**Próxima interacción recomendada:** revisión conjunta de C1 y C2 a partir de este expediente, con libertad para corregir, ampliar o aportar otro tutorial. No se solicitará un formulario genérico de todos los departamentos.
