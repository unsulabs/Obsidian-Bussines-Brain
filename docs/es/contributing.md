# Contribuir

[English](../../CONTRIBUTING.md) · [Guía de desarrollo](development.md)

Usa Python 3.11 o posterior y `requirements.txt`. Lee `AGENTS.md` antes de editar. Describe el problema concreto, el comportamiento resultante y la verificación. Preserva trabajo ajeno; añade al staging sólo rutas del cambio.

Usa fixtures sintéticos y rutas temporales. Nunca adjuntes datos empresariales, conversaciones, credenciales ni capturas de instancias reales a issues o pull requests. Reproduce fallos con un ejemplo mínimo inventado. Mantén el producto en este repositorio público y configuración, fuentes y conocimiento de instancias fuera de Git.

Para cambios de runtime ejecuta `python -m unittest discover -s tests -v` desde el entorno verificado y añade una prueba significativa de comportamiento cuando corresponda. Para skills comprueba rutas, instrucciones, alcance y sintaxis. Para documentación verifica enlaces locales, paridad inglés/español, ayuda real de comandos y afirmaciones respaldadas. No traduzcas comandos, flags, claves de esquema, enums, IDs ni nombres de archivos del runtime.

Preserva decisiones y datos de la instancia. No introduzcas país, moneda, impuesto, forma societaria ni organigrama por defecto. Pasar pruebas estructurales no acredita aceptación empresarial; documenta límites materiales.

Mantén procedencia de recursos de terceros y aporta sólo material distribuible. Las contribuciones originales se ofrecen bajo la [licencia MIT](../../LICENSE). La documentación adapta la estructura de ai-cursor-init; ver [flujo documental](documentation-workflow.md) para procedencia y mantenimiento.

Para trasladar una mejora desde un entorno privado, extrae el cambio mínimo de producto e inspecciona contenido e historial. Nunca fusiones ciegamente ramas privadas ni incorpores respaldos. Push, PR, publicación y despliegue requieren intención inequívoca del usuario y cualquier aprobación del sistema.
