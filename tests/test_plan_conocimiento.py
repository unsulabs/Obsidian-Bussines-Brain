"""Planeación de conocimiento: identidad, relaciones, fuentes y no sobrecrear."""
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
from lib_ce import split_frontmatter
from operacion import create_ficha, create_source
from plan_conocimiento import planificar


class DistribucionTest(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root=Path(temp.name)
        self.vault=create("FICTICIA","Empresa de prueba",self.root/"vault")
        create_source(self.vault,"F-DEMO-001","Conversación ficticia","urn:synthetic:uno","nota")
        body=self.root/"d01.md"
        body.write_text("# Dirección empresa de ejemplo\n\n## Negocio\n\n"
                        "<!-- kb:id=D01-B001 -->\nEl grupo ficticio identifica "
                        "situaciones de trabajo y analiza el valor aportado "
                        "por decisiones compartidas en sus proyectos.\n\n"
                        "## CONTROL\n\nMaterial sintético de prueba.\n",encoding="utf8")
        doc=create_document(self.vault,"D01","Dirección",body,
                            editorial="en_revision",sources=["F-DEMO-001"])
        self.doc=Path(doc["ruta"])
        self.input=self.root/"plan.json"

    def sample(self):
        return {
            "pregunta":"Organizar aspectos independientes de una conversación empresarial ficticia",
            "asuntos":[
                {"clave":"modelo-valor","criterio":"La dirección ha expresado un criterio del modelo general y su alcance.","por_que_importa":"Necesario para comparar decisiones del modelo sin duplicar ofertas.","fuentes":["F-DEMO-001"]},
                {"clave":"oferta-servicio","criterio":"El equipo explora un servicio cuyas condiciones comerciales pueden cambiar.","por_que_importa":"La oferta tiene términos y periodos independientes de la estrategia.","fuentes":["F-DEMO-001"]},
                {"clave":"proceso-servicio","criterio":"El trabajo necesita un proceso que otras personas puedan ejecutar y revisar.","por_que_importa":"Permite delegar tareas sin volver a leer la estrategia completa.","fuentes":["F-DEMO-001"]},
                {"clave":"detalle-pasajero","criterio":"Una anécdota aislada no se transforma automáticamente en política empresarial.","por_que_importa":"Se conserva en su fuente sin aumentar el número de notas.","fuentes":["F-DEMO-001"]}],
            "unidades":[
                {"clave":"direccion","titulo":"Síntesis del modelo","accion":"revisar","tipo":"documento","clase":"D01","id_existente":"D01","razon_identidad":"La síntesis integra decisiones estratégicas y enlaza a ofertas y procesos autónomos.","asuntos":["modelo-valor"],"etiquetas":["direccion/modelo-valor"]},
                {"clave":"oferta","titulo":"Oferta en estudio","accion":"crear","tipo":"oferta","razon_identidad":"La oferta tiene una vigencia y unas condiciones que evolucionan de forma independiente.","asuntos":["oferta-servicio"],"etiquetas":["comercial/ofertas"]},
                {"clave":"proceso","titulo":"Proceso documentado","accion":"crear","tipo":"proceso","razon_identidad":"El proceso admite uso, actualizaciones y responsables diferentes del documento de dirección.","asuntos":["proceso-servicio"],"etiquetas":["operacion/procesos"]},
                {"clave":"detalle","titulo":"Comentario aislado","accion":"no_crear","razon_identidad":"El comentario no necesita una nueva entidad y puede permanecer en la fuente original.","asuntos":["detalle-pasajero"]}],
            "relaciones":[
                {"origen":"direccion","destino":"oferta","predicado":"refiere_a","ambito":"síntesis estratégica","fundamento":"La dirección se enlaza con la oferta sin copiar todas sus condiciones."},
                {"origen":"direccion","destino":"proceso","predicado":"refiere_a","ambito":"ejecución operativa","fundamento":"La dirección cita el proceso operable sin duplicar instrucciones."}]
        }

    def save(self,data):
        self.input.write_text(json.dumps(data,ensure_ascii=False),encoding="utf8")

    def test_plan_connected_and_read_only(self):
        self.save(self.sample())
        original=self.doc.read_bytes()
        notes=set(self.vault.rglob("*.md"))
        r=planificar(self.vault,self.input)
        self.assertEqual(r["asuntos_detectados"],4)
        self.assertEqual(len(r["unidades_propuestas"]),4)
        self.assertEqual(len(r["relaciones_candidatas"]),2)
        self.assertTrue(r["plan_consistente"])
        self.assertFalse(r["documentos_modificados"])
        self.assertEqual(notes,set(self.vault.rglob("*.md")))
        self.assertEqual(original,self.doc.read_bytes())

    def test_monolith_requires_rethinking(self):
        p=self.sample()
        p["unidades"]=[{
            "clave":"direccion","titulo":"Todas las ideas en D01",
            "accion":"revisar","tipo":"documento","clase":"D01","id_existente":"D01",
            "razon_identidad":"Se decidió por comodidad colocar los temas comerciales y operativos en una sola sección.",
            "asuntos":[a["clave"] for a in p["asuntos"]],
            "etiquetas":["direccion/modelo-valor"]}]
        p["relaciones"]=[]
        self.save(p)
        result=planificar(self.vault,self.input)
        self.assertTrue(any("POSIBLE_MONOLITO" in s for s in result["advertencias"]))
        self.assertFalse(result["plan_consistente"])

    def test_existing_units_own_other_subjects_without_false_monolith(self):
        offer=create_ficha(self.vault,"oferta","Oferta ya documentada",sources=["F-DEMO-001"])
        process=create_ficha(self.vault,"proceso","Proceso ya documentado",sources=["F-DEMO-001"])
        p=self.sample()
        p["unidades"][0].update({
            "titulo":"Economía transversal","accion":"crear","clase":"D05",
            "razon_identidad":"Una decisión económica transversal requiere historia distinta de las condiciones de la oferta y del proceso."})
        p["unidades"][0].pop("id_existente")
        p["unidades"][1].update({
            "titulo":"Oferta ya documentada","accion":"referenciar","id_existente":offer["id"]})
        p["unidades"][2].update({
            "titulo":"Proceso ya documentado","accion":"referenciar","id_existente":process["id"]})
        self.save(p)
        result=planificar(self.vault,self.input)
        self.assertTrue(result["plan_consistente"])
        self.assertFalse(any("POSIBLE_MONOLITO" in s for s in result["advertencias"]))
        self.assertEqual(result["asuntos_detectados"],4)

    def test_double_owner_is_rejected(self):
        p=self.sample()
        p["unidades"][1]["asuntos"].append("modelo-valor")
        self.save(p)
        with self.assertRaisesRegex(ValueError,"dos dueños"):
            planificar(self.vault,self.input)

    def test_do_not_create_second_existing_D01(self):
        p=self.sample()
        p["unidades"][0]["accion"]="crear"
        del p["unidades"][0]["id_existente"]
        self.save(p)
        with self.assertRaisesRegex(ValueError,"ya existe"):
            planificar(self.vault,self.input)

    def test_missing_sources_warn_and_bad_tags_block(self):
        p=self.sample()
        p["asuntos"][0]["fuentes"]=["F-NO-EXISTE"]
        self.save(p)
        result=planificar(self.vault,self.input)
        self.assertEqual(result["fuentes_pendientes"],["F-NO-EXISTE"])
        self.assertFalse(result["plan_consistente"])
        p=self.sample()
        p["unidades"][1]["etiquetas"]=["persona identificable"]
        self.save(p)
        with self.assertRaisesRegex(ValueError,"etiquetas"):
            planificar(self.vault,self.input)

    def test_cli_plan(self):
        self.save(self.sample())
        cmd=[sys.executable,str(ROOT/"scripts"/"cerebro.py"),"plan-conocimiento",
             "--vault",str(self.vault),"--archivo",str(self.input)]
        completed=subprocess.run(cmd,check=True,capture_output=True,text=True)
        self.assertEqual(json.loads(completed.stdout)["modo"],"SOLO_LECTURA")

    def test_tag_properties_on_new_notes(self):
        fiche=create_ficha(self.vault,"proceso","Proceso sintético",
                           sources=["F-DEMO-001"],tags=["operacion/procesos"])
        fm,_=split_frontmatter(Path(fiche["ruta"]).read_text())
        self.assertEqual(fm["tags"],["operacion/procesos"])
        text=self.root/"d02.md"
        text.write_text("# Mercado ficticio\n\n## Situación\n\n"
                        "La organización sintética explora una necesidad "
                        "con distintos compradores y registra hipótesis de investigación.",
                        encoding="utf8")
        d=create_document(self.vault,"D02","Mercado ficticio",text,tags=["mercado/investigacion"])
        fm,_=split_frontmatter(Path(d["ruta"]).read_text())
        self.assertEqual(fm["tags"],["mercado/investigacion"])
        with self.assertRaisesRegex(ValueError,"Etiquetas"):
            create_ficha(self.vault,"oferta","No usar",tags=["Nombre completo"])

    def test_developed_ficha_has_content_without_placeholders(self):
        file=self.root/"operacion.md"
        content=("# Proceso de prueba\n\n## Inicio\n\n"
                 "Cuando ocurre una solicitud ficticia, el equipo registra "
                 "los responsables y confirma el objetivo del trabajo antes "
                 "de ajustar las herramientas e iniciar las revisiones.\n")
        file.write_text(content,encoding="utf8")
        out=create_ficha(self.vault,"proceso","Operación sintética",
                         content_file=file,sources=["F-DEMO-001"],
                         tags=["operacion/procesos"])
        meta,body=split_frontmatter(Path(out["ruta"]).read_text())
        self.assertEqual(body,content)
        self.assertTrue(out["nota_desarrollada"])
        self.assertEqual(meta["tags"],["operacion/procesos"])
        self.assertNotIn("Por desarrollar",body)

    def test_single_topic_does_not_require_artificial_no_crear(self):
        p=self.sample()
        p["asuntos"]=[p["asuntos"][0]]
        p["unidades"]=[p["unidades"][0]]
        p["relaciones"]=[]
        self.save(p)
        result=planificar(self.vault,self.input)
        self.assertTrue(result["plan_consistente"])
        self.assertEqual(result["advertencias"],[])
        self.assertTrue(result["recomendaciones"])

    def test_explicitly_independent_notes_need_no_fake_relation(self):
        p=self.sample()
        p["relaciones"]=[]
        p["justificacion_sin_relaciones"]=(
            "La oferta y el proceso son objetos completamente independientes "
            "en este proyecto sintético, sin vínculo de dependencia confirmado.")
        self.save(p)
        result=planificar(self.vault,self.input)
        self.assertTrue(result["plan_consistente"])
        self.assertFalse(result["relaciones_candidatas"])

    def test_x_id_is_not_document_class(self):
        p=self.sample()
        p["unidades"][1].update({"tipo":"documento","clase":"X01-IDENTIDAD-TEST"})
        self.save(p)
        with self.assertRaisesRegex(ValueError,"clase documental debe ser"):
            planificar(self.vault,self.input)

    def test_detect_existing_D_family_even_if_yaml_id_is_different(self):
        from lib_ce import make_note
        fm,body=split_frontmatter(self.doc.read_text(encoding="utf8"))
        fm["id"]="ID-DIRECCION-CANONICA"
        self.doc.write_text(make_note(fm,body),encoding="utf8")
        p=self.sample()
        p["unidades"][0].update({"accion":"crear","id_existente":None})
        self.save(p)
        with self.assertRaisesRegex(ValueError,"ya existe"):
            planificar(self.vault,self.input)

    def test_duplicate_entity_title_warns_without_creating_another(self):
        note=create_ficha(self.vault,"oferta","Oferta en estudio",
                          sources=["F-DEMO-001"])
        p=self.sample()
        self.save(p)
        before=Path(note["ruta"]).read_bytes()
        result=planificar(self.vault,self.input)
        self.assertFalse(result["plan_consistente"])
        self.assertEqual(result["posibles_duplicados"][0]["unidad"],"oferta")
        self.assertEqual(result["posibles_duplicados"][0]["ids_existentes"],[note["id"]])
        self.assertEqual(Path(note["ruta"]).read_bytes(),before)

    def test_no_crear_cannot_be_relation_endpoint(self):
        p=self.sample()
        p["relaciones"].append({
            "origen":"direccion","destino":"detalle","predicado":"refiere_a",
            "ambito":"anécdota ficticia",
            "fundamento":"Una relación sintética incorrecta a algo que no tendrá nota."})
        self.save(p)
        with self.assertRaisesRegex(ValueError,"No se puede enlazar"):
            planificar(self.vault,self.input)

    def test_plan_inside_vault_is_rejected(self):
        self.save(self.sample())
        inside=self.vault/"90_Sistema"/"plan.json"
        inside.write_bytes(self.input.read_bytes())
        with self.assertRaisesRegex(ValueError,"fuera de la bóveda"):
            planificar(self.vault,inside)


if __name__=="__main__":
    unittest.main()
