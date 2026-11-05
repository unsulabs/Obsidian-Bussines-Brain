# Evaluación humana D/X con G1–G7

Este incremento registra declaraciones de revisión humana y puede promover el estado editorial sólo bajo condiciones expresas. NO verifica identidad real, no firma actas ni certifica verdad empresarial.

## Registrar evaluación

Codex prepara un acta JSON privada fuera de Git y de la bóveda. Debe contener doc_id, sha_documento, revisor, referencia_decision, alcance_bloques y el mapa completo de G1–G7 con estado y fundamento específico. Decisiones admitidas: requiere_cambios, recomendar_parcial y recomendar_integral.

Ejecutar: python3 scripts/cerebro.py evaluar-dx --vault /ruta/privada --doc-id D01 --acta /ruta/privada/acta.json --sha-actual SHA256.

El comando crea un registro EVALDX en 90_Sistema/Evaluaciones_DX; NO altera D01. Las recomendaciones NO equivalen a aprobación. G2 y G6 no pueden ser no_aplica al recomendar una aprobación. Una recomendación integral exige todos los bloques y cobertura suficiente_para_tarea.

## Promoción editorial integral

ÚNICAMENTE tras autorización humana específica para el SHA y alcance concretos: python3 scripts/cerebro.py aprobar-dx --vault /ruta/privada --evaluacion EVALDX-ID --sha-actual SHA256 --responsable OPERADOR --referencia-autorizacion REFERENCIA --respaldo /ruta/privada/backups --confirmacion "APROBAR D01 <12 primeros caracteres de SHA>".

Se conservan originales en snapshot interno y externo y se incrementa la revisión. El cuerpo no cambia. Editorial aprobado no implica vigencia comercial, contractual, fiscal ni financiera. Codex debe comprobar que hubo consentimiento auténtico, autoridad de la persona revisora y conocimiento suficiente; la CLI sólo registra sus declaraciones.

D01 con cobertura parcial **no puede promoverse entero**. Puede recibir revisión parcial por bloque mientras permanezca en_revision.

## Límites

No ACL ni firma criptográfica. No recopilar documentación sensible o pruebas empresariales privadas en el repositorio maestro. No declarar gates superados por haber pasado validación de Markdown. No asumir aprobación por el simple hecho de que un agente pudo redactar una evaluación.
