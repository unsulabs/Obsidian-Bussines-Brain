# Contrato de traspaso documental a Obsidian y agentes — vNext

**Versión:** 0.9; **fecha:** 25 de octubre de 2026.  
**Naturaleza:** contrato de INTERFAZ del Paso 1 al Paso 2. **No** estructura física de bóveda, no plugin de Obsidian y no ejecución sobre datos reales.

## 1. Principios de recepción

El Paso 2 recibe un **paquete autoconsistente** que debe poder auditar sin adivinar cuál precio, política, etapa o fuente prevalece. El significado empresarial surge de D01–D07 y X01–X07; el contrato sólo lo transporta. Son compatibles diversas interfaces de ChatGPT, Claude, Codex y otros agentes, pero ninguna plataforma adquiere automáticamente conectores ni privilegios. El contrato marca permisos y fuentes ausentes en vez de inventar accesos [S26,S27,S28,S29,S30,S31].

## 2. Archivos lógicos requeridos (sin imponer carpetas)

1. **Documentos Markdown de negocio:** texto desarrollado, `doc_id` estable, revisión, encabezados de su clase, bloques `<!-- kb:id=... -->`, referencias a fuentes y fechas donde importan; incluyen históricos pertinentes o relaciones explícitas a los históricos.
2. **Registro de fuentes (CONTROL):** identificador `F-xxxx`, tipo, ubicación verificable, fecha del hecho, fecha de captura, permiso, lectura completa/parcial/no verificada y huella SHA-256 si existe copia local. Fuentes no accesibles se registran, no se inventan.
3. **Registro de autoridad y control:** quién prevalece por asunto, alcance y fecha; qué está aprobado editorialmente; cobertura por pregunta, pendientes, conflictos, decisiones, revisiones y derivados afectados.
4. **`manifest.json`:** índice portable de documentos, bloques, fuentes, autoridad, relaciones tipadas, restricciones, historial, problemas y pruebas de recuperación. El archivo de ejemplo `Ejemplo_Manifiesto_Traspaso.json` implementa esta forma.
5. **`Esquema_Manifiesto_vNext.schema.json`:** validación formal de campos, enumeraciones y estructura (JSON Schema draft 2020-12). `Validador_de_Traspaso.py` agrega comprobaciones de integridad referencial y rutas.
6. **Pruebas de consulta:** para cada afirmación sensible, preguntas previstas con bloque y fuente que deberían recuperarse; la etapa 2 deberá correrlas en el agente real. Un enlace interno nunca sustituye esta prueba.

**ACLARACIÓN:** el JSON y el validador complementan los siete entregables solicitados; no son la bóveda ni requieren que el dueño programe. Puede añadirse un ZIP para transportar el conjunto sin perder rutas relativas.

## 3. Qué significa una unidad de conocimiento

Un **documento** es una exposición humana mantenible; un **bloque** es un fragmento semántico con identidad que debe conservar fuentes/estados; una **fuente** es el registro de origen sin duplicaciones; una **relación** es una conexión TIPADA entre bloques o entidades; una **autoridad** es la regla explícita para una pregunta y ámbito dados, no un rango de «archivo más nuevo». Una **cita** da procedencia, no implica que la afirmación sea verdadera universalmente. Distinguir identidad de oferta frente a archivos PDF de cotizaciones sucesivas.

La guía utiliza un comentario Markdown portable `<!-- kb:id=... -->` justo antes del bloque sustantivo, no el formato privado de `^block` de Obsidian. La IA asigna y mantiene el ID; no se borra al renombrar encabezado o mover a otro archivo. Las referencias de bloque de Obsidian pueden generarse en el Paso 2 si aportan navegación [S29].

## 4. Estructura del objeto de traspaso

La raíz JSON contiene exactamente los siguientes campos:

