# Revisiones de documentos D/X: previsualización, resguardo y restauración

**Estado:** funcionalidad experimental. Requiere autorización para modificar cualquier instancia y **no implementa aprobación empresarial**.

## Diferenciar funciones

- **previsualizar-dx:** compara un borrador privado externo con un documento D/X existente y devuelve SHA actual, SHA candidato, bloques y diff limitado. Sólo lectura.
- **preparar-dx:** almacena una propuesta `PRDX-...` y una copia candidata **sin modificar D01**. No crea duplicados D/X: los archivos de trabajo son JSON y `.snapshot` bajo `90_Sistema/Propuestas_DX`.
- **Fuente correctiva nueva:** pasar `--fuente F-...` al previsualizar y preparar (repetible). La fuente debe existir en la bóveda. El plan muestra el conjunto de fuentes resultante y su `sha_fuentes`; al aplicar, confirmar esa huella con `--sha-fuentes`. Sin ese parámetro, las fuentes existentes permanecen iguales. Una referencia sólo en el cuerpo no actualiza la propiedad `fuentes`.
- **aplicar-dx:** después de autorización explícita y específica del propietario, exige las dos huellas, referencia de esa autorización, responsable y ruta de respaldo externa. Verifica que el documento no haya cambiado. Guarda snapshot interno y externo, aplica mediante sustitución atómica y valida; si falla, intenta restaurar los bytes originales.
- **restaurar-dx:** con nueva autorización y SHA actual, usa un snapshot previo para producir una **nueva revisión**. No rebobina silenciosamente el contador ni borra versiones.

## Ejemplo únicamente ficticio

```bash
python3 scripts/cerebro.py previsualizar-dx \
 --vault /privado/EmpresaFicticia --doc-id D01 --archivo /privado/borrador_propuesto.md

python3 scripts/cerebro.py preparar-dx \
 --vault /privado/EmpresaFicticia --doc-id D01 --archivo /privado/borrador_propuesto.md \
 --fuente F-CORRECCION-002

# SOLO después de mostrar diff, verificar fuentes, revisión humana y autorización.
python3 scripts/cerebro.py aplicar-dx \
 --vault /privado/EmpresaFicticia \
 --propuesta PRDX-<ID> \
 --sha-original <SHA256_PREVIO> --sha-candidato <SHA256_CANDIDATO> \
 --sha-fuentes <SHA256_FUENTES_RESULTANTES> \
 --responsable "Operador autorizado" \
 --referencia-autorizacion "Decisión del propietario sobre PRDX-ID" \
 --respaldo /privado/RespaldoExterno

# Restauración requiere huella actual y autorización nueva:
python3 scripts/cerebro.py restaurar-dx \
 --vault /privado/EmpresaFicticia --doc-id D01 --historial REVDX-<ID> \
 --sha-actual <SHA256_ACTUAL> \
 --responsable "Operador autorizado" --referencia-autorizacion "Decisión de restauración" \
 --respaldo /privado/RespaldoExterno
```

Los respaldos externos deben estar fuera del repositorio maestro y de la bóveda. **Nunca asumir autorización a partir del nombre ingresado en CLI**: esos campos registran una declaración, no prueban la identidad de quien la dio.

## Límites de seguridad

1. No aplica si el archivo actual tiene estado `aprobado` o `retirado`; su modificación requerirá gobernanza específica.
2. El documento original debe tener `doc_id` válido, `revision` en formato `N.N` y estar bajo `10_Conocimiento`. Se rechazan duplicados, links rotos y bloques con IDs repetidos.
3. Una revisión ordinaria no elimina ni renombra IDs de bloque existentes sin migración. Una restauración explícita puede volver a una versión anterior; `validar` detecta enlaces/manifiestos que se rompan.
4. Las fuentes registradas y el estado empresarial no se promocionan automáticamente; el contenido sigue `en_revision` y `revisado_por: por_validar`.
5. Se crea un lock exclusivo para operaciones del propio CLI; **no impide ediciones directas concurrentes desde Obsidian**. El control de hash minimiza riesgos, pero no sustituye coordinación con el operador.
6. Los snapshots internos están bajo `90_Sistema/Historial_DX`, los respaldos externos en la ruta indicada. No son notas Markdown ni se contabilizan como conocimiento empresarial.
7. G1–G7, revisión especializada y aprobación por afirmación aún requieren otro incremento. Una ejecución exitosa de Python no valida la calidad o el alcance de una decisión.

## Aceptación exigida para producción

Probar contra una copia aislada de una bóveda con D01 existente, comprobar la integración de los módulos actuales y revisar el caso real en Obsidian GUI/CLI **antes de autorizar cambios en una instancia empresarial activa**. Añadir pruebas de cambios concurrentes, corrupción de propuesta, error posterior a escritura, restauración y no sobrescritura de archivos aprobados.
