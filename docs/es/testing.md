# Pruebas y aceptación

[English](../en/testing.md) · [Documentación](README.md)

Usa el entorno Python 3.11+ verificado de [preparación](onboarding.md). Ejecuta desde la raíz del repositorio. Usa fixtures sintéticos y rutas temporales aisladas; nunca repares una bóveda real para aparentar que una prueba de producto pasa.

## Comprobaciones automáticas

El workflow `Platform installation` de GitHub Actions usa runners estándar de
Ubuntu 24.04, Windows Server 2022 y macOS 15 con Python 3.11. Cada checkout nuevo
crea y activa `.venv` con los mismos comandos por plataforma de ambos README y
después instala `requirements.txt`. No requiere forzar UTF-8 mediante variables
de entorno: el texto del producto usa UTF-8 y LF explícitos; los bytes originales
de las transcripciones permanecen intactos.

`scripts/verify_platform.py tests --output /fuera/del/checkout/evidencia` ejecuta
toda la suite unittest y registra commit, pruebas, fallos, errores y cada omisión.
Sólo la prueba nativa de alias macOS puede omitirse fuera de macOS, y las diez
pruebas nativas identificadas del filesystem Windows fuera de Windows. Sus jobs
nativos deben ejecutarlas. Cualquier otra omisión o fallo esperado rechaza la
aceptación. La fase `installation` verifica ayuda, doctor, documentación,
auditoría, creación/validación/estado sintéticos con Unicode y espacios, hashes y
exclusiones privadas del exportado. Los artefactos contienen sólo informes y logs
sintéticos. Estas pruebas sin interfaz gráfica no acreditan GUI/Bases ni aceptación empresarial.

El backend del banco en Windows requiere una ruta local NTFS/ReFS; rechaza rutas
UNC/dispositivo, streams alternativos y reparse points. Las carpetas privadas
exigen una DACL protegida limitada al propietario, SYSTEM y administradores;
rechaza ACL amplias existentes sin cambiarlas silenciosamente. POSIX conserva
sus controles de descriptores de directorio, permisos y flock. Windows usa
handles nativos, locks liberados al morir el proceso, flush de archivo y rename
write-through; no afirma equivalencia con fsync de directorios POSIX.

```bash
python scripts/cerebro.py doctor
python -m unittest discover -s tests -v
python scripts/check_docs.py
git diff --check
```

`doctor` es de solo lectura y comunica lo que observa; no instala componentes ni demuestra funcionamiento GUI/Bases. La suite prueba comportamiento estructural y controles con sus fixtures. Inspecciona fallos y omisiones; el código de salida por sí solo no acredita todos los gates.

Para cambios al verificador documental, la suite dirigida es:

```bash
python -m unittest discover -s tests -p 'test_check_docs.py' -v
```

Elige otras pruebas dirigidas según el comportamiento cambiado y ejecuta suite completa para cerrar cambios de runtime. Los cambios sólo documentales necesitan comprobaciones acotadas y revisión factual; no exigen por sí mismos leer una instancia privada. Contrasta comandos documentados con `--help` real y código. El verificador documental comprueba pares, enlaces locales y anchors admitidos, no equivalencia semántica ni diagramas renderizados.

## Regresiones de instalación (2026-11-05)

La revisión desde clon limpio encontró tres bloqueos: el inicio asistido exigía un router externo no disponible; validar una bóveda inexistente devolvía cero notas sin errores; y la auditoría del paquete rechazaba el `.venv` local ignorado que recomienda la documentación. Ahora el producto incluye un router que verifica el registro nativo, rechaza destinos inexistentes o que no son directorios y excluye de la auditoría local sólo el `.venv` raíz ignorado y completamente fuera del índice Git. Un paquete o entorno versionado sigue siendo rechazado; las exportaciones excluyen `.venv` a cualquier profundidad. La recomendación de doctor coincide con Python 3.11+.

Las pruebas dirigidas pasaron en macOS 26.5.1 arm64 con Python 3.11.15, usando registros sintéticos y bóvedas temporales:

```bash
python -m unittest discover -s tests -p 'test_*boveda_codex.py' -v
python -m unittest discover -s tests -p 'test_entrega.py' -v
python -m unittest discover -s tests -p 'test_exportar_producto.py' -v
python scripts/check_docs.py
git diff --check
```

Cubren selección explícita correcta, registro ambiguo/ausente/malformado, discrepancia de identidad nativa, escape de rutas/enlaces simbólicos, resolución de solo lectura, salida fallida del CLI ante bóveda inválida y límites de auditoría/exportación de entornos.

