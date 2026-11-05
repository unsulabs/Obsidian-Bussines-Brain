# Prompt de continuidad para Codex — empresa que YA tiene bóveda

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
