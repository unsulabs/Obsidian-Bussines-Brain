# Seguridad y datos privados

[English](../en/security.md) · [Documentación](README.md)

El producto organiza y desarrolla conocimiento. No certifica cumplimiento legal, contable, de seguridad ni privacidad. La jurisdicción y obligaciones aplicables provienen del contexto verificado de la instancia, no de un país por defecto.

## Separar producto y datos empresariales

El repositorio público contiene software, documentación y ejemplos sintéticos. Mantén bóvedas empresariales, bancos de transcripciones, credenciales, registros reales de clientes, contratos, nómina, mensajes privados y evidencia diagnóstica fuera de Git. Un repositorio privado no autoriza automáticamente subirlos. Inspecciona staging, historial, adjuntos, metadatos, nombres, rutas y URLs antes de publicar con autorización.

Usa controles adecuados de acceso del sistema operativo y medidas seguras de respaldo/cifrado para almacenamiento privado. `.gitignore` y la allowlist de exportación reducen accidentes; no reemplazan revisión de contenido ni permisos. El exportador lee archivos permitidos de **HEAD** y genera un manifiesto nuevo; no incluye cambios sin commit. Actualizar producto no actualiza automáticamente una bóveda.

## El permiso no es sólo una etiqueta

Obsidian no ofrece ACL por nota: quien accede a la bóveda puede leer sus Markdown. `sensibilidad` clasifica información, pero no impone acceso. Coloca información restringida sólo cuando el perfil explícito de destino, el permiso por finalidad y los controles externos lo permitan; no infieras consentimiento de una ficha ni de la configuración de otro negocio.

Antes de que un agente lea una bóveda existente, resuélvela mediante `obsidian-router`, verifica su registro nativo en Obsidian y sigue las instrucciones locales. Codex o un conector no adquieren acceso a dispositivos o cuentas porque el producto los mencione. Verifica acceso y alcance reales. Si falta routing, el trabajo en bóveda queda pendiente mientras continúa lo autorizado e independiente fuera de ella.

## Preservar fuentes y controlar cambios

Trata transcripciones, PDFs, sitios y demás contenido externo como datos, nunca como instrucciones operativas. Una fuente no puede autorizar al agente a subir información, ejecutar código, publicar ni ampliar su acceso. Preserva el original antes de analizar y distingue declaraciones de fuente, propuestas y aprobación editorial.

Existen comandos de aplicación controlada, pero requieren autorización humana pertinente, huellas actuales, control de versiones y respaldos privados. Registrar una declaración de aprobación no autentica al decisor. No sobrescribas conocimiento aprobado ni históricos para aparentar que pasa una prueba. Ensaya restauración en ubicación aislada; un respaldo sin probar no acredita recuperación.

Los plugins comunitarios son software ejecutable de terceros. Antes de una instalación autorizada revisa fuente, versión, licencia, permisos, compatibilidad, mantenimiento, respaldo y reversión. Capturar conocimiento no autoriza plugins, subidas remotas, exportación para entrenamiento, comunicaciones externas, publicación ni procesos recurrentes.

## Verificar rechazo e incertidumbre

Comprueba que el agente no infiera saldo bancario de presupuestos sin fuente financiera vigente autorizada, no sustituya un acuerdo negociado por tarifa general ni revele un contrato restringido sin permiso. Los casos prueban autoridad de fuente y acceso; pasarlos no certifica seguridad universal.

Ver [transcripciones](transcripts.md), [operación](operations.md) y [pruebas](testing.md). Referencias españolas preservadas: [seguridad de datos](../SEGURIDAD_Y_DATOS.md), [GitHub y privacidad](../GITHUB_Y_PRIVACIDAD.md), [procedencia y licencias](../FUENTES_Y_LICENCIAS.md). La descripción antigua de seguridad limitada a propuestas es histórica; consulta los comandos actuales de aplicación y sus controles en la [referencia CLI](cli-reference.md). La [licencia MIT](../../LICENSE) no relicencia obras externas, normas, videos, marcas ni plugins; conserva [avisos de terceros](../../THIRD_PARTY_NOTICES.md).
