# Incorporación mínima de documentos D/X — referencia histórica 0.2.x

**Este documento registra el primer incremento de creación D/X.** Su descripción de revisiones y rollback como funciones no implementadas ya no refleja la CLI actual. Para nuevas sesiones leer [REVISIONES_DX_CON_HISTORIAL.md](REVISIONES_DX_CON_HISTORIAL.md), [GOBIERNO_EDITORIAL_DX.md](GOBIERNO_EDITORIAL_DX.md) y [ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md](ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md). Mantener aquí el recorrido histórico sin convertirlo en instrucciones vigentes.

**Alcance:** publicar un borrador empresarial sustantivo en una bóveda privada, con identidad documental estable, estado editorial, revisión inicial y referencias a fuentes registradas. **No es una función de aprobación, reescritura o migración.**

## Por qué existe

Una empresa puede avanzar desde descubrimiento y documentos de trabajo hasta una sección D01 revisable sin esperar a tener el dossier completo. Antes de este incremento existían `fuente`, `continuidad` y `ficha` de entidades, pero **no** un comando específico para crear un documento de las clases D01–D07/X01–X07. Codex podía crear el Markdown manualmente, con riesgo de omitir identidad, propiedades y comprobaciones.

## Trabajo con el propietario

1. Desarrollar contenido con la metodología vNext-1.0R y fuentes originales autorizadas. Separar contenido útil de CONTROL. **G1–G7 determinan la aprobación final**, no si se puede conservar un borrador en revisión.
2. Revisar significado y alcance con el dueño. El `--estado en_revision` indica que está sometido a revisión, **no** que fue aprobado.
3. Preparar un Markdown **sin cabecera YAML** en una ruta privada externa a la bóveda y al checkout Git; no copiar datos restringidos ni notas heredadas rechazadas.
4. Tener registradas en `50_Fuentes` las fuentes de nivel `interno` que se van a relacionar. `--fuente` requiere un ID existente y crea un enlace verificable, pero no certifica por sí solo el alcance de la fuente.
5. Antes de incorporar, comprobar `estado`/`validar` de la bóveda y que no exista ya otro documento con ese `doc_id`.

Ejemplo con empresa **ficticia**:

```bash
python3 scripts/cerebro.py documento \
  --vault "/ruta/privada/EmpresaDemo" \
  --clase D01 \
  --titulo "Identidad y modelo de negocio" \
  --archivo "/ruta/privada/Trabajo/D01_seccion_revisada.md" \
  --estado en_revision \
  --cobertura parcial \
  --fuente F-DEMO-001
```

Para D01–D07, el `doc_id` es el de la clase (ej. D01), con un único documento por familia en `10_Conocimiento/`; el archivo lleva un nombre legible que describe su asunto y el ID permanece en propiedades. **El contenido puede ser una sección parcial**, sin crear las ocho secciones de la plantilla con relleno. Para X01–X07, cada expediente tiene identidad propia `Xnn-...`: usar `--doc-id X01-EJEMPLO-001` si se conoce la identidad autorizada, o dejar que la CLI asigne una.

El sistema añade automáticamente: `id`, `doc_id`, `tipo: documento`, `clase`, `empresa_id`, `schema_version: 0.9`, `revision: 0.1`, `estado_editorial` (`borrador` o `en_revision`), `cobertura` (por defecto `parcial` con fuentes o `sin_fuente` sin ellas, ajustable con `--cobertura`), `vigencia: sin_verificar`, sensibilidad, fecha de corte, hora de registro, fuentes e integridad del borrador de entrada. La cobertura declarada se refiere a la tarea concreta y no aprueba el contenido. **No añade pruebas semánticas ni autoriza claims**, y deja pendiente la normalización de bloques y el contrato completo para aprobación/promoción.

## Seguridad y conservación

- No sobrescribe documentos existentes; detecta colisiones de `doc_id` incluso cuando la nota anterior tiene otro nombre.
- Rechaza contenido con frontmatter ya elaborado por terceros, referencias a fuentes inexistentes, enlaces wiki rotos en la nueva nota y algunas señales de claves privadas.
- Sólo registra material interno autorizado, sin ACL para confidencial/restringido. Una bóveda privada en el disco **no** equivale a permisos empresariales granulares.
- Valida la estructura antes y después de escribir. Si la nueva nota falla validación, elimina **sólo la nota que intentó crear**, conservando las demás. No toca el repositorio maestro, ejemplos ni copias históricas.
- Si ya existe D01, no reutilices `documento` para crear D01 de nuevo: **prepara una propuesta de cambio**. La revisión, actualización aprobada, versiones anteriores y rollback siguen siendo una capacidad **no implementada**.

## Qué queda para una evolución completa

- Evaluación sustantiva de G1–G7 y aprobación del documento, sección o bloque con autoridad y responsable.
- Aplicación de cambios con comparación de hash, historial, copia de seguridad probada, revisión y reversión.
- Bloques semánticos `<!-- kb:id=... -->`, manifest de contrato, alcance temporal por afirmación y relaciones tipadas con origen explícito.
- Consultas con recuperación verificada por bloque+fuente+contexto, casos negativos y prueba en nueva sesión.
- Migraciones de versiones del producto sin sobrescribir datos o personalizaciones.

**Prueba de aceptación:** una persona revisa una sección D01 en Codex, autoriza guardarla `en_revision`; Obsidian permite abrir el documento y verlo en Bases «Documentos»; la CLI devuelve ruta, ID y estado; `validar` no reporta errores. Ninguna de esas pruebas implica que su contenido ya esté aprobado.
