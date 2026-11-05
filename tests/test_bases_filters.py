"""Regresión: las vistas Bases muestran conocimiento, no sus plantillas.

Comprueba YAML y la lógica documentada del filtro; NO sustituye GUI de Obsidian.
"""
from __future__ import annotations

from pathlib import Path
import re
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "plantilla_boveda" / "90_Sistema" / "Vistas"
DEMO = ROOT / "ejemplos" / "boveda_demo" / "Brisa_Modular" / "90_Sistema" / "Vistas"
PLANTILLAS = 'file.inFolder("90_Sistema/Plantillas")'
EXT = 'file.ext == "md"'

TIPOS_ESPERADOS = {
    "Comercial": {"propuesta_comercial", "cliente_cuenta", "acuerdo"},
    "Comunicacion": {"comunicacion"},
    "Decisiones": {"decision"},
    "Documentos": {"documento"},
    "Entidades": {"entidad"},
    "Fuentes": {"fuente"},
    "Fuentes_y_autoridad": {"fuente", "decision"},
    "Indicadores": {"indicador"},
    "Investigacion_y_aprendizajes": {"investigacion", "caso", "decision"},
    "Ofertas": {"oferta", "producto", "servicio", "consultoria"},
    "Personas_y_organizaciones": {"persona", "organizacion", "proveedor"},
    "Procesos_y_protocolos": {"proceso", "protocolo", "herramienta"},
    "Proyectos": {"proyecto", "implementacion", "caso"},
    "Recursos_y_dependencias": {"recurso", "proveedor", "herramienta"},
    "Reuniones_y_sesiones": {"reunion", "sesion", "continuidad"},
    "Tareas": {"tarea"},
}


def eval_filtro(f, path: str, tipo: str) -> bool:
    """Modelo limitado del filtro; no suplanta el motor de Obsidian."""
    if isinstance(f, str):
        if f == EXT:
            return path.endswith(".md")
        if f == PLANTILLAS:
            return path.startswith("90_Sistema/Plantillas/")
        m = re.fullmatch(r'tipo == "([^"]+)"', f)
        if m:
            return tipo == m.group(1)
        raise AssertionError(f"Expresión no prevista: {f}")
    if isinstance(f, dict) and len(f) == 1:
        op, terms = next(iter(f.items()))
        if op == "and":
            return all(eval_filtro(t, path, tipo) for t in terms)
        if op == "or":
            return any(eval_filtro(t, path, tipo) for t in terms)
        if op == "not":
            return not any(eval_filtro(t, path, tipo) for t in terms)
    raise AssertionError(f"Filtro fuera del subconjunto probado: {f!r}")


class BasesNoTemplatesTest(unittest.TestCase):
    def test_sixteen_views_have_consistent_scoped_filters(self):
        self.assertEqual({p.stem for p in TEMPLATE.glob("*.base")}, set(TIPOS_ESPERADOS))
        self.assertEqual({p.stem for p in DEMO.glob("*.base")}, set(TIPOS_ESPERADOS))
        for name, types in TIPOS_ESPERADOS.items():
            with self.subTest(base=name):
                a = (TEMPLATE / f"{name}.base").read_text(encoding="utf8")
                b = (DEMO / f"{name}.base").read_text(encoding="utf8")
                self.assertEqual(a, b)
                data = yaml.safe_load(a)
                self.assertIn("views", data)
                f = data["filters"]
                self.assertEqual(set(f), {"and"})
                self.assertIn(EXT, f["and"])
                self.assertIn({"not": [PLANTILLAS]}, f["and"])
                tipos = next((x["or"] for x in f["and"]
                              if isinstance(x, dict) and "or" in x), None)
                self.assertIsNotNone(tipos)
                self.assertEqual(set(tipos), {f'tipo == "{t}"' for t in types})
                for typ in types:
                    self.assertFalse(eval_filtro(f, f"90_Sistema/Plantillas/Ficha_{typ}.md", typ))
                    self.assertTrue(eval_filtro(f, f"20_Entidades/OBJ-001_{typ}.md", typ))
                    self.assertFalse(eval_filtro(f, f"20_Entidades/OBJ-001_{typ}.pdf", typ))
                self.assertFalse(eval_filtro(f, "20_Entidades/OTRA.md", "otro_tipo"))

    def test_new_vault_inherits_scoped_views(self):
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from crear_instancia import create
        with tempfile.TemporaryDirectory() as d:
            vault = create("DEMO-FILTROS", "Empresa ficticia", Path(d) / "vault")
            for name in TIPOS_ESPERADOS:
                self.assertEqual(
                    (vault / "90_Sistema" / "Vistas" / f"{name}.base").read_bytes(),
                    (TEMPLATE / f"{name}.base").read_bytes())


if __name__ == "__main__":
    unittest.main()
