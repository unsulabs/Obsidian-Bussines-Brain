---
name: ce-arquitectura-conocimiento
description: "Obligatoria antes de redactar D/X o manejar narraciones multiasunto: diseñar notas autónomas, reutilizar existentes, etiquetas, fuentes y relaciones antes de escribir."
---

# ce-arquitectura-conocimiento

Transcripciones nuevas pasan primero por [ce-banco-transcripciones](../ce-banco-transcripciones/SKILL.md) y ce-analizar-transcripcion. Usa matriz de todos los núcleos/asuntos y conciliación global, no resumen como original. Una ficha lógica por TR-ID con versiones; notas dueñas por asunto justificado. Planes de hasta 30 asuntos/30 unidades y 90 000 bytes: dividir propuestas en lotes con manifiesto padre y IDs globales, sin truncar ni duplicar la fuente. Una arquitectura aceptada no ratifica aristas ni autoriza sobrescribir aprobados. No cargar toda la bóveda para una corrección puntual.

## Disparadores proactivos

Actívala SIN que el usuario lo solicite cuando:
- Una entrevista, relato o transcripción contiene dos o más asuntos de vida propia (estrategia, oferta, proceso, decisión, caso, investigación).
- Se pide crear/revisar D01–D07/X01–X07 y parte del conocimiento merece otras notas especializadas.
- Se produjo un ensayo genérico que mezcla precios, procesos, estrategia y casos en una sola sección.

Para una corrección pequeña o consulta literal de una nota concreta, no hace falta replanear toda la empresa.

## Secuencia obligatoria

1. Relee fuentes originales admisibles e índices reales de la bóveda; no uses notas editoriales rechazadas.
2. Extrae asuntos en lenguaje del experto, por qué importan y para qué pregunta empresarial sirven. Mantén las razones de sus decisiones.
3. Para cada asunto propone: **reutilizar**, **revisar**, **crear** o **no crear** (si sólo merece mantenerse en la fuente).
4. Justifica autonomía por autoridad, vigencia, responsable, cambios independientes, historia o consulta. Una mención no obliga a nota.
5. Un asunto tiene un dueño canónico; otros documentos lo pueden enlazar y explicar sus implicaciones sin duplicar sus datos cambiantes.
6. Elige etiquetas temáticas y vínculos tipados con fuente, ámbito y sentido; tags y wiki links no son autoridad.
7. Prepara JSON privado siguiendo `docs/ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md` y `ejemplos/planes_conocimiento/plan_empresa_sintetica.json`. Ejecuta `python3 scripts/cerebro.py plan-conocimiento --vault RUTA --archivo PLAN_EXTERNO` en solo lectura.
8. Deja el mapa de distribución legible y rastreable para el empresario. Si el encargo ya autoriza construir o corregir la bóveda y el reparto está sustentado en fuentes, continúa con la redacción; no conviertas cada mapa en una nueva solicitud de permiso. Pregunta sólo cuando dos ubicaciones cambien materialmente autoridad o uso y el criterio no esté en las fuentes.
9. Con la arquitectura revisada, desarrolla notas sustantivas y estados/fuentes. Para una entidad usa ficha --archivo RUTA --etiqueta TAG con Markdown completo sin placeholders; para D/X usa documento --etiqueta sólo cuando aún no existe, y previsualizar-dx para revisiones. Registra aristas sólo tras IDs y fuentes.
10. Prueba una tarea que dependa de las notas creadas y una contraprueba de vigencia/atribución, no sólo coincidencias de búsqueda. Revisa la salida con `ce-consulta` antes de considerar útil la distribución.
11. Para hacer visibles conexiones ya existentes, ejecutar mapa-conocimiento sin escribir. Presentar los enlaces Markdown y Canvas derivados y sus estados. Sólo después de autorización específica, SHA/confirmación y respaldo fuera de la bóveda, publicar-mapa. No editar las notas para lograr el grafo.

**Salida:** un mapa mínimo de asuntos y dueños, notas actuales/nuevas/no creadas, razones, etiquetas, vínculos y fuentes. Falla B18 si Codex no hizo esto de oficio en material multiasunto, aunque el D01 final esté bien escrito. La CLI no reemplaza criterio experto.
