# 02 — Mapa de capacidades empresariales y cobertura

Esta matriz indica **qué debe poder hacer el producto**; no prescribe una carpeta, aplicación o número de documentos. `RQ` refiere a requisitos declarados en `requisitos_usuaria.md` del kit de videos; el cumplimiento está **pendiente**. D01–D07/X01–X07 son clases documentales existentes, no una ontología empresarial completa.

## Capacidades que el sistema debe cubrir

| ID | Familia de capacidad | Preguntas y operaciones exigibles | Enlace con vNext | RQ | Evidencia de aceptación a diseñar |
|---|---|---|---|---|---|
| CAP-01 | Identidad, propósito, estrategia y gobierno | ¿Qué empresa es, por qué existe, qué prioriza y qué decidió no hacer? | D01 | 001,006,007 | Respuesta con límites y decisión real, no misión inventada |
| CAP-02 | Modelo de negocio, propuestas de valor y oferta | Diferenciar vendido, ofrecido, consultoría, producto usado; crear/evolucionar ofertas | D01, D03, X01 | 008,010 | Precio y alcance por contexto con fuentes |
| CAP-03 | Mercado, comunicación y marca | A quién sirve, qué evidencia existe, qué mensaje está autorizado, generar piezas coherentes | D02, D03 | 011,012 | Texto alineado a criterios y sin claims inventados |
| CAP-04 | Prospección, CRM y ciclo comercial | Prospecto, contacto, cuenta, oportunidad, propuesta, aceptación, contratación, facturación y cobro | D03, X03, X05 | 009,023 | No confundir eventos comerciales |
| CAP-05 | Proyecto, caso, ejecución y experiencia | Qué está activo, en preparación, entregado, quién ejecutó, qué ocurrió | D04, X04 | 009,011,022 | Cronología recuperable con subproyecto, reunión, actividad y evidencia |
| CAP-06 | Procesos, servicios, calidad y lecciones | Cómo se hace, qué excepciones existen, qué proceso se aplica y quién lo aprobó | D04, X02, X07 | 008,011,025 | Caso real no se eleva a SOP sin evidencia y autoridad |
| CAP-07 | Abastecimiento, activos e inventarios | Qué recursos existen, disponibilidad, proveedores, dependencias y fuentes oficiales | D07, X06 | 021,025 | El registro de inventario manda cuando corresponde |
| CAP-08 | Finanzas y economía | Precios vs costos, margen, flujo, compromisos, mediciones, escenarios; no sustituir sistema financiero | D05, X01, X05 | 013,016,021 | Separar presupuesto, factura, pago y pronóstico |
| CAP-09 | Personas, roles y facultades | Quién participa, realiza, aprueba, es dueño del dato o del proceso | D06, X03, X04 | 001,009,018 | Una persona puede ocupar múltiples roles y ámbitos |
| CAP-10 | Cumplimiento, riesgos y acuerdos | Contratos, obligaciones, privacidad, dependencias y contingencias | D07, X05, X06 | 013,016,018 | Restricción por fuente y tarea; no asesoría legal automática |
| CAP-11 | Investigación, innovación y metodología | Encontrar investigación, experimento, hipótesis, resultado; convertir aprendizajes aprobados en práctica | D01–D07, X07 | 011,025,028 | Conocimiento abierto no se vuelve afirmación vigente |
| CAP-12 | Sistemas y tecnología | Qué herramientas usa la empresa; qué integra, licencia, tiene dueño y fuente de autoridad | D07, X06 | 008,024,027 | Diferenciar herramienta interna de producto contratado |
| CAP-13 | Gestión del conocimiento | Registrar fuentes, autoridad por asunto, vigencia, estados, relaciones, permisos, continuidad | Transversal, contrato 0.9 | 013–018,025–026,029 | Historial, conflicto, consulta temporal, control de acceso |
| CAP-14 | Agentes, chats e instrucciones | Seleccionar contexto, ejecutar tareas permitidas, entregar propuestas y auditar reescritura | Paso 2 | 004,005,024,029 | Mismo caso con Codex/Claude/chat; fallos explícitos |
| CAP-15 | Experiencia, instalación y mantenimiento | Instalar desde tutorial, crecer sin abrumar, actualizar sin romper empresas | Paso 2 | 002–004,019–020,027–030 | Instalación limpia, upgrade, rollback y uso inicial |

