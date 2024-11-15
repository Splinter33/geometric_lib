from unittest import TestCase, main
from triangle import area, perimeter
import unittest


class functionTestTriangle(TestCase):
    def test_triangle_area(self):
        self.assertAlmostEqual(area(1, 1, 1), 0.4330127018922193)

    def test_triangle_area1(self):
        with self.assertRaises(ValueError):
            area(1, 2, 3)

    def test_triangle_area2(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0)

    def test_triangle_area3(self):
        with self.assertRaises(ValueError):
            area(0, 1, 2)

    def test_triangle_area4(self):
        with self.assertRaises(ValueError):
            area(24, 69, 32)

    def test_triangle_area5(self):
        self.assertAlmostEqual(area(234, 532, 423), 47929.25018647277)

    def test_triangle_area6(self):
        with self.assertRaises(ValueError):
            area(9, 99, 999)

    def test_triangle_area7(self):
        with self.assertRaises(ValueError):
            area(-21, 32, 99)

    def test_triangle_area8(self):
        with self.assertRaises(ValueError):
            area(-25, -24, 69)

    def test_triangle_area9(self):
        self.assertAlmostEqual(area(10000, 10000, 10000), 43301270.18922193)

    def test_triangle_perimeter(self):
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_triangle_perimeter1(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)

    def test_triangle_perimeter2(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_triangle_perimeter3(self):
        with self.assertRaises(ValueError):
            perimeter(0, 1, 2)

    def test_triangle_perimeter4(self):
        with self.assertRaises(ValueError):
            perimeter(24, 69, 32)

    def test_triangle_perimeter5(self):
        self.assertEqual(perimeter(234, 532, 423), 1189)

    def test_triangle_perimeter6(self):
        with self.assertRaises(ValueError):
            perimeter(9, 99, 999)

    def test_triangle_perimeter7(self):
        with self.assertRaises(ValueError):
            perimeter(-21, 32, 99)

    def test_triangle_perimeter8(self):
        with self.assertRaises(ValueError):
            perimeter(-25, -24, 69)

    def test_triangle_perimeter9(self):
        self.assertEqual(perimeter(10000, 10000, 10000), 30000)

if __name__ == '__main__':
    unittest.main()