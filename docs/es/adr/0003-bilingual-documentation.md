# ADR 0003 — Documentación pareada en inglés y español

[English](../../en/adr/0003-bilingual-documentation.md) · [Flujo documental](../documentation-workflow.md)

## Estado

Registro de la estructura documental del producto en trabajo. Este archivo no certifica traducción completa de cada fuente histórica ni publicación de una versión. No se atribuye una fecha histórica de aprobación.

## Contexto

Las guías públicas de uso y desarrollo necesitan entrada consistente en inglés y guía equivalente en español. Metodología, contratos, referencias operativas e identificadores de runtime existentes tienen significado versionado que no debe sustituirse mediante traducciones renombradas.

## Decisión

Usar inglés como entrada pública principal, con equivalentes españoles declarados. Mantener páginas localizadas en `docs/en/` y `docs/es/`, y pares de entrada raíz según `docs/documentation-map.json`. Actualizar cada par junto con pasos, permisos, límites, ejemplos y enlaces equivalentes.

Preservar comandos, flags, claves de esquema, enums, IDs estables, skills y nombres de archivos de bóveda. Identificar explícitamente referencias originales españolas desde guías inglesas; conservar rutas, idioma e identidad histórica. Una guía temática resume y orienta a sus referencias; no afirma traducción línea por línea ni reemplazo.

Adaptar instrucciones y plantillas de ai-cursor-init al producto inspeccionado, conservando procedencia fijada y aviso MIT. Inventario y plantillas bilingües son extensiones locales. Usar el verificador Python para cobertura declarada y enlaces locales admitidos, con revisión humana/del agente de significado y exactitud de implementación.

## Alternativas y consecuencias

Una guía sólo inglesa omitiría el equivalente español. Renombrar archivos de runtime o sobrescribir silenciosamente metodología original rompería identidad y procedencia. Copiar afirmaciones genéricas del framework tergiversaría el producto.

Los pares aumentan mantenimiento y pueden divergir semánticamente aunque pasen enlaces. Los cambios deben revisar ambos significados, comandos y controles; las referencias históricas permanecen explícitamente fuera de la afirmación de paridad bilingüe completa. La adaptación es operada por agente, no sincronización automática ni servicio nuevo de runtime.

## Evidencia

[Inventario](../../documentation-map.json), [framework local](../../../.cursor/README.md), [verificador](../../../scripts/check_docs.py), [aviso de terceros](../../../THIRD_PARTY_NOTICES.md), [guía metodológica](../methodology.md) y [flujo documental](../documentation-workflow.md).
