# Obsidian-Bussines-Brain

**Convierte tu forma de trabajar y decidir en conocimiento empresarial que puedas usar.**

[English](README.md) · **Español**

[![Licencia: MIT](https://img.shields.io/badge/licencia-MIT-blue)](LICENSE) [![Python: 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](docs/es/onboarding.md) [![Docs: EN / ES](https://img.shields.io/badge/docs-EN%20%2F%20ES-green)](docs/es/README.md)

[Empieza aquí](EMPIEZA_AQUI.md) · [Continúa un negocio existente](PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md) · [Explora la documentación](docs/es/README.md) · [Reporta un problema](https://github.com/unsulabs/Obsidian-Bussines-Brain/issues)

## Contenido

- [Acerca del proyecto](#acerca-del-proyecto)
- [Tecnologías](#tecnologías)
- [Primeros pasos](#primeros-pasos)
- [Uso](#uso)
- [Privacidad y control editorial](#privacidad-y-control-editorial)
- [Hoja de ruta y límites actuales](#hoja-de-ruta-y-límites-actuales)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Soporte](#soporte)
- [Reconocimientos](#reconocimientos)

## Acerca del proyecto

Obsidian-Bussines-Brain es un espacio privado de conocimiento respaldado por fuentes para dueños de negocios, emprendedores y trabajadores por cuenta propia. Trabaja con Codex para conservar conversaciones, explicar decisiones y excepciones, y desarrollar conocimiento que tu equipo o tus agentes puedan usar en Obsidian.

Úsalo para responder «¿Por qué calificamos así a los clientes?», preparar una oferta a partir de criterios establecidos o recuperar qué cambió entre dos decisiones. El flujo conecta la evidencia original, el criterio del dueño, notas revisables y la tarea concreta.

- **Conservar el significado:** guardar originales completos y procedencia antes de resumir; trasladar razones, excepciones y correcciones al conocimiento resultante.
- **Desarrollar conocimiento útil:** identificar asuntos y notas existentes antes de redactar, distinguiendo propuestas y contenido aprobado.
- **Encontrarlo y mantenerlo:** recuperar pasajes originales, revisar versiones y navegar notas Markdown, vistas Bases y mapas Canvas.

| Ubicación | Qué contiene |
| --- | --- |
| Repositorio público del producto | Software, metodología, instrucciones para agentes, plantillas y ejemplos sintéticos |
| Bóveda privada de Obsidian | Conocimiento empresarial y su estado de revisión |
| Banco privado de fuentes, fuera de Git y de la bóveda | Transcripciones originales y sus registros de custodia |

Es una herramienta local operada durante una sesión del agente. No instala un servicio alojado ni un proceso en segundo plano. Codex y los conectores opcionales tienen sus propias condiciones de acceso y tratamiento de datos.

### Tecnologías

| Componente | Función |
| --- | --- |
| Python 3.11+, PyYAML, jsonschema | Comandos locales y validación; consulta las [dependencias](requirements.txt) |
| Markdown y Obsidian Desktop | Notas legibles, Properties, Bases nativas y Canvas |
| Codex y skills del repositorio | Revisión asistida de fuentes, desarrollo de conocimiento y flujo editorial |

Consulta los límites de cada componente en la [guía de arquitectura](docs/es/architecture.md).

## Primeros pasos

### Requisitos

- Git y **Python 3.11 o posterior**.
- Codex con acceso comprobado a archivos y comandos para el flujo asistido.
- Obsidian Desktop para ver la bóveda; comprueba Bases y CLI localmente.
- Ubicaciones privadas separadas para la bóveda empresarial y el banco de fuentes.

**Dependencia externa para bóvedas existentes:** `obsidian-router`, un registro local de destinos y verificación contra Obsidian. Clonar no los instala. Antes de listar o leer archivos de la bóveda, el agente debe resolver el destino y leer las instrucciones locales. La ventana activa o una ruta escrita en el CLI no reemplazan esas comprobaciones. Si falta routing, continúa el trabajo autorizado fuera de la bóveda y deja pendiente su acceso/integración.

### Instalación

Prepara el producto en macOS o Linux:

```bash
git clone https://github.com/unsulabs/Obsidian-Bussines-Brain.git
cd Obsidian-Bussines-Brain
python3.11 --version
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python scripts/cerebro.py --help
```

También se admite un intérprete Python 3 posterior; comprueba primero su versión. En Windows usa `py -3.11 -m venv .venv` y activa con `.venv\Scripts\Activate.ps1` en PowerShell en lugar de `source`. Tras activar, los comandos `python` son iguales. La instalación de paquetes puede acceder a la red y requiere la autorización correspondiente.

`doctor` es de solo lectura y no instala componentes faltantes. Si fallan imports, comprueba el intérprete y los entornos existentes. Este inicio rápido prepara la herramienta; no crea una bóveda ni verifica el comportamiento GUI de Obsidian o la utilidad empresarial.

### Elige el siguiente paso

| Tu situación | Siguiente paso |
| --- | --- |
| No existe una instancia empresarial | Sigue la [preparación](docs/es/onboarding.md#instancia-empresarial-nueva) para crear una instancia autorizada en una ruta privada nueva y después [desarróllala con Codex](PROMPT_INICIO_CODEX.md). |
| Ya existe una bóveda empresarial | Usa [Continúa con Codex](PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md). Verifica el routing; no ejecutes `crear`, copies plantillas encima ni reinicies la entrevista inicial. |
| Usar o actualizar conocimiento | Abre la [guía de uso](docs/es/user-guide.md). |
| Cambiar el producto | Abre la [guía de desarrollo](docs/es/development.md). |

Instalar una plantilla es sólo el comienzo: continúa por revisión de fuentes, arquitectura del conocimiento, redacción útil, revisión y una tarea empresarial real.

## Uso

Estos **ejemplos sintéticos** son prompts para Codex después de configurar la instancia privada y verificar su destino. No son afirmaciones sobre un negocio real.

**Incorporar una conversación nueva**

> Esta es una transcripción sintética nueva y completa para la demo Taller Nube: «Ofrecemos una sesión de diagnóstico antes de cotizar una reparación. Para clientes que regresan, primero revisamos el diagnóstico anterior. No hemos aprobado un precio fijo para el diagnóstico». Conserva el texto exacto antes de analizarlo. Dentro de la autorización de esta instancia, integra su ficha, acceso al texto íntegro y conexiones justificadas. Mantén el precio sin decidir y muestra qué cambió.

El ciclo de transcripciones abarca todos los asuntos, antecedentes y notas existentes pertinentes. Identifica las partes que falten por entregar; un enlace solo no equivale a un original capturado. Los documentos ordinarios y las preguntas largas conservan su tarea expresada y no se ingieren automáticamente como transcripciones. Consulta el [flujo de transcripciones](docs/es/transcripts.md).

**Hacer una consulta empresarial**

> En la demo Taller Nube, ¿qué debemos revisar antes de cotizar a un cliente que regresa? Abre los pasajes originales pertinentes y explica razones y excepciones. Distingue decisiones aprobadas de propuestas. Si el precio del diagnóstico no está establecido, déjalo desconocido en vez de sugerir un precio acordado.

**Corregir una nota de trabajo**

> La excepción para clientes que regresan aplica sólo cuando el diagnóstico anterior cubre el mismo problema. Revisa el original y las notas relacionadas; después propone la corrección y su impacto. Conserva la versión anterior y no sobrescribas silenciosamente conocimiento aprobado.

Consulta la [guía de uso](docs/es/user-guide.md) y el [flujo de conocimiento](docs/es/knowledge-workflow.md). Comprueba tanto una tarea útil como una pregunta que deba mantener incertidumbre; la validación estructural por sí sola no acredita una respuesta correcta.

## Privacidad y control editorial

Mantén fuentes reales, datos personales, credenciales y evidencia de clientes fuera de commits, issues y pull requests. Los permisos son específicos de la instancia, la fuente y la finalidad. Las etiquetas de sensibilidad son metadatos; Obsidian no aplica control de acceso por nota. Publicar, subir datos, instalar plugins e integrar servicios requieren la autorización correspondiente.

La salida de IA sigue siendo propuesta hasta la verificación y decisión pertinentes. Conserva evidencia contradictoria e historial en vez de reemplazar decisiones aprobadas por afirmaciones más recientes. Las fichas ayudan a localizar originales; no demuestran que el original se leyó en esta sesión. Mapas, vistas y enlaces apoyan la navegación y no establecen autoridad.

No se presupone país, moneda, régimen fiscal, forma jurídica, departamentos ni personal contratado. Lo desconocido permanece desconocido. Consulta [seguridad y privacidad](docs/es/security.md).

## Hoja de ruta y límites actuales

El producto está en desarrollo. La [hoja de ruta](docs/HOJA_DE_RUTA.md) prioriza instalación/recuperación en distintos sistemas operativos, revisión independiente de fidelidad semántica, adaptadores y controles externos de acceso, y pruebas de migración/restauración en copias aisladas. Son prioridades de validación, no compromisos de entrega.

La búsqueda de transcripciones es léxica. No están implementados un servicio alojado, sincronización automática con ERP/CRM, controles de acceso multiusuario ni migraciones universales. Las pruebas automáticas no acreditan exactitud empresarial, cumplimiento normativo, recuperación semántica ni compatibilidad GUI. Consulta los [límites actuales](docs/es/architecture.md), la [guía de aceptación](docs/es/testing.md) y los [cambios](docs/es/changelog.md).

## Contribuir

Lee la [guía de contribución](docs/es/contributing.md) antes de proponer un cambio. Usa reproducciones sintéticas, diagnósticos sin datos privados y comprobaciones proporcionales al cambio. Mantén alineadas las guías en inglés y español y conserva comandos, claves de esquema, IDs, enums y nombres de archivos de la bóveda.

## Licencia

El producto se distribuye bajo la [licencia MIT](LICENSE). Los recursos documentales adaptados se identifican por separado en los [avisos de terceros](THIRD_PARTY_NOTICES.md).

## Soporte

Usa [GitHub Issues](https://github.com/unsulabs/Obsidian-Bussines-Brain/issues) para preguntas del producto, reportes de errores y propuestas de mejora. Incluye la versión pertinente, el entorno y una reproducción sintética; elimina rutas privadas, fuentes y credenciales antes de publicar.

## Reconocimientos

La organización del README adapta [Best-README-Template](https://github.com/othneildrew/Best-README-Template/tree/fc444eb7b04b2e4863f6080b1507a219e95103fa), publicado bajo The Unlicense. Otras herramientas documentales adaptan [ai-cursor-init](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). Consulta [atribución y licencias](THIRD_PARTY_NOTICES.md).

La metodología original y las referencias operativas permanecen en español; el [índice documental](docs/es/README.md) ofrece guías equivalentes e identifica las fuentes preservadas.

[Volver arriba](#obsidian-bussines-brain)
