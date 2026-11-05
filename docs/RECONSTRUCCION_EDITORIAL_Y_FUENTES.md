# Reconstrucción editorial y admisibilidad de fuentes — primer uso y evolución

**Propósito:** impedir que el Cerebro Empresarial perpetúe documentación genérica, incorrecta o escrita por IA y expresamente rechazada por la persona que dirige la empresa. Este protocolo se aplica a cualquier PyME o emprendimiento; no contiene datos privados de ninguna empresa.

## 1. Prioridad de la voluntad del propietario

Si el usuario afirma que una bóveda o conjunto documental anterior **no representa su negocio**, el sistema debe respetar esa exclusión. **No** reutilizar textos, estructuras editoriales, taxonomías empresariales específicas, resúmenes, embeddings, fragmentos extraídos o notas históricas como base silenciosa para nuevos documentos. Tampoco «corregir el tono» conservando las afirmaciones y el encuadre heredados. La instrucción «no reinicies desde cero» de `AGENTS.md` protege el **producto y la metodología**, no impone reutilizar conocimiento empresarial descartado.

Los respaldos y custodias pueden conservarse en su estado original sin abrirse ni restaurarse. Un inventario técnico de rutas, fechas o hashes, cuando esté autorizado, **no** autoriza leer sus contenidos.

## 2. Clasificación por procedencia y admisibilidad

- `legado_rechazado`: notas, páginas, informes o síntesis anteriores que el propietario descartó; **no se leen para desarrollar nuevos contenidos, ni se importan**.
- `admisible_autorizado`: fuente original, documento vigente verificado, testimonio directo del propietario o recurso autorizado para este trabajo. Su alcance y autoridad deben documentarse.
- `pendiente_autorizacion`: fuente encontrada o mencionada sin permiso de lectura o reutilización; no acceder hasta obtener consentimiento.
- `referencia_tecnica_no_empresarial`: plugin, plantilla, configuración o documentación de una bóveda previa que puede informar una evaluación **técnica**, pero no determina cómo opera esa empresa ni se instala automáticamente.

Una fuente primaria **no se vuelve admisible automáticamente** por estar dentro de un respaldo rechazado. Pedir autorización concreta y preferir su ubicación original. Mantener diferencias entre fuente primaria, inferencia y declaración de un tercero.

## 3. Ruta de reconstrucción sin importar legado

1. **Comprobar instalación** y versionado del repositorio maestro por separado. No instalar sistemas antiguos para recuperar archivos.
2. **Diagnosticar posibles bóvedas existentes en lectura mínima** (existencia/ruta; metadatos técnicos si se autorizó); distinguir bóveda activa de respaldo o candidato.
3. **Presentar una ruta nueva**, vacía, privada y fuera de Git; no crearlo hasta obtener autorización. Preservar intactas custodias y originales.
4. **Preguntar qué problema empresarial quiere resolver** y cuáles son las fuentes nuevas/originales admisibles. Si ya existe rechazo editorial, no insistir en rescatar el legado.
5. **Construir criterio experto K1** desde episodios reales: qué ocurrió, opciones, por qué se eligió, señales, excepciones y límites. Localizar K2 en sus sistemas de registro; K3 permanece desconocido; K4 no bloquea.
6. **Usar la metodología vNext-1.0R** para escoger un D/X o bloque útil, sin crear archivos de relleno. Formular hipótesis como hipótesis; no convertir herramientas utilizadas en productos vendidos.
7. **Revisar primero contenido y voz con el dueño**. Evitar misión/visión/valores, prosa inflada, slogans, beneficios inventados y generalizaciones del sector salvo que tengan respaldo y valor real para el negocio. No imponer frases textuales del dueño si desea editarlas: preservar significado y comprobarlo.
8. **Incorporar a Obsidian tras revisión**, con fuente, estado editorial, identidad, relaciones tipadas, vigencia y permisos apropiados. Verificar consulta y reanudación en una sesión nueva; la validez estructural no equivale a aprobación editorial.

## 4. Prueba de calidad editorial

Antes de declarar una pieza aprobada, exigir una revisión que permita responder:

- ¿Qué decisiones reales, criterios de trabajo, mecanismos y límites explica que sean particulares de esta empresa?
- ¿Qué hechos están respaldados por fuentes autorizadas? ¿Qué todavía es propuesta o hipótesis?
- ¿El dueño reconoce su negocio en el documento sin que el agente tenga que justificar frases vacías o prestadas?
- ¿Podemos contestar una pregunta empresarial real usando ese texto, y detectar una pregunta que el documento **no** permite contestar?
- ¿Hay coincidencias semánticas sospechosas con el legado excluido por usos anteriores del sistema? No inspeccionar el legado para generar esa comparación sin autorización; usar trazabilidad de nuevas fuentes y revisión humana.

Si faltan estos elementos, mantener `borrador` o `descubrimiento_en_curso`. No pasar G2/G6/G7 sólo por coherencia narrativa.

## 5. Pruebas para el producto

- **Caso negativo:** el usuario rechaza todas las notas antiguas; Codex **no las indexa ni importa** y pide la fuente primaria nueva adecuada.
- **Caso positivo:** el usuario autoriza un contrato original específico; Codex registra su procedencia y aprovecha sólo lo que ese contrato acredita.
- **Prueba de aislamiento:** el repositorio maestro no recibe contenido privado; la bóveda nueva vive en ruta privada y custodias permanecen intactas.
- **Prueba editorial:** una ficha que suena «profesional» pero no incluye criterio ni casos particulares falla G2/G6, y un documento con datos sin autoridad falla G5.

Este protocolo trata la **admisibilidad editorial**, no sustituye contratos de seguridad, controles de acceso, licencias ni normativa de datos personales.
