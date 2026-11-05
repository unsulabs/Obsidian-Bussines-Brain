# Integración transaccional local de transcripciones

`scripts/transcripciones_integracion.py` implementa U20/U31. Su resultado es
integridad técnica de archivos; no certifica análisis semántico, consentimiento
ni aceptación empresarial. La aplicación real corresponde al coordinador después
de resolver la bóveda con `obsidian-router`, comprobar autorización y ensayar
backup/restauración en una copia. El módulo no elige la bóveda por ventana activa.

## Interfaces

```python
manifest = prepare_batch(candidates, {
    "vault": "/ruta/canónica/bóveda",
    "backup_dir": "/ruta/privada/respaldos",
    "bank_root": "/ruta/canónica/banco",
    # "hashes": {"ruta/relativa": "sha256"},  # opcional: snapshot esperado
})
result = apply_batch(manifest, {
    "manifest_sha": manifest["manifest_sha"],
    "scope": "apply_batch",
    "writers_quiescent": True,  # declaración: editores/sincronizadores cerrados
    "responsable": "Persona que autoriza",
    "referencia": "Referencia concreta de autorización obtenida fuera del programa",
}, fencing_token=1)
rollback_batch(manifest)
```

Cada candidato tiene `path` relativo, `content` UTF-8 como string o bytes,
`kind`, `id`; `expected_sha256` opcional (obligatorio para navigation_append)
debe coincidir con los bytes previos, o ser null al crear. El renderer puede
añadir metadatos de trazabilidad; estos no reemplazan frontmatter validado.

Las fichas/vistas requieren `source_refs` (tr_id/version_id/sha256), `scope`
(company/audience/purpose=local_analysis) y `permission_snapshot` de ese conjunto
exacto. Se comprueban permisos efectivos para local_analysis **e internal_query**,
bytes del original, y se incorpora snapshot de consulta al manifest. Si provienen
de un análisis, llevan además tr_id/run_id/analysis_sha256/semantic_review;
se revalidan bundle, cobertura vigente y archivos de revisión ligados por hash.
La navegación derivada hereda `access_checks` completos de cada fuente.
Todos los tipos de candidato requieren dependencias explícitas, incluidos
entidades, D/X y navegación; retirar los controles del renderer no es un bypass.
Las fichas enlazadas por contenido nuevo deben pertenecer a ese conjunto de
dependencias autorizado, además de resolver correctamente como wikilinks.
Prepare y apply reevalúan estas dependencias; una revocación entre ambos detiene
el lote antes de escribir contenido. También se comprueban en cada write.

Sin perfil de destino privado válido, sensibilidad no interna o
`local_private_only=true` rechaza la materialización;
el frontmatter se comprueba independientemente de ese flag. La ausencia de
sensibilidad en una ficha/vista tampoco autoriza exposición. La clasificación
del catálogo no se inventa: renderer recibe atestaciones del operador y usa
restringido cuando faltan. Un [perfil privado autorizado y sellado](DESTINO_PRIVADO_TRANSCRIPCIONES.md)
permite integrar confidencial/restringido sólo para los IDs, destino, empresa y
audiencia explícitos, con permisos vivos y sin rebajar clasificación. No concede
publicación ni acceso a otra bóveda; los guards específicos de cada adaptador
siguen aplicándose.

| kind | Validación específica |
|---|---|
| source | tipo fuente, carpeta directa 50_Fuentes, transcripcion_id/version_id; mantiene identidad y sólo evoluciona versión/run mediante transición verificada |
| transcript_view | tipo transcripcion, bajo 50_Fuentes/Transcripciones, transcripcion_id/version_id; vista existente inmutable, variante explícita cuando otro run requiere nuevos pasajes |
| entity | tipo operativo de `modelo/tipos_entidad.json` (excepto fuente), clase igual a tipo e ID con prefijo del catálogo; carpeta del catálogo o `90_Sistema/Bandeja_Propuestas`; campos comunes completos y fuentes como lista de wikilinks resolubles cubiertos por permisos |
| dx | documento D/X ya existente en 10_Conocimiento; reutiliza `_document`, `_next_revision`, `_check_body` de revisiones_dx; revisión consecutiva |
| navigation | tipo mapa en 00_Mapas |
| base_view | archivo .base **nuevo** bajo 90_Sistema/Vistas/Transcripciones; YAML filters.and con tipo fuente/transcripcion_id y views |
| navigation_append | Inicio.md, 90_Sistema/Como_usar.md o Como_usar.md raíz existente; bytes anteriores como prefijo exacto; identidad/frontmatter preservados; nunca copia el manual entre rutas |

