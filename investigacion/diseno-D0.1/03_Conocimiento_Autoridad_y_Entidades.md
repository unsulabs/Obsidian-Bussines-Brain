# 03 — Semántica empresarial, autoridad y modelo conceptual EN EVALUACIÓN

**Estado:** contrato documental vNext heredado y objetos empresariales candidatos por probar. No es el esquema físico de la bóveda, ni especificación de base de datos, ni ontología aprobada.

## 1. Tres cosas distintas

- **Clase documental**: explica un ámbito del negocio para humanos (D01–D07) o su expediente opcional (X01–X07). Un documento puede alojar varias entidades; una entidad puede aparecer en varios documentos sin duplicar autoridad.
- **Entidad o acontecimiento de negocio**: persona, organización, oferta, oportunidad, proyecto, tarea, acuerdo, reunión, decisión, experimento, activo, etc.; tiene identidad estable cuando requiere historial, consulta, relaciones o permisos propios.
- **Sistema de registro/autoridad**: donde se mantiene el dato oficial de un asunto concreto, que puede ser un contrato firmado, sistema financiero, CRM, fuente normativa o bloque aprobado y controlado en el repositorio.

## 2. Inventario semántico candidato (abierto)

| Clase candidata | Qué representa / identidad propia cuando… | Confusión que debe impedirse | Pregunta que debería contestar |
|---|---|---|---|
| Empresa / unidad | Identidad, propósito, decisiones y ciclos distintos | Empresa ≠ departamento ≠ negocio secundario | ¿De qué empresa y ámbito hablamos? |
| Modelo de negocio | Mecánica de valor y renuncias diferenciadas | Modelo ≠ documento de marketing | ¿Cómo gana y entrega valor? |
| Oferta | Promesa comercial vendible y condiciones revisables | Oferta ≠ producto/servicio/herramienta usada | ¿Qué se puede contratar hoy? |
| Producto | Bien, licencia o producto digital diferenciable | Producto usado ≠ producto vendido | ¿Qué producto se entrega y a quién? |
| Servicio / consultoría | Prestación, alcance, exclusiones y criterios | Consultoría ≠ herramienta ni proyecto | ¿Qué trabajo se contrata y qué incluye? |
| Herramienta / sistema | Recurso utilizado, con dueño y proveedor | Uso interno ≠ venta de licencia | ¿Con qué se presta el servicio? |
| Implementación | Ejecución concreta de una solución | Implementación ≠ metodología universal | ¿Qué se hizo para este cliente? |
| Metodología / framework | Criterios reutilizables con alcance/evidencia | Framework externo ≠ regla empresarial aprobada | ¿Qué método aplica y por qué? |
| Proceso / procedimiento / protocolo | Secuencia, criterio, control o pauta de ejecución | Proceso ≠ checklist ≠ política | ¿Qué se hace bajo qué condiciones? |
| Cliente / cuenta / organización | Relación comercial u organización con historial | Cliente ≠ persona de contacto ≠ usuario final | ¿Quién contrata, paga o participa? |
| Persona / rol / facultad | Sujeto, función contextual y autoridad separables | Participante ≠ responsable ≠ aprobador | ¿Quién puede autorizar esta excepción? |
| Prospecto / oportunidad | Hipótesis comercial con etapas | Cotización ≠ aceptación ≠ contrato | ¿Qué negociación está abierta? |
| Propuesta / cotización | Oferta particular versionada, no siempre aceptada | Presupuesto ≠ dinero recibido | ¿Qué se ofreció exactamente? |
| Proyecto / subproyecto | Trabajo acotado con dependencias y resultados | Proyecto ≠ servicio estándar ni caso general | ¿Qué se está ejecutando y por qué? |
| Sesión / reunión / interacción | Episodio fechable y participantes | Reunión ≠ decisión aprobada | ¿Qué se dijo, acordó y quedó pendiente? |
| Tarea / compromiso | Acción, responsable, vencimiento y ejecución | Pendiente ≠ entregado ni aprobado | ¿Qué se debe hacer, cuándo y por quién? |
| Caso / experiencia | Trayectoria situada con resultado y evidencias | Caso individual ≠ política general | ¿Qué aprendimos de este episodio? |
| Investigación / experimento | Preguntas, método, hallazgos e incertidumbre | Hallazgo ≠ causalidad demostrada | ¿Qué sabemos y con qué límites? |
| Decisión / política / excepción | Acto autorizado en ámbito y fecha | Propuesta ≠ decisión ≠ regla universal | ¿Qué prevalece hoy para este contexto? |
| Contrato / acuerdo / obligación | Compromisos y vigencia particulares | Documento referenciado ≠ texto vigente confirmado | ¿Qué se pactó y con quién? |
| Proveedor / recurso / activo / inventario | Dependencia física/operativa y responsable | Nota ≠ existencia/disponibilidad oficial | ¿Tenemos capacidad para cumplir? |
| Movimiento / resultado económico | Evento financiero registrado vs estimación | Precio ≠ costo ≠ factura ≠ cobro | ¿Cuál es el valor verificado? |
| Fuente / evidencia | Origen verificable, lectura, permiso y fecha | Cita ≠ prueba de verdad universal | ¿De dónde salió esta afirmación? |
| Instrucción / skill de agente | Procedimiento de IA, versión, alcance y permiso | Instrucción de sistema ≠ política de negocio | ¿Qué puede hacer el asistente y con qué límites? |

No se propone crear una nota por fila o instancia; antes hay que probar umbrales de autonomía, fuente de autoridad, privacidad y reutilización.

## 3. Reglas de identidad y relaciones — principio, no formato final

