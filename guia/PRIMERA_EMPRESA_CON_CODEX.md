# Primera empresa con Codex — guía de ejecución y aceptación

**Para quién:** emprendedor, propietario o trabajador por cuenta propia, en cualquier país, sin experiencia con Obsidian ni programación. Esta guía define un flujo conversacional; **Codex hace lo técnico**. El dueño decide alcance y confirma hechos.

## Fase C0 — Entregar el repositorio

- Clona o descarga este producto conservando sus carpetas ocultas. Usa Codex con acceso local autorizado y crea la instancia privada fuera del repositorio.
- Pega `PROMPT_INICIO_CODEX.md`. Codex debe detectar que es repo maestro y no tratarlo como empresa.
- **Salida:** ruta exacta, commit o estado de checkout, versión de producto, archivos leídos y capacidades reales del entorno.

## Fase C1 — Diagnosticar sin tocar nada

Codex ejecuta `python3 scripts/cerebro.py doctor`; comprueba si Python sirve, si existen PyYAML/jsonschema, Obsidian instalado, GUI, Bases y CLI real. `doctor` no afirma que la aplicación está abierta. Si no hay dependencias no inventar resultados: pedir autorización para `venv`, instalar en entorno virtual y registrar salidas. Para usuarios de Mac antiguos considerar requisitos de Obsidian y Python; no desactivar seguridad para hacerlo pasar.

- **Salida:** tabla: observado / no verificado / impedimento / acción posible. NO instalar plugins ni abrir fuentes empresariales aún.

## Puerta de admisibilidad editorial (previa a C2–C4)

Cuando el propietario indique que documentación anterior es incorrecta, artificial, genérica o fue expresamente descartada, **NO** la conviertas en base del nuevo negocio por el solo hecho de encontrarla. Conserva custodias sin modificarlas. Clasifica los materiales como `admisible_autorizado`, `pendiente_autorizacion`, `legado_rechazado` o `referencia_tecnica_no_empresarial`. La fuente primaria original puede solicitarse **por separado** y sólo utilizarse con consentimiento. No se requiere inspeccionar contenido del legado rechazado para crear una bóveda nueva. Véase `docs/RECONSTRUCCION_EDITORIAL_Y_FUENTES.md`.

## Fase C2 — Autorización y espacio empresarial separado

Preguntar únicamente nombre de empresa, ruta privada preferida y autorización de crear bóveda. ID técnico estable, de 2–64 caracteres. El dueño no necesita saber qué es YAML. Preferir fuera del clon Git: `~/Documents/CerebroEmpresarial/<empresa>` o ruta autorizada; comprobar que **no existe**, crear con:

```bash
python3 scripts/cerebro.py crear --id EMPRESA-001 --nombre "Nombre real" --dest "/ruta/privada"
python3 scripts/cerebro.py validar --vault "/ruta/privada"
```

- No copiar `ejemplos/` ni bóvedas heredadas rechazadas como conocimiento de negocio. Si se solicita reconstrucción editorial desde cero, crear la nueva instancia en ruta privada y vacía tras autorización, dejando intactos respaldos y candidatos anteriores.
- Abrir la carpeta como bóveda existente en Obsidian Desktop, habilitar Bases y Templates **desde la aplicación**, verificar visualmente `Inicio.md` y abrir una vista `.base` en interfaz si se puede.
- Cuando Codex tenga instalado `obsidian-router`, registrar **la bóveda nueva ya abierta** con `python3 scripts/registrar_boveda_codex.py --vault "/ruta/privada" --nombre "Nombre real" --alias EMPRESA-001 --proyecto "/ruta/del/proyecto-codex"`. `--proyecto` asocia únicamente ese proyecto con la bóveda para que una sesión nueva pueda resolverla sin pedir otra vez la ruta; si no hay un proyecto estable, omitirlo y usar después el selector explícito de bóveda. En una instalación ya registrada, repetir el comando con `--proyecto` añade la asociación con respaldo y sin tocar la bóveda. Verificar con `python3 -B /ruta/obsidian-router/scripts/resolve_vault.py --project "/ruta/del/proyecto-codex"` que devuelve `selected` y `native_registry_verified: true`. El ID nativo lo asigna Obsidian; el script lo lee y respalda el registro local de Codex antes de añadir la entrada. Si Obsidian no la ha abierto o no hay acceso GUI, no inventar el ID ni continuar como si el router hubiera seleccionado la instancia. Esta operación pertenece a C2, antes del primer trabajo empresarial, y evita que una bóveda recién creada quede inaccesible para el agente.
- **Salida:** instancia y comprobaciones observadas; si GUI no está disponible, escribir `NO VERIFICADO` y continuar solo con archivos autorizados.

## Fase C2b — Mapa de empresa completa

