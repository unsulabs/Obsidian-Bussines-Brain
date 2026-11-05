# Obsidian-Bussines-Brain

Un segundo cerebro para negocios, emprendedores y trabajadores por cuenta propia: organiza fuentes, decisiones y conocimiento operativo en una bóveda privada de Obsidian, con instrucciones para trabajar con Codex.

Open source bajo [MIT](LICENSE). Producto en desarrollo: las pruebas técnicas no certifican exactitud empresarial, cumplimiento normativo ni compatibilidad visual en tu equipo.

## Qué permite hacer

- Conservar conversaciones y documentos autorizados con procedencia y permisos.
- Desarrollar conocimiento desde fuentes y criterio de la persona responsable, sin imponer organigramas o documentos vacíos.
- Recuperar antecedentes, mantener revisiones y conectar notas mediante Markdown, Bases y Canvas.
- Separar hechos, hipótesis, propuestas y decisiones aprobadas, con respaldos y detección de cambios concurrentes.

## Empezar

Necesitas Python 3.11 o posterior y las dependencias de `requirements.txt`. Para el flujo asistido necesitas Codex con acceso a archivos y comandos. Para ver la bóveda necesitas Obsidian Desktop; verifica la compatibilidad de Bases y CLI en tu instalación. Las credenciales y conectores opcionales se configuran aparte.

```bash
git clone https://github.com/unsulabs/Obsidian-Bussines-Brain.git
cd Obsidian-Bussines-Brain
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python -m unittest discover -s tests -v
python scripts/cerebro.py crear --id MI-NEGOCIO --nombre "Mi negocio" --dest /ruta/privada/MiNegocio
python scripts/cerebro.py validar --vault /ruta/privada/MiNegocio
```

En Windows activa el entorno con `.venv\Scripts\Activate.ps1`. Sustituye el destino por una ruta privada fuera de este repositorio. `crear` rechaza un destino existente.

Abre el repositorio en Codex y usa [EMPIEZA_AQUI.md](EMPIEZA_AQUI.md). Si ya tienes una instancia, usa [el prompt de continuidad](PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md): no vuelvas a crearla.

**Dependencia externa:** el flujo asistido sobre una bóveda existente requiere la skill `obsidian-router`, un registro local de destinos y su verificación contra Obsidian. No están incluidos ni se instalan al clonar. Si faltan, conserva el trabajo autorizado fuera de la bóveda y sigue la [alternativa segura](.agents/skills/ce-banco-transcripciones/references/flujo-predeterminado.md#preparación-de-instancia-y-dependencias). El CLI de producto puede trabajar con rutas explícitas, pero no sustituye ese contrato del agente.

## Contexto de cada negocio

No hay país, moneda, régimen fiscal ni estructura organizativa obligatorios. Antes de interpretar cifras u obligaciones, recupera país y jurisdicción, moneda, impuestos aplicables, fechas y fuentes autorizadas de la instancia. Lo desconocido permanece sin definir. Las referencias legales o contables internacionales no implican aplicabilidad universal; requieren comprobación local pertinente.

Los [ejemplos](ejemplos/README.md) son sintéticos. Sus monedas y supuestos pertenecen a cada escenario y no se copian como configuración inicial. [Caso de autoempleo](ejemplos/escenarios/04_autoempleo_internacional.md).

## Privacidad y contribuciones

El producto y el conocimiento privado se almacenan por separado. No incluyas fuentes reales, datos personales, secretos ni evidencias de clientes en commits, issues o pull requests. Obsidian no ofrece ACL por nota: la sensibilidad declarada no bloquea el acceso a los archivos. Lee [privacidad](docs/SEGURIDAD_Y_DATOS.md), [contribución](CONTRIBUTING.md) y [procedencia/licencias](docs/FUENTES_Y_LICENCIAS.md).

El exportador `python scripts/exportar_producto.py --dest /ruta/fuera/producto.zip` requiere un checkout Git con commit y exporta únicamente archivos permitidos de HEAD. No exporta cambios sin commit. El manifiesto se genera con hashes actuales; no incluye instancias privadas.

La aceptación GUI, recuperación semántica y utilidad de cada instancia se verifican por separado: [criterios](docs/CRITERIOS_DE_ACEPTACION.md).
