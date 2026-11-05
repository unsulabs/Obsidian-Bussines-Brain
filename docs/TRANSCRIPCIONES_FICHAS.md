# Fichas propuestas y navegación de transcripciones

`scripts/transcripciones_fichas.py` expone dos funciones puras respecto de escritura.
No publica ni modifica banco o bóveda, no genera entidades por similitud y no
ratifica conocimiento. El caller resuelve Obsidian antes de construir el snapshot.

```python
rendered = render_source(tr_id, run_id, {
    "bank": bank,
    "company": company, "audience": audience, "purpose": "local_analysis",
    "vault_snapshot": {"Inicio.md": original_text},
    "source_sensitivity": {tr_id: "interno"},
})
navigation = propose_navigation(rendered["candidates"], snapshot)
```

`vault_snapshot` contiene rutas relativas y texto UTF-8 exacto. La salida contiene
`candidates`: `path`, `content`, `kind`, `id`, `expected_sha256` (null para crear),
`local_private_only`, sensibilidad, referencias originales y permisos de origen.
El integrador debe volver a verificar originales, ámbito y permisos al preparar y
aplicar. Recibir candidatos no autoriza aplicación; no se debe editar la bóveda
directamente desde esta API.

`source_sensitivity` es una atestación explícita del operador por fuente, no una
inferencia del permiso local. Sin ella la clasificación permanece `restringido`.
La clasificación más restrictiva de todas las fuentes del análisis y de la ficha
existente prevalece. Material confidencial/restringido permanece en staging privado;
este renderer no supera la prohibición de datos protegidos en la bóveda MVP sin ACL.
Otro company/audience/purpose nunca hereda los permisos del análisis.

Se exige cobertura actual mediante `coverage_report`; se vuelven a abrir los
originales custodiados y comprobar sus hashes. La ficha conserva todos los asuntos,
afirmaciones, razones, excepciones, categorías, relaciones y conflictos propuestos.
Un TR produce un F-ID determinista compatible con el modelo. Un snapshot con una
ficha previa del mismo TR conserva su ID y ruta; duplicados bloquean generación.
La lectura de bytes no garantiza completitud de la reunión ni fidelidad semántica.

La vista derivada completa vive bajo `50_Fuentes/Transcripciones/TR/Version.md`;
contiene el raw entero en bloque literal, sin modificar sus bytes custodiados.
Los enlaces ficha→pasaje usan bloques estables derivados del span con hash/offsets;
cada pasaje enlaza al texto íntegro y vuelve a la ficha. El enlace `file://` apunta
al archivo raw existente, sin inventar `#byte`. Los bloques literales escapan fences
del texto externo. Los manifiestos auxiliares se validan por identidad, hashes,
reconstrucción exacta y permiso actual; las etiquetas del proveedor permanecen
sin resolver. No se elige una representación como autoridad preferida.

## Dictamen semántico externo

Opcionalmente `profile.semantic_review` acepta exactamente:

```json
{
  "run_id": "RUN-...",
  "submission_sha256": "hash canónico json_bytes del bundle",
  "submission_path": "/ruta/privada/submission-sellada.json",
  "submission_file_sha256": "hash de bytes exactos sellados",
  "review_path": "/ruta/privada/dictamen.md",
  "review_sha256": "hash de bytes del dictamen sellado",
  "reviewer": "identificador de revisor independiente",
  "status": "reviewed"
}
```

También admite `changes_requested`. `validate_semantic_review` coteja ambos archivos,
el run y el hash canónico de submission contra el bundle. Los hashes deben provenir
de la entrega sellada del revisor. No lee palabras como PASS para inferir aprobación;
la identidad del revisor y su independencia son atestaciones del operador, no
autenticación de esta API local. Dictamen y cobertura mecánica se muestran por
separado. Incluso con dictamen, la ficha queda `en_revision` y `ratified=false`.

## Lotes y navegación

`batch_parent` concilia todos los asuntos con IDs globales y paquetes de máximo
30 asuntos, 30 destinos existentes y 90000 bytes. No son planes empresariales
ya validados: el caller debe razonar arquitectura y convertir esos paquetes al
contrato `plan-conocimiento`. No se crean notas para llenar cuotas. Un asunto
individual mayor al límite bloquea con `SUBJECT_EXCEEDS_BATCH_LIMIT`, sin truncarlo.

`propose_navigation` propone cuatro Bases nuevas en
`90_Sistema/Vistas/Transcripciones/` (Transcripciones, Pendientes, Categorias,
Conflictos), un mapa en `00_Mapas/Corpus de transcripciones.md` y anexos mínimos a
Inicio/Como_usar presentes en el snapshot. Conserva exactamente los textos
personalizados, nunca cambia las 16 Bases existentes ni regenera sus vistas propias.
Inicio/Como_usar sin ID en frontmatter no se proponen: requieren resolver primero
su identidad por el flujo de la bóveda. La navegación transporta `access_checks`
con las dependencias de permisos de cada ficha; también deben revalidarse antes
de integrar y al aplicar.
La navegación sigue siendo derivada y no acredita autoridad. Su aceptación visual
en Obsidian debe probarse aparte.

Pruebas sintéticas: `python3.11 -m unittest discover -s tests -p test_transcripciones_fichas.py -v`.
La suite no acredita aceptación del corpus real ni revisión empresarial.