Tras instalar o recuperar una instancia, activar `.agents/skills/ce-desarrollo-empresa/SKILL.md` y `docs/FLUJO_EMPRESA_COMPLETA.md`. Mostrar cobertura por tarea de D01–D07: qué sabe el negocio, fuente, estado y primera decisión que puede apoyarse. Una familia puede ser bloque, nota o varias unidades enlazadas; no crear siete documentos. Priorizar la primera necesidad útil y registrar las demás sin perderlas. Si la necesidad es marketing, aplicar `docs/MARKETING_EMPRESARIAL.md`: kit aprobado, voz de clientes, oferta vigente, investigación verificable, opciones, revisión y aprendizaje de correcciones. No activar publicación, programación o memoria automática por defecto.

## Fase C3 — Descubrimiento de toda la empresa, sin formulario universal

Codex lee `.agents/skills/ce-descubrimiento/SKILL.md`, `metodologia/vNext-1.0R/Guia_Metodologia_Documentacion_Empresarial_vNext_1_0R.md` y el catálogo. Preguntar por la situación del negocio solo para elegir qué investigar:

- **Se está creando:** recuperar ideas/supuestos, distinguir hipótesis, investigar mercado y desarrollar decisiones empresariales.
- **Opera sin orden:** recuperar **únicamente fuentes autorizadas y admisibles** (no el material editorial rechazado); distinguir hechos, testimonios, decisiones, histórico y propuestas. Si el dueño rechazó textos anteriores, reconstruir desde criterio experto y evidencia primaria.
- **Opera con documentación:** analizar fuentes de autoridad y sistemas oficiales, no copiar todo a la bóveda.

La situación puede ser distinta por función. **Primero recuperar**, después K1 experto / K2 sistema o documento / K3 no sabemos / K4 no necesario. Pedir solo información de alto valor (máx. 5 preguntas por ronda sobre un tema concreto). Evitar PII, secretos y contratos completos en bóveda sin controls.

- **Salida:** asuntos materiales de toda la explicación y fuentes recuperadas; mapa de cobertura por tareas, criterios/episodios/patrones transferibles y prioridades de trabajo. Si el propietario ya autorizó construir, continuar con las piezas sustentadas sin detenerse en un plan de primera nota.

## Fase C3b — Captura progresiva verificable durante el descubrimiento

Antes de volver a preguntar, organiza lo observado en un registro de trabajo de la bóveda: fuentes originales admisibles, observaciones, interpretaciones, atribución a la empresa aún por confirmar, temas K1–K4 y relaciones candidatas. No reducir una empresa con varios tipos de trabajo al primer proyecto encontrado. No elevar por inferencia proyectos de clientes a servicios contratados por la empresa.

Con permiso para escribir **sólo notas provisionales**, registrar fuentes internas admisibles con `fuente` (sin copiar originales confidenciales) y usar `capturar` para crear una nota bajo `90_Sistema/Descubrimiento/`. Preparar el texto de la captura fuera de Git y de la bóveda; omitir materiales privados innecesarios y contenido del legado rechazado. Ejecutar `estado` y `validar`, mostrar ruta/ID y siguiente pregunta prioritaria. Este artefacto NO reemplaza la revisión, el desarrollo D/X ni los gates G1–G7.

Si aún no existe permiso de escritura, solicitar autorización de **alcance limitado**, no para documentos aprobados ni para toda la empresa. Ver `docs/CAPTURA_PROGRESIVA.md`.

## Fase C3c — Desarrollar significado antes de seguir preguntando

Seguir `docs/CICLO_EXPERTO_DESARROLLO_EMPRESARIAL.md` en cada ronda sustantiva: contrastar el original con capturas y correcciones antes de convertirlo en conocimiento. Al continuar una instancia existente, usar el mismo ciclo sin repetir C2 ni la entrevista inicial.

La captura C3b es sólo memoria provisional; no satisface la creación empresarial. A partir de material admisible y criterio del dueño, producir una **síntesis constructiva de trabajo**: qué hace la empresa, qué capacidad o elección se observa, cómo opera, qué aporta o permite decidir y cuáles son sus posibles implicaciones de desarrollo. Diferenciar lo que está construido, lo ofrecido, lo comercializado y lo futuro, pero **no exigir una factura para documentar un proceso o el criterio estratégico del propietario**. No confundir la prudencia sobre un contrato con una ausencia de capacidad. El cuerpo explica el negocio; CONTROL documenta evidencia, restricciones e hipótesis, según la regla explícita de vNext-1.0R.

El primer borrador puede estar **en revisión** aun si falla un gate: eso impide aprobarlo, no analizar ni proponer escenarios. Debe ofrecer una interpretación reconocible y útil para que el dueño la corrija, antes de insistir en preguntas adicionales. Revisar `docs/SINTESIS_EMPRESARIAL_CONSTRUCTIVA.md`. Si la salida es sobre todo «no se acredita», «pendiente» o «falta verificar», rehacer el trabajo con lo que las fuentes sí permiten decir y mover las reservas a CONTROL.

## Fase C3d — Diseñar el conocimiento antes de redactar

