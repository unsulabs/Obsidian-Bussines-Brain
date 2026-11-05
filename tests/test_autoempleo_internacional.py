"""A sole trader's explicit context must not acquire regional defaults."""
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from crear_instancia import create
from operacion import create_ficha, create_source, read_note
from validar_boveda import validate


class AutoempleoInternacionalTest(unittest.TestCase):
    def test_portugal_eur_source_preserves_unknown_tax_and_draft(self):
        with tempfile.TemporaryDirectory() as temp:
            vault = Path(temp) / 'audio'
            create('AUDIO-SINTETICO', 'Edición de audio por cuenta propia', vault)
            offer = create_ficha(vault, 'oferta', 'Edición de podcast')
            _, props, _ = read_note(vault, offer['id'])
            self.assertEqual(props['moneda'], 'por_definir')
            self.assertEqual(props['impuestos'], 'por_verificar')
            create_source(vault, 'F-AUDIO', 'Escenario sintético de autoempleo',
                          str(ROOT / 'ejemplos/escenarios/04_autoempleo_internacional.md'),
                          'documento', read_status='leida_completa')
            contextual = create_ficha(
                vault, 'oferta', 'Propuesta de edición situada',
                resumen='Portugal. Trabajo individual. Propuesta: EUR 90 por 45 minutos de audio. Impuestos desconocidos.',
                sources=['F-AUDIO'])
            _, props, body = read_note(vault, contextual['id'])
            self.assertIn('EUR 90', body)
            self.assertIn('Portugal', body)
            self.assertEqual(props['estado_editorial'], 'borrador')
            self.assertEqual(props['impuestos'], 'por_verificar')
            self.assertEqual(props['moneda'], 'por_definir')  # No extraction by guessing.
            self.assertTrue(props['fuentes'])
            self.assertNotIn('MXN', body)
            self.assertEqual(validate(vault)['errores'], [])


if __name__ == '__main__':
    unittest.main()
