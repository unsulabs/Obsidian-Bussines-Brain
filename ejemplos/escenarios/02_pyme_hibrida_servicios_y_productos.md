# Escenario SINTÉTICO B — empresa con servicio y productos

**Entrada:** «Fabricamos mesas y ofrecemos consultorías de interiores. En un proyecto usamos una herramienta de planos, pero no la vendemos».

**Resultado esperado:** distinguir producto `mesa`, servicio `asesoría`, oferta comercial (forma de contratar), herramienta usada, proyecto de cliente, propuesta, acuerdo y experiencia. Codex recupera cotización aceptada y contrato si existen; no transforma uso de software en licencia vendida.

**Prueba negativa:** «¿Vendimos nuestro programa de planos al cliente?» → solo uso interno registrado; responder que no hay evidencia de venta. «¿Cuánto se cobró?» → exigir factura/registro de caja, no confundir importe cotizado.

**Vistas que deberían servir:** Ofertas, Proyectos, Comercial, Fuentes.
