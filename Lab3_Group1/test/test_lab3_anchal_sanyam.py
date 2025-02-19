from math import pi
import unittest
from app.lab3_anchal_sanyam import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid_int(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_valid_float(self):
        self.assertAlmostEqual(circle_area(9.9), 307.90749597833565)

    def test_circle_area_valid_zero(self):
        self.assertAlmostEqual(circle_area(0), 0)

    def test_circle_area_valid_one(self):
        self.assertAlmostEqual(circle_area(1), pi)

    def test_circle_area_invalid_non_numeric(self):
        with self.assertRaises(ValueError):
            circle_area("six")
        with self.assertRaises(ValueError):
            circle_area(None)

    def test_circle_area_invalid_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_circle_area_invalid_large_number(self):
        with self.assertRaises(ValueError):
            circle_area(10**10000000)

    def test_trapezium_area_valid(self):
        pass

    def test_trapezium_area_invalid(self):
        pass

    def test_ellipse_area_valid(self):
        pass

    def test_ellipse_area_invalid(self):
        pass

    def test_rhombus_area_valid(self):
        pass

    def test_rhombus_area_invalid(self):
        pass

if __name__ == "__main__":
    unittest.main()