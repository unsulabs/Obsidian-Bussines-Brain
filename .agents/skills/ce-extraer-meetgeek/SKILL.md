---
name: ce-extraer-meetgeek
description: "petición autorizada de inventario/extracción en cuenta identificada."
---

# ce-extraer-meetgeek

Lee el [contrato común](../ce-banco-transcripciones/references/contrato-comun.md) para estados, permisos, contexto y disponibilidad.

- **Trigger:** petición autorizada de inventario/extracción en cuenta identificada.
- **Inputs:** alias de cuenta verificado en UI, alcance/secciones, corte, cursor e inventario previo, IDs asignados. No recibir credenciales en brief.
- **Outputs:** inventario con fin observable o límite, exportaciones intactas en staging, evidencia de comienzo/final y continuidad de turnos, método, faltantes por reunión y conciliación por cuenta. Copia vacía es error, no original válido.
- **Errores:** `ACCOUNT_MISMATCH`, `SESSION_REQUIRED`, `RETENTION_UNAVAILABLE`, `VIRTUALIZED_PARTIAL`, `COPY_EMPTY`, `END_NOT_OBSERVED`. Preservar inventario; probar como máximo dos alternativas seguras distintas antes de requerir acción concreta.
- **Gate:** muestra corta/larga/antigua íntegra comprobada antes de escalar; todas las ocurrencias inventariadas tienen resultado. Duración y resumen del proveedor no prueban completitud. Un solo operador UI/portapapeles entre todos los agentes.

## Ejecución

Lee [recepción v1](references/recepcion-v1.md) antes de operar. Es el único contrato de entrega del extractor: sólo recepción, original primero y manifiesto sellado al final. Descubre herramientas/sesión disponibles, verifica cuenta visible y conserva desconocidos. Nunca recibir credenciales en brief ni inventar IDs del proveedor. Un único operador UI/portapapeles, sin analizar contenido, editar taxonomía/código ni escribir bóveda. Comprobar paginación y límites de retención; no confundir tarjetas visibles con inventario total. Si falta sesión, la única acción necesaria es abrir/iniciar MeetGeek en el chat extractor. Preservar la cuenta accesible aunque la segunda no esté abierta. No pagar ni activar nuevos servicios.

Consolidador independiente lee sólo entregas selladas y valida ruta, hash y esquema; el extractor no promueve originales al catálogo. Hash correcto no demuestra completitud. El estado inaccessible no cuenta como descarga. El contrato de recepción gobierna sus nombres/campos aunque el catálogo interno use otro vocabulario.
