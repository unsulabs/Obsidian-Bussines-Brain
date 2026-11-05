# Guía de uso

[English](../en/user-guide.md) · [Documentación](README.md)

## Construir conocimiento para una tarea real

Empieza por una pregunta o tarea: explicar cómo calificas a un cliente, preparas una oferta, entregas trabajo o tomas una decisión. El producto sirve a negocios y autoempleo sin presuponer departamentos ni personal.

1. Recupera originales autorizados y criterio del dueño. Distingue hechos, propuestas, hipótesis, afirmaciones históricas y decisiones aprobadas.
2. Identifica asuntos y notas canónicas existentes. Ante varios asuntos, muestra la arquitectura del conocimiento antes de redactar. D01–D07 y X01–X07 organizan síntesis y expedientes; no son una cuota de archivos vacíos.
3. Desarrolla mecanismos, razones, excepciones y alternativas. Materializa trabajo autorizado con IDs estables, enlaces a fuentes, estado editorial, historia y respaldos cuando corresponda.
4. Usa el conocimiento para la tarea real y plantea una pregunta que deba conservar incertidumbre. Contrasta fuente → nota y nota → respuesta antes de afirmar utilidad.
5. Registra correcciones y continuidad. Una primera nota o validación estructural no acepta todo el cerebro empresarial.

## Continuar una instancia existente

Usa [Continúa con Codex](../../PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md). El agente verifica routing antes de acceder a la bóveda; después lee instrucciones locales, `Como_usar`, `Inicio`, notas y pasajes originales pertinentes. No recrea la bóveda ni repite la entrevista inicial. Leer una ficha no demuestra haber leído el original en esta sesión.

## Añadir una conversación o transcripción

Identifica el material como conversación/transcripción e indica si habrá más partes. El ciclo predeterminado preserva cada entrega exacta antes del análisis, registra procedencia/sensibilidad/completitud, revisa todos los asuntos y antecedentes e integra ficha, acceso al texto íntegro y conexiones justificadas dentro de la autorización de la instancia.

Un enlace solo no es un original capturado. Accesos o partes faltantes quedan pendientes. Documentos ordinarios, código, enlaces GitHub y preguntas largas conservan su tarea; su longitud no autoriza ingestión como transcripción. Los permisos pertenecen a esta instancia y finalidad, no al perfil de otro cliente. Ver [transcripciones](transcripts.md).

## Corregir conocimiento y navegarlo

Una corrección activa revisión de fuentes y propuesta explícita; no sobrescribe silenciosamente conocimiento aprobado ni reescribe históricos. Si evidencia nueva contradice una decisión aprobada, conserva ambas y presenta la decisión material. La redacción empresarial rechazada no debe volver como autoridad a través de resúmenes.

Bases y mapas ayudan a navegar; los enlaces no prueban relaciones. Previsualiza el mapa antes de publicarlo, acción que necesita autorización propia, hashes y respaldo privado externo. No implica migración automática ni procesamiento recurrente. Ver [flujo de conocimiento](knowledge-workflow.md) y [operación](operations.md).

## Comprobar estado y pedir ayuda

Tras activar el entorno Python y verificar el destino de la bóveda:

```bash
python scripts/cerebro.py estado --vault /private/path/MyBusiness
python scripts/cerebro.py validar --vault /private/path/MyBusiness
```

Son comprobaciones estructurales, no prueba de exactitud semántica ni comportamiento GUI. Si falla routing, conserva trabajo autorizado fuera de la bóveda. Si fallan dependencias, verifica intérprete y entorno existente. Si una respuesta pierde significado, vuelve al original y recorre fuente → respuesta en lugar de editar notas para aparentar que pasa una prueba.

Para un fallo de producto entrega una reproducción sintética y diagnóstico saneado según [contribución](contributing.md). Nunca adjuntes fuentes empresariales reales ni credenciales. Ver [seguridad](security.md) para los límites de privacidad.
