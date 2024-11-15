import unittest
from circle import area, perimeter


class functionTestCircle(unittest.TestCase):
    def test_circle_area(self):
        # Проверяем площадь круга с радиусом 0
        self.assertAlmostEqual(area(0), 0.0, places=7)

    def test_circle_area1(self):
        # Проверяем площадь круга с радиусом 3
        self.assertAlmostEqual(area(3), 28.27433, places=3)

    def test_circle_area2(self):
        # Проверяем площадь круга с радиусом 2
        self.assertAlmostEqual(area(2), 12.56637, places=3)

    def test_circle_area3(self):
        # Проверяем площадь круга с радиусом 9
        self.assertAlmostEqual(area(9), 254.46900, places=3)

    def test_circle_area4(self):
        # Проверяем площадь круга с радиусом 96
        self.assertAlmostEqual(area(96), 28956.032, places=3)

    def test_circle_area5(self):
        # Проверяем площадь круга с радиусом 3120
        self.assertAlmostEqual(area(3120), 30678688.216, places=3)

    def test_circle_area6(self):
        # Проверяем площадь круга с дробным радиусом
        self.assertAlmostEqual(area(3.14), 30.97484, places=5)

    def test_circle_area7(self):
        # Проверяем, что отрицательный радиус вызывает исключение
        with self.assertRaises(ValueError):
            area(-69)

    def test_circle_area8(self):
        # Проверяем площадь круга с очень большим радиусом
        self.assertAlmostEqual(area(14882284201337), 6.96742085e14,
                               places=5)

    def test_circle_perimeter(self):
        # Проверяем периметр круга с радиусом 0
        self.assertAlmostEqual(perimeter(0), 0.0, places=7)

    def test_circle_perimeter1(self):
        # Проверяем периметр круга с радиусом 3
        self.assertAlmostEqual(perimeter(3), 18.84956, places=3)

    def test_circle_perimeter2(self):
        # Проверяем периметр круга с радиусом 2
        self.assertAlmostEqual(perimeter(2), 12.56637, places=3)

    def test_circle_perimeter3(self):
        # Проверяем периметр круга с радиусом 9
        self.assertAlmostEqual(perimeter(9), 56.54867, places=3)

    def test_circle_perimeter4(self):
        # Проверяем периметр круга с радиусом 96
        self.assertAlmostEqual(perimeter(96), 603.18579, places=3)

    def test_circle_perimeter5(self):
        # Проверяем периметр круга с радиусом 3120
        self.assertAlmostEqual(perimeter(3120), 19579.462, places=3)

    def test_circle_perimeter6(self):
        # Проверяем периметр круга с дробным радиусом
        self.assertAlmostEqual(perimeter(3.14), 19.72445, places=5)

    def test_circle_perimeter7(self):
        # Проверяем, что отрицательный радиус вызывает исключение
        with self.assertRaises(ValueError):
            perimeter(-69)

    def test_circle_perimeter8(self):
        # Проверяем периметр круга с очень большим радиусом
        self.assertAlmostEqual(perimeter(14882284201337), 
                               93356739505382.94, places=2)

if __name__ == '__main__':
    unittest.main()
