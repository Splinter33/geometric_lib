from unittest import TestCase, main
from calculate import calc
import unittest


class TestCalculate(TestCase):
    def test_valid_cases(self):
        self.assertAlmostEqual(calc("circle", "area", [3]), 28.274333882308138)

    def test_valid_cases1(self):
        self.assertAlmostEqual(calc("circle", "perimeter", [3]), 18.84955592153876)

    def test_valid_cases2(self):
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_valid_cases3(self):
        self.assertEqual(calc("square", "perimeter", [4]), 16)

    def test_valid_cases4(self):
        self.assertAlmostEqual(calc("triangle", "area", [3, 4, 5]), 6.0)

    def test_valid_cases5(self):
        self.assertEqual(calc("triangle", "perimeter", [3, 4, 5]), 12)

    def test_invalid_figures(self):
        calc("hexagon", "area", [4])

    def test_invalid_functions(self):
        calc("circle", "volume", [3])

    def test_invalid_sizes(self):
        calc("circle", "area", [-2, 4])

    def test_invalid_sizes1(self):
        calc("triangle", "perimeter", [342, 4112])

    def test_invalid_sizes2(self):
        calc("square", "area", [])

if __name__ == '__main__':
    unittest.main()