| Campo | Significado verificable | Restricción |
|---|---|---|
| `contract_version` | Identidad del esquema | `0.9` |
| `generated_at` | Instante de exportación con zona | ISO 8601 |
| `company` | ID/nombre de empresa; `synthetic` | Aislar datos de demostración |
| `documents[]` | `doc_id`, tipo, ruta relativa, revisión, editorial, corte, acceso y cobertura por pregunta | Documento accesible, versión única |
| `sources[]` | Fuente original y localizador, fecha de evento/captura, permiso, read status y checksum opcional | Fuente una vez; `no_verificada` ≠ observación |
| `blocks[]` | Bloque, documento, heading path, tipo semántico, 4 ejes, soporte, fechas, asunto, fuente y acceso | Identidad estable y referencia existente |
| `authorities[]` | `topic_key`, `scope`, `doc_id`, bloque y vigencia | No dos autoridades activas incompatibles |
| `relationships[]` | `subject_id`, predicado, `object_id`, fuente y estado de relación | Aristas explícitas verificadas |
| `pending[]` | Preguntas pendientes y tarea bloqueada | No convertir ausencia en «N/A» |
| `historicals[]` | Evento, fecha, razón y `replaced_by` | Conservar lo anterior |
| `restrictions[]` | Restricción por fuente/bloque/doc con tratamiento | No exportar secretos |
| `retrieval_tests[]` | Pregunta, bloques/fuentes esperados, estado y ejecución | Ejecutar en el Paso 2 |

### Estados exactos y su independencia

**Cuatro ejes independientes, nunca un estado único:**

1. **Editorial:** `borrador` / `en_revision` / `aprobado` / `retirado`. Indica quién revisó la redacción, no que toda la materia está completa.
2. **Cobertura por pregunta:** `sin_fuente` / `parcial` / `suficiente_para_tarea` / `no_aplica` (con justificación). En cuanto cambie una tarea o contexto puede cambiar la suficiencia.
3. **Conocimiento de cada afirmación:** `hecho_observado` / `decision_aprobada` / `propuesta` / `hipotesis` / `historico` / `pendiente` / `desconocido` / `conflicto`. No se deduce la certeza de la confianza retórica de la IA.
4. **Vigencia temporal:** `vigente` / `futuro` / `superseded` / `caducado` / `sin_verificar`, con `valid_from`, `valid_to` cuando se conoce. Además guardar `recorded_at` para separar fecha de ocurrencia de fecha en que se registró.

La **clase de soporte** es independiente: `documental_directo`, `testimonio_atribuido`, `observacion`, `derivado_calculado`, `sin_fuente`, `fuentes_en_conflicto`. Una decisión puede estar aprobada pero apoyarse en una hipótesis no validada. Un precio aprobado puede ser histórico. Una sección editada puede mantener cobertura insuficiente. Registrar sensibilidad (`interno`, `confidencial`, `restringido`) y acceso por unidad; no exponer datos porque el PDF se vea bonito.
## 5. Regla de autoridad cuando las fuentes discrepan

**Regla operativa de autoridad:** una afirmación no tiene autoridad global: se resuelve por *asunto + entidad + contexto + vigencia + fuente + ámbito*. Para un cliente y proyecto concreto, un acuerdo aceptado puede prevalecer sobre una condición comercial general para ese alcance, pero no convierte la excepción en política universal. Para datos de caja mandan transacciones registradas/conciliadas, no un PDF presupuestal. Para intención estratégica manda el decisor autorizado; para preferencias de clientes la evidencia observada y su muestra; para leyes, la fuente normativa y asesoría aplicable, no una propuesta de IA.

**Una sola autoridad por asunto y contexto:** si X01 gobierna el precio específico de una oferta, D03 no copia su valor como regla alternativa: enlaza la ficha y muestra una síntesis *no autoritativa*. Si no existe X01, la subsección versionada de D03 es autoridad. Si X05 gobierna contrato particular, D03/X01 no lo sobreescriben. Lo que una fuente demuestra y su alcance prevalecen sobre resúmenes posteriores.

**Separación de hechos comerciales:** `usado` ≠ `ofrecido` ≠ `cotizado` ≠ `aceptado` ≠ `contratado` ≠ `entregado` ≠ `facturado` ≠ `cobrado`. Son eventos distintos que requieren evidencia diferente. `Autorizado para usar material` tampoco significa `autorizado para compartirlo fuera del equipo`.

