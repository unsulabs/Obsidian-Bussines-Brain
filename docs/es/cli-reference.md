# Referencia CLI

[English](../en/cli-reference.md) · [Operaciones](operations.md) · [Contratos TR](transcripts.md)

Comandos, flags, claves y enums conservan su escritura existente. Ejecutar desde raíz del producto con Python que tenga dependencias de `requirements.txt`. Son scripts locales, no endpoints REST. Consultar `--help` por comando; ninguna línea demuestra autorización auténtica.

```bash
python scripts/cerebro.py --help
python scripts/cerebro.py doctor
python scripts/transcripciones.py --help
```

`cerebro.py` no tiene dry-run/commit global. Algunos comandos escriben inmediatamente; revisar tabla. La mayoría exige `--vault`. Resolver destinos existentes antes de leerlos. Rutas siguientes son placeholders sintéticos.

## CLI empresarial: sólo lectura

| Comando | Argumentos adicionales | Comportamiento |
|---|---|---|
| `doctor` | `--vault` opcional | Diagnosticar entorno/dependencias sin instalar. |
| `estado` | `--vault` | Resumen estructural, no completitud empresarial. |
| `validar` | `--vault` | Validar notas, IDs, enlaces y traspasos, no verdad. |
| `tipos` | `--tipo` opcional | Mostrar registro candidato. |
| `buscar` | `--vault --texto`, `--limite` opcional (12) | Búsqueda literal en bóveda. |
| `autoridad` | `--vault --tema --ambito`, `--fecha` opcional | Autoridad exacta declarada en contrato importado; fecha predeterminada hoy. |
| `consulta-contextual` | `--vault --texto`, opcionales `--tema --ambito --fecha --limite` (10), `--orientar` | Candidatos de bloques; ordenamiento opcional no genera respuesta semántica. |
| `plan-conocimiento` | `--vault --archivo` | Validar JSON privado antes de redactar; no crea notas/relaciones. |
| `previsualizar-dx` | `--vault --doc-id --archivo`, `--fuente` repetible | Comparar D/X con borrador externo. |
| `relaciones` | `--vault`, `--id` opcional | Consultar aristas y revisión. |
| `mapa-conocimiento` | `--vault` | Preview Markdown/Canvas, hashes y límites. |
| `aceptacion` | `--vault` | Preflight estructural del piloto, no aceptación del dueño. |

## Creación y escrituras provisionales

| Comando | Argumentos obligatorios | Opciones y efecto |
|---|---|---|
| `crear` | `--id --nombre --dest` | Crear bóveda sin sobrescritura; infraestructura sin conocimiento. Nunca repetir sobre existente. |
| `ficha` | `--vault --tipo --titulo` | `--resumen`, `--archivo`, repetibles `--fuente --etiqueta`; nota tipada borrador. Markdown externo de `--archivo` sin YAML. |
| `fuente` | `--vault --id --titulo --localizador --clase` | `--lectura` = `no_verificada`/`leida_parcial`/`leida_completa`; `--fecha-evento`. Registra referencia sin copiar original. |
| `capturar` | `--vault --titulo --archivo` | `--fuente` repetible; descubrimiento provisional. |
| `documento` | `--vault --clase --titulo --archivo` | `--doc-id`, `--estado` = `borrador`/`en_revision`, `--cobertura`, `--fecha-corte`, repetibles `--fuente --etiqueta`; D/X desarrollado. |
| `proponer` | `--vault --id --motivo --archivo` | Propuesta en bandeja sin cambiar objetivo. |
| `preparar-dx` | `--vault --doc-id --archivo` | `--fuente` repetible; propuesta/snapshot PRDX, conserva D/X actual. |
| `evaluar-dx` | `--vault --doc-id --acta --sha-actual` | Evaluación G1–G7, no aprobación. |
| `relacion-proponer` | `--vault --origen --destino --predicado --fuente --ambito --motivo` | `--fuente` repetible; sólo arista propuesta. |
| `continuidad` | `--vault --resumen --siguiente` | `--revisado-por` opcional; cierre de sesión. |
| `grafo` | `--vault` | `--output` opcional; escribe JSON **dentro** de bóveda, por defecto `90_Sistema/grafo.json`. No es consulta de lectura. |
| `importar` | `--vault --manifest` | `--permitir-real` sólo autorizado y datos internos admisibles; importación vNext-0.9 preparada, no sincronización. |

Coberturas: `sin_fuente`, `parcial`, `suficiente_para_tarea`, `no_aplica`. Sin opción explícita, tener fuentes implica parcial, no suficiente. Flags no acreditan lectura, identidad humana ni condiciones comerciales aprobadas.

## Cambios controlados

