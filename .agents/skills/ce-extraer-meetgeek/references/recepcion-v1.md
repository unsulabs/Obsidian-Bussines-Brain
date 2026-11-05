# Recepción MeetGeek v1

Adaptación portable del contrato operativo aprobado el 2026-11-04. Conserva el formato de entrega y el protocolo de sellado; parametriza únicamente el destino. El contrato local `docs/plans/CONTRATO_RECEPCION_V1.md` del workspace original permanece congelado y no es una dependencia del producto distribuido.

Único destino de escritura del extractor: `<bank>/recepcion/meetgeek/<ejecucion>/<cuenta>/<reunion>/<intento>/`. `bank` es la ruta absoluta privada del perfil explícito, verificada antes de escribir; nunca se infiere del cwd ni de la raíz del producto exportado. Verifica la raíz real del producto y cualquier repositorio contenedor de `bank` con Git; rechaza un banco dentro de cualquier árbol Git (aunque esté ignorado), dentro de la bóveda o que escape por symlinks. Si falta el perfil/destino verificable, conserva el trabajo sin iniciar captura y solicita sólo ese destino. La existencia de un directorio no acredita permiso de escritura.

En el workspace original, el mapeo autorizado es `bank = <raiz_workspace_verificada>/banco-transcripciones`, hermano de `cerebro-empresarial/`; comprueba que la raíz contenedora siga fuera de Git antes de utilizarlo. En otro despliegue usa el banco externo configurado, no reproduzcas ese nombre relativo dentro del checkout. Los componentes posteriores a `bank` son identificadores locales seguros, sin barras ni `..`. Cada intento es nuevo e inmutable después de sellado. El extractor es el único operador de navegador y portapapeles; el consolidador sólo lee entregas selladas.

Escribir primero el original íntegro sin corregirlo. Publicar por rename atómico, al final, `capture-manifest.v1.json`, UTF-8, con esta estructura (valores ilustrativos):

```json
{
  "schema_version": "capture-manifest.v1",
  "job_id": "run-20261104",
  "attempt_id": "attempt-001",
  "account": {"id": "cuenta-01", "observed_identity": "identidad visible o desconocida"},
  "meeting": {"id": "id-observado", "url": "https://app.meetgeek.ai/meeting/id-observado", "title": "título observado"},
  "captured_at": "2026-11-04T12:00:00Z",
  "method": "ui-copy-transcript",
  "file": {"path": "original.txt", "size_bytes": 123, "sha256": "64 caracteres hexadecimales"},
  "completeness": "unverified",
  "evidence": {"beginning": "observación del inicio", "ending": "observación del final", "continuity": "cómo se comprobó la continuidad", "gaps": [], "uncertainties": []}
}
```

`completeness`: `complete`, `partial`, `unverified`, `inaccessible`. Sólo `complete` si inicio, final y continuidad fueron comprobados; un hash prueba bytes, no completitud. Para inaccesibles sin archivo usar `file: null`, describir el límite en gaps/uncertainties. No inventar ID, fecha, identidad ni evidencia. `file.path` es relativo al intento, sin escapes ni symlinks. SHA-256 y tamaño se calculan de los bytes guardados. No guardar credenciales.

Inventario y progreso se guardan bajo el mismo prefijo, en `<ejecucion>/<cuenta>/_inventario/<intento>/`, como `inventory.json` y `progress.md`. Inventario: versión, cuenta observada, fecha, secciones inspeccionadas, final de paginación observado o límite, lista de IDs/URLs/títulos/estados e intentos. No confundir inventario con captura. El estado inaccesible no cuenta como descarga. Las dos cuentas conservan procedencias independientes aunque tengan bytes iguales.

Orden: descubrir sesión propia; inventariar; comprobar muestras corta, larga y antigua; escalar sólo con conservación íntegra; priorizar antiguos accesibles; conciliar cada reunión con resultado. No pagar, usar servicios nuevos, interpretar contenido ni modificar código, bóveda o taxonomía. Si falta sesión, pedir abrir/iniciar MeetGeek en el chat extractor. El acceso ausente a la segunda cuenta no bloquea preservar la primera.
