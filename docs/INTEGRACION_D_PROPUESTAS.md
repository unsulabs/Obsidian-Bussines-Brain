# Adaptadores D para auditoría y propuestas

La unidad D amplía `transcripciones_integracion.py` usando validadores de
`integracion_d.py` y referencias locales de `referencias_externas.py`.
No sustituye una revisión empresarial: toda nueva redacción empresarial se
guarda exclusivamente como propuesta en Bandeja, sin editar su objetivo.

## Tipos y límites

| kind | Operación admitida |
|---|---|
| legacy_source | Parche de cuerpo de ficha existente no TR en 50_Fuentes; frontmatter idéntico |
| navigation_patch | Parche de cuerpo de mapa/control/manual existente en 00_Mapas, Inicio, Como_usar, Autoridades o Pendientes; estado y frontmatter idénticos |
| control_proposal | Actualización técnica del cuerpo de propuesta existente en 90_Sistema/Bandeja_Propuestas; conserva propiedades e identidad, incluso huella histórica de objetivo |
| proposal_staging | Crea una nota nueva propuesta_de_cambio en Bandeja; borrador/propuesta/sin_verificar y objetivo_id/huella_objetivo exactos; nunca actualiza una nota empresarial |

Los tres tipos de parche exigen `patches=[{old,new},...]`: cada old debe aparecer
exactamente una vez en el cuerpo, y su aplicación debe reproducir íntegramente
el candidato. No puede tocar la cabecera YAML. Una corrección de navegación
puede conservar estado aprobado previo sin ratificar afirmaciones nuevas; sólo
admite los tipos y ubicaciones indicados, no documentos D/X, investigación ni
descubrimiento. Una nota de control no se fuerza a `tipo: documento`.

## Paquete del candidato

```python
candidate = {
    "path": "90_Sistema/Bandeja_Propuestas/Propuesta revisable.md",
    "id": "PROP-cambio",
    "kind": "proposal_staging",
    "content": texto_propuesta_con_frontmatter,
    "expected_sha256": None,  # creación; los parches requieren SHA actual exacto
    "scope": {"company": company_id, "audience": audience, "purpose": "local_analysis"},
    "external_refs": [candidate_ref, review_ref],
    "candidate_ref": candidate_ref,
    "target_binding": {"path": ruta_relativa_objetivo, "id": objetivo_id, "sha256": sha_actual_objetivo},
    "review_binding": {
        "review_ref": review_ref,
        "candidate_sha256": sha_bytes_candidato,
        "target_id": objetivo_id,
        "target_sha256": sha_actual_objetivo,
        "decision": "staging_only",  # technical para los otros tres tipos
        "reviewer": nombre_revisor_declarado,
        "evidence": [referencia_dictamen_y_alcance],
    },
}
manifest = prepare_batch([candidate], {"vault": vault, "bank_root": bank, "backup_dir": backup})
```

Registrar previamente el archivo de candidato y el dictamen como referencias
externas `source_type=control`, con sus hashes observados y permisos exactos
para `local_analysis` e `internal_query`. El hash de `candidate_ref` debe ser
idéntico al contenido que se propone escribir. `review_binding` es declaración
del operador vinculada a versión del dictamen, candidato y objetivo; no es firma
digital ni validación automática del razonamiento del juez.

Los archivos originales autorizados se registran como primarios. Sus dependencias
se declaran en los registros de control; el cierre transitivo se verifica completo,
incluidas fuentes TR. Una primaria puede declarar `note_ids` de fichas legadas
que representa. Los wikilinks nuevos a esas fichas requieren esa correspondencia
versionada, además de permisos actuales. Una referencia de control no puede
autoconcederse vinculación primaria cambiando la bandera del candidato.

`external_refs` también puede vivir dentro de cada `access_checks` junto a su
scope. Se conserva la API TR previa; los tipos D exigen, además, referencias
externas verificadas para candidato y revisión. No existe exención de permisos
por kind. El integrador fija snapshots de análisis/consulta y los vuelve a
comprobar al preparar, aplicar y restaurar. Sensibilidad no interna, revocación,
hash diferente o pasaje parcial fuera del alcance bloquean el lote.
Los kinds C anteriores no admiten añadir `external_refs` para eludir el contrato
de revisión D. El archivo candidato de control requiere cotejo completo de sus
bytes; sus fuentes primarias pueden conservar lectura parcial con spans acotados.

Un archivo externo usado como dependencia no puede ser también un destino
mutable del mismo lote: evitaría revalidación y restauración seguras. Los
objetivos de `proposal_staging` y `control_proposal` tampoco pueden aparecer
como archivos a modificar en ese lote.

## Aplicación y recuperación

Usa la autorización técnica y fencing de C, con `writers_quiescent=True`.
Prepare sigue sin escribir en bóveda/backup. Manifest contiene bytes base para
comprobar que el parche conserva metadatos; el snapshot/diff es privado.
Apply usa el mismo lock, backup externo, journal de intención y replace atómico.
Reintentos conservan idempotencia y no vuelven a crear una propuesta.

Rollback D comprueba dependencias actuales y permisos antes de restaurar. Si se
revocó una fuente, cambió un archivo externo o hubo una edición posterior,
rechaza sin sobrescribir. Resolver la causa mediante decisión autorizada o nueva
propuesta; no borrar journal, falsificar grants ni editar hashes a mano. Esto no
promete atomicidad global frente a editores no cooperantes: mantener la quiescencia
durante aplicación y restauración, igual que C.

## Validación

`python3.11 -m unittest discover -s tests -p test_integracion_d.py -v`
ejercita los cuatro tipos, estado aprobado preservado en navegación, objetivo
empresarial intacto, propuesta nueva en borrador, rollback exacto, interrupción,
edición posterior, permiso transitivo revocado, fuente alterada, sensibilidad
restringida y revisión/parche inválidos. Sólo fixtures sintéticos. Evidencia en
`_verify/integracion-d/`; pendiente aceptación independiente y aplicación real.

La evolución de una ficha TR existente es una unidad separada descrita en
[Evolución de fichas TR](EVOLUCION_FICHAS_TR.md); su aceptación se verifica por
separado de los adaptadores D.
