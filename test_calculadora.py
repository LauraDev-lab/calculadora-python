"""
Testes unitários automatizados para a Calculadora.
Utiliza o framework padrão 'unittest' do Python.
"""

import unittest
from operacoes import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    calcular_porcentagem,
)


class TestCalculadora(unittest.TestCase):

    # 1. Testes das operações básicas
    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-2, 3), 1)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(-2, 5), -10)
        self.assertEqual(multiplicar(10, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 2), 4.5)

    def test_divisao_por_zero(self):
        """Verifica se uma exceção é levantada ao dividir por zero."""
        with self.assertRaises(ValueError):
            dividir(10, 0)

    # 2. Testes da nova operação: Porcentagem
    def test_porcentagem(self):
        # 10% de 200 = 20
        self.assertEqual(calcular_porcentagem(200, 10), 20.0)
        # 50% de 80 = 40
        self.assertEqual(calcular_porcentagem(80, 50), 40.0)
        # 15% de 150 = 22.5
        self.assertAlmostEqual(calcular_porcentagem(150, 15), 22.5)
        # 0% de qualquer número = 0
        self.assertEqual(calcular_porcentagem(500, 0), 0.0)


if __name__ == "__main__":
    unittest.main()