**Algoritmo recomendado:**

1. Identificar la pregunta, asunto, entidad, contexto y fecha consultada. Una tarifa general y un acuerdo particular pueden coexistir sin contradicción porque tienen ámbitos diferentes.
2. Filtrar documentos/bloques por restricciones de acceso y por vigencia en fecha consultada.
3. Recuperar autoridad explícita `topic_key + scope` y sus fuentes: documento firmado para obligación particular; ficha de oferta aprobada para precio general; sistema financiero para efectivo; decisor documentado para política.
4. Verificar clase de evidencia, fecha efectiva y que no haya contradicción irresuelta. Si dos autoridades son plausibles, devolver `conflicto`, no elegir por fecha del archivo.
5. Contestar con su contexto y fuente exacta. La fuente que «menciona» un tema no necesariamente es autoridad para decidirlo.
6. Señalar límites de permisos y grado de cobertura. Nunca recuperar información confidencial a quien no está autorizado.

## 6. Temporalidad bitemporal mínima

Cada afirmación material registra `valid_from`/`valid_to` cuando se conocen y `recorded_at` siempre. Ejemplo: el 25/10 descubrimos que una política dejó de aplicar el 01/10: el hecho cambió antes del registro. Un parser que solo ordene por fecha de archivo daría una respuesta falsa. `supersedes` y `historicals[]` permiten consultar el estado previo sin confundirlo con vigente.

## 7. Estrategia de procedencia

La fuente se registra una sola vez con `F-xxxx`, localizador y permisos. Si existen versiones distintas del mismo contrato, se crean registros distintos o hashes por revisión con vínculo explícito; no sobrescribir la evidencia anterior. Un PDF de presupuesto en Drive con URL puede apuntarse sin exportarse si permisos no lo permiten. La etiqueta «leida_parcial» exige registrar qué quedó sin leer; ninguna inferencia basada en texto no visto se presenta como evidencia.

Para cada bloque sustantivo: ¿qué evento lo originó?, ¿cuál es el tramo verificable?, ¿qué alcance tiene?, ¿quién lo aprobó, si es una decisión?, ¿a qué cambia? Esto adapta el principio de entidades/actividades/agentes de PROV-O [S26] sin exigir una implementación RDF. Para los casos se conserva cronología y contexto antes de sintetizar.

## 8. Gates de validación (PASO 1 debe entregar evidencia)

**Gate V1 — estructura:** JSON Schema válido, todos los campos obligatorios y enumeraciones correctas.  
**Gate V2 — referencias:** todos los ID de documento/fuente/bloque son únicos; vínculos y autoridades apuntan a elementos existentes; no hay rutas `../` ni rutas absolutas; comentarios de bloque están realmente presentes en Markdown; hashes coinciden en archivos que lo declaran.  
**Gate V3 — semántica:** revisar afirmaciones sensibles contra originales y estados; no hay precio vigente sin autoridad, caso transformado en regla o contratos deducidos de uso. Requiere auditoría humana/IA, no lo resuelve JSON Schema.  
**Gate V4 — temporal:** pruebas de «¿qué era vigente el día X?» y «¿qué cambió después?», con no solapamiento injustificado de autoridad.  
**Gate V5 — permisos:** solo fuentes autorizadas viajan al destino; secret/PII protegidos, minimizados o referenciados.  
**Gate V6 — recuperación:** un agente del Paso 2 recibe preguntas, identifica bloques/fuentes autorizados, da respuestas correctas con límites y supera casos negativos; `retrieval_tests.result` no debe falsearse como aprobado si no se ejecutó.  
**Gate V7 — reanudación:** en segunda conversación/otro harness se recupera contrato, fuentes y estado sin que el dueño reconstruya a mano todo el negocio.

## 9. Ejemplo íntegro y comandos de validación

El directorio `Ejemplo_sintetico/` incluye cuatro documentos Markdown y dos fuentes **completamente ficticios**. El manifest `Ejemplo_Manifiesto_Traspaso.json` contiene cinco bloques, una autoridad de precio, referencias, tres pruebas de consulta que figuran honestamente como `no_ejecutada` y pendientes reales del ejemplo. Nunca extrapolar sus precios a empresas reales.

