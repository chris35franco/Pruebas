import unittest

def calcular_descuento(precio_original, porcentaje_descuento):
    if precio_original <= 0:
        raise ValueError("El precio debe ser mayor a cero.")
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return round(precio_final, 2)

class TestCalculadoraDescuentos(unittest.TestCase):
    
    def test_calculo_descuento_correcto(self):
        self.assertEqual(calcular_descuento(100, 20), 80)
        self.assertEqual(calcular_descuento(200, 50), 100)
        self.assertEqual(calcular_descuento(1000, 15), 850)

    def test_precio_menor_o_igual_a_cero(self):
        with self.assertRaises(ValueError):
            calcular_descuento(0, 10)
        with self.assertRaises(ValueError):
            calcular_descuento(-50, 20)

    def test_porcentaje_descuento_invalido(self):
        with self.assertRaises(ValueError):
            calcular_descuento(100, -10)
        with self.assertRaises(ValueError):
            calcular_descuento(100, 150)

if __name__ == '__main__':
    unittest.main()








