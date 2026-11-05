# Actualización de producto e instancias

Actualizar el código del **repositorio maestro** no debe tocar una empresa real. Los directorios versionados (`modelo/`, `metodologia/`, `scripts/`, `plantilla_boveda/`, `.agents/`) son el producto; una bóveda contiene conocimiento privado con su propia versión y autoridad.

## Estado de esta versión

- Una bóveda nueva creada desde el candidato 0.4 utiliza `90_Sistema/config_empresa.yaml` con `version_instancia: 0.4.0-rc.1`. Una bóveda anterior puede conservar su número de versión: **no se modifica por actualizar el repositorio**.
- No existe migrador automático desde v0.1 ni desde versiones futuras. Si una empresa ya tiene información en v0.1, NO copiar `plantilla_boveda/` sobre ella.
- La importación vNext 0.9 es una operación no destructiva con preflight, staging y rollback best-effort, pero no un motor de edición concurrente.

## Antes de construir un migrador

1. Inspeccionar y registrar versión/huella/estado de instancia, plugins y esquema; comprobar permisos y cierres de fuentes.
2. Crear respaldo cifrado autorizable con hashes, probar restauración en directorio aislado antes de cambiar originales.
3. Comparar diff de notas/propiedades; no sobrescribir decisiones, acuerdos ni históricos; migrar representaciones derivadas como Bases por separado.
4. Implementar dry-run y plan de reversión que no dependa de una conexión externa. Pedir autorización antes de modo apply.
5. Test con empresa sintética de origen y casos de renombre, duplicados, antiguos templates, datos restringidos y dos modificaciones concurrentes.

`docs/HOJA_DE_RUTA.md` contiene el incremento en el que se desarrollará este componente. **No está implementado en v0.2.0-alpha**.

## Incrementos del piloto 0.3

La rama del piloto incorpora un migrador específico de vistas Bases y un ciclo de revisión documental D/X con previsualización, huellas, respaldo externo, registro de historial y restauración como revisión nueva. **No hay todavía un migrador general y probado de todo el esquema**.

- Las instalaciones existentes conservan sus documentos: NO ejecutar otra vez `crear`, ni copiar toda `plantilla_boveda`.
- Para Bases, usar `scripts/actualizar_vistas_bases.py` en modo diagnóstico, revisar bloqueos y sólo aplicar con respaldo fuera de Git y autorización puntual.
- Para contenido D/X, `previsualizar-dx` y `preparar-dx` no alteran documentos. `aplicar-dx`, `restaurar-dx` y `aprobar-dx` requieren consentimiento explícito; la CLI no prueba identidad.
- La actualización del código en GitHub no cambia por sí misma la versión del contenido, los plugins ni la configuración de la bóveda. Probar en una copia aislada antes de cualquier escritura local.

El procedimiento de aceptación de la Mac de trabajo se encuentra en [CIERRE_DEL_PILOTO_0_3.md](CIERRE_DEL_PILOTO_0_3.md).

## Actualización de la red de conocimiento v0.4

La red Markdown/Canvas se genera únicamente con **mapa-conocimiento** (sin escritura) y **publicar-mapa** (permisos explícitos + SHA original/propuesto + backup externo). No es un migrador de estructura ni modifica documentos, fichas o relaciones originales; no copiar `plantilla_boveda` sobre una bóveda existente.

Si hay un mapa personal previo en la ruta reservada, el publicador rechaza sobrescribirlo. Un mapa derivado antiguo puede regenerarse si se conserva el marcador de propiedad, se contrasta la huella y se autoriza el nuevo resultado. Los 16 archivos .base existentes no cambian por esta funcionalidad: aplicar su migración por separado cuando corresponda y sólo con consentimiento.


La compatibilidad de filtros antiguos usa `recursos/bases_baseline.json`, calculado desde `tests/fixtures_bases_v0_2/`. No es un manifiesto de release ni certificación de esta distribución.
