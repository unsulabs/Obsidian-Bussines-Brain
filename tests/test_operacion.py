"""Regresión de operaciones MVP sin datos de empresa real."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

REPO=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(REPO/'scripts'))
from crear_instancia import create
from importar_traspaso import import_package
from operacion import (authority_lookup, create_ficha, create_source, exact_search,
                       load_registry, propose_change, save_continuity, summary)
from validar_boveda import validate

FIXTURE=REPO/'ejemplos/traspaso_sintetico/manifest.json'

class OperacionTest(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.root=Path(t.name)
        self.vault=self.root/'boveda'
        create('EMPRESA-PRUEBA','Negocio de prueba ficticio',self.vault)

    def source(self,id='F-TEST-01'):
        return create_source(self.vault,id,'Fuente creada para prueba','urn:synthetic:source','nota',read_status='no_verificada')

    def test_registry_has_clear_distinctions_and_valid_relations(self):
        reg=load_registry()
        self.assertEqual(len(reg),27)
        self.assertIn('producto',reg);self.assertIn('oferta',reg)
        self.assertIn('consultoria',reg);self.assertIn('herramienta',reg)
        self.assertIn('persona',reg);self.assertIn('cliente_cuenta',reg)
        self.assertIn('propuesta_comercial',reg);self.assertIn('acuerdo',reg)
        for item in reg.values():
            self.assertGreater(len(item['no_confundir']),10)
            self.assertGreater(len(item['pregunta_de_prueba']),15)
            self.assertTrue(set(item['relaciones_candidatas']).issubset(reg))
            self.assertTrue((REPO/'plantilla_boveda'/'90_Sistema'/'Plantillas'/('Ficha_'+item['tipo']+'.md')).is_file())

    def test_first_installed_vault_has_no_fake_business_data(self):
        self.assertEqual(validate(self.vault)['errores'],[])
        self.assertEqual(list((self.vault/'20_Entidades').glob('*.md')),[])
        self.assertFalse((self.vault/'30_Registros').exists())
        self.assertIn('no un formulario', (self.vault/'Inicio.md').read_text())

    def test_create_ficha_draft_with_source(self):
        self.source()
        result=create_ficha(self.vault,'consultoria','Diagnóstico técnico de proyectos',sources=['F-TEST-01'])
        p=Path(result['ruta']); self.assertTrue(p.exists())
        props,body=__import__('lib_ce').split_frontmatter(p.read_text())
        self.assertEqual(props['estado_conocimiento'],'pendiente')
        self.assertEqual(props['estado_editorial'],'borrador')
        self.assertEqual(props['vigencia'],'sin_verificar')
        self.assertIn('[[50_Fuentes/Fuente creada para prueba]]',props['fuentes'])
        self.assertIn('no equivale a aprobación',body.lower())
        self.assertEqual(validate(self.vault)['errores'],[])

    def test_new_ficha_without_source_never_approved(self):
        result=create_ficha(self.vault,'oferta','Oferta aún no aprobada')
        text=Path(result['ruta']).read_text()
        self.assertIn('sin_verificar',text)
        self.assertIn('fuentes: []',text)
        self.assertIn('pendiente',text)
        self.assertEqual(validate(self.vault)['errores'],[])

    def test_ficha_rejects_unregistered_source(self):
        with self.assertRaises(ValueError):
            create_ficha(self.vault,'oferta','Oferta',sources=['F-AUSENTE'])
        self.assertEqual(list((self.vault/'20_Entidades').glob('*.md')),[])

    def test_ficha_rejects_unsupported_type(self):
        with self.assertRaises(ValueError):create_ficha(self.vault,'sistema_de_contabilidad_magico','invento')
        with self.assertRaises(ValueError):create_ficha(self.vault,'fuente','use source function')

    def test_injection_title_rejected(self):
        with self.assertRaises(ValueError):create_ficha(self.vault,'proyecto','Titulo\notro dato')

    def test_same_visible_name_blocks_collision_without_losing_first_note(self):
        x=create_ficha(self.vault,'proyecto','Mismo título')
        before=Path(x['ruta']).read_bytes()
        with self.assertRaises(FileExistsError):
            create_ficha(self.vault,'proyecto','Mismo título')
        self.assertEqual(Path(x['ruta']).read_bytes(),before)
        self.assertEqual(validate(self.vault)['errores'],[])

    def test_sources_are_references_not_originals_and_no_overwrite(self):
        src=self.source();self.assertTrue(Path(src['ruta']).exists())
        self.assertFalse(src['copia_original'])
        self.assertNotIn('documento original íntegro',Path(src['ruta']).read_text())
        with self.assertRaises(FileExistsError):self.source()

    def test_protected_source_rejected(self):
        with self.assertRaises(ValueError):
            create_source(self.vault,'F-TEST-01','material','url','contrato',permission='restringido')

    def test_status_summary_tracks_only_actual_notes(self):
        before=summary(self.vault)
        self.assertEqual(before['por_tipo'].get('oferta'),None)
        create_ficha(self.vault,'oferta','Demo')
        after=summary(self.vault)
        self.assertEqual(after['por_tipo']['oferta'],1)
        self.assertEqual(after['conocimiento']['pendiente'],1)
        self.assertIn('NO cobertura suficiente',after['advertencia'])

    def test_proposal_is_separate_and_hash_provenance(self):
        o=create_ficha(self.vault,'oferta','Oferta bajo estudio')
        target=Path(o['ruta']);original=target.read_bytes()
        change=propose_change(self.vault,o['id'],'Se requiere actualizar el alcance', 'Agregar condiciones sujetas a revisión')
        self.assertTrue(Path(change['archivo']).is_file())
        self.assertEqual(target.read_bytes(),original)
        self.assertEqual(change['objetivo_sha256'],hashlib.sha256(original).hexdigest())
        self.assertEqual(validate(self.vault)['errores'],[])

    def test_proposal_does_not_write_nonexistent_target(self):
        with self.assertRaises(ValueError):
            propose_change(self.vault,'NO-EXISTE','motivo','contenido')

    def test_continuity_records_not_as_authority(self):
        r=save_continuity(self.vault,summary='Se evaluó una oferta sintética.',next_step='Recuperar fuente real antes de aprobar',reviewer='por_validar')
        self.assertEqual(summary(self.vault)['ultima_continuidad'],str(Path(r['ruta']).resolve().relative_to(self.vault.resolve())))
        self.assertIn('no es autoridad',Path(r['ruta']).read_text())
        self.assertEqual(validate(self.vault)['errores'],[])

    def test_continuity_requires_next_step(self):
        with self.assertRaises(ValueError):save_continuity(self.vault,summary='hecho',next_step='')

    def test_literal_search_is_not_semantic(self):
        create_ficha(self.vault,'proyecto','Campaña de lanzamiento',resumen='Vamos a investigar inventarios')
        res=exact_search(self.vault,'inventarios')
        self.assertEqual(res['total'],1)
        self.assertIn('NO semantic retrieval',res['alcance'])
        self.assertEqual(exact_search(self.vault,'no_existe_algo')['total'],0)

    def test_authority_query_no_import_returns_unknown(self):
        res=authority_lookup(self.vault,'precio','oferta:xxx')
        self.assertEqual(res['estado'],'sin_autoridad_explicita')

    def test_authority_query_imported_synthetic_price(self):
        # isolated correct matching company
        other=self.root/'brisa';create('BRISA-SINTETICA','Brisa Ficticia',other)
        import_package(FIXTURE,other)
        before=authority_lookup(other,'precio_modulo_estandar','oferta:OFR-BRISA-001',as_of='2026-09-30')
        active=authority_lookup(other,'precio_modulo_estandar','oferta:OFR-BRISA-001',as_of='2026-10-15')
        self.assertEqual(before['estado'],'sin_autoridad_explicita')
        self.assertEqual(active['estado'],'candidato_para_verificar')
        self.assertEqual(len(active['coincidencias']),1)
        self.assertTrue(active['coincidencias'][0]['fuentes'])

    def test_authority_rejects_bad_date(self):
        with self.assertRaises(ValueError):authority_lookup(self.vault,'precio','scope',as_of='2026-13-80')

    def test_bases_templates_and_schemas_present(self):
        files=list((REPO/'plantilla_boveda'/'90_Sistema'/'Vistas').glob('*.base'))
        self.assertGreaterEqual(len(files),12)
        for p in files:
            obj=yaml.safe_load(p.read_text())
            self.assertIn('filters',obj);self.assertIn('views',obj)
            self.assertTrue(all('type' in v and 'name' in v for v in obj['views']))
        docs=json.loads((REPO/'modelo/clases_documentales.json').read_text())['clases']
        self.assertEqual({d['id'] for d in docs},{f'{p}{i:02}' for p in ('D','X') for i in range(1,8)})
        for doc in docs:
            self.assertTrue(any((REPO/'plantilla_boveda/90_Sistema/Plantillas').glob(doc['id']+'_*')))
            self.assertGreaterEqual(len(doc['encabezados']),7)

    def test_doctor_with_no_dependencies(self):
        cmd=[sys.executable,'-S',str(REPO/'scripts'/'cerebro.py'),'doctor']
        p=subprocess.run(cmd,capture_output=True,text=True,check=True)
        data=json.loads(p.stdout)
        self.assertEqual(data['producto'],'Cerebro Empresarial 0.4.0-rc.1')
        self.assertEqual(data['obsidian_gui'],'NO VERIFICADO')
        self.assertEqual(data['dependencias_python']['yaml'],'NO INSTALADO')

    def test_consulta_missing_dependency_offers_existing_python_before_install(self):
        cmd=[sys.executable,'-S',str(REPO/'scripts'/'cerebro.py'),
             'consulta-contextual','--vault',str(self.vault),'--texto','compras']
        p=subprocess.run(cmd,capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
        self.assertIn('Dependencia faltante en',p.stderr)
        self.assertIn('python3.11',p.stderr)
        self.assertLess(p.stderr.index('Antes de instalar'),p.stderr.index('solicita autorización'))
        self.assertEqual(p.stdout,'')

    def test_oferta_never_assumes_country_or_currency(self):
        x=create_ficha(self.vault,'oferta','Oferta ficticia internacional')
        fm,_=__import__('lib_ce').split_frontmatter(Path(x['ruta']).read_text())
        self.assertEqual(fm['moneda'],'por_definir')
        self.assertEqual(fm['precio_sistema_fuente'],'')
        self.assertEqual(fm['estado_editorial'],'borrador')

    def test_approval_not_inferred_from_text(self):
        x=create_ficha(self.vault,'decision','Aprobamos la venta según alguien dijo',resumen='aprobado aprobado aprobado')
        fm,_=__import__('lib_ce').split_frontmatter(Path(x['ruta']).read_text())
        self.assertEqual(fm['estado_editorial'],'borrador')
        self.assertEqual(fm['estado_conocimiento'],'pendiente')

if __name__=='__main__':unittest.main()
