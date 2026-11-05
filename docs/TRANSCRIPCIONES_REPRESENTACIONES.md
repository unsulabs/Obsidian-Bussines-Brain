# Representaciones auxiliares verificadas

`scripts/transcripciones_representaciones.py` ofrece la API Python
`importar_representacion` (alias `import_representation`). No incorpora un comando
CLI. Añade vistas de una versión canónica existente, sin cambiar su preferencia,
crear otra conversación ni resolver identidades humanas.

```python
importar_representacion(
    bank, tr_id, version_id,
    artifacts={"dom_source": dom_json_path, "with_speakers": headered_path,
               "html": html_path},
    expected_hashes={"dom_source": sealed_dom_sha256,
                     "with_speakers": sealed_headered_sha256,
                     "html": sealed_html_sha256},
    company="empresa", audience="equipo", commit=False,
)
```

Los hashes deben proceder de la entrega/revisión sellada que el caller verificó.
Calcularlos del mismo archivo modificado justo antes de llamar no acredita su
procedencia. La API prueba correspondencia con los hashes entregados; no autentica
al operador ni infiere permiso del contenido. `company` y `audience` son obligatorios;
el ledger debe otorgar `local_analysis` exactamente al TR, versión y ámbito antes
de leer originales o auxiliares. Custodia sola no basta. Se registra el snapshot
del ledger usado; no es autorización para lecturas futuras. Un consumidor debe
revalidar su finalidad y los hashes antes de acceder a los blobs.

`artifacts` y `expected_hashes` deben tener exactamente las mismas claves. Son
obligatorias `dom_source` y `with_speakers`; se admiten otros roles seguros para
HTML, revisión u otros bytes auxiliares. Todos se conservan íntegros, sin interpretar
instrucciones en su texto. El manifiesto registra path de procedencia, hash y tamaño.
Los bytes originales del DOM incluyen todos los campos adicionales, incluso HTML,
metadatos y etiquetas que no aparecen en el mapa derivado.

El adaptador `provider-groups-lf-v1` espera JSON con `meeting_id` coincidente con la
ocurrencia registrada, `sha256`, `with_speakers_sha256` y `groups`. Cada grupo contiene
`header` literal y `sentences`; cada sentencia tiene `id`, `source_id`, `text` no
vacíos. Los IDs de sentencia son únicos; textos iguales con IDs distintos son
válidos. Si están presentes, `sentence_count`, `first` y `last` se cotejan. Otros
campos quedan preservados como evidencia del proveedor, sin elevarlos a garantía.

La reconstrucción debe ser exacta, incluyendo puntuación, espacios, Unicode y
ausencia/presencia de salto final:

```python
raw = "\n".join(s["text"] for g in groups for s in g["sentences"])
headered = "\n\n".join(g["header"] + "\n" +
                       "\n".join(s["text"] for s in g["sentences"])
                       for g in groups)
```

No se normalizan saltos de línea ni se agrega un salto final. Ambos resultados UTF-8
se comparan byte a byte; raw debe ser el original custodiado de la versión y ambos
hashes declarados en el DOM deben coincidir. Otro formato exige un adaptador explícito,
no heurísticas que alteren texto. El caller debe proporcionar todo el DOM, no sólo
la página visible o una muestra.

El esquema `modelo/transcripciones/representacion.schema.json` contiene grupos y
sentencias con offsets absolutos en bytes UTF-8, intervalos `[start,end)`, sobre
raw y headered. Los rangos de sentencia excluyen separadores; los de grupo incluyen
separadores entre sus sentencias, pero excluyen el separador entre grupos. En
headered, el rango del grupo incluye su header. Los ordinales empiezan en cero.
`provider_sentence_id` y `provider_source_id` enlazan pasajes repetidos sin búsquedas
ambiguas por texto. `provider_header` siempre conserva el literal, la atribución
permanece `etiqueta_proveedor_sin_resolver` y `resolved_entity_id` es null.
Sólo un token terminal HH:MM:SS de dos dígitos por campo, separado por espacio o
al inicio del header, produce `time_seconds`; concatenaciones, MM:SS y formatos
ambiguos conservan null. El tiempo es una lectura de formato, no identidad ni
verificación de alineación audiovisual.

En dry-run no se crea ningún archivo. Commit usa el lock común del banco y valida
otra vez dentro de él. Los blobs inmutables se escriben primero bajo
`representaciones/blobs/<sha>.bin`; el manifiesto bajo
`representaciones/manifests/REP-<sha>.json` se publica al final. Sólo manifiestos
publicados hacen visible una representación. Una interrupción deja como máximo
blobs sin referencia y reintentar la misma llamada completa la escritura. Una
representación existente se coteja, nunca se repara silenciosamente.

El ID se deriva del manifiesto completo salvo el propio ID: incluye bytes,
procedencia, ámbito y snapshot de permisos. La misma llamada sin cambios es
idempotente; correcciones de headers o metadatos, cambios de procedencia o snapshot
generan otro ID sin sobrescribir. Esta API no establece una representación preferida
ni marca una corrección como aprobada. El banco debe estar fuera de Git y bóveda,
según los mismos controles compartidos de custodia.

Verificación sintética dirigida:

```bash
python3.11 -m unittest discover -s tests -p test_transcripciones_representaciones.py -v
```

Estas pruebas verifican integridad y controles técnicos; no aceptan semánticamente
una fuente real, resuelven hablantes ni prueban completitud de la reunión.
