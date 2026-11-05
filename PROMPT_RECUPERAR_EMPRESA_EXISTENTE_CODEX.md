# Continuar con Codex — bóveda existente

[English](CONTINUE_WITH_CODEX.md) · [Guía de uso](docs/es/user-guide.md)

## Continuidad cotidiana

Copia este pedido para una tarea cotidiana:

> Continúa mi instancia existente. Lee AGENTS.md y activa ce-continuidad, o ce-consulta para mi tarea concreta. Resuelve primero la bóveda mediante obsidian-router, verifica el registro nativo de Obsidian y sus instrucciones locales antes de leer dentro; después consulta Como_usar, Inicio y sólo el estado, las notas y los originales autorizados pertinentes. No crees otra bóveda, copies plantillas, repitas la entrevista inicial ni reescribas D01 por defecto.
>
> Recupera mis permisos y decisiones editoriales. Excluye textos rechazados, conserva incertidumbre y distingue fuentes, propuestas y conocimiento aprobado. Ante correcciones o evidencia nueva, revisa antecedentes y usa el flujo de cambios con IDs estables, versiones y respaldos. Muestra arquitectura antes de redactar varios asuntos y completa la integración autorizada sin repetir permisos rutinarios.
>
> Verifica la tarea real y las comprobaciones estructurales pertinentes. Informa qué cambió, qué se verificó, qué falta y cómo continuar. Continuar no autoriza por sí solo aceptación de instalación, migración, publicación de mapa, subida externa ni tareas recurrentes.

## Aceptación de integración real

El siguiente prompt conserva el alcance del prompt histórico de recuperación. Úsalo cuando el encargo sea aceptar una instalación, migración o cambio de integración, no para una consulta cotidiana.


Continúa el Obsidian-Bussines-Brain que ya está instalado y conectado a esta empresa. Esta es una tarea de INTEGRACIÓN REAL del software con la bóveda existente, no de redacción ni instalación de una empresa nueva.

Lee AGENTS.md, guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md y docs/ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md en el checkout maestro.

1. Identifica la ruta existente de la bóveda de esta empresa y el repositorio maestro. No crees otra bóveda, no copies plantillas, no abras textos empresariales expresamente rechazados ni supongas que los resúmenes anteriores sustituyen las fuentes.
2. Ejecuta un preflight de Git: rama, SHA y status. Si el árbol tiene modificaciones, NO fuerces cambios, detén la actualización y explica cómo preservarlos. Si está limpio, sincroniza al commit de main autorizado por el propietario; verifica SHA exacto después.
3. Ejecuta desde el checkout actualizado el programa scripts/aceptacion_integracion_local.py con los argumentos --vault, --salida y --commit-esperado, usando el intérprete local comprobado. La carpeta --salida debe ser NUEVA, privada y EXTERNA a bóveda y Git. El programa no modifica la empresa. Si falla, conserva y entrega el ZIP con resultados saneados.
4. Contrasta desde Obsidian GUI las 16 Bases, D/X, enlaces a las fuentes autorizadas y si se pueden navegar. CLI sólo cuando esté funcional. NO marques PASS de GUI por observar rutas en disco.
5. Ejecuta la prueba completa con una empresa enteramente ficticia y aislada. Si una prueba falla, diagnostica su causa, no alteres la bóveda real para corregirla.
6. No apliques migración de Bases, revisión D/X, relaciones o mapa Canvas en la empresa real. Primero entrega al dueño el reporte, los bloqueos y el plan de corrección con respaldos.
7. Declara por separado: código GitHub, pruebas Mac, estado de la bóveda, interfaz Obsidian, Codex autónomo, segunda sesión, restauración y segunda computadora; PASS, FAIL o NO_VERIFICADO. Anexa evidencia observada y no una conclusión general sin pruebas.
8. No redactes una nueva D01. Recuperar y aplicar la arquitectura de notas requiere otra revisión específica después de validar la integración.

Tu entregable principal es el ZIP saneado del diagnóstico junto con una interpretación de los fallos y próximos gates, no otro texto comercial genérico.

No subas información privada al repositorio maestro ni envíes comunicaciones a terceros.
