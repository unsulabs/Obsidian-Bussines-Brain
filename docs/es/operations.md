# Operaciones locales y recuperación

[English](../en/operations.md) · [CLI](cli-reference.md) · [Pruebas](testing.md)

## Actualizar producto e instancia

Actualizar el checkout no actualiza automáticamente una empresa privada. No repetir `crear` ni copiar `plantilla_boveda/` sobre bóveda existente. Versión, contenido, plugins y permisos pertenecen a su instancia. No hay migrador general probado para todos los esquemas históricos/futuros. Las migraciones acotadas siguientes tienen guards distintos y no deben generalizarse.

Antes de un cambio autorizado: resolver bóveda con `obsidian-router`; revisar configuración/autoridad; identificar archivos/versiones; crear respaldo privado externo y ensayar restauración aislada; revisar diff; detener escritores; aplicar alcance aprobado; verificar hashes y utilidad. Conservar cambios ajenos. Un checkout sucio puede requerir copia aislada para atribuir aceptación a un commit; no justifica descartar trabajo ni bloquear consulta cotidiana.

## Diagnóstico de Python y rutas

Primero `python scripts/cerebro.py doctor`: sólo lectura y anterior a dependencias. Ante módulo ausente, comprobar ejecutable y entornos existentes; probar `import yaml, jsonschema` con el intérprete previsto. En macOS puede existir `/opt/homebrew/bin/python3.11`, sin asumirlo. Instalar `requirements.txt` sólo con autorización aplicable. Registrar intérprete usado.

El guard de `scripts/documentos.py` sólo admite ancestros nativos macOS verificados `/var` → `/private/var` y `/tmp` → `/private/tmp`, comprobando readlink y resolución física. Symlinks del usuario, archivos de entrada y otros aliases siguen rechazados; fuera de Darwin no hay excepción. No debilitar guards para un fixture. La aceptación macOS prueba temporales predeterminados, `TMPDIR=/tmp` y `TMPDIR=/private/tmp`, manteniendo negativos de symlink. Cambiar TMPDIR solo no prueba corrección.

## Revisiones D/X y promoción editorial

`previsualizar-dx` sólo lee. `preparar-dx` crea PRDX JSON y `.snapshot` en `90_Sistema/Propuestas_DX`, sin cambiar documento. `aplicar-dx` comprueba SHA original/candidato, conjunto de fuentes cuando cambia y respaldo externo. Guarda historial interno en `90_Sistema/Historial_DX`, reemplaza atómicamente y valida; si falla intenta restaurar. Conservar IDs de bloque; revisión ordinaria no los elimina/renombra silenciosamente. Rechaza aprobados/retirados. Aplicación exitosa queda en revisión.

`restaurar-dx` exige autorización nueva y SHA actual, produce **nueva revisión** desde historial. No rebobina contador ni borra historia. Locks CLI coordinan escritores propios, no Obsidian.

`evaluar-dx` registra G1–G7 humanos sin cambiar documento. Sólo recomendación integral válida, cobertura suficiente, SHA exacto, autorización explícita, respaldo y literal `APROBAR <doc_id> <primeros 12 caracteres SHA>` permiten `aprobar-dx`. Cuerpo idéntico, revisión nueva. Estado editorial no prueba vigencia financiera/contractual ni identidad humana autenticada.

## Integración de lotes TR

Son funciones Python locales; no existe una CLI de integración inventada:

```python
manifest = prepare_batch(candidates, {
    "vault": "/private/business-vault",
    "backup_dir": "/private/backups/batch-001",
    "bank_root": "/private/transcript-bank",
})
# Sólo con autorización auténtica y específica, y escritores detenidos:
result = apply_batch(manifest, {
    "manifest_sha": manifest["manifest_sha"],
    "scope": "apply_batch",
    "writers_quiescent": True,
    "responsable": "Operador autorizado",
    "referencia": "Referencia a la autorización real",
}, fencing_token=1)
# Una recuperación posterior autorizada puede usar rollback_batch(manifest).
```

Importar desde `scripts/transcripciones_integracion.py` en el entorno de scripts. `prepare_batch` no escribe bóveda/respaldo: valida overlay en copia temporal privada y devuelve diff/snapshot/manifiesto completo privado. Contiene bytes base/propuestos: guardarlo privado. `bank_root` es obligatorio; respaldo fuera de bóveda, repositorio y banco, sin symlinks.

Apply revalida bytes, permisos y snapshot entero antes del primer write, y acceso en cada write. Usa `flock` cooperante junto a bóveda, fencing monotónico persistente y journal externo de intención antes de cada reemplazo atómico. Nuevo lote necesita token superior; retry idéntico puede reutilizarlo. No consume tokens de cola. No es lote globalmente atómico ni compare-and-swap contra editores arbitrarios.

