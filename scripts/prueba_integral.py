#!/usr/bin/env python3
"""Smoke test real del repo en carpeta TEMPORAL, sin modificar ningún negocio."""
from __future__ import annotations
import json
from pathlib import Path
import tempfile
from crear_instancia import create
from importar_traspaso import import_package
from validar_boveda import validate
from exportar_grafo import graph
from operacion import authority_lookup, create_ficha, create_source, propose_change, save_continuity, summary

R=Path(__file__).resolve().parent.parent
FIXTURE=R/'ejemplos/traspaso_sintetico/manifest.json'


def run():
    with tempfile.TemporaryDirectory(prefix='cerebro-smoke-') as root:
        vault=Path(root)/'BRISA-SINTETICA'
        create('BRISA-SINTETICA','Brisa Modular FICTICIA',vault)
        imp=import_package(FIXTURE,vault)
        source=create_source(vault,'F-DEMO-NUEVA','Fuente de trabajo sintética','urn:synthetic:nueva','nota')
        ficha=create_ficha(vault,'consultoria','Consultoría experimental',resumen='Idea para prueba, no venta',sources=['F-DEMO-NUEVA'])
        proposal=propose_change(vault,ficha['id'],'Mejorar alcance de prueba','Hipótesis: estudiar un alcance más claro')
        continuity=save_continuity(vault,summary='Prueba sintética completada.',next_step='Validar con persona y fuente real')
        g=graph(vault)
        val=validate(vault)
        auth=authority_lookup(vault,'precio_modulo_estandar','oferta:OFR-BRISA-001',as_of='2026-10-15')
        assert not val['errores'],val['errores']
        assert auth['estado']=='candidato_para_verificar',auth
        assert imp['bloques']==5
        assert ficha['aprobado'] is False
        assert proposal['modificacion_del_objetivo'] is False
        return {'resultado':'PASS', 'empresa':'SINTETICA','importacion':imp,'notas':val['notas'],
                'ids':val['ids'],'bloques':val['bloques'],'aristas':len(g['aristas']),
                'autoridad':auth['estado'],'propuesta_no_destructiva':True,
                'continuidad':Path(continuity['ruta']).name,
                'limite':'No prueba Obsidian GUI, permisos reales ni recuperación semántica'}

if __name__=='__main__': print(json.dumps(run(),ensure_ascii=False,indent=2))
