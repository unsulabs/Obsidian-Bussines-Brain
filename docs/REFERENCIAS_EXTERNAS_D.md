# Referencias locales para la migración D

`scripts/referencias_externas.py` registra referencias versionadas a archivos
locales ya autorizados. No transforma documentos, código ni AGENTS.md en una
transcripción. Nunca copia fuentes al banco/bóveda, ejecuta su contenido ni usa
servicios externos. El banco privado conserva únicamente metadatos y permisos.

## API para el operador

El operador resuelve una ruta local canónica y suministra datos de su auditoría,
incluidos los bytes/hash esperados. No debe completar lectura, propietario o
autoridad con inferencias del nombre de archivo.

```python
from referencias_externas import (
    register_reference, reference_ref, record_external_decision, verify_references,
)

metadata = {
    "reference_id": "ER-fuente-primaria",  # identidad estable, sin datos privados
    "locator": {"kind": "local_file", "value": "/ruta/canónica/fuente.md"},
    "owner": "Propietario declarado",
    "authority": "Facultad declarada para esta fuente",
    "evidence": ["Referencia concreta a la autorización/auditoría"],
    "source_type": "primary",  # primary | control | external_reference
    "note_ids": ["F-ficha-legada"],  # sólo primarias pueden respaldar estas fichas locales
    "admissibility": "admissible",  # historical_only/rejected no sirven para aplicar
    "sha256": sha_observado,
    "byte_length": cantidad_bytes_observada,
    "access_state": "available",
    "reading_state": "complete",  # declaración del operador; hashing no demuestra lectura
    "reading_evidence": ["Auditoría y pasajes efectivamente leídos"],
    "sensitivity": "interno",
    "dependencies": [],
}
preview = register_reference(bank, metadata)  # no crea archivos
record = register_reference(bank, metadata, commit=True)
ref = reference_ref(record)
scope = {"company": company_id, "audience": audience, "purpose": "local_analysis"}
decision = {
    "reference_id": record["reference_id"], "version_id": record["version_id"],
    **scope, "action": "grant", "authority": "Responsable con facultad declarada",
    "evidence": ["Autorización específica verificable"],
    "decided_at": fecha_utc_iso8601,
}
record_external_decision(bank, decision, commit=True)
verified = verify_references(bank, [ref], scope, require_read=True, require_internal=True)
```

Repetir la decisión con `purpose="internal_query"` requiere autoridad para esa
finalidad: el grant de análisis no la concede. Una revocación usa `action="revoke"`
en la misma identidad/versión/empresa/audiencia/finalidad. No modifica el grant
anterior: agrega un evento a una cadena con secuencia y hash previo. El sistema
registra declaraciones, no autentica identidad humana ni suplanta un ACL del SO.

Los registros viven en `referencias_externas/versions/EV-<hash>.json` y
`referencias_externas/permissions/<secuencia>.json` del banco. La versión se
calcula a partir de **todos** los metadatos y dependencias: cambiar archivo,
lectura, localizador, propietario o admisibilidad produce una versión nueva.
Los registros previos siguen disponibles; permisos de la versión vieja no se
heredan. Un archivo con los mismos bytes puede tener referencias distintas si
su contexto o autoridad son diferentes.

## Dependencias y límites

`reference_ref(record)` devuelve
`{kind:"external", reference_id, version_id, sha256}`. Una dependencia TR usa
`{kind:"transcript", tr_id, version_id, sha256}`. El verificador recorre el cierre
transitivo y exige el permiso exacto para cada fuente, incluso si el padre está
autorizado. Rechaza hashes discrepantes de la misma dependencia, permisos
revocados, registros alterados, symlinks, lectura insuficiente y fuentes
rechazadas o sólo históricas. `require_internal=True` impide que una fuente
confidencial/restringida pase a la bóveda por una bandera falsa del candidato.

`verify_references` devuelve `snapshot_sha256` del conjunto efectivo verificado.
Incluye decisiones, versiones y dependencia TR; cambios ajenos al conjunto no lo
invalidan. Un adaptador debe guardar ese snapshot y volver a comprobarlo antes
de preparar/aplicar, junto con hashes objetivo y autorización del lote. No debe
inferir dependencias de una ruta de archivo ni permitir que un kind omita
permisos. El motor de integración D todavía se implementa por separado.

Un localizador remoto puede registrarse únicamente como metadato no verificado,
sin bytes/hash ni lectura acreditada. No es utilizable como evidencia de
aplicación. No hay conector, descarga, sincronización, autenticación remota ni
dependencia de Dropbox en esta unidad.

Los estados `partial`/`unread` conservan lo observado. Una referencia parcial
puede usarse sin fingir lectura completa cuando el registro contiene
`read_spans=[{start,end,sha256}]` de pasajes efectivamente leídos y el consumidor
solicita `reference_ref(record, spans=[...])`. Los offsets son bytes UTF-8 con
fin exclusivo. El módulo verifica los hashes de todos los pasajes y exige que
cada intervalo solicitado esté contenido en la unión de los intervalos leídos.
Pasajes contiguos pueden cubrir un solicitado; un hueco o extremo fuera de lo
leído impide usarlo. La selección de pasajes y las razones siguen siendo
declaraciones del operador; un hash no acredita interpretación semántica.
La referencia conserva `reading_state=partial`. Sin `spans` explícitos, una
referencia parcial sigue bloqueada. Las dependencias transitivas conservan esos
rangos y el snapshot incluye la selección exacta del consumidor.

Desactivar `require_read` permite inventariar acceso
técnico, no convertirlo en lectura semántica. No se debe usar esa opción para
eludir los gates de los candidatos D.

## Comprobación sintética

`python3.11 -m unittest discover -s tests -p test_referencias_externas.py -v`
comprueba dry-run, no copia, versiones, grants exactos/idempotentes, revocación,
dependencias transitivas externas/TR, archivo alterado, symlink, admisibilidad,
lectura/sensibilidad, metadatos remotos no verificados y cadena alterada.
Evidencia en `_verify/referencias-externas/`; no equivale a aprobación del dueño
ni aceptación del adaptador de aplicación D.
