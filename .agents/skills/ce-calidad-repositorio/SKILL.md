---
name: ce-calidad-repositorio
description: "Auditar, mejorar o evolucionar el código del repositorio maestro con pruebas, migraciones y preservación de funcionalidades ya existentes."
---

# ce-calidad-repositorio

1. Leer `guia/EVOLUCION_PARA_CODEX.md`, docs de arquitectura/hoja de ruta y estado Git; identificar versión base y cambios ajenos.
2. Ejecutar suite completa y crear instancia sintética, nunca usar datos privados para pruebas sin aprobación.
3. Elegir falla reproducible vinculada a un requisito o caso de aceptación; diseñar prueba positiva y negativa, y evaluar alternativas existentes.
4. Implementar cambio mínimo, actualizar validadores/esquemas/plantillas de manera coherente; no eliminar vNext ni cambiar su significado para facilitar parsing.
5. Si cambia una instancia, generar migración con dry-run, backup y rollback antes de aplicar. No marcar una versión como lista sin experiencia GUI en máquina destino ni pruebas semánticas de agente.
6. Actualiza changelog, decisiones, documentación y corre suite; deja evidencia con comandos, salida, pruebas pendientes.
**Salida:** diff verificable, resultados reales, riesgos y siguiente decisión humana.
