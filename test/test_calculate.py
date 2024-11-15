import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):
    def test_valid_cases(self):
        # Проверяем корректный расчет площади круга
        self.assertAlmostEqual(calc("circle", "area", [3]), 28.274333882308138, places=7)

    def test_valid_cases1(self):
        # Проверяем корректный расчет периметра круга
        self.assertAlmostEqual(calc("circle", "perimeter", [3]), 18.84955592153876, places=7)

    def test_valid_cases2(self):
        # Проверяем корректный расчет площади квадрата
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_valid_cases3(self):
        # Проверяем корректный расчет периметра квадрата
        self.assertEqual(calc("square", "perimeter", [4]), 16)

    def test_valid_cases4(self):
        # Проверяем корректный расчет площади треугольника
        self.assertAlmostEqual(calc("triangle", "area", [3, 4, 5]), 6.0, places=7)

    def test_valid_cases5(self):
        # Проверяем корректный расчет периметра треугольника
        self.assertEqual(calc("triangle", "perimeter", [3, 4, 5]), 12)

    def test_invalid_cases(self):
        # Проверяем случай, когда указана неверная фигура
        with self.assertRaises(ValueError):
            calc("hexagon", "area", [3])

    def test_invalid_cases1(self):
        # Проверяем случай, когда указан неверный расчет
        with self.assertRaises(ValueError):
            calc("circle", "volume", [3])

    def test_invalid_cases2(self):
        # Проверяем случай, когда переданы неверные параметры для квадрата
        with self.assertRaises(ValueError):
            calc("square", "area", [4, 5])

    def test_invalid_cases3(self):
        # Проверяем случай, когда указаны некорректные стороны для треугольника
        with self.assertRaises(ValueError):
            calc("triangle", "area", [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