Tras caída, reintentar mismo manifiesto distingue base/propuesta por journal/SHA. No reemplazar respaldos establecidos. Rollback precomprueba archivos/respaldos, restaura sólo propuesta del lote y elimina sólo archivos nuevos intactos propios. Edición posterior bloquea sobrescritura/borrado ciego. Lote revertido no se reaplica; preparar otro. Rollback D también revalida referencias/permisos actuales; revocación puede requerir resolución autorizada, nunca grants inventados ni hashes editados a mano.

## Filtros Bases

Las 16 Bases de plantilla excluyen `90_Sistema/Plantillas` y filtran Markdown para no presentar plantillas como ofertas/documentos reales. Bóvedas existentes usan `scripts/actualizar_vistas_bases.py`, primero sin `--apply`.

| Diagnóstico | Significado |
|---|---|
| `LISTO` | Vista baseline original elegible. |
| `LISTO_FILTRO` | Presentación personalizada con filtro semánticamente original. |
| `AL_DIA`, `AL_DIA_PERSONALIZADO` | Filtro actualizado, quizá presentación personalizada. |
| `BLOQUEADO_PERSONALIZADO`, `BLOQUEADO_FALTANTE` | Detener: no forzar filtro empresarial modificado ni vista ausente. |

Después de observar GUI, cerrar Obsidian y sincronizadores, **luego regenerar plan actual**. El autoguardado puede reserializar legítimamente `.base` y `workspace.json`; no restaurar bytes viejos por fuerza. Revisar/conservar `sha_plan` exacto. Con autorización limitada a filtros raíz:

```bash
python scripts/actualizar_vistas_bases.py --vault /private/business-vault
python scripts/actualizar_vistas_bases.py --vault /private/business-vault \
  --backup-dir /private/backups/bases-001 --sha-plan SHA_FROM_CURRENT_PLAN --apply
```

Respalda las 16 vistas actuales y workspace existente. Reemplaza sólo `filters` elegible, conserva bytes desde `views:` incluyendo `groupBy`, columnas, tabs y comentarios, valida estructura ajena. Cambios concurrentes causan conflicto/recuperación; `workspace.json` se respalda sin restauración automática. Reabrir GUI, comprobar que ofertas/documentos excluyen plantillas y D01/fuentes no cambian. Esperado: cero pendientes/bloqueadas. YAML válido no prueba GUI. No cambia fuentes, permisos, Sync ni plugins.

## Nombres legibles

Notas nuevas tienen títulos legibles e IDs estables en propiedades. Renombres existentes usan `scripts/nombres_legibles.py` y especificación privada como `{"notas":[{"id":"D01","nombre":"Dirección empresarial"}]}`. Preview muestra rutas, enlaces y `sha_plan`; apply exige ese SHA y carpeta de respaldo externo nueva.

```bash
python scripts/nombres_legibles.py --vault /private/business-vault --spec /private/names.json
# Añadir sólo después de revisión autorizada:
# --apply --sha-plan SHA_FROM_CURRENT_PLAN --backup-dir /private/backups/names-001
```

Cerrar Obsidian y excluir cambios concurrentes. Actualiza wikilinks/nodos Canvas, valida y conserva bytes originales. Otros formatos de enlace a rutas antiguas bloquean para tratamiento explícito; Bases queda fuera. Para revertir, comparar estado con manifiesto posterior y restaurar sólo rutas/enlaces del manifiesto. Si existen ediciones posteriores, preparar reversión que las conserve.

## Mapas derivados y cierre cotidiano

`mapa-conocimiento` previsualiza; `publicar-mapa` exige autorización, confirmación literal, SHA anterior/nuevo y respaldo. Rechaza mapa personal ajeno en ruta reservada. Regenerar sólo mapa derivado propio; no copiar plantillas ni cambiar notas/relaciones/Bases. Actualidad de mapa nunca acredita autoridad.

Cerrar con archivos/IDs cambiados, checks exactos y pendientes materiales. Aceptación de instalación/migración incluye ensayo aislado y GUI; continuidad cotidiana no exige repetir aceptación completa ni segunda computadora. Referencias: [actualizaciones](../ACTUALIZACIONES_Y_ROLLBACK.md), [Bases](../BASES_FILTROS_Y_ACTUALIZACION.md), [nombres](../NOMBRES_LEGIBLES.md), [rutas macOS](../COMPATIBILIDAD_MACOS_RUTAS.md), [revisiones](../REVISIONES_DX_CON_HISTORIAL.md), [cierre piloto](../CIERRE_DEL_PILOTO_0_3.md), [aceptación existente](../../guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md).
