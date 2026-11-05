# Criterios verificables — instalación, creación, consulta y continuidad

## Aceptación por instancia

Cada negocio define tareas representativas y fuentes autorizadas. Una sesión independiente debe resolverlas leyendo originales y notas, con casos negativos y revisión de la persona responsable. Los tests sintéticos verifican integridad técnica; no acreditan fidelidad empresarial ni autorizan cambios en una instancia activa.

## A. Instalación y entorno

- A1 — Con Python sin dependencias instaladas, `python -S scripts/cerebro.py doctor` responde y marca `NO VERIFICADO` GUI/CLI.
- A2 — Codex inspecciona dependencias reales, solicita permiso antes de descargar o escribir y documenta ruta/versión real.
- A3 — `crear` en ruta nueva produce Inicio/Bases/plantillas; repetición falla sin sobrescribir nada.
- A4 — Bóveda empresarial permanece fuera de Git; comprobar `git status --ignored` y que no se incluyan datos.
- A5 — Obsidian Desktop abre la instancia, `Inicio.md` y por lo menos una vista `.base`; requiere **prueba GUI**, no covered por unittest.

## B. Primera construcción empresarial

- B1 — Codex recupera **sólo material admisible y autorizado** antes de preguntar, con inventario por lectura completa/parcial/no disponible. Lo expresamente rechazado no es fuente para síntesis ni se consulta por defecto.
- B2 — K1/K2/K3/K4 registrado para la necesidad, no un formulario genérico ni preguntas de memoria sobre hechos K2.
- B3 — El usuario comprende y aprueba **qué primer documento D/X** corresponde y para qué actividad servirá.
- B4 — G1–G7 evaluados, en especial G2 y G6; si no pasan, no declarar documento terminado.
- B5 — Ninguna afirmación sobre venta/contrato/cobro derivada de herramienta usada, propuesta o una reunión.
- B6 — Si hay ficha autónoma, `ficha` crea ID único y propiedades en borrador; fuentes referidas y relaciones explícitas, no inventadas.
- B7 — Reconstrucción editorial: prueba negativa de contaminación. Ningún texto, esquema específico, clasificación de ofertas o afirmación no autorizada procede de bóveda heredada rechazada. Sólo se admite documentación primaria revisada y aprobada por fuente.
- B8 — El dueño reconoce criterio y voz auténticos: hay decisiones, distinciones, casos y límites particulares; no se aprueba un texto por ser fluido, largo, persuasivo o tener palabras de marketing. Si no hay elementos suficientes, mantener borrador/pendiente.
- B9 — Conservar separados los respaldos históricos, los documentos descartados y la nueva instancia. Nunca activar plugins, instrucciones o sistemas antiguos sólo por su existencia.
- B10 — Con autorización de captura, una ronda sustantiva deja una nota provisional en `90_Sistema/Descubrimiento/`, con ID único, fuentes declaradas y estado borrador/no autoritativo. No genera una oferta, cliente o caso como hecho empresarial.
- B11 — Codex devuelve rutas/IDs de lo creado y resultados de `estado` + `validar` antes de otra entrevista; si no escribió, declara `sin_archivo_generado`.
- B12 — La síntesis de lectura inicia con **capacidad, mecanismo, decisiones o valor observado**, no con una sucesión de ausencias de evidencia. Los aspectos no acreditados se conservan en CONTROL y aparecen en el cuerpo sólo si alteran decisiones.
- B13 — Autoridad correcta por pregunta: testimonio directo del decisor puede fundar su estrategia/criterio; repositorios fundan hechos técnicos; ventas, pagos y resultados externos necesitan sus registros. No degradar un sistema implementado a «sólo posibilidad» por falta de factura.
- B14 — En revisión humana, la persona identifica al menos un mecanismo o decisión particular y una oportunidad de mejora basada en evidencia. Si la salida sólo enumera pendientes o repite abstracciones, **no** pasa aceptación editorial aunque toda su información sea formalmente prudente.

## B15–B19. Distribución y fidelidad antes de escribir

