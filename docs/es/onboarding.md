# Preparación

[English](../en/onboarding.md) · [Documentación](README.md)

## Requisitos y almacenamiento

Usa Python 3.11 o posterior, Git para un checkout y los paquetes de `requirements.txt`. El trabajo asistido necesita Codex con acceso comprobado a archivos y comandos. Para ver la bóveda necesitas Obsidian Desktop; comprueba Bases y CLI localmente. Los conectores opcionales requieren credenciales y autorización propias.

Separa tres ubicaciones: este repositorio público del producto, una bóveda empresarial privada y un banco privado de transcripciones fuera de ambos. Nunca inicialices un negocio usando archivos de otro cliente. No se preconfigura país, moneda, régimen fiscal, estructura jurídica ni personal.

## Preparar el producto

Ejecuta desde un checkout local. Instalar paquetes puede acceder a la red; el agente debe tener la autorización correspondiente.

```bash
git clone https://github.com/unsulabs/Obsidian-Bussines-Brain.git
cd Obsidian-Bussines-Brain
python3.11 --version
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python scripts/cerebro.py --help
```

También se admite un intérprete Python 3 posterior; comprueba su versión antes de crear el entorno. En Windows usa `py -3.11 -m venv .venv` y activa con `.venv\Scripts\Activate.ps1` en PowerShell en lugar de `source`. Tras activar, los comandos `python` son iguales.

`doctor` es de solo lectura; no instala componentes faltantes. Si fallan imports, comprueba el intérprete y los entornos existentes antes de concluir que el producto no funciona. Este diagnóstico no verifica GUI ni utilidad empresarial.

## Instancia empresarial nueva

Sólo si no existe instancia y está autorizada la creación, elige una ruta privada nueva fuera de Git. Sustituye la ruta de ejemplo por una ruta absoluta propia; `crear` rechaza un destino existente.

```bash
python scripts/cerebro.py crear --id MY-BUSINESS --nombre "My business" --dest /private/path/MyBusiness
python scripts/cerebro.py validar --vault /private/path/MyBusiness
python scripts/cerebro.py estado --vault /private/path/MyBusiness
```

En Windows usa un destino local absoluto como `C:\Private\MyBusiness`. Abre la bóveda creada en Obsidian Desktop y compruébala allí. Completa el registro siguiente antes de que el agente acceda a ella como bóveda existente.

## Registrar y resolver la bóveda

La [skill de routing incluida](../../.agents/skills/obsidian-router/SKILL.md) funciona desde este checkout sin instalación global. Tras abrir la carpeta elegida como bóveda en Obsidian, sustituye ruta, nombre e ID de ejemplo por los tuyos:

```bash
python scripts/registrar_boveda_codex.py --vault /private/path/MyBusiness --nombre "My business" --alias MY-BUSINESS
python scripts/resolver_boveda_codex.py --selector /private/path/MyBusiness
```

El registro verifica el ID nativo de Obsidian y escribe sólo `~/.codex/obsidian/vaults.json`, respaldando el registro existente. Nunca escribe la bóveda ni el registro de Obsidian. La resolución es de solo lectura: exige salida 0, `status: selected` y `native_registry_verified: true`; después lee `instructions` antes de `entrypoint`. El registro ausente o conflictivo bloquea el acceso; no fabriques IDs ni edites JSON para evadirlo. Para una bóveda ya registrada, comienza con la resolución. Registrar una bóveda existente requiere el destino previsto por su dueño y autorización.

Rutas nativas predeterminadas: macOS `~/Library/Application Support/obsidian/obsidian.json`, Linux `$XDG_CONFIG_HOME/obsidian/obsidian.json` (o `~/.config/obsidian/obsidian.json`) y Windows `%APPDATA%/obsidian/obsidian.json`. Para instalaciones no estándar, verifica la ubicación nativa real y usa `--nativo "RUTA"` en ambos comandos. Usa `--registro "RUTA"` sólo para un registro local alternativo elegido explícitamente. Estas rutas son valores predeterminados, no pruebas de que Obsidian esté instalado o funcionando.

Opcionalmente añade `--proyecto "/ruta/absoluta/ProyectoCodex"` al registro y resuelve con `python scripts/resolver_boveda_codex.py --project "/ruta/absoluta/ProyectoCodex"`. El proyecto explícito o una subruta debe coincidir con una sola asociación registrada; no se selecciona implícitamente por carpeta actual ni ventana activa.

Usa el [prompt de inicio](../../PROMPT_INICIO_CODEX.md) para continuar por descubrimiento, revisión de fuentes, arquitectura del conocimiento, redacción útil, revisión y una tarea real. Una plantilla o captura provisional no termina ese trabajo.

## Instancia empresarial existente

No ejecutes `crear`, copies plantillas encima ni reinicies la entrevista inicial. Usa el [prompt de continuidad](../../PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md). Antes de listar o leer dentro de la bóveda, resuélvela con `obsidian-router`, verifica su registro nativo en Obsidian y lee sus instrucciones locales. La ventana activa o una ruta escrita no bastan.

Si falta routing, conserva el trabajo autorizado fuera de la bóveda y deja pendiente su acceso/integración. No inventes un registro ni afirmes que comprobaste el entorno. El uso cotidiano no requiere una campaña completa de aceptación de instalación.

## Verificar el resultado pertinente

Para desarrollar producto ejecuta las pruebas de [desarrollo](development.md). Para aceptar una instalación o integración usa [pruebas](testing.md) y el procedimiento dedicado de aceptación. Verifica por separado integridad estructural, GUI de Obsidian, recuperación semántica y utilidad empresarial. Una prueba sintética no aprueba decisiones de un negocio real.

Siguiente: [Guía de uso](user-guide.md).