```bash
python Validador_de_Traspaso.py Ejemplo_Manifiesto_Traspaso.json
```

**Resultado esperado:** PASS para JSON, referencias, rutas, localizadores y hashes; tests de recuperación semántica siguen `no_ejecutada` y requieren un agente real del Paso 2. Esta separación de pruebas impide confundir validez estructural con utilidad demostrada.

Ejemplo abreviado (el JSON entregado es la autoridad del formato completo):

```json
{
  "contract_version": "0.9",
  "company": {"id": "BRISA-SINTETICA", "display_name": "Brisa Modular [FICTICIA]", "synthetic": true},
  "authorities": [
    {"topic_key": "precio_modulo_estandar", "scope": "oferta:OFR-BRISA-001",
     "doc_id": "X01-BRISA-001", "block_id": "X01-BRISA-001-B001",
     "temporal_status": "vigente", "valid_from": "2026-10-01"}
  ],
  "retrieval_tests": [
    {"test_id": "Q-02", "question": "¿Se aprobó tarifa sabatina?",
     "expected_block_ids": ["D03-B004"], "expected_source_ids": ["F-0100"],
     "expected_state": "propuesta", "result": "no_ejecutada"}
  ]
}
```

## 10. Tratamiento de restricciones y autonomía del harness

No entregar cuentas completas de clientes, datos bancarios, expedientes laborales, contraseñas, claves API, informes legales protegidos o copias de contratos sensibles sin autorización. El manifest puede incluir un origen no exportable y devolver «fuente restringida» a un agente sin permiso; la recuperación no debe eludir accesos. `AGENTS.md` de Codex puede indicar políticas de un repositorio [S30] pero no sustituye control de acceso de fuentes, ni se presume implementado en Grokbot, Claude u otros. No escribir una integración «automática» si carece de API/conector y autorización.

## 11. Interfaz contractual mínima para un agente futuro

**Entrada:** ruta de paquete, política de permisos, fecha de consulta y listas de tareas. **Procesamiento obligatorio:** validar JSON y archivos, construir índice de bloques y fuentes, resolver autoridad/tiempo/permiso, exponer relaciones con prueba de procedencia, y correr queries adversariales. **Salida del Paso 2 cuando se implemente:** conocimiento indexado con trazas a `doc_id`/`block_id`/fuentes, evidencia de pruebas y listado de discrepancias; detalles de carpetas Obsidian, formato de notas, embeddings, plugins y automatización de edición se diseñarán después. No debe pedir al propietario que explique de nuevo lo ya suficientemente documentado, pero sí puede solicitar la fuente o decisión faltante exacta.

## 12. Fallos que rechazan el traspaso

- JSON válido pero un bloque no existe físicamente.
- Dos precios vigentes para idéntica oferta/ámbito/fecha, sin decisión de preferencia.
- Una nueva sesión usa un resumen previo que contradice documento fuente.
- Una cotización se registra como pago, o uso de asistente como venta de licencia.
- Se divulga una conversación restringida en respuesta a pregunta genérica.
- Una pregunta histórica devuelve el precio actual y oculta la versión pasada.
- El esquema fuerza campos de sitio web en empresa exclusivamente de consultoría.
- El agente solo demuestra que tiene enlaces, no que encontró el episodio correcto.

**Estado de este contrato:** validable estructuralmente; pendiente de prueba de recuperación semántica por al menos dos agentes y de piloto real. No constituye una ontología completa ni un diseño de bóveda.

## 13. Fuentes técnicas y metodológicas

- [S26] W3C PROV-O: https://www.w3.org/TR/prov-o/
- [S27] OASIS DITA topic architecture: https://docs.oasis-open.org/dita/v1.0/archspec/topics.html
- [S28] Obsidian Properties: https://obsidian.md/help/properties
- [S29] Obsidian Internal Links: https://obsidian.md/help/links
- [S30] OpenAI Codex AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- [S31] JSON Schema: https://json-schema.org/specification
