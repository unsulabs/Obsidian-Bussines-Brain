---
name: ce-continuidad
description: "Retomar y mantener diariamente una bóveda empresarial ante conversaciones, clientes, archivos, decisiones, correcciones y tareas, sin perder fuentes ni reentrevistar al dueño."
---

# ce-continuidad

Conversa nueva/partes pendientes → [ce-banco-transcripciones](../ce-banco-transcripciones/SKILL.md). Reanuda lote por job_id, intento, versión, snapshot/cursor y hashes; no vuelvas a descargar ni analizar indiscriminadamente. Corrección/categoría/permiso → [ce-revisar-antecedentes](../ce-revisar-antecedentes/SKILL.md), invalida derivados afectados y conserva lo no afectado. La aceptación de instalación aplica a instalación/migración, no a cada consulta o mantenimiento cotidiano; recupera sólo estado y fuentes pertinentes. Fuente original nueva no implica aprobación editorial.

**Primero recuperar estado real:** si ya existe bóveda, resolver primero obsidian-router y sus instrucciones, luego localizar estado y fuentes pertinentes sin modificaciones. En aceptación de instalación/migración sigue guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md. No considerar continuidad SES o resumen anterior como sustituto de originales. No reejecutar crear ni regenerar notas existentes.

1. Reabrir una instancia específica confirmando ruta e identidad de la empresa; ejecutar `estado` y `validar` para relectura del estado real. Si falla el Python predeterminado por un módulo ausente, buscar el intérprete o venv ya verificado para esa instancia y repetir allí. Registrar ambos resultados; sólo declarar la capacidad no verificada después de ese intento seguro.
2. Revisar el último archivo de `90_Sistema/Continuidad/` si existe, las notas afectadas y sus fuentes, no asumir que bitácora antigua prevalece.
3. Trata cada entrada nueva como posible cambio del conocimiento: identifica el episodio, las decisiones, señales, excepciones y patrones del dueño; ubica su fuente original y las notas que dependen de ella. Recupera y compara antes de pedir información que ya consta. Una captura provisional no reemplaza el trabajo de incorporarla a la unidad pertinente.
4. Distingue corrección de error anterior, hecho nuevo, propuesta y decisión aprobada. Si cambia una afirmación canónica, usa `ce-cambios`: conserva versión, fecha, motivo, fuente y repercusiones; corrige todos los lugares afectados sin propagar una interpretación cuestionada. Si aparece un asunto con identidad propia, usa `ce-arquitectura-conocimiento`, evitando duplicados.
5. Ejecuta una tarea real con las notas actualizadas mediante `ce-consulta`; comprueba que la versión anterior no se presenta como vigente y que otro agente puede seguir la instrucción transferible. No declares mantenimiento terminado por guardar una continuidad.
6. Cierra después del trabajo mediante `python scripts/cerebro.py continuidad --vault ... --resumen "..." --siguiente "..." --revisado-por "..."`. No incluir secretos ni relatos especulativos. Verifica los archivos modificados, `estado` y `validar` y devuelve una ruta de continuación natural.
**Salida:** conocimiento y trabajo efectivamente actualizados, impactos comprobados, rutas/IDs y siguiente necesidad real. Si no hubo cambio, explica qué fuente o decisión concreta lo impidió; no fabriques progreso.
