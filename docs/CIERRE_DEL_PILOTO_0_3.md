> **Protocolo histórico de aceptación del candidato 0.3.** Para la versión actual 0.4, ejecutar adicionalmente F1–F9 de [CRITERIOS_DE_ACEPTACION.md](CRITERIOS_DE_ACEPTACION.md) y la [especificación de red](ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md). No asumir aceptación previa del mapa ni de la arquitectura agéntica.

# Cierre del piloto 0.3 — protocolo de Codex en computadora autorizada

## Objetivo y ámbito

Probar un producto de conocimiento empresarial reproducible, no únicamente una instalación de Obsidian. El código maestro es GitHub; el conocimiento y sus originales viven en bóvedas privadas. Las pruebas de escritura se realizan primero con empresa ficticia o **copia aislada**, nunca sobre el D01 real sin decisión específica.

La suite local prueba el código; no sustituye pruebas de Obsidian GUI/CLI ni decisiones de la empresa. El workflow remoto se retiró cuando la cuenta dejó de iniciar jobs por facturación o límite de gasto; ese fallo no se convierte en fallo de Python.

## Preparación y controles

1. Codex confirma checkout Git limpio, commit exacto y Python 3.11 disponible. No abre bóvedas cuyo contenido haya sido rechazado.
2. Comprueba que la bóveda real esté fuera de Git. Antes de migrar verifica inventario, ID, hashes de D01, seis fuentes, continuidad y configuraciones Obsidian. **No sobrescribir** la bóveda real ni reejecutar el comando crear.
3. Ejecuta en la bóveda real solamente comandos de lectura: `estado`, `validar` y `aceptacion`. Reporta qué se ha comprobado y qué todavía no.
4. Prepara una copia de prueba **externa al repositorio y fuera de la bóveda real**, que no exponga datos sensibles. Preferir empresa 100 % sintética para pruebas adversariales. Si la copia contiene contenido real, no abrirla sin permiso expreso.
5. Comprobar en Obsidian Desktop y CLI: abrir Inicio, Documentos y Ofertas; 16 Bases accesibles; plantillas excluidas; D01 legible y en_revision; fuentes navegables. Registrar capturas y errores sin publicar datos empresariales.
6. En la copia aislada ejecutar creación D/X, modificación por propuesta, revisión de G1–G7, rechazo de aprobación con cobertura parcial, conflicto de SHA, respaldo externo privado, restauración y relaciones propuestas/ratificadas. Comprobar que la nota real y custodia histórica permanecen idénticas.
7. Reanudar otra sesión sin depender del texto de un chat previo. Utilizar `consulta-contextual` para localizar bloques candidatos con fuentes, fecha y estado; **no afirmar que esa búsqueda es semántica**.  Preguntar por un hecho documentado citando fuente/ámbito/fecha y por un hecho deliberadamente no documentado. Nunca fingir capacidad de búsqueda semántica si sólo hay búsqueda literal.
8. Probar en una **segunda computadora limpia**, previa autorización del propietario, el repositorio, dependencias, Obsidian GUI, CLI, capacidades core y recuperación desde un paquete de ejemplo sintético.
9. Elaborar acta de aceptación con PASS/FAIL/NO VERIFICADO por prueba, rutas y hashes, capturas de GUI y decisión humana sobre aprobación del producto. Guardar el acta privada en la computadora; subir a GitHub sólo reporte técnico anonimizado autorizado.

## Criterios de salida

- **Código integrado:** la suite completa y la prueba integral aprueban en la Mac para el commit exacto, con salidas guardadas fuera de Git; el árbol principal coincide con el SHA probado. No atribuir PASS a un runner remoto que no inició.
- **Piloto local aceptado:** además, Codex ejecutó los pasos 1–7 y documentó la evidencia en una copia.
- **Reutilizable por otra empresa:** además, paso 8 aprobado y procedimiento de instalación explicado para una persona no técnica.
- **Producción con datos sensibles o varios usuarios:** sólo cuando haya permisos externos efectivos, backup/restauración probado, responsabilidad del operador y alcance de fuentes autorizadas.

Una interfaz que muestra notas no garantiza recuperación correcta, ni un registro de aprobación firmada por texto valida la identidad del revisor. Los cuatro estados no son equivalentes.

## Prompt para Codex (sin escritura productiva)

**Continúa la aceptación del Cerebro Empresarial.** Desde el checkout actualizado, recupera el estado real, ejecuta `python3 scripts/cerebro.py aceptacion --vault "<bóveda privada autorizada>"` en sólo lectura y revisa `docs/CIERRE_DEL_PILOTO_0_3.md`. Prueba nuevas funciones únicamente con empresa ficticia o copia aislada, informa cada PASS/FAIL/NO VERIFICADO y pide autorización separada para cualquier aplicación/migración en la bóveda real. No reutilices textos empresariales rechazados ni publiques información privada. No declares producción lista sin pruebas locales y aceptación del propietario.
