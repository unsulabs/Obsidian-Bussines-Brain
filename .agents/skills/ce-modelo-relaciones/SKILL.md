---
name: ce-modelo-relaciones
description: "Diferenciar tipos de entidades y construir relaciones verificables en Obsidian: ofertas, productos, servicios, clientes, reuniones, procesos, proyectos y fuentes."
---

# ce-modelo-relaciones

**0. Primero arquitectura:** activa `ce-arquitectura-conocimiento`. No crees una ficha por cada mención. Decide qué tiene identidad y ciclo propios, qué existe, qué queda en la fuente y qué es vínculo. Valida con `plan-conocimiento`; etiquetas para navegar, aristas con fuente/ámbito para modelar relaciones, sin confundir ambas.

1. Consulta `modelo/tipos_entidad.json`, el catálogo D/X y contrato de traspaso vNext-0.9. El registry es candidato: justificar separaciones por identidad, cambios, historia, permisos, reutilización y consulta.
2. Antes de crear, comprobar si la entidad ya existe por ID, sistema autoritativo, alias y contexto. Una mención NO obliga a nota.
3. Verificar distinciones: producto/oferta; consultoría/herramienta; proyecto/caso/sesión/reunión; cliente-cuenta/persona/organización; oferta/propuesta/acuerdo; investigación/resultado.
4. Si una unidad necesita archivo propio, `python scripts/cerebro.py ficha --vault ... --tipo ... --titulo ...`; queda borrador. Enlazar fuentes registradas.
5. Registrar relaciones tipadas con evidencia, direccionalidad y alcance; no usar `related` genérico como autoridad. Evitar duplicar precio, estado financiero o contrato en varias notas.
6. `validar` y `grafo` tras cambios; la vista Graph muestra navegación, no verdad. Prueba una pregunta real y una negativa.
**Salida:** entidades justificadas, relaciones expresas, fuentes y ausencia/presencia de casos ambiguos.
