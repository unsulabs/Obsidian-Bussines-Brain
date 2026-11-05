# 06 — Cómo incorporar nuevos assets, videos, metodologías, plugins y documentación

Este flujo permite seguir recibiendo recursos sin empezar desde cero cada vez y **sin instalar automáticamente** nada que aparezca en un tutorial.

## Clasificar el material de entrada

| Clase | Ejemplos | Qué se intenta recuperar |
|---|---|---|
| `TUTORIAL_VIDEO` | Video YouTube + subtítulos | Flujo explicado, acciones, restricciones, timestamps, demostraciones pendientes de observar |
| `TEMPLATE_BOVEDA` | Nota/paquete comercial o GitHub | Propósito, estructura, licencia, dependencias, datos de ejemplo, límites |
| `PLUGIN` | TaskNotes, visualizaciones, automatización | Función, compatibilidad, mantenimiento, privilegios, portabilidad |
| `FRAMEWORK` | Metodología empresarial, investigación, libro | Problema, supuestos, ámbito, evidencia, criterios y límites de generalización |
| `FUENTE_EMPRESARIAL` | Contrato, CRM, documento, audio, correo | Dato, autoridad, permisos, edición, temporalidad, vínculo con empresa concreta |
| `INSTRUCCION_AGENTE` | Skill, AGENTS.md, CLAUDE.md, workflow | Herramienta compatible, precondiciones, permisos, efectividad observada |
| `ACTIVO_INTERNO_PREVIO` | Kit vNext, contrato 0.9, CE Core v0.1 | Continuidad, estado probado, partes a reusar y puntos sin aprobar |

## Protocolo de siete pasos

1. **Registrar:** ID, título, autor/editor, URI/origen, versión, fecha de acceso, tipo de licencia, alcance del consentimiento y disponibilidad de contenido completo.
2. **Recuperar:** fuente íntegra cuando sea posible (transcripción con tiempos, documentación oficial, repo específico). Distinguir `obtenido`, `parcial`, `no_accessible`, `no_verificado`.
3. **Extraer hallazgos:** cada hallazgo con cita/localizador, ejemplo, tarea que resuelve, dependencias, incertidumbre y lo que **no demuestra**.
4. **Relacionar:** qué requisitos declarados RQ-xxx, clases vNext o capacidades CAP-xx ilumina; qué contradice; qué es nuevo; qué resulta duplicado.
5. **Comparar alternativas:** nativo Obsidian vs plugin vs proceso asistido vs sistema externo, y efecto de remoción.
6. **Evaluar compatibilidad:** licencia, mantenimiento, riesgo de seguridad, costo, privacidad, soporte y prueba reproducible antes de aceptar componente.
7. **Solicitar decisión:** etiqueta `candidato`, `aceptado_para_prueba`, `aceptado_para_implementacion` o `descartado_con_motivo`. Solo una decisión explícita puede elevar una alternativa a arquitectura aprobada.

## Esquema lógico mínimo de ficha (no obliga formato físico)

- `asset_id`, `tipo`, `nombre`, `fuente_primaria`, `localizador`, `autor`, `fecha_acceso`.
- `captura_estado` y `cobertura_de_lectura` (nunca declarar visto completo si solo hay transcript o resumen).
- `licencia_y_uso_permitido`, `restricciones`, `version`, `compatibilidad` cuando apliquen.
- `hallazgos[]`: ID, referencia al fragmento, descripción, evidencia, nivel de confianza y limitación.
- `capacidades_relacionadas[]` y `requisitos_RQ[]`.
- `contradicciones[]`, `hipotesis[]`, `preguntas_abiertas[]`, `prueba_sugerida`.
- `estado_de_decision` y `autoridad_de_aprobacion`.

## Tratamiento especial de videos

- El enlace de YouTube es un localizador; la transcripción puede estar en varios idiomas o no estar disponible.
- Leer subtítulos con tiempos permite analizar **lo dicho**, no verificar todas las pantallas, rutas, plugins, configuraciones o efectos visuales.
- No asumir que todos los videos tienen transcripción ni que un tutorial actualizado es compatible con futuras versiones.
- Para validar un plugin: contrastar documentación oficial/repositorio/mantenimiento, no solo seguir el tutorial.
- Respetar derechos de autor y licencias: no redistribuir transcripciones completas o bóvedas propietarias sin autorización.
- Si dos videos del mismo creador describen la misma idea, no contarlos como validación independiente.

## Tratamiento especial de archivos empresariales

- K1 criterio del experto / K2 registro oficial / K3 desconocido / K4 no necesario ahora.
- Conservar huella/verificación del origen, fecha efectiva, estado editorial, restricciones y ámbito.
- No copiar datos sensibles a GitHub público ni integrar muestras reales a plantillas distribuidas.
- Si ya existe autoridad documental en CRM/contabilidad/contrato, conservar referencia controlada y no crear copia autoritativa en la bóveda.

## Cómo evitar que el expediente de investigación se convierta en el conocimiento de la empresa

**Dos circuitos separados:**

- **Biblioteca del producto:** tutoriales, hallazgos, decisiones de diseño, licencias, pruebas de plugins y patrones genéricos de instalación. Pertenece al repositorio maestro.
- **Conocimiento de cada empresa:** documentos, entidades, fuentes, autorizaciones, proyectos y datos de esa empresa; vive en instancia privada. La metodología del producto puede usarse aquí, pero no trasladar automáticamente tutoriales como reglas comerciales.

## Punto de control antes de la arquitectura

Cada propuesta importante debe tener una cadena: `problema real → requisito RQ → evidencia / caso → alternativa técnica → riesgo/limitación → prueba → aprobación`. Si falta un eslabón, no es parte de la arquitectura aprobada.
