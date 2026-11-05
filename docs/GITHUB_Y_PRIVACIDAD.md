# Repositorio público y datos privados

Versiona exclusivamente software, documentación propia y ejemplos sintéticos. Conserva `.agents/skills/` y `plantilla_boveda/.obsidian/`: forman parte del producto.

Las instancias, fuentes, credenciales y evidencias privadas viven fuera de Git. `.gitignore` y el exportador reducen accidentes, pero no sustituyen la inspección de contenido e historial antes de publicar. Revisa adjuntos, metadatos, rutas, nombres y URLs.

El exportador selecciona archivos de HEAD por allowlist y bloquea contenedores privados en cualquier componente de la ruta. Genera un manifiesto nuevo con hashes y commit de esa distribución. No incorpora cambios sin commit.

Antes de publicar, ejecuta la suite y revisa licencia, avisos de terceros y destino autorizado. Una actualización de código no actualiza automáticamente las bóvedas.
