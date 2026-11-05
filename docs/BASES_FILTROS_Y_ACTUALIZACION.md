# Vistas Bases: excluir plantillas y actualizar instancias existentes

## Causa y corrección

Las vistas del lanzamiento 0.2.0-alpha filtran por `tipo`, pero las plantillas
bajo `90_Sistema/Plantillas` tienen esos mismos valores. Bases busca en toda
la bóveda salvo que se delimite el conjunto. En una empresa sin ofertas, la
vista «Ofertas» mostraba cuatro archivos Ficha_* como falsos registros.

Las 16 vistas maestras y 16 de demostración agregan un filtro sobre
`file.ext` y una exclusión `file.inFolder("90_Sistema/Plantillas")`. La
condición por tipo original permanece igual. **No se eliminan las plantillas**.

Sintaxis oficial: https://obsidian.md/help/bases/syntax

## Instalación nueva

Después de integrar este cambio en GitHub y actualizar el checkout de Codex,
`scripts/crear_instancia.py` copiará las vistas corregidas. No hace falta
instalar un plugin comunitario.

## Una bóveda ya creada: proceso seguro con Codex

Nunca ejecutar de nuevo `crear` sobre una empresa existente ni copiar
toda la plantilla sobre sus notas.

1. Confirmar ruta, commit y respaldo. **Primero sólo lectura**:

   ```bash
   /opt/homebrew/bin/python3.11 scripts/actualizar_vistas_bases.py --vault "/ruta/privada/MiNegocio"
   ```

2. Interpretar `LISTO` como vista idéntica al lanzamiento; `LISTO_FILTRO`
   como vista con presentaciones personalizadas pero filtro **semánticamente igual**
   al original 0.2; `AL_DIA` o `AL_DIA_PERSONALIZADO` como filtro ya actualizado.
   `BLOQUEADO_PERSONALIZADO` o `BLOQUEADO_FALTANTE` implican detención
   obligatoria. Nunca forzar cambios en filtros comerciales modificados por la empresa.
   El diagnóstico incluye SHA-256 antes y propuesto para revisión.
3. **Cerrar primero Obsidian Desktop y detener sincronizadores que escriban .base**.
   Releer el plan AHORA, porque abrir Bases en la GUI puede haber reserializado
   las 16 vistas o `.obsidian/workspace.json`. No restaurar versiones
   anteriores sólo por diferencias de formato: se conservan las vistas actuales.

   El diagnóstico entrega `sha_plan`. **Guardar esa huella exacta**. Sólo
   después de autorización explícita del propietario para modificar los
   filtros raíz de estas vistas, con respaldo fuera de Git y de la bóveda:

   ```bash
   /opt/homebrew/bin/python3.11 scripts/actualizar_vistas_bases.py \
     --vault "/ruta/privada/MiNegocio" \
     --backup-dir "/ruta/privada/Respaldos_Vistas" \
     --sha-plan "SHA_PLAN_DEL_DIAGNOSTICO_ACTUAL" \
     --apply
   ```

4. El aplicador verifica que el plan no cambió y guarda una instantánea
   privada completa de las 16 Bases, incluida la disposición actual de
   `views:`, más `.obsidian/workspace.json` cuando existe. El respaldo
   permanece fuera de Git y de la bóveda. Conserva los cambios producidos
   por el autoguardado GUI antes de migrar. Si Obsidian modifica los archivos
   DURANTE la operación, se detecta un conflicto y se restauran las Bases
   modificadas a partir de la instantánea. **No restaurar workspace.json
   automáticamente**; ese archivo sólo se respalda para diagnóstico.

5. Reabrir Obsidian, comprobar desde la GUI y la CLI que «Ofertas» ya no
   enumera las cuatro plantillas. Si todavía no hay ofertas, debe verse vacía.
   Probar fichas de ejemplo sólo en una bóveda TEMPORAL.
6. Registrar commit, respaldo, SHA y resultado real. Pasar YAML/test unitario
   **no** certifica que el filtro opere en la versión de Obsidian instalada.

El actualizador sólo cambia `90_Sistema/Vistas/*.base` si los hashes
corresponden al baseline original 0.2, **o si el filtro actual equivale al baseline
aunque el archivo tenga personalizaciones de presentación**. En este segundo caso,
reemplaza únicamente el bloque `filters` y conserva byte por byte el contenido
a partir de `views:`, incluido `groupBy`, columnas, órdenes, tabs y comentarios.
Valida que la estructura no relacionada con filtros conserve su significado.
No admite una personalización del filtro mismo, ni claves raíz intercaladas que
puedan alterarse accidentalmente.

Después de migrar, un archivo personalizado se reconoce como
`AL_DIA_PERSONALIZADO` por su filtro, aunque su SHA no sea igual a la plantilla
maestra. Antes de cualquier escritura respalda; si falla, intenta restaurar.
Este diagnóstico habilita una propuesta de migración segura, **no sustituye
la autorización del propietario ni la comprobación en Obsidian GUI**.

## Límites

No importa documentación antigua, no genera afirmaciones, no toca notas,
fuentes, contratos, permisos, Sync ni plugins. Es una actualización de vistas,
no una aprobación de contenido empresarial.


## Autoguardado real de Obsidian: reglas de aceptación

En un piloto real, la GUI reserializó 14 vistas antiguas sólo por abrirlas;
otras dos conservaron personalizaciones. No es seguro afirmar que abrir la GUI
es una operación byte-idéntica. El flujo correcto es **respaldar después de
esa observación, cerrar Obsidian y migrar el estado vigente, no revertir
automáticamente a la plantilla antigua**.

Una vista normalizada puede figurar `LISTO_FILTRO`, incluso si antes era
`LISTO`. Es correcto: el migrador sustituye sólo la sección raíz `filters`
y conserva byte por byte `views:` a partir del estado actual. La huella
`sha_plan` debe coincidir al aplicar. El resultado esperado es
`AL_DIA` o `AL_DIA_PERSONALIZADO`, `por_actualizar: 0`,
`bloqueadas: 0`, y comprobación GUI/CLI de que Documentos ya no muestra
plantillas y Ofertas no lista plantillas como ofertas reales.

Si la GUI vuelve a escribir YAML después de reabrir, comparar estructura
`filters` y `views` y sus resultados, no exigir igualdad de bytes del
archivo `workspace.json`. Probar que D01, fuentes, contenidos y revisiones
canónicos siguen con sus hashes originales.
