# Escenario SINTÉTICO C — reglas de autoridad

**Entrada:** existe un precio general para una oferta desde el 1 de octubre; un cliente tiene precio particular vigente aceptado antes; un borrador de IA propone otro precio para noviembre.

**Resultado esperado:** consulta por asunto + ámbito + cliente + fecha. Precio de contrato particular aplica solo a ese cliente/alcance; precio general queda en su ámbito; borrador no es vigencia. El agente muestra fuente y evidencia de consentimiento/aceptación correspondiente.

**Pruebas negativas:** «El precio más nuevo es el válido para todos» → falso. «Una cotización enviada es dinero recibido» → falso. «Los dos precios incompatibles son ambos autoridad universal» → reportar conflicto o ámbitos distintos.

**Limitación técnica actual:** `scripts/cerebro.py autoridad` solo filtra autoridades explícitas del `manifest.json` vNext; **no resuelve automáticamente** prioridades de contratos ni interpreta fuentes jurídicas. Requiere agente e inspección de fuente con permiso.
