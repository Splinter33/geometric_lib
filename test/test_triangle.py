import unittest
from triangle import area, perimeter


class functionTestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        # Проверяем площадь равностороннего треугольника со сторонами 1
        self.assertAlmostEqual(area(1, 1, 1), 0.4330127018922193, places=7)

    def test_triangle_area1(self):
        # Проверяем, что треугольник с невалидными сторонами вызывает исключение
        with self.assertRaises(ValueError):
            area(1, 2, 3)

    def test_triangle_area2(self):
        # Проверяем площадь прямоугольного треугольника (3, 4, 5)
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=7)

    def test_triangle_area3(self):
        # Проверяем, что при наличии нулевой стороны вызывается исключение
        with self.assertRaises(ValueError):
            area(0, 1, 2)

    def test_triangle_area4(self):
        # Проверяем, что треугольник с некорректными сторонами вызывает исключение
        with self.assertRaises(ValueError):
            area(24, 69, 32)

    def test_triangle_area5(self):
        # Проверяем площадь треугольника с большими сторонами
        self.assertAlmostEqual(area(234, 532, 423), 47929.25018647277, places=7)

    def test_triangle_area6(self):
        # Проверяем, что слишком длинная сторона вызывает исключение
        with self.assertRaises(ValueError):
            area(9, 99, 999)

    def test_triangle_area7(self):
        # Проверяем, что отрицательная сторона вызывает исключение
        with self.assertRaises(ValueError):
            area(-21, 32, 99)

    def test_triangle_area8(self):
        # Проверяем, что отрицательные стороны вызывают исключение
        with self.assertRaises(ValueError):
            area(-25, -24, 69)

    def test_triangle_area9(self):
        # Проверяем площадь равностороннего треугольника с большими сторонами
        self.assertAlmostEqual(area(10000, 10000, 10000), 43301270.18922193, places=7)

    def test_triangle_perimeter(self):
        # Проверяем периметр равностороннего треугольника
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_triangle_perimeter1(self):
        # Проверяем, что треугольник с невалидными сторонами вызывает исключение
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)

    def test_triangle_perimeter2(self):
        # Проверяем периметр прямоугольного треугольника (3, 4, 5)
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_triangle_perimeter3(self):
        # Проверяем, что при наличии нулевой стороны вызывается исключение
        with self.assertRaises(ValueError):
            perimeter(0, 1, 2)

    def test_triangle_perimeter4(self):
        # Проверяем, что треугольник с некорректными сторонами вызывает исключение
        with self.assertRaises(ValueError):
            perimeter(24, 69, 32)

    def test_triangle_perimeter5(self):
        # Проверяем периметр треугольника с большими сторонами
        self.assertEqual(perimeter(234, 532, 423), 1189)

    def test_triangle_perimeter6(self):
        # Проверяем, что слишком длинная сторона вызывает исключение
        with self.assertRaises(ValueError):
            perimeter(9, 99, 999)

    def test_triangle_perimeter7(self):
        # Проверяем, что отрицательная сторона вызывает исключение
        with self.assertRaises(ValueError):
            perimeter(-21, 32, 99)

    def test_triangle_perimeter8(self):
        # Проверяем, что отрицательные стороны вызывают исключение
        with self.assertRaises(ValueError):
            perimeter(-25, -24, 69)

    def test_triangle_perimeter9(self):
        # Проверяем периметр равностороннего треугольника с большими сторонами
        self.assertEqual(perimeter(10000, 10000, 10000), 30000)

if __name__ == '__main__':
    unittest.main()
