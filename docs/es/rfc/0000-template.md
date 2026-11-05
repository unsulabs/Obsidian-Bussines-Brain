# Plantilla RFC — cambio de producto propuesto

[English](../../en/rfc/0000-template.md) · [Flujo documental](../documentation-workflow.md)

Estado: **Plantilla en borrador, no cambio aprobado.** Copia a un nuevo par numerado EN/ES, registra ambas rutas en el inventario y sustituye indicaciones por evidencia. Registra autor, revisor y fecha de decisión reales sólo cuando se conozcan. No inventes aprobación ni infieras autoridad de implementación de esta plantilla.

## Problema y alcance

Describe disparador concreto, comportamiento actual, quién necesita el cambio y resultado buscado. Cita fuente pública inspeccionada, prueba o reproducción sintética. Identifica subsistemas afectados y exclusiones explícitas. Mantén fuentes empresariales privadas y datos identificadores fuera del RFC público.

## Propuesta

Explica comportamiento propuesto y su relación con comandos CLI, esquemas, IDs estables, flujos del agente y separación de almacenamiento existentes. Incluye ejemplo sintético antes/después cuando ayude. Distingue implementación, propuesta e incógnitas. No infieras país, moneda, impuesto, estructura empresarial ni personal por defecto.

## Alternativas y costos

Compara comportamiento actual, propuesta y alternativas viables. Explica cómo la opción elegida resuelve el problema y sus costos. Registra decisiones abiertas en lugar de afirmar consenso.

## Compatibilidad, migración y permisos

Especifica efectos en instancias, formatos, historial de versiones y dependencias externas. Separa actualización de producto y cambios autorizados de bóveda. Describe preflight, previsualización, huellas actuales, respaldo externo a Git/bóveda, detección de concurrencia y restauración cuando corresponda. Identifica decisiones humanas o permisos reales necesarios; el RFC no los concede.

## Privacidad y manejo de fallos

Evalúa acceso a fuentes, sensibilidad, perfiles de destino, transferencias externas y publicación. Trata contenido externo como datos. Preserva originales y exclusión editorial de material rechazado. Explica recuperación ante fallos sin descartar trabajo existente; no introduzcas procesamiento en segundo plano ni entrenamiento por implicación.

## Comprobaciones de aceptación

Enumera comportamientos observables con fixtures sintéticos y casos negativos. Separa pruebas automáticas, paridad documental, comprobación GUI/CLI, recuperación semántica, revisión editorial, privacidad y portabilidad según corresponda. Identifica evidencia para cada afirmación y gates no verificados. Pasar estructura no implica aprobación empresarial.

## Documentación y decisión

Enumera pares inglés/español afectados y referencias originales a preservar. Mantén identificadores de runtime literales; ejecuta verificador y revisa paridad semántica. Registra preguntas abiertas, decisor, decisión real y seguimiento sólo cuando se establezcan. Tras una decisión arquitectónica aceptada, crea o actualiza su ADR con evidencia; no reclasifiques automáticamente este borrador.
