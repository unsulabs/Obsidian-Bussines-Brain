# Relaciones tipadas del Cerebro Empresarial

Las propiedades y enlaces wiki sirven para navegar, pero no prueban una relación. Esta implementación agrega relaciones declaradas **con identidad, asunto, fuentes y estado** bajo la carpeta privada 90_Sistema/Relaciones, sin copiar documentos externos ni publicar información en Git.

## Cómo funciona

- relacion-proponer exige IDs existentes en la bóveda, un predicado de vocabulario controlado, un ámbito específico, una justificación y al menos una ficha de fuente interna autorizada. El resultado SIEMPRE es propuesta.
- relaciones permite consultar origen/destino, predicado, alcance y estado, indicando que la autenticidad externa de la validación no es comprobada por el programa.
- relacion-confirmar exige la huella exacta de la propuesta, referencia y revisor humano y una confirmación literal. Guarda una segunda declaración independiente; no reescribe la propuesta ni las notas.
- validar comprueba referencias a notas y fuentes, IDs y predicados. grafo distingue aristas local_propuesta de local_ratificada_por_revisor, además de las capas de navegación y contratos existentes.

La ratificación exige criterio y autoridad de quien decide; un modelo o script puede registrar el acto, pero NO probar por sí solo que la persona haya autorizado el vínculo.

## Seguridad y límites

Las aristas se admiten únicamente entre notas internas. Las referencias no acreditan automáticamente contratos, ventas, cobros ni participación del negocio en una organización tercera. No se incorporan datos restringidos: Obsidian no implementa ACL granulares por sí solo. Los predicados deben ajustarse a la pregunta real de consulta y no formar conexiones genéricas sin explicación.

No existe motor RAG/embeddings validado en este incremento; el grafo es explícito y las consultas siguen siendo estructuradas. Para demostrar recuperación semántica habrá que ejecutar preguntas concretas sobre fuentes, ámbito, fechas y casos negativos con un agente real.

## Proyección en Obsidian desde el candidato 0.4

Las aristas estructuradas no aparecen por sí solas como flechas en la vista Graph de Obsidian. La operación `mapa-conocimiento` lee exclusivamente las notas y relaciones ya registradas y prepara dos proyecciones: Markdown con enlaces wiki y un Canvas nativo con nodos de archivo y flechas etiquetadas con predicado y estado.

La publicación es **opt-in**, mediante `publicar-mapa` y doble huella, confirmación literal y respaldo externo. Nunca escribe vínculos hacia dentro de las notas empresariales ni afirma que la arista haya sido validada porque es visible. Codex debe renovar el mapa al cambiar las notas si el dueño autoriza. Consultar la [especificación v0.4](ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md).

Las etiquetas en properties/tags son índices temáticos; Bases permite navegar propiedades, pero no es un motor de autoridad. La conexión semántica necesita predicado, fuente, alcance y revisión.
