# Flujo documental

[English](../en/documentation-workflow.md) · [Documentación](README.md)

Este repositorio adapta [mgiovani/ai-cursor-init en fc15400e4baab4607f408f5b83fed19263e564e3](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). La adaptación usa instrucciones específicas para el agente, plantillas bilingües y un verificador local determinista. No instala ejecutable upstream, servicio alojado ni sincronización en segundo plano. El aviso y licencia MIT originales se preservan en [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

## Elegir la instrucción

| Tarea | Instrucción local |
| --- | --- |
| Inicializar páginas pareadas faltantes | [init-docs](../../.cursor/commands/cursor-init/init-docs.md) |
| Actualizar desde código cambiado | [update-docs](../../.cursor/commands/cursor-init/update-docs.md) |
| Validar y comunicar límites | [check-docs](../../.cursor/commands/cursor-init/check-docs.md) |
| Proponer una decisión de arquitectura | [adr](../../.cursor/commands/cursor-init/adr.md) |
| Actualizar diagramas de arquitectura | [gen-arch-diagram](../../.cursor/commands/cursor-init/gen-arch-diagram.md) |

En Cursor selecciona el comando personalizado disponible desde la interfaz del editor; su descubrimiento depende de la versión instalada. Estos Markdown son instrucciones para un agente, no comandos de shell. En Codex pide explícitamente leer el archivo exacto y ejecutar sus pasos con las herramientas disponibles. No presupongas descubrimiento de comandos slash de Cursor en Codex. `AGENTS.md` sigue siendo el contrato del repositorio.

## Actualizar desde evidencia

1. Lee `AGENTS.md`, [notas del framework](../../.cursor/README.md), [.cursor-init.yaml](../../.cursor-init.yaml) e [inventario documental](../documentation-map.json). Inspecciona diff acotado, código actual, pruebas y ayuda de comandos pertinentes.
2. Identifica los pares afectados. Cambia inglés y español juntos, conservando comandos, flags, claves de esquema, enums, IDs, nombres de runtime y significado de enlaces relativos. Lee sólo fuentes públicas pertinentes del producto; no accedas a bóveda privada ni banco de transcripciones para documentarlo.
3. Usa plantillas en [inglés](../../.cursor/cursor-init/templates/en/) y [español](../../.cursor/cursor-init/templates/es/) para páginas faltantes o estructura. Sustituye indicaciones por contenido verificado. Una plantilla genérica no acredita base de datos, API web, servicio de despliegue, política de ramas ni promesa de rendimiento. No reemplaces metodología, contratos ni skills existentes por plantillas.
4. Añade nuevos pares ADR/RFC al inventario. Describe decisiones actuales desde evidencia sin inventar fechas de aprobación; un RFC sigue siendo propuesta hasta que una decisión real cambie su estado.
5. Ejecuta comprobaciones, contrasta significado y controles entre idiomas, inspecciona ejemplos y revisa diagramas por separado. Comunica resultados observados y límites.

`.cursor-init.yaml` conserva categorías upstream; `local_extension` y las rutas/plantillas bilingües son extensiones locales interpretadas por los prompts. El verificador Python lee directamente el inventario JSON, no YAML. No existe proceso de sincronización automática.

## Comprobar e informar

Tras activar el entorno Python verificado, ejecuta desde la raíz:

```bash
python scripts/check_docs.py
python -m unittest discover -s tests -p 'test_check_docs.py' -v
git diff --check
```

El verificador detecta pares declarados ausentes/duplicados, Markdown localizado no registrado, rutas inseguras, enlaces locales inline/de referencia y anchors admitidos. Omite ejemplos en bloques de código y URLs remotas. No certifica equivalencia semántica, comportamiento contra código, toda la sintaxis Markdown, renderizado ni disponibilidad de URLs externas. Revísalos aparte y no declares verificado visualmente un diagrama sin renderizar.

El inventario identifica referencias españolas preservadas y guías temáticas. Una guía temática no es traducción línea por línea ni reemplazo del original. Identifica referencias españolas al enlazarlas desde inglés, conserva rutas e identidad histórica y distingue resultados históricos o planes de implementación vigente. Ver [metodología](methodology.md) y [ADR bilingüe](adr/0003-bilingual-documentation.md).
