# Compatibilidad macOS: aliases nativos de directorios temporales

## Incidencia resuelta en el código

Los archivos temporales de Python en macOS pueden escribirse bajo `/var/folders/...`
o `/tmp/...`, aunque sus rutas físicas son `/private/var/folders/...` y
`/private/tmp/...`. En macOS, las pruebas pueden fallar si el protector
admitía `/var` pero no reconocía el alias exacto `/tmp`.

El detector `scripts/documentos.py::_is_symlinked` ahora permite **sólo**
estos ancestros en macOS, después de verificar los tres elementos siguientes:

- `/var` con `readlink` igual a `private/var` o `/private/var`, y `resolve(strict=True)` igual a `/private/var`.
- `/tmp` con `readlink` igual a `private/tmp` o `/private/tmp`, y `resolve(strict=True)` igual a `/private/tmp`.
- En `sys.platform != 'darwin'`, ninguna excepción aplica.

**Todos los demás symlinks se rechazan**, incluidos los creados por el usuario
debajo de `/tmp` o `/var`, symlinks de archivos de entrada, otros aliases o
rutas externas no permitidas. Los controles de bóveda y repositorio siguen
operando después de resolver la ruta física.

## Pruebas obligatorias

La aceptación local en la Mac usa Python 3.11 y ejecuta la suite completa
con temporal predeterminado sin `TMPDIR`, `TMPDIR=/tmp` (reproducción del
equipo destino) y `TMPDIR=/private/tmp`. Los tests negativos de symlinks siguen en
la suite; registrar las tres salidas para el SHA exacto.

En la Mac autorizada se requiere adicionalmente:

```bash
env -u TMPDIR /opt/homebrew/bin/python3.11 -m unittest discover -s tests -q
TMPDIR=/tmp /opt/homebrew/bin/python3.11 -m unittest discover -s tests -q
```

No modificar D01 ni la bóveda para que las pruebas pasen. Si alguna falla,
mostrar la traza y detener la migración de Bases. No usar únicamente un
`TMPDIR` alternativo como prueba de solución.

## Estado de aceptación

Un PASS local valida la ruta y el código de esta Mac; **no sustituye**
la comprobación en la GUI de Obsidian ni una segunda instalación. Consultar
`guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md`.
