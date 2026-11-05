# Documentación

[English](../en/README.md) · [Descripción del proyecto](../../README.es.md)

El inglés es el idioma principal de las guías públicas de uso y desarrollo. Cada página siguiente tiene equivalente en español. Comandos, claves de esquema, enums, IDs, nombres de skills y archivos de bóveda conservan sus identificadores de runtime en ambos idiomas.

## Usar el producto

- [Empieza aquí](../../EMPIEZA_AQUI.md): elige instancia empresarial nueva o existente.
- [Preparación](onboarding.md): requisitos, almacenamiento privado, instalación y routing verificado.
- [Guía de uso](user-guide.md): desarrollar conocimiento, utilizarlo, añadir fuentes y corregirlo.
- [Transcripciones](transcripts.md): custodia, análisis, permisos e integración.
- [Flujo de conocimiento](knowledge-workflow.md): arquitectura, autoridad y decisiones editoriales.
- [Operación](operations.md): instancias existentes, cambios, respaldos y aceptación.
- [Seguridad](security.md): límites de privacidad y autorización.
- [Metodología](methodology.md): cómo usar los originales preservados en español.

## Desarrollar y mantener

- [Desarrollo](development.md) y [contribución](contributing.md).
- [Arquitectura](architecture.md), [modelo de datos](data-model.md) y [referencia CLI](cli-reference.md).
- [Pruebas](testing.md): distinguir comprobaciones estructurales y aceptación real.
- [Flujo documental](documentation-workflow.md): plantillas adaptadas de ai-cursor-init y comprobaciones bilingües.
- Decisiones: [almacenamiento local](adr/0001-local-first.md), [custodia de fuentes](adr/0002-source-custody.md), [documentación bilingüe](adr/0003-bilingual-documentation.md).
- [Plantilla de propuesta](rfc/0000-template.md) y [cambios](changelog.md).

## Originales y referencias

Los originales metodológicos de `metodologia/` y `contratos/`, y el material histórico de diseño/investigación, conservan su redacción española e identidad de versión. Las referencias operativas de `guia/`, rutas previas de `docs/` y referencias de skills pueden seguir enlazadas explícitamente como españolas. Preservan detalle y procedencia; no convierten planes históricos en capacidades implementadas. Empieza por las guías vigentes anteriores y abre originales sólo cuando la tarea lo necesite.

El repositorio es el producto; no contiene bóveda de clientes ni corpus de transcripciones. Lee `AGENTS.md` antes del trabajo del agente y resuelve una bóveda existente mediante la skill incluida `obsidian-router` antes de acceder a ella.
