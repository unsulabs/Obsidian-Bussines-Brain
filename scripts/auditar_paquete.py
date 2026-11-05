#!/usr/bin/env python3
"""Auditoría preventiva del producto distribuible. No revisa material privado autorizado."""
from __future__ import annotations
import fnmatch
import json
import os
from pathlib import Path
import re
import sys
import subprocess
from exportar_producto import es_ruta_privada

REPO=Path(__file__).resolve().parent.parent
PRIV_DIRS={'instancias','bovedas_privadas','empresas_reales','local_data','private','.venv','.git'}
PRIVATE_GLOB=['.env','.env.*','*.pem','*.p12','*.pfx','credentials.json','secrets.*','id_rsa*','id_ed25519*']
SUSPECT_KEY=re.compile(r'(?i)(?:sk-(?:proj-)?[A-Za-z0-9_\-]{24,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})')
EXCLUDE={'scripts/auditar_paquete.py'}


def ignored_local_venv(root):
    """Only a real Git checkout's ignored, entirely untracked root venv is local tooling."""
    if not (root / '.git').exists():
        return False
    try:
        ignored = subprocess.run(['git', '-C', str(root), 'check-ignore', '-q', '--', '.venv/'],
                                 capture_output=True).returncode == 0
        tracked = subprocess.check_output(['git', '-C', str(root), 'ls-files', '--', '.venv'],
                                          stderr=subprocess.DEVNULL)
        return ignored and not tracked
    except (OSError, subprocess.CalledProcessError):
        return False


def audit(root=REPO):
    root=Path(root).resolve()
    violations=[];analyzed=0
    # Podar antes de descender: la auditoría no necesita abrir el corpus para
    # detectar que un contenedor privado se coló en el producto.
    paths=[]
    local_venv = ignored_local_venv(root)
    for directory, dirs, files in os.walk(root, followlinks=False):
        base=Path(directory)
        for name in list(dirs):
            p=base/name
            rel=p.relative_to(root)
            if name == '.git' or rel.parts[0] == 'material_privado':
                dirs.remove(name)
            elif rel.as_posix() == '.venv' and local_venv and not p.is_symlink():
                dirs.remove(name)
            elif es_ruta_privada(rel.as_posix()) or name in PRIV_DIRS:
                violations.append('Directorio privado/temporal dentro del paquete: '+str(rel))
                dirs.remove(name)
            else:
                paths.append(p)
        paths.extend(base/name for name in files)
    for p in paths:
        rel=p.relative_to(root)
        # El checkout Git no forma parte del paquete distribuido.
        if '.git' in rel.parts:
            continue
        # El piloto privado está autorizado en este repositorio, pero nunca
        # forma parte del producto exportable ni de esta auditoría.
        if rel.parts[0] == 'material_privado':
            continue
        if p.is_symlink():
            violations.append('Enlace simbólico en paquete: '+str(rel))
            continue
        if es_ruta_privada(rel.as_posix()):
            violations.append('Ruta privada dentro del paquete: '+str(rel))
            continue
        # Archivos que .gitignore excluye: pueden existir durante tests locales,
        # pero no se deben incluir en ZIP ni en `git add`.
        if '__pycache__' in rel.parts or p.suffix in ('.pyc','.pyo') or p.name=='.DS_Store':
            continue
        if any(part in PRIV_DIRS for part in rel.parts):
            violations.append('Directorio privado/temporal dentro del paquete: '+str(rel))
            continue
        if not p.is_file():continue
        if any(fnmatch.fnmatch(p.name,g) for g in PRIVATE_GLOB):
            violations.append('Archivo con nombre de secreto: '+str(rel))
        if p.suffix in ('.pyc','.pyo') or p.name == '.DS_Store':
            violations.append('Caché o archivo temporal en paquete: '+str(rel))
        if rel.as_posix() in EXCLUDE:continue
        if p.suffix.lower() in ('.md','.py','.txt','.json','.yaml','.yml','.csv','.sh'):
            try:text=p.read_text(encoding='utf8')
            except UnicodeError:continue
            if SUSPECT_KEY.search(text): violations.append('Posible credencial en '+str(rel))
            analyzed+=1
    expected=['AGENTS.md','PROMPT_INICIO_CODEX.md','.agents/skills/ce-instalacion/SKILL.md',
              'metodologia/vNext-1.0R/Guia_Metodologia_Documentacion_Empresarial_vNext_1_0R.md',
              'modelo/tipos_entidad.json','plantilla_boveda/Inicio.md','scripts/cerebro.py',
              'ejemplos/traspaso_sintetico/manifest.json']
    for x in expected:
        if not (root/x).is_file():violations.append('Archivo esencial ausente: '+x)
    return {'estado':'PASS' if not violations else 'REVISAR', 'archivos_texto_inspeccionados':analyzed,
            'material_privado_excluido':(root/'material_privado').exists(),
            'problemas':violations,'limite':'Audita sólo el producto. No revisa material_privado, historial Git, licencias completas ni contenido semántico sensible. Revisar aparte cualquier publicación de datos.'}

if __name__=='__main__':
    obj=audit()
    print(json.dumps(obj,ensure_ascii=False,indent=2))
    if obj['problemas']:raise SystemExit(1)
