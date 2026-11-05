# 05 — Sistema agéntico conceptual e interoperabilidad

**Estado:** especificación de comportamientos y pruebas futuras. No hay integración de agentes implementada ni validada por esta entrega.

## El mismo producto debe servir para tres superficies distintas

| Superficie | Qué podría hacer si está autorizada | Qué NO hay que suponer | Intercambio mínimo |
|---|---|---|---|
| Codex con archivos/Terminal | Leer repositorio, configurar instancia local, ejecutar pruebas, crear propuestas y cambios versionados | Acceso a Google, internet, secretos o aplicaciones gráficas sin verificar | Contratos + estado + rutas + fuente + autorización por operación |
| Claude Code u otro harness | Leer/editar según herramientas y permisos reales, seguir skills específicas | Que `AGENTS.md`, `CLAUDE.md`, `SKILL.md` signifiquen lo mismo | Traductor de instrucciones verificado por harness |
| Chat de IA sin conectores/agencia | Analizar paquetes suministrados, preguntar, redactar y devolver cambios propuestos | Acceso al disco, Obsidian, correo, CRM, ejecución o memoria permanente | Context pack acotado y retorno con fuentes/decisiones |

**Terminología:** no todo asistente al que una persona llama «agente» tiene ejecución autónoma. El producto no debe mentir sobre las capacidades habilitadas.

## Contrato de ejecución propuesto, independiente de herramienta

1. **Identificar usuario, empresa, propósito, ámbito y capacidad real del asistente.**
2. **Determinar fuentes autorizadas**: archivos vNext, notas, sistemas externos o evidencia no accesible.
3. **Recuperar por pregunta y contexto**: buscar autoridad, fecha, límites de acceso y contraevidencia.
4. **Clasificar objetivo**: `consultar`, `desarrollar`, `crear_propuesta`, `actualizar_aprobado`, `ejecutar_actividad_externa`.
5. **Producir resultado con estado correcto**: hechos citados, hipótesis señaladas, preguntas K1, fuentes K2, K3 pendientes.
6. **Preparar cambios con diff e impacto**, límites, riesgos y prueba; solicitar autorización para actos relevantes.
7. **Escribir solo en alcance permitido**; verificar relectura y registrar referencias de revisión.
8. **Comprobar recuperación y continuidad**: una segunda sesión debe responder desde fuentes, no desde su propia conversación anterior.

## Propuesta de paquete de contexto portable (formato aún abierto)

Contenido lógico mínimo: `empresa/instancia`, `intención/tarea`, `fecha_de_consulta`, `rol_y_permisos`, `autoridad_por_asunto`, `fragmentos_con_ID`, `fuentes`, `restricciones`, `referencias_temporales`, `preguntas_o_pruebas`, `formato_de_respuesta` y `protocolo_de_retorno`. No entregar toda la bóveda por defecto; preparar la evidencia necesaria para la pregunta.

Debe haber **control de minimización**: si la tarea es redactar una pieza de marketing, no adjuntar contratos confidenciales de clientes ni datos bancarios por comodidad. Un permiso en un JSON sin contención técnica real no debe tratarse como defensa de acceso.

## Acciones operativas a desarrollar por iteraciones

| Tipo de operación de agente | Entrada | Salida esperada | Guardarraíl |
|---|---|---|---|
| Recuperar y responder | Pregunta y ámbito | Respuesta con referencias y vigencia | Señalar no verificado/conflicto |
| Construir conocimiento | Conversación, documentos, criterio experto | D/X, bloque o entidad propuesta | No inventar fuentes ni rellenar K1 con genéricos |
| Enlazar | Dos objetos, evidencia y sentido de relación | Relación tipada justificable | No asumir causalidad/contratación por simple mención |
| Crear proyecto/tarea | Decisión u obligación concreta | Proyecto/tareas/fechas en estado propuesto | No declarar completado por creación |
| Revisar estrategia | Prioridades y resultados verificables | Discrepancias y oportunidades con incertidumbre | No deducir inacción de ausencia de notas |
| Gestionar cambios | Afirmación original + modificación | Diff, histórico, impacto, autorización | No pisar fuente autoritativa externa |
| Actualizar instrucciones | Resultado de prueba real | Propuesta de mejora a skill/instrucción | No autoeditar permisos ni políticas por conveniencia |
| Exportar contexto | Uso previsto y destinatario | Paquete autorizado legible por otro harness | Sin secretos ni archivos de terceros restringidos |

## Skills candidatos y delimitación

- `descubrir_contexto_empresarial`: inventariar fuentes y detectar K1–K4.
- `resolver_autoridad`: escoger fuente competente o devolver conflicto con prueba.
- `desarrollar_documento`: incorporar criterio experto sin convertirlo en contenido genérico.
- `vincular_entidades`: extraer y validar relaciones semánticas.
- `consultar_oferta_vigente`: distinguir oferta general, condición particular y contrato.
- `revisar_proyecto`: eventos, compromisos, responsables y dependencias.
- `registrar_reunion`: hechos, participantes, decisiones confirmadas y pendientes.
- `analizar_impactos`: proponer cambios derivados con límites.
- `revisar_coherencia_estrategica`: contrastar prioridades y evidencia de ejecución.
- `auditar_boveda`: integridad, referencias, vencimientos, permisos y recuperación.

**Son candidatos de responsabilidad**, no diez skills que deban instalarse ni APIs prometidas. La distribución funcional se decidirá comparando simplicidad, independencia de harness y cobertura de pruebas.

## Autorización de cambios y sistemas oficiales

- Consultar un registro autorizado no concede permiso de modificarlo.
- Cambiar un dato interno, modificar una fuente externa, enviar un mensaje, publicar una oferta y ejecutar una transacción son **acciones distintas**.
- El `inbox` de propuestas inspirado en VID-004 es útil para revisión; no es mecanismo de seguridad si el agente mantiene permisos de escritura globales. Requiere aislamiento de herramientas/directorios/credenciales o entorno con restricciones efectivas cuando aplique.
- Una operación comercial o de privacidad sensible exige comprobar identidad del aprobador, alcance, revisión original y permiso antes de escribir.
- Cuando falten herramientas/conexiones, devolver bloqueo exacto y procedimiento autorizado, no navegar interfaces o crear sustitutos sin permiso.

## Evolución del repositorio sin corromper instancias

**Separación lógica propuesta:** producto maestro (código, contratos, plantillas, pruebas, versiones) / instancia privada de empresa (información, índices, permisos, personalizaciones, conexiones). Cómo distribuir, actualizar, sincronizar y respaldar se investigará antes de aprobar tecnología.

La aceptación debe demostrar actualización reversible en una empresa ya poblada, sin convertir archivos de demostración en datos reales, sin sobrescribir extensiones y preservando IDs/fuentes/históricos.

## Riesgos de inyección y confianza de contenido

Una transcripción, web, documento o nota es **dato externo**, no instrucciones para el asistente sobre cómo operar. Separar fuentes de reglas del producto, verificar comandos antes de ejecutar, pedir autorización de instalaciones y no derivar privilegios de textos hallados en una página.
