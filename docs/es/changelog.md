# Cambios de la edición pública

[English](../../CHANGELOG.md)

## Sin publicar

### 2026-11-05 — Correcciones de instalación desde clon limpio

- Skill de routing propia del repositorio y resolver de solo lectura, con identidad nativa Obsidian verificada, rutas predeterminadas por sistema y selectores/asociaciones de proyecto explícitos. Sustituye el requisito de router externo registrado abajo.
- Rechazo al validar bóvedas inexistentes o que no son directorios; doctor alineado con Python 3.11+.
- Auditoría del checkout compatible con `.venv` raíz ignorado y completamente fuera del índice Git, manteniendo exclusiones de paquetes y exportación.
- Instrucciones equivalentes de registro/preparación y controles probados. Reparación de enlaces conservando la distribución aislada de skills. Consulta el [registro de verificación acotado](testing.md#regresiones-de-instalación-2026-11-05) para fallos de la suite completa, reparaciones dirigidas, comportamiento macOS/Obsidian observado y límites restantes.

### Trabajo documental anterior de la edición pública

- Documentación principal en inglés con preparación, uso, desarrollo y guías técnicas equivalentes en español.
- Separación entre continuidad cotidiana y aceptación de instalación e integración.
- Documentación del router externo, almacenamiento privado e identificadores de runtime sin cambios.
- Adaptación de la estructura documental de ai-cursor-init a la herramienta local inspeccionada; las plantillas genéricas no implican APIs alojadas, bases de datos ni servicios en segundo plano.

## Candidato inicial

- Distribución independiente de software, metodología, skills y ejemplos sintéticos.
- Sirve a negocios, emprendedores y trabajadores por cuenta propia sin restricción geográfica.
- Licencia MIT y guía de contribución; fuentes privadas separadas del producto.
- Exportación con allowlist y manifiesto generado desde el commit distribuido.

Este registro comienza con la edición pública. Sus entradas no certifican aceptación empresarial, publicación de una versión ni una instalación concreta.
