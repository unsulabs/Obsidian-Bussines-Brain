# Mantener y evolucionar el repo sin recrearlo

La primera versión es una plataforma **candidata**: contiene código probado localmente y diseños a validar en empresas sintéticas y reales autorizadas. En cada nueva sesión de desarrollo:

1. Abrir este repositorio maestro, no una instancia privada. Leer `AGENTS.md`, `docs/ARQUITECTURA.md`, `docs/DECISIONES_ABIERTAS.md`, `docs/HOJA_DE_RUTA.md` y los cambios recientes; inspeccionar estado Git y versión Python.
2. Ejecutar `python -m unittest discover -s tests -v`, y comparar salida observada con `docs/CRITERIOS_DE_ACEPTACION.md`. No modificar datos de empresas reales durante tests.
3. Elegir un **caso empresarial concreto** que actualmente falla, no un plugin llamativo. Registrar problema, fuente/evidencia, contrato esperado, alternativa existente y prueba positiva + negativa.
4. Primero evaluar fuentes oficiales y recursos ya catalogados; si un plugin está archivado o la licencia es ambigua, tratarlo como referencia de diseño hasta resolverlo.
5. Cambio incremental con compatibilidad hacia atrás: esquema versionado, herramienta de migración en simulación, respaldo y rollback antes de cambiar una instancia.
6. Tras implementación ejecutar tests, prueba sintética de extremo a extremo, comprobación visual solo cuando hay GUI y caso de continuación en otra sesión. Registrar qué no pudo probarse.
7. Actualizar docs, decisiones y changelog. Pedir aprobación antes de instalar/desplegar/transferir o alterar fuentes de autoridad.

**No copiar** el contenido de `investigacion/` a instancias de empresas como si fuera información verdadera. **No** poner `instancias/`, claves, `.env`, base de clientes ni contratos privados en GitHub.
