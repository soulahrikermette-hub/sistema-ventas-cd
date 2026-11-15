import unittest
from ventas import calcular_total


class TestVentas(unittest.TestCase):
    def test_venta_normal(self):
        self.assertEqual(calcular_total(50, 2), 100)

    def test_venta_decimal(self):
        self.assertEqual(calcular_total(10.5, 2), 21)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total(-10, 2)


if __name__ == "__main__":
    unittest.main()
