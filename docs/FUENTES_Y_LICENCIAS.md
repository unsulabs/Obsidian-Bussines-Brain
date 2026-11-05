# Procedencia de activos y decisiones de reutilización

## Activos propios previamente desarrollados

| Fuente incorporada | Ruta en el repo | Estado |
|---|---|---|
| Guía empresarial vNext-1.0R + catálogo + prompts especializados | `metodologia/vNext-1.0R/` | **Copia completa Markdown**, incluida adenda del piloto K1–K4 y gates |
| Contrato de traspaso vNext-0.9, esquema, validador, ejemplo | `contratos/vNext-0.9/`, `ejemplos/traspaso_sintetico/` | Preservado y funcional con fixture sintético |
| Prototipo CE Core v0.1 | `scripts/`, `plantilla_boveda/`, `tests/test_core.py` | Reutilizado y ampliado, con regresión existente |
| Expediente de diseño D0.1 | `investigacion/diseno-D0.1/` | Evidencia de requisitos, **no arquitectura aprobada** |
| Cinco tutoriales YouTube con hallazgos/timestamps | `investigacion/videos-2026-10/` | Análisis y URLs; no redistribuye transcripciones completas |

Los materiales vNext-1.0R y su informe de investigación son autoridad metodológica del Paso 1 para este prototipo; el modelo de 27 entidades es un diseño técnico candidato para el Paso 2. No reintroducir el antiguo catálogo de 45/64 assets como requisitos.

## Plugins y recursos externos (NO incorporados como código)

| Recurso | Hecho y decisión actual | Fuente |
|---|---|---|
| **Obsidian Bases** | Core nativo; vistas `.base` creadas. Verificar versión y GUI destino; Kanban requiere Obsidian 1.14+ según docs. | https://obsidian.md/help/bases/syntax · https://obsidian.md/help/bases/views |
| **Obsidian CLI** | Opcional para Codex con GUI local y versión compatible; diagnóstico no lo presume instalado. CLI requiere instalador 1.12.7+ y app en ejecución. | https://obsidian.md/help/cli |
| **Obsidian Projects** de Marcus Olsson | Repositorio archivado; autor discontinuó desarrollo mayo 2025 y lo retiraron de catálogo en julio 2025. **No se copia ni instala automáticamente.** README/`LICENSE` Apache-2.0 pero `package.json` dice MIT; aclarar antes de reutilización de código. | https://github.com/obsmd-projects/obsidian-projects |
| **TaskNotes** | Plugin opcional; ideas de tareas en nota, estado, tiempo, scheduled/due. No gobernará autoridad comercial. | https://github.com/callumalpass/tasknotes |
| **Codex AGENTS.md y Skills** | Archivo raíz e instrucciones pequeñas en `.agents/skills/` (convención documentada, no extensión universal para todo chatbot). | https://developers.openai.com/blog/skills-agents-sdk · https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex |
| **W3C PROV-O** | Inspiración para origen/agente/actividad, **no** se instala un grafo RDF automáticamente. | https://www.w3.org/TR/prov-o/ |
| **JSON Canvas** | Exportación del mapa visual del ejemplo, derivado sin autoridad independiente. | https://jsoncanvas.org/spec/1.0/ |

## Licencia del producto

El código, las instrucciones y la documentación propia se distribuyen bajo [MIT](../LICENSE). Las referencias a terceros conservan sus autores, títulos y enlaces; la licencia de este repositorio no relicencia obras externas, normas, videos, marcas ni plugins. No se incluyen copias de plugins ni transcripciones completas de terceros.