Las notas semánticas sólo admiten borrador/en_revision. No se reemplazan notas
aprobadas o históricas. El append técnico conserva el estado previo y no ratifica
afirmaciones. No hay API de aprobación editorial. Las 16 Bases anteriores nunca
se actualizan mediante este adaptador. La validación de YAML de Bases es
estructural; la ejecución y presentación en Obsidian requiere aceptación GUI.

Las entidades nuevas y sus actualizaciones requieren `estado_conocimiento:
propuesta`, `vigencia: sin_verificar`, `sensibilidad: interno` y `registrado_en`
ISO explícito. El tipo genérico `entidad` no pertenece al catálogo y se rechaza.
Una propuesta nueva no necesita fingir un objetivo existente en `proposal_staging`.
Actualizar preserva ID, tipo y clase y sólo afecta otra propuesta interna sin
verificar en borrador/en revisión. Prepare y apply vuelven a validar este contrato,
incluso si se recalcula el hash de un manifest modificado; la integridad del hash
no sustituye la autorización humana. Las dependencias verificadas se recalculan;
`bound_source_ids` y `verified_external_refs` aportados por el caller no conceden
acceso. Las fuentes siguen requiriendo su adapter específico.

El puente de versión/run y conservación de historial se describe en
[Evolución de fichas TR](EVOLUCION_FICHAS_TR.md).

El renderer nombra fichas nuevas con el título observado saneado; sólo en una
colisión añade un sufijo estable corto. Los IDs completos quedan en propiedades.
Una ficha existente conserva su ruta e identidad. Todos los enlaces se generan
desde esa ruta final; no se renombra material existente ni se copia el manual.

## Preparación, respaldo y recuperación

Prepare no escribe ni en bóveda ni en backup; crea una copia temporal privada
para ejecutar `validar_boveda.validate`, incluyendo enlaces faltantes/ambiguos,
IDs y bloques duplicados y metadatos incompatibles. Rechaza fichas/vistas
duplicadas por transcripción y versión. Devuelve diff completo, SHA base/propuesto,
contenido base64, snapshot de todos los archivos y SHA canónico del manifest.
El adaptador resuelve enlaces a archivos `.base` existentes con ruta exacta o
nombre único, sin silenciar otros fallos del validador Markdown anterior.
El manifest contiene contenido privado: guardarlo fuera de Git, con permisos
restringidos. No imprimirlo en logs públicos.

El backup debe estar fuera de bóveda, repositorio y banco (incluido raw), sin
symlinks. La ruta `bank_root` es obligatoria: el caller debe proporcionar el banco
resuelto. Los nombres relativos rechazan traversal, carpetas ocultas y Plantillas.

Un flock por bóveda vive junto a ésta en `.ce-integracion-<hash>/writer.lock`;
no se anida con locks de revisiones_dx ni de la cola. Su lease es la vida del
descriptor: el sistema operativo lo libera al caer el proceso. El fencing entero
monotónico persistido en ese directorio rechaza tokens anteriores y reutilización
del mismo token por otro lote. Un retry del mismo lote puede usar el mismo token;
un lote nuevo requiere uno superior. El integrador no consume tokens de la cola.

Antes del primer write se compara todo el snapshot y se verifican todos los
respaldos byte por byte. Cualquier cambio previo detiene todo el lote, sin
sobrescribir archivos. El journal externo registra la intención **antes** del
replace atómico individual. Tras una caída se vuelve a llamar apply con el mismo
manifest: distingue base/propuesta usando SHA e intención registrada, y no crea
otra ficha. Los backups no se sustituyen después de empezar la aplicación.

Rollback comprueba todos los archivos afectados y respaldos antes de comenzar.
Restaura sólo la propuesta de ese lote; una edición posterior detiene la
operación. Sólo elimina los archivos creados por el lote que conservan su SHA
propuesto; nunca borra otros archivos ni directorios. También puede reanudarse
tras una caída. Un lote revertido no vuelve a aplicarse: preparar otro manifest.

flock coordina exclusivamente escritores cooperantes. No existe compare-and-swap
atómico de archivos frente a Obsidian u otro editor: para la aplicación real,
cerrar editores/sincronizadores durante el lote. SHA antes de replace detecta
cambios observados, pero no promete excluir la carrera microscópica con un
escritor no cooperante. Una falla a mitad conserva journal/backup; no oculta
el estado parcial con una afirmación de transacción atómica global.

## Verificación sintética

```sh
/opt/homebrew/bin/python3.11 -m unittest discover -s tests -p test_transcripciones_integracion.py -v
```

Prueba prepare sin cambios, aplicación/reintento, restauración exacta, conflictos,
edición posterior, interrupciones antes/después de intención y escritura, backup,
rollback interrumpido, fences, flock, symlinks, IDs/versiones, fuentes/enlaces,
D/X, nuevas Bases y append que conserva el manual. La evidencia está en
`_verify/integracion-c/`. No equivale a prueba GUI ni aplicación en bóveda real.