| Comando | Controles requeridos |
|---|---|
| `aplicar-dx` | `--vault --propuesta --sha-original --sha-candidato --responsable --referencia-autorizacion --respaldo`; `--sha-fuentes` al añadir fuentes. |
| `restaurar-dx` | `--vault --doc-id --historial --sha-actual --responsable --referencia-autorizacion --respaldo`; crea revisión nueva. |
| `aprobar-dx` | `--vault --evaluacion --sha-actual --responsable --referencia-autorizacion --respaldo --confirmacion`; literal `APROBAR <doc_id> <primeros 12 caracteres SHA>`. |
| `relacion-confirmar` | `--vault --relacion-id --sha-relacion --revisor --referencia-autorizacion --confirmacion`; usar formato literal del runtime. |
| `publicar-mapa` | `--vault --sha-actual --sha-propuesto --confirmacion --respaldo`; sólo mapa derivado autorizado. |

Obtener confirmación exacta del help/preview actual y skill pertinente. No inventar hashes, usar placeholders como aprobación ni editar manifiesto para eludir rechazo. Ver [revisión/restauración](operations.md).

## CLI de transcripciones

Todo comando exige `--bank --profile --request-id --purpose`; `--output` opcional crea reporte inmutable nuevo. `allowed_purposes` no otorga acceso a fuentes. Sólo comandos **preview/commit** aceptan `--commit`; los demás leen/reportan. `buscar` exige `--output` privado y sólo devuelve ruta/hash/conteos a consola.

| Comando | Argumentos específicos | Efecto |
|---|---|---|
| `registrar` | `--capture-manifest` | Preview/commit captura sellada. |
| `ingresar` | Exactamente uno `--archivo`, `--stdin`, `--parts-manifest`; `--source-id --account-id --attempt-id`; opcionales `--closed --expected-parts` para entrada sin manifest | Preview/commit exacto. Manifest lleva cierre/conteo propios; no combinarlos. |
| `estado` | `--audience` opcional | Conteos/watermark; audiencia añade snapshot de revisión. |
| `verificar` | sin extras | Verificar custodia. |
| `inventario-validar` | `--snapshot` | Validar inventario autorizado. |
| `conciliar` | `--snapshot` | Conciliar inventario/catálogo. |
| `permiso` | `--input` | Preview/commit declaración grant/revoke; finalidad de operación `custody`. |
| `segmentar` | `--tr-id --version --policy --audience`, opcionales `--max-core-bytes` (4096), `--context-bytes` (256) | Preview/commit núcleos de bytes. |
| `taxonomia` | `--input`, `--event` opcional obligatorio para actualización | Preview/commit taxonomía; finalidad `local_analysis`. |
| `analizar` | `--input --audience` | Preview/commit análisis escrito por agente. |
| `cobertura` | `--tr-id --run --audience` | Revalidar cobertura, permisos y dependencias. |
| `indexar` | `--snapshot --audience` | Preview/commit índice derivado; `current` o watermark exacto. |
| `buscar` | `--request --output` | Contexto privado acotado; no respuesta empresarial. |
| `revisar-antecedentes` | `--event --snapshot --audience`, opcionales `--results --previous --taxonomy-version` | Preview/commit revisión; sin resultados semánticos quedan pendientes. |

Ejemplo de solicitud de lectura, no permiso para consultar fuente real:

```json
{
  "query": "descuentos",
  "company": "EMPRESA-SINTETICA",
  "audience": "internal",
  "purpose": "internal_query",
  "task": "Localizar criterios y excepciones de descuentos",
  "entities": [],
  "period": null,
  "mode": "exploracion",
  "references": [],
  "limit": 10
}
```

```bash
python scripts/transcripciones.py buscar \
  --bank /private/bank --profile /private/profile.json \
  --request-id QUERY-001 --purpose internal_query \
  --request /private/query.json --output /private/reports/query-001.json
```

Ámbitos, offsets, completitud, historia y datasets: [transcripciones](transcripts.md). Banco devuelve `resultado.v1`; `DONE`/`DONE_WITH_CONCERNS` salen 0, bloqueos 2. Errores de validar empresarial salen 1; errores manejados de entrada/IO, 2. Revisar salida y código; éxito técnico no ratifica significado.

## Scripts auxiliares y APIs Python

`actualizar_vistas_bases.py` y `nombres_legibles.py` tienen preview/apply propios y controles de plan exacto; seguir [operaciones](operations.md). `aceptacion_integracion_local.py`, `prueba_integral.py`, `auditar_paquete.py`, `exportar_producto.py` apoyan aceptación/auditoría/distribución; consultar su `--help` sin inventarlos como subcomandos de `cerebro.py`.

Renderizado (`render_source`), integración (`prepare_batch`/`apply_batch`/`rollback_batch`), representaciones (`importar_representacion`), referencias externas y datasets (`prepare_export`) son APIs Python, no subcomandos TR ni servicios de red. Sus contratos/límites se enlazan desde [transcripciones](transcripts.md).