- B15 — Codex separa asuntos por identidad, fuente, vigencia, permisos y necesidad de consulta; **activa la planificación por sí mismo** cuando el relato mezcla varias funciones.
- B16 — Entrega mapa reutilizar/actualizar/crear/no crear, un dueño canónico por afirmación, razón de autonomía y prevención de duplicados entre D01 y X01 u otras fichas.
- B17 — Propone enlaces, etiquetas temáticas y aristas tipadas sustentadas; no infiere hechos de tags ni vínculos.
- B18 — Si redacta directamente una sección larga D01 con varios asuntos y no propone arquitectura, **no pasa aceptación**, aunque escriba bien o valide YAML. Probarlo en chat nuevo de Codex con negocio sintético y sin instrucción explícita de descomponer.
- B19 — En el ensayo sintético de `CICLO_EXPERTO_DESARROLLO_EMPRESARIAL.md`, Codex contrasta la captura equivocada con la declaración original y la corrección temporal, no generaliza una cifra hipotética ni convierte una oferta histórica en vigente. Entrega desarrollo y destino canónico de los asuntos antes de nuevas preguntas. Registrar respuesta cruda y evaluación humana; CI no acredita B19.

## C. Recuperación y autoridad

- C1 — `validar` sin errores y enlazado físico; una prueba negativa detecta link roto.
- C2 — Para dato vigente devolver fuente con autoridad en ámbito y fecha; el historial a fecha distinta retorna la versión correcta o «no verificado».
- C3 — La consulta `buscar` declara ser textual y no afirma motor semántico.
- C4 — Datos restringidos no se recuperan ni se incorporan por ausencia de ACL; código se prueba pero permisos reales requieren piloto.

## D. Evolución y seguridad

- D1 — `proponer` conserva SHA-256 de la nota original y no altera bytes de esa nota.
- D2 — La revisión D/X tiene diff, huellas, backup y restauración preliminar; la CLI registra una declaración de aprobación pero **no autentica al decisor**. Sólo aplicar tras autorización humana real y verificación local. ACL y revisión semántica no están automatizadas.
- D3 — `continuidad` crea registro explícito; la sesión nueva relee originales y no confunde resumen con autoridad.
- D4 — Plugins comunitarios solo bajo evaluación de compatibilidad, mantenimiento, licencia y reversión.

## Prueba de aceptación de dueño (aún pendiente)

El empresario, sin conocer archivos YAML, crea el espacio con Codex, explica el negocio, produce una primera pieza útil y verifica que otra sesión la recupere **con las fuentes correctas**. Registrar tiempo, fricción, errores, consentimiento y qué se pudo verificar. Hasta ejecutarla el producto sigue en alfa.

## E. Candidato a piloto 0.3: pruebas adicionales obligatorias

- E1 — La interfaz muestra sólo fichas reales en las 16 vistas, no modelos de Plantillas; comprobar específicamente Ofertas y Documentos en Obsidian.
- E2 — Registrar un D/X de cobertura parcial con fuentes y bloques estables; `estado` distingue infraestructura, fuentes, continuidad, entidades y documentos reales.
- E3 — Con dos cierres el mismo día, `estado` elige `registrado_en` y marca fechas inválidas, no orden alfabético del ID.
- E4 — En una bóveda sintética aislada: previsualizar revisión, proponer, bloquear cambios concurrentes, respaldar, aplicar, verificar historial y restaurar. En la bóveda real exigir nuevo permiso.
- E5 — La evaluación editorial registra G1–G7 y alcance por bloque, no permite recomendar aprobación integral si D01 mantiene cobertura parcial y no infiere verdad de las marcas YAML.
- E6 — Relaciones tipadas llevan origen, destino, asunto, justificación y fuente. El grafo separa propuesta y ratificación; no deriva contratación de un vínculo de navegación.
- E7 — Reanudar en otra sesión de Codex y recuperar una decisión o afirmación por fuente, ámbito y fecha. Probar al menos una pregunta adversarial (respuesta debe conservar incertidumbre).
- E8 — Probar instalación de producto desde GitHub en otra computadora limpia y registrar tiempos, errores, permisos y compatibilidad Obsidian.
- E9 — Ejecutar `aceptacion` sin modificar la bóveda: no puede declarar producción lista por aprobar CI. Guardar reporte local fuera de Git y ejecutar pasos manuales del protocolo de cierre.

**No declarar producción lista** sin E1, E4, E7, E8 y revisión de privacidad respaldadas por evidencia local. La fase de aceptación es separada del desarrollo de código.

## F. Red navegable y planificación universal (candidato 0.4)