Para cualquier clase candidata, la futura ficha de especificación debe indicar: `definicion`, `ejemplos_reales`, `no_es`, `criterio_de_identidad`, `propiedades_indispensables`, `estados`, `ciclo_de_vida`, `aprobador`, `fuentes`, `relaciones_permitidas`, `cardinalidad`, `permisos`, `preguntas_respondibles`, `errores_de_confusion` y `pruebas_de_consulta`.

Ejemplos de **predicados semánticos** por explorar: `contrata`, `paga`, `usa`, `se_ofrece_a`, `participa_en`, `aprueba`, `deriva_de`, `depende_de`, `se_ejecuta_en`, `evidencia`, `sustituye`, `aplica_a`, `genera`, `es_excepcion_de`. Un campo único `related` puede servir a navegación, pero no transmite esas distinciones.

Separar identidades del nombre legible, ruta de archivo, nota Obsidian, bloque y URL. Un cambio de título no puede cambiar la identidad del cliente, contrato, oferta o fuente.

## 4. Contrato de autoridad heredado v0.9

Para recuperar una afirmación sensible, resolver: `asunto + entidad + contexto + ámbito + fecha efectiva + fuente competente + permisos`. Cuando hay desacuerdo entre dos candidatos igualmente autorizados, **responder conflicto**, no seleccionar el archivo más reciente. Una excepción firmada puede prevalecer para un cliente específico sin cambiar el precio general.

Cuatro ejes **independientes** de cada afirmación sensible:

1. Editorial (`borrador`, `en_revision`, `aprobado`, `retirado`).
2. Cobertura por pregunta (`sin_fuente`, `parcial`, `suficiente_para_tarea`, `no_aplica` con motivo).
3. Estado de conocimiento (`hecho_observado`, `decision_aprobada`, `propuesta`, `hipotesis`, `historico`, `pendiente`, `desconocido`, `conflicto`).
4. Vigencia (`vigente`, `futuro`, `superseded`, `caducado`, `sin_verificar`) y fechas efectivas.

Más clase de apoyo, restricciones y niveles de confidencialidad. Para historia temporal registrar fecha de vigencia y fecha de registro (`recorded_at`): que algo se supiera ayer no significa que se volvió válido ayer.

### Autoridad y revalidación (propuesta a probar)

| Tema consultado | Fuente que probablemente gobierna | Riesgo de duplicación | Verificación pretendida |
|---|---|---|---|
| Estrategia de empresa | Decisión explícita de propietario/decisor con facultad | Un resumen de reunión cambia estrategia | Ver aprobación y fecha efectiva |
| Precio general | Condición aprobada de oferta X01/D03 | Contratos particulares contradicen lista | Buscar oferta y ámbitos de excepción |
| Compromiso de cliente | Contrato o aceptación vigente para ese proyecto | Cotización no aceptada se trata como contrato | Comprobar aceptación/firmas y anexos |
| Pagos/caja | Transacción/sistema de registro conciliado | Modelo financiero pasa por efectivo real | Releer con fecha de corte y permisos |
| Inventario/disponibilidad | Sistema de inventario/operación autorizado | Listado de bodega desactualizado | Confirmar reservas/movimientos |
| Ley/obligación regulatoria | Norma vigente y asesoría competente | Resumen de IA se vuelve consejo definitivo | Verificar norma, jurisdicción y vigencia |
| Preferencia de mercado | Evidencia de clientes/muestra y contexto | Opinión del fundador se vuelve dato de mercado | Mostrar fuentes y límites de extrapolación |

**Siempre vigente** deberá interpretarse como sistema que sabe `qué fuente consultar`, `cuándo revalidar` y `cómo reconocer imposibilidad de verificar`; no prometer sincronización mágica.

## 5. Cambio e impacto

Cuando se propone modificar un precio, compromiso, proceso o estrategia:

- Resolver primero la identidad, autoridad y vigencia de la afirmación a cambiar.
- Conservar versión previa, fechas y causa; no sobrescribir históricos.
- Identificar derivados y dependencias candidatas, distinguiendo navegación de dependencia real.
- Generar **propuesta de cambio** con alcance, diferencial, afectados, fuentes y responsable de autorización.
- Aplicar **solo** dentro de permisos y aprobación, revalidar contra fuente y reconstruir vistas derivadas.
- Probar preguntas históricas y actuales después de la modificación.

El formato del índice de dependencias, reglas de transacción y mecanismo de sincronización sigue abierto.

## 6. Privacidad y restricciones de seguridad

El video VID-003 muestra notas sobre intereses personales: útil como ejemplo de relaciones, **no** recomendación de recolectar gustos privados. Para cada dato personal, exigir fin legítimo, minimización, control de acceso y tratamiento adecuado. Una carpeta `inbox` no impide escritura a un agente que conserve permisos sobre el resto de la bóveda.

## 7. Preguntas que todavía no se han resuelto

- ¿Qué entidades merecen nota, qué permanece como bloque y qué se referencia en sistemas externos?
- ¿Qué relaciones se validan en Properties YAML y cuáles requieren una estructura independiente?
- ¿Cómo mantener autoridad cuando un humano edita Obsidian manualmente y otro agente modifica el contrato?
- ¿Cómo representar condición de vigencia por tipo, campo y contrato, sin exigir metadatos excesivos a un dueño?
- ¿Cómo implementar permisos **reales** fuera del mero convenio de instrucciones de un agente?
- ¿Cuál es la identidad y diferencia exacta entre `caso`, `episodio`, `reunión`, `sesión`, `proyecto` e `implementación` en dos giros empresariales?

**Regla de aceptación futura:** demostración con casos contradictorios, distintos agentes y fechas históricas; no vale solo un diagrama atractivo.
