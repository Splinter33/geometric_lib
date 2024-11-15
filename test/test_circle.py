import unittest
from circle import area, perimeter


class functionTestCircle(unittest.TestCase):
    def test_circle_area(self):
        # Проверяем площадь круга с радиусом 0
        self.assertAlmostEqual(area(0), 0.0, places=7)

    def test_circle_area1(self):
        # Проверяем площадь круга с радиусом 3
        self.assertAlmostEqual(area(3), 28.274333882308138, places=7)

    def test_circle_area2(self):
        # Проверяем площадь круга с радиусом 2
        self.assertAlmostEqual(area(2), 12.566370614359172, places=7)

    def test_circle_area3(self):
        # Проверяем площадь круга с радиусом 9
        self.assertAlmostEqual(area(9), 254.46900494077323, places=7)

    def test_circle_area4(self):
        # Проверяем площадь круга с радиусом 96
        self.assertAlmostEqual(area(96), 28952.917895483533, places=7)

    def test_circle_area5(self):
        # Проверяем площадь круга с радиусом 3120
        self.assertAlmostEqual(area(3120), 30581519.527104482, places=7)

    def test_circle_area6(self):
        # Проверяем площадь круга с радиусом 3.14
        self.assertAlmostEqual(area(3.14), 30.974846927333928, places=7)

    def test_circle_area7(self):
        # Проверяем площадь круга с радиусом 20.77
        self.assertAlmostEqual(area(20.77), 1355.260765450796, places=7)

    def test_circle_area8(self):
        # Проверяем, что при отрицательном радиусе выбрасывается исключение
        with self.assertRaises(ValueError):
            area(-69)

    def test_circle_area9(self):
        # Проверяем площадь круга с очень большим радиусом
        self.assertAlmostEqual(area(14882284201337), 6.958074274874452e+26, places=7)

    def test_circle_perimeter(self):
        # Проверяем периметр круга с радиусом 0
        self.assertAlmostEqual(perimeter(0), 0.0, places=7)

    def test_circle_perimeter1(self):
        # Проверяем периметр круга с радиусом 3
        self.assertAlmostEqual(perimeter(3), 18.84955592153876, places=7)

    def test_circle_perimeter2(self):
        # Проверяем периметр круга с радиусом 2
        self.assertAlmostEqual(perimeter(2), 12.566370614359172, places=7)

    def test_circle_perimeter3(self):
        # Проверяем периметр круга с радиусом 9
        self.assertAlmostEqual(perimeter(9), 56.548667764616276, places=7)

    def test_circle_perimeter4(self):
        # Проверяем периметр круга с радиусом 96
        self.assertAlmostEqual(perimeter(96), 603.1857894892403, places=7)

    def test_circle_perimeter5(self):
        # Проверяем периметр круга с радиусом 3120
        self.assertAlmostEqual(perimeter(3120), 19603.538158400308, places=7)

    def test_circle_perimeter6(self):
        # Проверяем периметр круга с радиусом 3.14
        self.assertAlmostEqual(perimeter(3.14), 19.729201864543903, places=7)

    def test_circle_perimeter7(self):
        # Проверяем периметр круга с радиусом 20.77
        self.assertAlmostEqual(perimeter(20.77), 130.50175883012, places=7)

    def test_circle_perimeter8(self):
        # Проверяем, что при отрицательном радиусе выбрасывается исключение
        with self.assertRaises(ValueError):
            perimeter(-69)

    def test_circle_perimeter9(self):
        # Проверяем периметр круга с очень большим радиусом
        self.assertAlmostEqual(perimeter(14882284201337), 93508149431111.52, places=7)

if __name__ == '__main__':
    unittest.main()
