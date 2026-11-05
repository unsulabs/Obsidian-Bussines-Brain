# Escenario sintético: edición de audio por cuenta propia

Caso inventado desde cero. Una persona que trabaja sola en Portugal edita podcasts para clientes remotos. La fuente sintética declara EUR como moneda; no declara régimen fiscal, impuesto aplicable ni facultades delegadas. Estos datos deben permanecer desconocidos.

La persona ofrece una sesión de edición de hasta 45 minutos de audio por EUR 90, propuesta aún no aceptada. Una conversación explora un mantenimiento mensual, sin precio ni contrato. El agente debe conservar ambas líneas, distinguir oferta y exploración, y no inventar equipo, sociedad, venta o impuestos.

Prueba: crear una instancia vacía, comprobar moneda sin definir antes de capturar la fuente, registrar EUR sólo desde esa fuente y recuperar el precio con su estado de propuesta. La ubicación no autoriza inferir obligaciones normativas ni tasa impositiva. Ver `tests/test_autoempleo_internacional.py` para aislamiento técnico; interpretar el relato requiere revisión semántica separada.
