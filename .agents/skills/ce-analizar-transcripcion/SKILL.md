---
name: ce-analizar-transcripcion
description: "versión preservada a analizar, corrección o invalidación de análisis anterior."
---

# ce-analizar-transcripcion

Lee el [contrato común](../ce-banco-transcripciones/references/contrato-comun.md) para estados, permisos, contexto y disponibilidad.

- **Trigger:** versión preservada a analizar, corrección o invalidación de análisis anterior.
- **Inputs:** original y hash, mapa de offsets, todas las partes, taxonomía versionada, contexto canónico con hashes y políticas de acceso. Una versión parcial puede analizarse provisionalmente, sin declararla completa.
- **Outputs:** análisis de cada núcleo, afirmaciones atribuidas, matriz asunto→pasaje→destino, cobertura mecánica/semántica, conciliación de conversación entera, run inmutable con dependencias. Diferenciar decisiones, ideas, razones, excepciones y dudas; campos ausentes permanecen ausentes.
- **Errores:** `SOURCE_CHANGED`, `OFFSET_INVALID`, `COVERAGE_GAP`, `UNSUPPORTED_ENCODING`, `ANALYSIS_INCOMPLETE`, `CONTEXT_STALE`. No resolver atribución incierta inventando identidad.
- **Gate:** partición reconstruye bytes exactos; cada núcleo examinado; todos los asuntos materiales tienen destino o conservación razonada en fuente; juez independiente comprueba muestra y pasajes con correcciones cruzadas. Cobertura numérica de 100% no demuestra comprensión por sí sola.

## Ejecución

La interpretación es trabajo del agente lector: ningún título, regex, lista de palabras o categoría preasignada acredita análisis semántico. Validadores sólo comprueban estructura, hashes y cobertura mecánica. Examina cada núcleo con vecinos, identifica cambios tardíos y vuelve al conjunto antes de conciliar. Si hay laguna, conserva incertidumbre. Registra explícito/paráfrasis/inferencia, voz atribuida, mecanismo, razones, alternativas y excepciones; una síntesis comercial no reemplaza asuntos secundarios.

Verifica cada cita abriendo los bytes originales en esta ejecución: TR-ID, versión, SHA-256, offsets bytes UTF-8 [start,end), hash del extracto; comprobar límites de carácter. No citar una ficha como si se leyó el original. Un run requiere text_sha256, segmenter_version, analyzer_version, taxonomy_version, canonical_context_hashes y permission_snapshot. Cambio de cualquiera invalida lo afectado; nuevo run preserva historial y repite conciliación global.

Usa [taxonomía](../ce-taxonomia-conocimiento/SKILL.md) para identidad y [antecedentes](../ce-revisar-antecedentes/SKILL.md) para conexiones. Después arquitectura: una ficha lógica por transcripción, notas dueñas por asunto cuando se justifique. Permiso para analizar no autoriza integrar ni ratificar.

Si el dueño ya autorizó integrar fuentes sensibles en su bóveda privada, conserva sensibilidad original y aplica el [perfil de destino privado](../ce-banco-transcripciones/references/destino-privado.md): ruta/empresa/audiencia/TR explícitos, política sellada y permisos vivos local_analysis/internal_query. No excluirlas por ser confidenciales ni reclasificarlas a interno; no ampliar esa autorización a otras bóvedas o finalidades. Las Bases y manuales genéricos ya enlazados se conservan; las fichas, vistas íntegras y mapas con fuentes sensibles propagan la clasificación máxima.
