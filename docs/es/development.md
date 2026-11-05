# Guía de desarrollo

[English](../en/development.md) · [Documentación](README.md)

## Preparar e inspeccionar

Sigue la [preparación](onboarding.md) para Python 3.11+, entorno virtual y dependencias. Lee `AGENTS.md`, inspecciona Git status y preserva trabajo existente antes de editar. Es un CLI Python y producto de instrucciones para agentes: el flujo central no requiere servidor de desarrollo, base de datos ni API alojada.

| Ruta | Función |
| --- | --- |
| `scripts/` | CLI, validación, cambios controlados, aceptación, exportación |
| `tests/` | Pruebas automáticas y fixtures sintéticos |
| `contratos/`, `modelo/` | Contratos estructurales, esquemas y distinciones de entidades |
| `.agents/skills/` | Flujos del agente por intención |
| `plantilla_boveda/` | Plantilla de instancia nueva, no actualización de bóveda existente |
| `metodologia/` | Originales metodológicos preservados |
| `docs/en/`, `docs/es/` | Documentación equivalente de uso y desarrollo |

Ver [arquitectura](architecture.md), [modelo de datos](data-model.md) y [referencia CLI](cli-reference.md). Datos empresariales, permisos privados y bancos de transcripciones pertenecen fuera del producto público.

## Cambiar y verificar

Reproduce fallos de runtime con datos sintéticos, realiza el cambio pertinente mínimo y prueba el comportamiento afectado. Antes de cerrar cambios de runtime ejecuta:

```bash
python scripts/cerebro.py --help
python -m unittest discover -s tests -v
git diff --check
```

Usa el entorno activado de preparación. Para cambios sólo documentales comprueba enlaces, ejemplos, paridad de idiomas y comportamiento documentado sin atribuir aceptación de runtime. Conserva literalmente comandos, flags, claves de esquema, enums, IDs y nombres de archivos de bóveda en ambas lenguas. Consulta el [flujo documental](documentation-workflow.md) para el verificador y procedencia de plantillas.

Las pruebas automáticas no verifican GUI de Obsidian, recuperación semántica, aprobación editorial ni utilidad empresarial. Registra cada una por separado; ver [pruebas](testing.md).

## Exportar e integrar

El exportador requiere un checkout Git con commit y exporta archivos permitidos de **HEAD**, no cambios sin commit del árbol de trabajo:

```bash
python scripts/exportar_producto.py --dest /private/path/product.zip
```

Usa un destino externo al repositorio. Su manifiesto usa hashes de los archivos exportados. Las instancias privadas deben quedar excluidas. Una exportación es un artefacto local; no publica una versión.

Actualizar código de producto no autoriza copiarlo sobre una bóveda empresarial activa. Aceptar instalación, migración o integración requiere reporte dedicado de solo lectura y ensayo sintético aislado antes de cambios reales autorizados por separado. La continuidad cotidiana no exige esa campaña. Lee [operación](operations.md), [pruebas](testing.md) y [contribución](contributing.md).
