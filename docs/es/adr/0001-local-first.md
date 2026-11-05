# ADR 0001 — Separar conocimiento empresarial local y producto

[English](../../en/adr/0001-local-first.md) · [Arquitectura](../architecture.md)

## Estado

Registro del contrato e implementación actuales del repositorio, no aprobación nueva ni afirmación de aceptación de una instalación concreta. No se atribuye una fecha histórica de aprobación.

## Contexto

El producto público debe reutilizarse entre negocios sin arrastrar contenido de clientes ni permisos de instancias. Agente, checkout, bóveda Obsidian y banco de fuentes tienen responsabilidades y límites de acceso distintos.

## Decisión

Conservar en Git software reutilizable, metodología, instrucciones y ejemplos sintéticos. Guardar conocimiento de cada negocio en una bóveda privada separada del producto y mantener su banco de transcripciones fuera de ambos. Usar rutas explícitas en el CLI; el acceso asistido a una bóveda existente exige además `obsidian-router`, verificación del registro nativo de Obsidian e instrucciones locales. Nunca seleccionar por la ventana activa sola.

Actualizar producto no autoriza copiar plantillas sobre una bóveda existente. El trabajo ocurre durante una sesión del agente; el repositorio no crea servicio alojado ni monitor en segundo plano. Los conectores opcionales conservan requisitos propios de autorización y acceso.

## Alternativas y consecuencias

Guardar datos reales de instancias en el producto o interpretar un remoto Git privado como permiso mezclaría distribución y autoridad empresarial; el contrato actual excluye ambas opciones. Un servicio compartido alojado no es la arquitectura implementada.

El almacenamiento local permite archivos legibles y respaldos controlados, pero no aporta por sí solo cifrado, ACL por nota, restauración verificada ni corrección semántica. El usuario mantiene controles adecuados de almacenamiento; el agente verifica destinos y permisos. La falta de routing puede impedir acceso a bóveda sin bloquear trabajo autorizado e independiente fuera de ella.

## Evidencia

[Contrato del repositorio](../../../AGENTS.md), [preparación](../onboarding.md), [seguridad](../security.md), [entrada CLI](../../../scripts/cerebro.py) y [exportador](../../../scripts/exportar_producto.py). Fuente española preservada: [GitHub y privacidad](../../GITHUB_Y_PRIVACIDAD.md). Relacionado: [custodia de fuentes](0002-source-custody.md).
