# Consulta contextual de conocimiento — apoyo al agente, no RAG

El CLI incorpora **consulta-contextual** para localizar fragmentos por coincidencia literal en bloques D/X y secciones de las unidades de `20_Entidades/` (ofertas, servicios, procesos, clientes, proyectos y decisiones, cuando existan) con identidad, fecha, fuentes de la nota y estado editorial. Para una petición formulada como pregunta, `--orientar` devuelve coincidencias de términos y **no** una respuesta semántica. Si un D/X parcial todavía no tiene marcadores `kb:id`, la consulta orienta por sus secciones, marcadas `seccion_derivada_sin_id_estable`: ese localizador no es una identidad contractual ni debe citarse como bloque permanente. No lee plantillas, fichas de fuente, capturas provisionales ni la sección CONTROL como si fueran hechos del cuerpo empresarial. Antes de responder, el agente debe abrir la nota candidata y las fuentes originales relevantes; las fichas de fuente sirven para localizarlas, no para sustituirlas.

Ejemplo ficticio:

python3 scripts/cerebro.py consulta-contextual --vault "/ruta/privada/ficticia" --texto "asignaciones" --tema "precio" --ambito "oferta:ejemplo" --fecha 2026-10-28

- Devuelve candidatos por bloque o sección junto con ID documental, tipo de fragmento, tipo de nota, estado editorial, vigencia declarada, fecha consultada y **fuentes a nivel de nota**, con advertencia de que no prueban por sí solas cada afirmación. Un D/X sin bloques vNext sigue siendo recuperable por sección, pero sus localizadores derivados pueden cambiar al editarse: antes de revisar o relacionar una afirmación, se necesita un bloque estable.
- Una coincidencia de una oferta `en_revision` con `vigencia: sin_verificar` **no** permite dar su precio como vigente. Para condiciones comerciales, recuperar la versión y autoridad que correspondan a la fecha y al cliente, y decir con claridad cuando no estén verificadas.
- Si se pide tema y ámbito, consulta también la autoridad explícita del contrato vNext importado; puede responder sin_autoridad_explicita aunque exista un bloque que menciona el tema.
- Filtra restricciones temporales registradas cuando existen fechas valid_from y valid_to; cuando faltan esas fechas NO se inventa vigencia.
- Excluye documentos con sensibilidad confidencial/restringido del índice literal MVP (sin ACL granular).
- No sintetiza respuestas, no usa embeddings ni declara recuperación semántica. Codex debe releer las fuentes originales y razonar con el contexto/permiso correctos antes de responder preguntas empresariales.

La aceptación final requiere prueba con preguntas positivas/negativas en otra sesión de Codex y con el criterio del propietario. Las pruebas unitarias sólo verifican que el motor conserva los límites anteriores.
