# Arquitectura del primer incremento — referencia histórica v0.2.0-alpha

**Estado:** describe el diseño de inicio. Para operar la versión actual, leer [ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md](ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md), [ESTADO_REAL.md](ESTADO_REAL.md) y las skills activas. Algunas funciones que este texto considera futuras ya están implementadas de manera preliminar; esta referencia histórica no prevalece sobre el contrato vigente.

## Objetivo de diseño

Un emprendedor que no sabe Obsidian/Codex debe poder recibir un repositorio listo para **desarrollar su empresa junto con el asistente**, no solamente una bóveda vacía. Es una herramienta basada en **Obsidian y Codex**, extensible a otros harness con permisos y capacidades verificadas. El repositorio es el producto, la bóveda privada es la instancia, los documentos empresariales son el conocimiento.

## Niveles y límites

| Nivel | Implementación en este repositorio | No hace |
|---|---|---|
| Metodología de creación | vNext-1.0R completa: D01–D07/X01–X07, K1–K4, gates G1–G7 | No certifica mercados ni forma documentos por sí sola |
| Contrato de conocimiento | vNext-0.9 (manifest, fuentes, bloques, autoridad, temporalidad) | No infiere autoridad por fecha del archivo |
| Modelo operativo candidato | `modelo/tipos_entidad.json` con 27 distinciones; plantillas y CLI `ficha` | No obliga a 27 notas/áreas/departamentos |
| Infraestructura Obsidian | `plantilla_boveda/` con Inicio, mapas, 12 vistas Bases + 4 anteriores, plantillas y referencias | No es ERP/CRM ni control de permisos |
| Capa de ejecución determinista | `scripts/cerebro.py`, `scripts/importar_traspaso.py`, `validar_boveda.py` | No hace RAG, navegación autónoma ni cambios oficiales automáticos |
| Capa agéntica | `AGENTS.md`, `.agents/skills/` y `guia/` | No ejecuta acciones sin agente y sus herramientas reales |
| Investigación y evolución | `investigacion/`, `docs/` y pruebas | No aprueba plugins por aparecer en tutoriales |

```
Repositorio público (código del producto)
           |
           v
Codex con acceso al checkout — lee AGENTS y skills
           |
     diagnóstico y permisos
           |
           v
Bóveda privada en computadora del usuario (FUERA de Git)
           |
    recuperar → desarrollar (vNext) → verificar
           |
    documentos + fuentes + bloques + relaciones → vistas Obsidian
           |
    consultar / proponer / continuar, releyendo originales
```

## Invariantes de almacenamiento

1. Instancia de una empresa nunca dentro del árbol versionado, salvo `instancias/` temporal local **ignorado**. Todo script exige ruta de bóveda explícita.
2. `Inicio.md` y `00_Mapas/` son navegación, no autoridad duplicada. Las vistas `.base` derivan de notas Markdown y Properties; no originan hechos.
3. D01–D07 y X01–X07 son clases de **exposición documental**; 27 tipos de `modelo/tipos_entidad.json` son distinciones **operativas**. No son equivalentes, no crean número fijo de archivos.
4. El contrato 0.9 conserva IDs de documentos, bloques `<!-- kb:id=... -->`, fuentes, aristas y autoridades con fechas. Importación preflight+stage+rollback evita sobrescrituras evitables, pero **no tiene bloqueo de concurrencia**.
5. Las fuentes oficiales permanecen en sus sistemas: Obsidian puede tener fichas con localizadores y permisos, no datos bancarios ni contratos completos por defecto.
6. La automatización ejecuta tareas estructurales; la IA desarrolla conocimiento sujeto a criterio humano. El punto de autorización sigue siendo externo a las propiedades YAML.
7. La búsqueda literal y el `authority_lookup` exacto son **mecanismos de apoyo**, no un sistema de recuperación semántica validado.

## Por qué Obsidian Bases y no Projects como requisito

Bases nativo presenta tablas/tarjetas/Kanban sobre propiedades existentes sin depender de una comunidad externa; se comprobará versión de Obsidian requerida en instalación real. El plugin de Marcus Olsson `obsmd-projects/obsidian-projects` es **investigación de diseño** (tabla, tablero, calendario, galería y plantillas), pero su repositorio está archivado y descontinuado desde mayo de 2025. No instalar automáticamente ni incorporarlo como fuente de datos. TaskNotes es candidato opcional para seguimiento de tareas/tiempo, sin reemplazar el núcleo.

## Extensiones futuras

- Perfiles de capacidad: agente con archivos local/solo chat/connector remoto. No asumir herramientas no disponibles.
- Relaciones tipadas con fuentes verificadas y resolución por ámbito/tiempo.
- Aplicación controlada de cambios con revisiones, diff, locks y rollback.
- Migraciones versionadas de instancias: no tocar empresas al actualizar repositorio.
- Recuperación semántica probada contra preguntas adversariales con al menos dos agentes.

## Anterior y trazabilidad

Se preserva el código del prototipo v0.1 (`scripts/crear_instancia.py`, `importar_traspaso.py`, etc.), su fixture sintético y la validación del contrato 0.9. Las guías originales vNext-1.0R completas están en `metodologia/` y la consolidación D0.1 en `investigacion/diseno-D0.1/`. El detalle de decisiones abiertas está en `docs/DECISIONES_ABIERTAS.md`.


## Puerta de distribución del conocimiento (incorporada posteriormente al núcleo 0.2)

Ver docs/ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md: las notas D/X resumen temas transversales y enlazan fuentes, entidades, ofertas, decisiones, procesos y casos con identidad, vigencia y mantenimiento autónomos. Antes de redactar un documento multiasunto, Codex debe analizar si conviene revisar una nota existente, crear una nueva, referenciar o no crear. El comando plan-conocimiento revisa cobertura, IDs, fuentes, etiquetas y relaciones candidatas **sin escribir**.

Una instancia nueva no debe proliferar fichas con placeholders; las nuevas notas pueden crearse con contenido completo en Markdown externo mediante ficha --archivo. La clasificación semántica continúa siendo trabajo humano asistido, no una inferencia automática del validador.
