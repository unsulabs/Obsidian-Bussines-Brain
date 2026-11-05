# Captura progresiva: del descubrimiento a archivos verificables

## Problema observado

El descubrimiento puede pasar varias rondas describiendo una empresa sin escribir nada en Obsidian. Eso deja al propietario sin visibilidad del avance. El contrato vNext sigue exigiendo revisión antes de admitir afirmaciones como conocimiento vigente; no exige esperar hasta el final para registrar hallazgos como provisionales.

## Qué registra el producto

- Captura de trabajo con ID único `CAP-...` en propiedades y un nombre de archivo legible en `90_Sistema/Descubrimiento/`.
- Estado editorial borrador, estado de conocimiento pendiente, vigencia sin verificar y autoridad ninguna.
- Referencias a fuentes internas admisibles y ya registradas; la evidencia primaria continúa en su ubicación autorizada.
- Separación explícita entre hechos documentados, lo que dijo el propietario, interpretación del agente, atribución empresarial por confirmar, hipótesis y preguntas K1/K2/K3/K4.
- Temas de trabajo cruzados y relaciones candidatas, no categorías obligatorias ni vínculos sin sustento.

Una captura es un registro de trabajo, no una oferta, decisión aprobada, venta, cliente o documento D/X. No se vuelca contenido de bóvedas anteriores rechazadas ni material confidencial bajo la etiqueta interno.

## Flujo recomendado al agente

1. Comprobar la ruta de la empresa, ejecutar estado y validar en modo consulta.
2. Recuperar material original admisible y autorizado de más de un tipo de actividad cuando resulte pertinente. No quedarse exclusivamente en un producto o en un único caso porque fue el primer archivo encontrado.
3. Preparar una síntesis breve, diferenciando claramente fuente, observación, interpretación y pregunta pendiente. Mantener la síntesis en carpeta privada temporal fuera de la bóveda y de Git.
4. Si la fuente se puede registrar con permiso interno, utilizar el subcomando fuente para crear una referencia; no copiar el original ni inventar permisos. Si es sensible, detener su ingesta y solicitar revisión del alcance.
5. Con autorización de escritura limitada en la bóveda, ejecutar:

    /opt/homebrew/bin/python3.11 scripts/cerebro.py capturar --vault "/ruta/privada/Empresa" --titulo "Descubrimiento inicial" --archivo "/ruta/privada/temporal/sintesis.md"

   Agregar --fuente F-... sólo cuando el ID ya exista y la fuente sea admisible.
6. Comprobar archivo, ID y su estado mediante estado y validar. Informar qué fue creado, qué quedó pendiente y qué pregunta puntual ayuda a avanzar. Si no se escribió nada, decir sin_archivo_generado.
7. Después de la revisión editorial del propietario, aplicar la metodología vNext G1–G7 para decidir si esa información se incorpora a D01–D07, X01–X07, entidades independientes o queda como antecedente.

## La captura no sustituye desarrollo empresarial

Una lista de fuentes y una continuidad no son el contenido del cerebro. A partir de cada ronda debe emerger una **interpretación empresarial concreta** y una propuesta de trabajo, no un reporte de lo que todavía no se demuestra. Una nota CAP sirve como insumo provisional; la creación D/X requiere análisis sustantivo y revisión. La explicación principal debe privilegiar mecanismo, capacidad, decisiones y significado; CONTROL conserva detalles de procedencia y dudas. Ver `docs/SINTESIS_EMPRESARIAL_CONSTRUCTIVA.md`.

## Regla de atribución comercial

Un sistema o proyecto técnico de una organización tercera puede acreditar la existencia de una implementación o una secuencia de trabajo, pero no acredita por sí solo qué contrato, venta, cobro u obligación correspondió a una empresa que está documentándose. Si la participación empresarial no está comprobada, escribir expresamente: atribución a la empresa por confirmar.

No repetir la misma pregunta sin antes registrar lo que ya sabemos y la información que faltaría verificar.

## Límites y aceptación

- Requiere permiso del propietario antes de escribir la primera nota de captura.
- El comando no lee automáticamente conversaciones ni extrae hechos: el agente debe preparar un insumo fiel y minimizado.
- No se instalan plugins ni se modifica una nota empresarial aprobada.
- El archivo fuente de la captura debe estar fuera del repositorio y fuera de la bóveda; no incorporar secretos, datos restringidos ni expedientes completos.
- Prueba positiva: la nota provisional existe y validar no reporta errores.
- Prueba negativa: no aparecen ofertas/clientes/contratos aprobados, el ID de fuente desconocido se rechaza y se preservan capturas previas.
- Queda pendiente probar en Obsidian GUI la nueva experiencia conversacional con un dueño real. Las pruebas automatizadas sólo demuestran las operaciones estructurales.
