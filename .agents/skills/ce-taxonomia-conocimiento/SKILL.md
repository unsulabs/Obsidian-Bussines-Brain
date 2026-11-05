---
name: ce-taxonomia-conocimiento
description: "asunto no cubierto, alias dudoso, categoría/fusión/división o cambio de criterio solicitado."
---

# ce-taxonomia-conocimiento

Lee el [contrato común](../ce-banco-transcripciones/references/contrato-comun.md) para estados, permisos, contexto y disponibilidad.

- **Trigger:** asunto no cubierto, alias dudoso, categoría/fusión/división o cambio de criterio solicitado.
- **Inputs:** categorías actuales, pasajes justificativos, ámbito/identidad de entidades, equivalencias históricas y versión objetivo.
- **Outputs:** propuesta multieje con IDs estables, definición/inclusión/exclusión/ejemplos, alias candidatos, diff versionado y cola de reclasificación. Una sola conversación puede justificar categoría útil.
- **Errores:** `ENTITY_COLLISION`, `AMBIGUOUS_ALIAS`, `TAXONOMY_CYCLE`, `BASE_VERSION_STALE`; una homonimia no se corrige por fusión automática.
- **Gate:** fixtures de homónimos y marca/empresa/proyecto siguen separados; fusiones preservan procedencia; cada entrada afectada obtiene job y los casos no acotables abren barrido completo del snapshot del catálogo.

## Ejecución

Clasifica por ejes independientes (asunto, función, entidad, tiempo/estado y uso), sustentados en pasajes originales. El agente decide significado; coincidencia de palabras no decide identidad, materialidad ni categoría. Una idea futura mantiene su estado; clasificar no la hace vigente. Nunca fusionar empresa, marca, proyecto y cliente por nombre o proximidad. Registrar alias ambiguo sin resolverlo arbitrariamente.

Versiona diff y equivalencias fusiona/divide/renombra, con ámbito y evidencia. No borrar IDs históricos. Antes de consolidar comprobar versión base y decisión correspondiente. Cambio crea evento y trabajo para cada entrada afectada; cuando no se pueda acotar con evidencia, abrir barrido completo del snapshot mediante [antecedentes](../ce-revisar-antecedentes/SKILL.md). No aplicar sustituciones masivas en notas.