La revisión independiente desde clon limpio del candidato `4444224` ejecutó **460 pruebas: 458 pasaron y 2 fallaron** en 550.845 segundos. Ambos fallos correspondían a enlaces documentales de skills: una ruta relativa incorrecta y un enlace fuera del contrato de distribución aislada de skills. Se corrigieron sin cambiar código de runtime ni tests; después una repetición independiente pasó las 29 pruebas dirigidas: enlaces de routing (7), resolver (9), registro (8) y entrega (5). Tras la corrección también pasaron documentación y espacios. Esto es una ejecución completa seguida de verificación dirigida de las dos reparaciones, no una afirmación de que otra ejecución ininterrumpida de 460 pruebas pasó.

Otro ensayo con clon/venv nuevos pasó creación, validación, estado y casos negativos. En la misma máquina macOS, Obsidian 1.15.0 ya instalado abrió la bóveda sintética, mostró `Inicio` y la Base `Ofertas`, y asignó el ID nativo comprobado por los comandos incluidos de registro/resolución con un registro Codex aislado. Los 72 archivos originales de la bóveda quedaron intactos; Obsidian creó 4 archivos normales de `.obsidian`. El ZIP candidato contenía 472 archivos, con todos los tamaños/huellas del manifiesto coincidentes y sin contenido privado ni `.venv`.

Límites: no se probó instalar Obsidian desde cero, todas las vistas Bases, instalación Windows/Linux, utilidad empresarial semántica ni aceptación del dueño. Las pruebas de rutas Linux/Windows usan simulaciones. La observación GUI cubre una Base y un negocio sintético; no acredita los gates restantes.

## Qué requiere evidencia separada

| Gate | Evidencia requerida |
| --- | --- |
| Integridad estructural | Salida real de validación/pruebas con intérprete, estado de checkout y rutas pertinentes |
| Integración Obsidian | Navegación GUI, Bases, enlaces y CLI disponible observados |
| Arquitectura del conocimiento | El agente identifica asuntos y dueños canónicos antes de redactar varios asuntos; una nota indivisible justificada sigue siendo válida |
| Recuperación semántica | Sesión nueva lee originales autorizados y responde preguntas representativas con ámbito, fecha y autoridad |
| Fidelidad editorial | El dueño reconoce mecanismos, decisiones, excepciones y voz; contraste fuente→nota y nota→fuente |
| Privacidad | Alcance autorizado, casos negativos de datos restringidos y artefactos públicos inspeccionados |
| Recuperación | Ensayo aislado de rechazo de cambio concurrente, respaldo, aplicación y restauración |
| Portabilidad | Evidencia de instalación/sesión independiente cuando lo exige el alcance de aceptación |

Incluye casos negativos: fuente vigente ausente, tarifa general que no debe reemplazar un acuerdo, material editorial rechazado que permanece excluido y plan que no se convierte en venta. Conserva incertidumbre si la evidencia no responde. Para evaluar explicación integral del negocio, usa un prompt abierto en lugar de proporcionar la tesis deseada; conserva prompt y respuesta crudos. Un ensayo dirigido puede provocar el fallo que intenta medir.

## Aceptar una instalación o cambio de integración

Esta campaña es distinta de la consulta cotidiana. Resuelve y autoriza la bóveda existente antes del acceso. Registra rama, commit exacto y estado del árbol; preserva cambios y usa un candidato aislado apropiado en lugar de descartarlos. Desde el checkout verificado, consulta los argumentos del programa dedicado:

```bash
python scripts/aceptacion_integracion_local.py --help
```

El procedimiento usa `--vault`, `--salida` y `--commit-esperado`. La salida debe ser una ruta absoluta privada nueva fuera de Git y bóveda. El programa inspecciona sin modificar la bóveda y produce reporte saneado; no instala ni migra. Su ejecución predeterminada incluye pruebas. No declares aprobada una suite omitida.

Después comprueba GUI de Obsidian y las 16 Bases, ensaya cambios en un negocio enteramente ficticio aislado y obtiene revisión humana pertinente. Migrar la bóveda, publicar mapas y cambiar contenido editorial conservan autorización separada. Informa PASS, FAIL o NO_VERIFICADO observado por gate; pasar Python no acredita producción ni aceptación empresarial.

Referencias españolas detalladas: [criterios de aceptación](../CRITERIOS_DE_ACEPTACION.md), [procedimiento de integración](../../guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md), [cierre del piloto](../CIERRE_DEL_PILOTO_0_3.md) y [estado registrado del producto](../ESTADO_REAL.md). Sus resultados históricos no son evidencia fresca del checkout actual ni de otra instancia.