Si las fuentes o la explicación mezclan varios asuntos, Codex activa `ce-arquitectura-conocimiento` sin esperar indicación del dueño. Reconstruye temas, autoridad y notas preexistentes. Elige por identidad qué **reutilizar, revisar, crear o no crear**, con dueño canónico por afirmación, etiquetas temáticas y relaciones tipadas. Usa `scripts/cerebro.py plan-conocimiento` con un JSON externo al repositorio y bóveda; presenta el resultado legible y la alternativa de agrupar asuntos en una sola nota, justificándola.

**No redactar directamente un D01 largo sin haber enseñado antes el mapa cuando exista conocimiento multiasunto.** Ver `docs/ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md`.

## Fase C4 — Construir conocimiento empresarial utilizable

Ejecutar la guía P01/P01B/P01C/G1–G7/DES-[ID]/P03; usar prompts especializados del catálogo (no escribir «misión, visión, valores» genéricos). El dueño puede elegir una necesidad distinta: oferta, proceso, prioridad, cliente, investigación, acuerdo, caja, etc. **Una clase documental no impone una nota nueva**; decidir identidad por historia/permiso/autoridad/vigencia/reutilización.

- Si falla G2 o G6, queda `descubrimiento_en_curso`, NO documento terminado.
- Si se requiere una entidad autónoma, Codex puede usar `python3 scripts/cerebro.py ficha --tipo ... --titulo ...`. La nota es borrador y debe sustituir la sección de placeholder con la explicación validada; preservar ID, fuentes, estados, registro de cambios y semántica.
- Para fuente no sensible: `python3 scripts/cerebro.py fuente --id F-... --titulo ... --localizador ... --clase ...`. La ficha no copia la fuente ni verifica permisos implícitamente.
- Si hay paquete vNext conforme al contrato, puede importarse después de `validar_traspaso` con `scripts/cerebro.py importar`. Nunca usar `--permitir-real` sin revisión y autorización.

- **Salida:** notas desarrolladas y conectadas para las tareas que las fuentes permiten, con mecanismo, criterio, excepción, responsable, procedencia y uso transferible. Tras la primera pieza, continuar con los demás asuntos materiales sin esperar que el dueño pida cada D/X. Cotejar original→nota y nota→original; una idea futura sustantiva no desaparece por no ser operación vigente. Someter el contenido a revisión humana de voz y utilidad. No aprobar por sonar formal ni por mencionar nombres o cifras.

## Fase C5 — Navegación y pruebas

`python3 scripts/cerebro.py validar --vault ...` y `estado`. Consultar el documento desde Obsidian y luego desde Codex en otra pregunta. Para fuentes y precios, verificar fuente original/fecha y, si aplica, `python3 scripts/cerebro.py autoridad --tema ... --ambito ... --fecha ...`. Si el sistema solo hizo una búsqueda literal, **no llamarlo recuperación semántica**.

- **Prueba negativa:** pedir una afirmación no documentada o un precio histórico. Debe admitir `no se sabe` o preservar la vigencia histórica.

## Fase C5b — Navegación derivada y verificable (opt-in)

Cuando ya existan varias notas conectadas, usar python3 scripts/cerebro.py mapa-conocimiento --vault RUTA. El resultado muestra enlaces Markdown/Canvas, SHA actual y propuesto, notas omitidas por sensibilidad y si el Canvas es parcial. La operación es de **sólo lectura**.

Si el propietario quiere activar esa proyección, pedir autorización exacta, respaldo **externo a la bóveda y fuera de Git**, y ejecutar publicar-mapa con --sha-actual, --sha-propuesto, --confirmacion y --respaldo. La CLI no puede validar la identidad de quien concedió permiso; Codex debe obtenerlo del propietario. No sustituir mapas personales ni D/X, no editar notas originales. Abrir los archivos generados en Obsidian, comprobar que los enlaces funcionan y que las flechas distinguen propuestas y revisiones declaradas.

El mapa es un índice que requiere regeneración autorizada tras cambios; no es una base de conocimiento independiente ni un RAG. La guía técnica completa está en docs/ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md.

## Fase C6 — Continuidad y aceptación

Codex resume solo lo comprobado, guarda el registro de sesión mediante `python3 scripts/cerebro.py continuidad --resumen "..." --siguiente "..." --revisado-por "..."` y deja próxima pregunta real. En nueva sesión relee la nota y las fuentes; no considerar el resumen anterior como autoridad superior a los originales.

**No anunciar éxito total** sin verificar por separado: (a) instalación técnica; (b) contenido empresarial desarrollado desde originales completos; (c) enlaces, estados y versiones; (d) tarea real ejecutada por otra sesión/persona, con contraprueba; (e) permisos; (f) corrección propagada y continuidad. La consulta literal no equivale a comprensión. Para aceptar una instancia, leer sus originales autorizados y probar tareas reales; usar datos sintéticos para aislamiento y reversión.

## Frase que el empresario podrá usar después

«Sigamos construyendo mi empresa. Recupera la última continuidad y revisa el estado real. No repitas lo que ya hemos desarrollado. Dime qué puedes hacer con lo que existe y qué decisión mía falta.»
