import unittest
from circle import area, perimeter


class functionTestCircle(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(area(0), 0.0)

    def test_circle_area1(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)

    def test_circle_area2(self):
        self.assertAlmostEqual(area(2), 12.566370614359172)

    def test_circle_area3(self):
        self.assertAlmostEqual(area(9), 254.46900494077323)

    def test_circle_area4(self):
        self.assertAlmostEqual(area(96), 28952.917895483533)

    def test_circle_area5(self):
        self.assertAlmostEqual(area(3120), 30581519.527104482)

    def test_circle_area6(self):
        self.assertAlmostEqual(area(3.14), 30.974846927333928)

    def test_circle_area7(self):
        self.assertAlmostEqual(area(20.77), 1355.260765450796)

    def test_circle_area8(self):
        with self.assertRaises(ValueError):
            area(-69)

    def test_circle_area9(self):
        self.assertAlmostEqual(area(14882284201337), 6.958074274874452e+26)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(perimeter(0), 0.0)

    def test_circle_perimeter1(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)

    def test_circle_perimeter2(self):
        self.assertAlmostEqual(perimeter(2), 12.566370614359172)

    def test_circle_perimeter3(self):
        self.assertAlmostEqual(perimeter(9), 56.548667764616276)

    def test_circle_perimeter4(self):
        self.assertAlmostEqual(perimeter(96), 603.1857894892403)

    def test_circle_perimeter5(self):
        self.assertAlmostEqual(perimeter(3120), 19603.538158400308)

    def test_circle_perimeter6(self):
        self.assertAlmostEqual(perimeter(3.14), 19.729201864543903)

    def test_circle_perimeter7(self):
        self.assertAlmostEqual(perimeter(20.77), 130.50175883012)

    def test_circle_perimeter8(self):
        with self.assertRaises(ValueError):
            perimeter(-69)

    def test_circle_perimeter9(self):
        self.assertAlmostEqual(perimeter(14882284201337), 93508149431111.52)

if __name__ == '__main__':
    unittest.main()