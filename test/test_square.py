from unittest import TestCase
from square import area, perimeter
import unittest


class functionTestSquare(TestCase):
    def test_square_area(self):
        self.assertEqual(area(0), 0)

    def test_square_area0(self):
        self.assertEqual(area(3), 9)

    def test_square_area1(self):
        self.assertEqual(area(2), 4)

    def test_square_area2(self):
        self.assertEqual(area(9), 81)

    def test_square_area3(self):
        self.assertEqual(area(96), 9216)

    def test_square_area4(self):
        self.assertEqual(area(3120), 9734400)

    def test_square_area5(self):
        self.assertAlmostEqual(area(3.14), 9.8596)

    def test_square_area6(self):
        self.assertAlmostEqual(area(20.77), 431.3929)

    def test_square_area7(self):
        with self.assertRaises(ValueError):
            area(-69)

    def test_square_area8(self):
        self.assertEqual(area(14882284201337), 221482383049364867952587569)

    def test_square_perimeter(self):
        self.assertEqual(perimeter(0), 0)

    def test_square_perimeter0(self):
        self.assertEqual(perimeter(3), 12)

    def test_square_perimeter1(self):
        self.assertEqual(perimeter(2), 8)

    def test_square_perimeter2(self):
        self.assertEqual(perimeter(9), 36)

    def test_square_perimeter3(self):
        self.assertEqual(perimeter(96), 384)

    def test_square_perimeter4(self):
        self.assertEqual(perimeter(3120), 12480)

    def test_square_perimeter5(self):
        self.assertAlmostEqual(perimeter(3.14), 12.56)

    def test_square_perimeter6(self):
        self.assertAlmostEqual(perimeter(20.77), 83.08)

    def test_square_perimeter7(self):
        with self.assertRaises(ValueError):
            perimeter(-69)

    def test_square_perimeter8(self):
        self.assertEqual(perimeter(14882284201337), 59529136805348)

if __name__ == '__main__':
    unittest.main()