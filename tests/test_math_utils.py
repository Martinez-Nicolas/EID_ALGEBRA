"""
Pruebas unitarias básicas.
"""

import unittest
from core.math_utils import analizar_funcion

class TestMathUtils(unittest.TestCase):
    def test_funcion_cuadratica(self):
        resultado = analizar_funcion("x**2 + 2*x + 1")
        self.assertIn("expr", resultado)
        self.assertIn("dominio", resultado)

    def test_error(self):
        resultado = analizar_funcion("2*/x")  # Error sintáctico
        self.assertIn("error", resultado)

if __name__ == "__main__":
    unittest.main()
