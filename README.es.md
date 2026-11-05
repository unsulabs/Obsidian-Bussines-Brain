# Obsidian-Bussines-Brain

[English](README.md) · [Documentación](docs/es/README.md) · [Licencia MIT](LICENSE)

Un espacio privado de conocimiento empresarial respaldado por fuentes para negocios, emprendedores y trabajadores por cuenta propia. Trabaja con Codex para convertir conversaciones, decisiones y formas de trabajar en conocimiento útil en Obsidian.

El repositorio contiene software, metodología, instrucciones para agentes y ejemplos sintéticos. El conocimiento empresarial vive en una bóveda privada de Obsidian separada; las transcripciones originales, en un banco privado separado. Es una herramienta local operada durante una sesión del agente, no un servicio alojado ni un proceso en segundo plano. Codex y los conectores opcionales tienen sus propias condiciones de acceso y tratamiento de datos.

## Empieza según tu situación

| Tu situación | Entrada |
| --- | --- |
| Usas el producto por primera vez | [Empieza aquí](EMPIEZA_AQUI.md) |
| Ya existe una bóveda del negocio | [Continúa con Codex](PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md) |
| Usar o actualizar conocimiento | [Guía de uso](docs/es/user-guide.md) |
| Cambiar el producto | [Guía de desarrollo](docs/es/development.md) |

Necesitas Python **3.11 o posterior**, los paquetes de `requirements.txt` y Codex con acceso comprobado a archivos y comandos para el flujo asistido. Obsidian Desktop muestra la bóveda; comprueba Bases y CLI en tu instalación. Sigue la [preparación](docs/es/onboarding.md) para configurar el entorno y distinguir una bóveda nueva de una existente.

**Dependencia externa:** el trabajo asistido sobre una bóveda existente requiere `obsidian-router`, un registro local de destinos y verificación contra Obsidian. Clonar no los instala. Si no se verifica el destino, conserva el trabajo autorizado fuera de la bóveda y deja su acceso pendiente. Una ruta explícita del CLI no reemplaza las comprobaciones de routing del agente.

## Qué puedes construir

- Conservar fuentes autorizadas con procedencia, sensibilidad y permisos por finalidad.
- Desarrollar conocimiento operativo desde evidencia y criterio del dueño, distinguiendo propuestas y contenido aprobado.
- Recuperar pasajes, mantener revisiones y navegar notas Markdown, vistas Bases y mapas Canvas.
- Comprobar una tarea empresarial real y una pregunta que deba conservar incertidumbre, por separado de la validación estructural.

No se presupone país, moneda, régimen fiscal, forma jurídica, departamentos ni personal contratado. Lo desconocido permanece desconocido. La salida de IA sigue siendo propuesta hasta la verificación y decisión pertinentes. El producto está en desarrollo: las pruebas automáticas no acreditan exactitud empresarial, cumplimiento normativo, recuperación semántica ni compatibilidad GUI.

## Privacidad y distribución

No incluyas fuentes reales, datos personales, credenciales ni evidencia de clientes en commits, issues o pull requests. Las etiquetas de sensibilidad son metadatos; Obsidian no aplica control de acceso por nota. Los mapas y vistas son navegación derivada, no autoridad independiente. Publicar, subir datos, instalar plugins e integrar servicios requieren la autorización correspondiente.

Lee [contribución](docs/es/contributing.md), [cambios](docs/es/changelog.md) y el [índice documental](docs/es/README.md). Los originales metodológicos permanecen en español y se identifican como tales. Comandos, claves de esquema, IDs, enums y nombres de archivos de la bóveda conservan sus identificadores.
