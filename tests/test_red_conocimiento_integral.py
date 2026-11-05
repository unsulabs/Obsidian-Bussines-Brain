"""Recorrido sintético: instalación -> arquitectura -> notas -> enlaces -> mapa -> otra sesión."""
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))

from crear_instancia import create
from documentos import create_document
from operacion import create_source,create_ficha,summary
from plan_conocimiento import planificar
from relaciones import propose,query
from mapa_conocimiento import previsualizar,publicar,MAP_MD,MAP_CANVAS
from consulta_contextual import consulta
from validar_boveda import validate


class RedPortableIntegralTest(unittest.TestCase):
    def test_new_company_develops_connected_knowledge_without_copying_templates(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        private=Path(temp.name)
        vault=create("NEGOCIO-PORTABLE","Empresa hipotética",private/"empresa")
        self.assertEqual(validate(vault)["errores"],[])
        config=(vault/"90_Sistema"/"config_empresa.yaml").read_text()
        self.assertIn("0.4.0-rc.1",config)
        vista=(vault/"90_Sistema"/"Vistas"/"Ofertas.base")
        original_vista=vista.read_bytes()

        create_source(vault,"F-TEST-001","Declaración imaginaria","urn:synthetic:conversation","entrevista")
        direction=private/"direccion.md"
        direction.write_text(
            "# Dirección de un negocio ficticio\n\n"
            "## Modelo y criterios\n\n<!-- kb:id=D01-B001 -->\n"
            "La organización ficticia decide cuáles actividades priorizar y "
            "cómo transmitir las decisiones del equipo que atiende sus proyectos.\n\n"
            "## CONTROL\n\nNo existen ventas reales en este ejemplo.\n",encoding="utf8")
        d01=create_document(vault,"D01","Dirección ficticia",direction,
                            tags=["direccion/modelo-valor"],sources=["F-TEST-001"],
                            editorial="en_revision")
        original_d01=Path(d01["ruta"]).read_bytes()

        plan={
            "pregunta":"Distribuir decisiones, oferta y proceso ficticios sin copiar información",
            "asuntos":[
                {"clave":"principio","criterio":"El responsable define una orientación general para el funcionamiento ficticio.","fuentes":["F-TEST-001"],"por_que_importa":"La dirección sirve para comparar alternativas sin contener todas las reglas."},
                {"clave":"producto","criterio":"El equipo considera una oferta con alcance específico y condiciones cambiantes.","fuentes":["F-TEST-001"],"por_que_importa":"La oferta necesita su estado comercial y referencias independientes."},
                {"clave":"flujo","criterio":"El negocio documenta una secuencia recurrente para que otras personas la ejecuten.","fuentes":["F-TEST-001"],"por_que_importa":"La secuencia se mantiene sin reescribir la visión estratégica."}],
            "unidades":[
                {"clave":"direccion","titulo":"Dirección ficticia","tipo":"documento",
                 "clase":"D01","accion":"referenciar","id_existente":"D01",
                 "razon_identidad":"Ya existe D01 y debe ser referencia del modelo sin duplicar condiciones comerciales.",
                 "asuntos":["principio"],"etiquetas":["direccion/modelo-valor"]},
                {"clave":"oferta","titulo":"Servicio imaginario","tipo":"oferta",
                 "accion":"crear","razon_identidad":"La oferta tiene precio y alcance revisables con una historia propia.",
                 "asuntos":["producto"],"etiquetas":["comercial/ofertas"]},
                {"clave":"proceso","titulo":"Proceso imaginario","tipo":"proceso",
                 "accion":"crear","razon_identidad":"El flujo tiene responsables y versiones que pueden evolucionar separadamente.",
                 "asuntos":["flujo"],"etiquetas":["operacion/procesos"]}],
            "relaciones":[
                {"origen":"direccion","destino":"oferta","predicado":"refiere_a",
                 "ambito":"síntesis general","fundamento":"El documento de dirección debe enlazar una oferta sin duplicarla."},
                {"origen":"direccion","destino":"proceso","predicado":"refiere_a",
                 "ambito":"trabajo operativo","fundamento":"La síntesis dirige al procedimiento de ejecución sin reescribirlo."}]}
        plan_file=private/"plan.json"
        plan_file.write_text(json.dumps(plan,ensure_ascii=False))
        tracked=set(vault.rglob("*.md"))
        plan_result=planificar(vault,plan_file)
        self.assertTrue(plan_result["plan_consistente"])
        self.assertEqual(set(vault.rglob("*.md")),tracked)

        paths=[]
        for typ,title,text,tags in [
            ("oferta","Servicio imaginario",
             "# Servicio imaginario\n\n## Alcance\n\n"
             "Ofrecer un acompañamiento únicamente si el cliente de prueba "
             "acepta un alcance y se registra una decisión humana independiente.",
             ["comercial/ofertas"]),
            ("proceso","Proceso imaginario",
             "# Proceso imaginario\n\n## Ejecución\n\n"
             "El equipo registra una solicitud, revisa sus antecedentes y "
             "propone una solución que una persona revisa antes de ejecutar.",
             ["operacion/procesos"])
        ]:
            content=private/(typ+".md")
            content.write_text(text,encoding="utf8")
            item=create_ficha(vault,typ,title,content_file=content,
                             sources=["F-TEST-001"],tags=tags)
            paths.append(item)
            self.assertTrue(item["nota_desarrollada"])
        for item in paths:
            propose(vault,"D01",item["id"],"refiere_a",
                    fuentes=["F-TEST-001"],ambito="empresa ficticia",
                    motivo="Relación propuesta de una nota de dirección a la entidad de prueba.")
        self.assertEqual(query(vault)["total"],2)

        # No hacer cambios en la nota original ni inventar facturas.
        self.assertEqual(Path(d01["ruta"]).read_bytes(),original_d01)
        self.assertEqual(vista.read_bytes(),original_vista)
        self.assertEqual(validate(vault)["errores"],[])
        state=summary(vault)
        self.assertEqual(state["documentos_dx"]["total"],1)
        self.assertGreaterEqual(state["capas"]["entidades_operativas"],2)

        first=previsualizar(vault)
        self.assertEqual(first["sha_actual"],"NUEVO")
        self.assertEqual(first["relaciones_tipadas"],2)
        self.assertFalse((vault/MAP_MD).exists())
        published=publicar(vault,sha_actual=first["sha_actual"],
                           sha_propuesto=first["sha_propuesto"],
                           confirmacion=first["confirmacion_requerida"],
                           backup_dir=private/"respaldos")
        self.assertEqual(published["resultado"],"APLICADO")
        self.assertEqual(validate(vault)["errores"],[])
        self.assertEqual(Path(d01["ruta"]).read_bytes(),original_d01)
        self.assertEqual(vista.read_bytes(),original_vista)
        markdown=(vault/MAP_MD).read_text()
        self.assertIn("Servicio imaginario",markdown)
        self.assertIn("comercial/ofertas",markdown)
        canvas=json.loads((vault/MAP_CANVAS).read_text())
        self.assertEqual(len(canvas["edges"]),2)

        # Simulación de otra sesión/otro proceso recuperando desde archivos, no del chat.
        child=subprocess.run([
            sys.executable,str(ROOT/"scripts"/"cerebro.py"),"relaciones",
            "--vault",str(vault)],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(child.stdout)["total"],2)
        finding=consulta(vault,"organización ficticia",fecha="2026-10-29")
        self.assertEqual(finding["total_coincidencias"],1)
        negative=consulta(vault,"ventas confirmadas",fecha="2026-10-29")
        self.assertEqual(negative["total_coincidencias"],0)
        self.assertFalse(negative["respuesta_semantica_generada"])


if __name__=="__main__":
    unittest.main()