### Necesidades horizontales, independientemente del departamento

- Autoridad por asunto y ámbito; dueños/aprobadores explícitos.
- Fechas efectivas y de captura; conflictos, revisión y obsolescencia comprobable.
- Evidencia, fuentes, restricciones y autorización de acciones.
- Gestión de dependencias e impacto cuando una regla cambia.
- Vinculación entre estrategia, operación, recursos, finanzas, decisiones, personas y resultados.
- Recuperación a partir de **preguntas reales**, no solo de búsquedas por nombre.
- Contexto mínimo, portable y seguro para asistentes heterogéneos.
- Modelado parcial y de excepciones sin inventar un organigrama o un ERP.

## Cobertura visible en experiencia vs estructura profunda

**Vistas posibles del dueño:** Inicio/organización, prioridades, ofertas vigentes, clientes/prospectos, proyectos, tareas, reuniones, recursos, economía, personas, acuerdos, investigaciones, decisiones, fuentes/pendientes, configuración del cerebro.

**Debajo:** pueden existir familias documentales D/X, entidades, bloques, fuentes, relaciones y proyecciones. La pantalla no obliga a que existan 14 carpetas, una carpeta por departamento ni una nota por tarea. Un mismo dueño puede operar varias vistas sin duplicar personas o datos.

## Mapa de 30 criterios de diseño

| Requisito | Principal ubicación de análisis en esta entrega | Estado |
|---|---|---|
| RQ-001 | `00` / `01` dueño multitarea | Criterio de diseño |
| RQ-002 | `01` / `08` onboarding no técnico | Criterio de diseño |
| RQ-003 | `00` / `07` producto GitHub reutilizable | Criterio de diseño |
| RQ-004 | `01` / `05` instalación asistida | Criterio de diseño |
| RQ-005 | `01` / `05` agentes y chats simples | Criterio de diseño |
| RQ-006 | `00` / `03` no inventar datos ni autoridad | Criterio de diseño |
| RQ-007 | CAP-01 | Criterio de diseño |
| RQ-008 | CAP-02 / `03` tipos de oferta y herramientas | Criterio de diseño |
| RQ-009 | CAP-04/05/09 / `03` entidades diferenciadas | Criterio de diseño |
| RQ-010 | CAP-02 / `03` ofertas vivas | Criterio de diseño |
| RQ-011 | CAP-05/06/11 / `03` | Criterio de diseño |
| RQ-012 | CAP-03 / `10` | Criterio de diseño |
| RQ-013 | CAP-04/10/13 / `03` | Criterio de diseño |
| RQ-014 | `03` identidad e historial | Criterio de diseño |
| RQ-015 | `03` relaciones, exclusiones y preguntas | Criterio de diseño |
| RQ-016 | `03` autoridad por asunto/ámbito/fecha | Criterio de diseño |
| RQ-017 | `03` vigencia, caducidad y discrepancias | Criterio de diseño |
| RQ-018 | `03` / `05` permisos reales | Criterio de diseño |
| RQ-019 | `01` / `04` Obsidian interfaz | Criterio de diseño |
| RQ-020 | `04` recursos Obsidian | Candidato, no stack aprobado |
| RQ-021 | CAP-01–15 | Criterio de diseño |
| RQ-022 | CAP-05 / `01` | Criterio de diseño |
| RQ-023 | CAP-04 / `10` | Criterio de diseño |
| RQ-024 | `05` contexto para asistentes | Criterio de diseño |
| RQ-025 | `06` ingesta y trazabilidad | Criterio de diseño |
| RQ-026 | `08` / `10` pruebas reales | Criterio de diseño |
| RQ-027 | `05` / `08` / `09` migraciones | Criterio de diseño |
| RQ-028 | `03` / `04` extensiones por giro | Criterio de diseño |
| RQ-029 | `05` / `07` metaconocimiento | Criterio de diseño |
| RQ-030 | `00` / `06` / `09` no cerrar arquitectura | Criterio de proceso |

## Vacíos declarados que aún deben estudiarse

Contabilidad vs conocimiento financiero, privacidad por rol, trabajo fuera de línea, reconciliación entre ediciones humanas y agente, extensibilidad de entidades, seguridad de scripts/plugins, sincronización entre distintos equipos, permisos por instancia, metodología de migración y señal para cambiar una práctica común. Los videos no los solucionan.
