# Contrato semántico (resumen para operadores)

La referencia canónica es `contratos/vNext-0.9/Contrato_Traspaso_vNext.md` junto al esquema y al manifest específico de cada transferencia.

**No confundir cuatro ejes:**

- Editorial: `borrador`, `en_revision`, `aprobado`, `retirado`.
- Cobertura POR PREGUNTA: `sin_fuente`, `parcial`, `suficiente_para_tarea`, `no_aplica` (justificado).
- Estado de CONOCIMIENTO por afirmación: `hecho_observado`, `decision_aprobada`, `propuesta`, `hipotesis`, `historico`, `pendiente`, `desconocido`, `conflicto`.
- Vigencia: `vigente`, `futuro`, `superseded`, `caducado`, `sin_verificar` más fechas disponibles.

**Evidencia:** `documental_directo`, `testimonio_atribuido`, `observacion`, `derivado_calculado`, `sin_fuente`, `fuentes_en_conflicto`.

**Sensibilidad:** `interno`, `confidencial`, `restringido`. No es ACL: si una bóveda se comparte, sus archivos pueden quedar visibles. El importador MVP solo admite `interno` y documentos sin marcas de restricción superior.

**Autoridad:** se resuelve por pregunta + asunto + entidad + contexto + intervalo temporal + permiso; no gana automáticamente el documento nuevo. Registro de fuente y registro financiero/CRM no se sustituyen por la memoria documental.

**Revisión de cambios:** antes de actualizar precio/política/acuerdo, identificar fuente autoritativa, alcance, qué contradice, decisiones para autorizar, dependientes afectados, fechas, versión previa. Historial no se destruye.

**Datos incompletos:** conservar explícitamente `pendiente`, `no_verificada`, los huecos K1–K4 del Paso 1. Ningún script o modelo certifica la verdad del negocio por tener YAML válido.
