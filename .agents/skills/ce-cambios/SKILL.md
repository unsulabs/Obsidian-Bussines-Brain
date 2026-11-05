---
name: ce-cambios
description: "Gestionar modificaciones en conocimiento empresarial sin sobrescribir autoridad: cambios de precios, procesos, decisiones o promesas."
---

# ce-cambios

Corrección, taxonomía o permiso sobre corpus activa [ce-revisar-antecedentes](../ce-revisar-antecedentes/SKILL.md): evento versionado, fuentes antigua/nueva, dependientes e incertidumbre. No propagar el texto cuestionado mediante resumen/cita circular. Revalidar SHA base y autorización vigente antes de aplicar con interfaz real; proponer no cambia original. Comprueba --help y contrato del tipo de nota: el producto dispone de flujos específicos de revisión D/X y relaciones, no de merge ni integrador universal. No inventar comandos ni afirmar aplicación por generar propuesta. Reutiliza autorización de escritura dentro de su alcance sin confundirla con ratificación editorial.

1. Identifica qué fue solicitado, qué nota/bloque es autoridad, su versión y vigencia, qué otras piezas dependen de ella.
2. Recupera fuente de cambio y quién tiene facultad de aprobar. Propuesta de IA no equivale a decisión.
3. Guarda cambio candidato en archivo temporal local y ejecuta `python scripts/cerebro.py proponer --vault ... --id ID --motivo ... --archivo /ruta/candidato.md`; esto **no cambia el original** y conserva SHA-256 previo.
4. Compara contradicciones, excepciones, contratos particulares y fechas; presenta diff humano y efecto sobre derivados.
5. Comprueba aprobación explícita del decisor para el cambio editorial de autoridad o vigencia; si falta, solicita esa decisión concreta antes de aplicarlo. La autorización técnica persistida para integrar fuentes o guardar propuestas se reutiliza dentro de su alcance sin repetir permiso, pero no ratifica afirmaciones ni autoriza sobrescribir notas aprobadas. No hay motor automático de merge en esta versión, por lo que no declares vigente una modificación por haber guardado su propuesta.
6. En una aplicación autorizada mediante interfaz comprobada preservar histórico/versiones y volver a validar, no sobrescribir para tests verdes.
**Salida:** propuesta, fuentes, impactos, aprobación pendiente y límites de alcance.