- F1 — Relato con varias unidades: sin instrucción explícita de dividir notas, Codex muestra un plan de unidades independientes, ya existentes, candidatas y no creadas, con dueño canónico, referencias y relaciones.
- F2 — Relato con **un solo mecanismo indivisible**: Codex justifica una sola nota y no inventa un elemento no_crear ni una relación tipada falsa.
- F3 — plan-conocimiento detecta duplicados de tipo/título, clases X01–X07 incorrectas y Dnn existentes con ID YAML distinto; fuentes pendientes son reconocidas y no se declaran verificadas.
- F4 — Dos notas nuevas pueden tener etiquetas temáticas y contenido profesional completo sin plantillas vacías. El mapa de distribución no escribe en la bóveda.
- F5 — Se crean aristas propuestas con dos IDs y fuente, y se distinguen de ratificaciones declaradas. Una relación no se vuelve contrato por tener etiqueta.
- F6 — mapa-conocimiento produce previsualización determinista Markdown/Canvas, no modifica notas ni relaciones y omite material restringido.
- F7 — publicar-mapa exige confirmación y SHA actuales, backup fuera de Git y bóveda, rechaza mapas manuales, valida y restaura ante errores. Probar con empresa **100 % ficticia**.
- F8 — En Obsidian GUI funcionan enlaces de ambas vistas, Canvas y Bases; el agente responde una pregunta positiva por fuente/fecha y una negativa. Una consulta literal no se presenta como respuesta semántica validada.
- F9 — Con otra empresa desde instalación limpia, no aparecen términos, clientes, fuentes ni precios del piloto previo, ni una moneda preconfigurada.

Ninguna combinación de pruebas de Python cubre por sí sola los gates F1, F2, F8 y F9, que requieren prueba de agente y de GUI.

## G. Integración reproducible con instancia empresarial ya existente

- G1 — Codex en Mac observa rama/SHA/árbol Git y distingue maestro de bóveda. Si Git está sucio, conserva cambios, no fuerza checkout.
- G2 — Ejecuta scripts/aceptacion_integracion_local.py contra la bóveda real con ZIP saneado externo; comprueba hashes y no modifica D01, fuentes, Bases, configuración ni relaciones.
- G3 — La suite pasa con temporal de macOS por defecto y, como comparación, con /private/tmp; el SHA corresponde al main autorizado.
- G4 — Codex prueba en Obsidian **las 16 Bases** y GUI/CLI reales. El plan no sustituye la vista.
- G5 — En una instancia ficticia, la red de notas, relaciones, mapa y revisión/rollback funcionan y un nuevo chat las recupera sin que se le recuerde la arquitectura.
- G6 — Si Bases están obsoletas, prepara diff y backups externos, pide autorización para esa migración independiente de D/X.
- G7 — Una segunda persona/máquina reproduce el procedimiento con datos ficticios sin datos de la empresa piloto.
- G8 — El propietario revisa la arquitectura y el significado antes de nuevas notas D/X; las fuentes originales, aprobaciones y permisos son independientes del Git.

La suite local no cierra G4, G5 conversacional ni G7. El workflow remoto fue retirado tras un bloqueo de la cuenta antes de iniciar jobs; registrar las salidas locales del SHA exacto y continuar corrigiendo mediante PR. No declarar producción multiempresa por llegar a G3.

## H. Aceptación semántica de comunicación empresarial

- H1 — La prueba de explicación integral usa una petición natural y **abierta** en sesión nueva, sin proporcionar la tesis, la estructura, un producto específico o un síntoma como marco de identidad. Conserva el prompt y la salida cruda. Una pregunta situada sobre un producto, una objeción o un caso sólo prueba la respuesta a ese caso; no acredita que el agente explique por sí mismo la empresa completa.
- H2 — La pieza recupera decisiones, intercambio y mecanismos particulares desde originales admisibles; distingue actividad actual, oferta en revisión e investigación futura.
- H3 — El dueño reconoce o corrige una tesis concreta. Si el nombre de la empresa puede sustituirse sin pérdida de significado, el resultado es FAIL aunque el texto sea prudente y `validar` pase.
- H4 — Una corrección del dueño localiza la fuente, nota o instrucción responsable antes de generar otra pieza. Ningún borrador se vuelve público o aprobado por superar una prueba técnica.
- H5 — Al evaluar un fallo, compara primero el prompt de prueba con la salida. Si el prompt introdujo el encuadre rechazado, registra un defecto del ensayo y repite con una petición abierta antes de atribuirlo a recuperación, notas o skills. El reconocimiento parcial de un mecanismo no aprueba la pieza ni sus promesas.
