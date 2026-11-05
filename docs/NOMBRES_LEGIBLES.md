# Nombres legibles e identidad estable

Las notas nuevas muestran en el explorador un asunto breve y reconocible. El identificador (`doc_id`, `source_id`, `capture_id`, `session_id` o `id`) permanece en las propiedades y se usa para recuperar la nota, validar la unicidad y enlazar revisiones. Un nombre puede cambiar sin cambiar la identidad ni el estado editorial. No se infiere un área, departamento u oferta a partir del nombre.

La CLI crea nombres desde el título proporcionado para D/X, fichas, fuentes y capturas. En continuidad usa la fecha y la primera línea del resumen. Los nombres se normalizan a Unicode NFC, se quitan caracteres incompatibles con rutas y se rechazan colisiones, incluso con diferencias sólo de mayúsculas. Los comandos de lectura buscan el ID en las propiedades, no deducen una ruta `ID.md`.

Para una bóveda existente, `scripts/nombres_legibles.py` recibe una especificación privada JSON `{"notas":[{"id":"D01","nombre":"Dirección y modelo empresarial"}]}`. El diagnóstico sin `--apply` produce `sha_plan`, rutas y enlaces afectados. La aplicación exige ese SHA exacto y una carpeta de respaldo nueva fuera de Git y de la bóveda. Renombra los archivos, actualiza enlaces wiki y nodos de archivo de Canvas, valida y conserva los bytes originales en el respaldo. Hay que cerrar Obsidian y descartar cambios concurrentes antes de aplicar. Los vínculos en otros formatos que apuntan a rutas antiguas bloquean la operación para que se traten explícitamente. Las Bases no forman parte de esta migración.

Ejemplo de diagnóstico:

```sh
python3 scripts/nombres_legibles.py --vault /ruta/privada/empresa --spec /ruta/privada/nombres.json
```

La aplicación requiere `--apply --sha-plan SHA_DEL_DIAGNOSTICO --backup-dir /ruta/privada/respaldo-nuevo`. Para revertir, cerrar Obsidian, verificar que los archivos actuales coinciden con el manifiesto posterior y restaurar únicamente las rutas del manifiesto desde el respaldo, incluyendo los enlaces afectados. Si hubo cambios nuevos después de la migración, no restaurar a ciegas: preparar una reversión que los conserve.
