# Aceptación integrada de Codex, GitHub y una bóveda existente

## Objetivo
No declarar terminado Cerebro Empresarial por un PASS de la suite. Deben funcionar juntas cuatro superficies: código maestro, instancia privada existente, ejecución efectiva de Codex y navegación GUI/CLI de Obsidian. Cada prueba produce PASS, FAIL o NO_VERIFICADO; lo no verificado no equivale a PASS.

## A. Diagnóstico inicial, sin tocar la bóveda
1. Codex identifica el checkout original, SHA, rama y Git status. Si el árbol está sucio, preservar los cambios y detener la actualización; NO usar reset --hard ni git clean. Si está limpio, avanzar de forma segura al commit main autorizado.
2. Confirmar que el repositorio maestro y la bóveda privada están en rutas distintas. Actualizar el código nunca autoriza copiar plantillas sobre una instancia existente.
3. Usando Python ya disponible, ejecutar desde raíz del checkout:

    python scripts/aceptacion_integracion_local.py --vault "RUTA_DE_INSTANCIA_EXISTENTE" --salida "CARPETA_NUEVA_FUERA_DE_BOVEDA_Y_GIT" --commit-esperado SHA_REAL_MAIN

4. El script lee estado y estructura, D01 y fuentes por hashes, 16 Bases, plan de filtros, mapa derivado y ejecuta la suite con temporal por defecto; en Mac repite la suite con /private/tmp. Produce un ZIP saneado. No incluye rutas, contenidos de negocio, transcripciones ni contratos. No hace migraciones ni publicación de mapas. Código 2 significa problema a corregir; conservar el ZIP.
5. No publicar ese ZIP en GitHub ni interpretarlo como aceptación del criterio del propietario.

## B. Prueba real de Obsidian y Codex
1. Codex abre la bóveda ya existente en Obsidian Desktop y comprueba Inicio, D01, propiedades, vínculos a fuentes, Documentos y Ofertas, y las 16 Bases. Si no puede observar la GUI marcar NO_VERIFICADO.
2. Comprobar por CLI cuando la versión instalada lo permita. Doctor solo informa si encuentra rutas, no demuestra interfaz funcional.
3. Ejecutar mapa-conocimiento solo lectura y comprobar que las relaciones propuestas y ratificadas son distintas. No publicar Canvas sin autorización.
4. Para una sesión nueva del **mismo proyecto Codex**, comprobar que `obsidian-router --project` resuelva la bóveda correcta con ID nativo. Si la bóveda ya está registrada pero falta esa asociación, ejecutar `scripts/registrar_boveda_codex.py` con sus datos actuales y `--proyecto "RUTA_DEL_PROYECTO_CODEX"`; el comando respalda el registro local, añade sólo esa ruta y no toca la bóveda. Repetir `--project` en una sesión independiente. No asignar una bóveda a proyectos ajenos por conveniencia.

## C. Prueba aislada con negocio ficticio
1. En una bóveda ficticia externa a Git, la sesión de Codex debe convertir un relato con estrategia, oferta, proceso y decisión en un mapa de conocimiento SIN que el empresario le recuerde descomponerlo. Justificar si conviene una sola nota.
2. Crear notas con contenido y propiedades, registrar relaciones y consultar fuentes con una pregunta positiva y otra deliberadamente sin respuesta documentada.
3. Publicar Markdown y Canvas derivados en esa instancia ficticia, abrirlos en Obsidian y comprobar enlaces. Ejecutar propuesta D/X, rechazo de SHA obsoleto, respaldo, revisión y restauración. Comparar huellas anteriores.
4. Al iniciar un chat nuevo, Codex debe recuperar los asuntos, notas, vínculos y estados desde archivos, no inventarlos desde la conversación anterior.

## D. Instancia real: puerta de autorización independiente
1. Sólo después de pasar A–C, presentar diff, plan de migración y respaldo privado externo para actualizar Bases. El hecho de que haya 14 LISTO y 2 LISTO_FILTRO depende de que esas vistas no hayan cambiado; si no coincide, detenerse.
2. No alterar D01, CAP/SES ni fuentes fuera del alcance autorizado; conservar su revisión, fuente y huella anterior.
3. Releer originales autorizados y la continuidad privada; preparar plan-conocimiento real: reutilizar, revisar, crear, referenciar y no crear, con dueño canónico, etiquetas y relaciones. Mostrarlo al propietario ANTES de escribir.
4. Cada escritura real (Bases, nota, revisión, relación y publicación Canvas) requiere autorización de su alcance, huella actual, respaldo y verificación posterior. No abrir las notas antiguas rechazadas.

## E. Uso por otras personas
Instalar en otra computadora autorizada o cuenta de Codex desde el mismo GitHub, crear una empresa ficticia distinta, verificar sus 16 Bases, plan, notas, relaciones, consultas, respaldo/restauración y segunda sesión. No arrastrar datos de una empresa a otra. Antes de distribución pública revisar permisos, licencia y seguridad.

## Gate de cierre
Para concluir: suite y prueba integral locales sobre el commit exacto PASS, Mac con su temporal normal PASS, instancia real sin alteraciones no autorizadas, Bases/Canvas visibles, prueba aislada de revisión y restauración, Codex en chat nuevo recuperando correctamente, aceptación del propietario y prueba de portabilidad. El workflow remoto fue retirado porque la cuenta no iniciaba jobs; no sustituirlo por un PASS supuesto. Fallo controlable = corregir código mediante PR y repetir gate. No declarar producción multiempresa por pasar sólo pruebas de Python.

## Reparación y uso efectivo tras el diagnóstico

Si la suite de macOS falla porque `/tmp` es alias del SO, actualizar
primero el checkout al commit corregido y repetirla con el temporal normal,
**sin workaround**. No declarar sistema listo por un PASS con `TMPDIR`
forzado. Con el workflow remoto retirado, conservar la salida completa
de la prueba en la Mac de trabajo para el SHA exacto.

Si las 16 Bases aparecen `LISTO_FILTRO` por autoguardado GUI, **NO usar
los SHA de la observación anterior como autorización**. Guardar el estado
actual, cerrar Obsidian, generar el nuevo plan y tomar `sha_plan`. Con
autorización para cambiar únicamente filtros raíz, aplicar usando
`actualizar_vistas_bases.py --apply --sha-plan ... --backup-dir ...`
y verificar que el respaldo contiene las 16 versiones actuales y
workspace.json. Comprobar que `views:` y groupBy no se perdieron.

Al reabrir Obsidian, comparar de nuevo contenido/estructura: se acepta
normalización YAML de la GUI, pero no pérdida de filtros, notas,
relaciones, D01 ni fuentes. Ejecutar en CLI el query real de Bases
Documentos y Ofertas: deben desaparecer las entradas de Plantillas.
No declarar la instancia funcional si los filtros no operan en GUI.

**Una instancia puede usarse antes de una segunda computadora:**
esa última prueba corresponde al gate de distribución multiempresa, no
a la aceptación de la instancia local. La aceptación local exige:
suite nativa PASS, Bases reales filtradas, D01/fuentes preservados,
Obsidian GUI/CLI operables, consultas de conocimiento y continuidad
desde nueva sesión. Después puede proponerse el desarrollo de sus notas
sin reescribir D01 por defecto.
