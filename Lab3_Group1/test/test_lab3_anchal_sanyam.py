# Name: Anchalpreet kaur and Sanyam Singh Sachdeva
# Name of the program: Area Calculator test cases
# Date: Feb 20, 2025
# Description: Test cases for circle_area, trapezium_area, ellipse_area, and rhombus_area
from math import pi
import unittest
from app.lab3_anchal_sanyam import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid_int(self):
        self.assertAlmostEqual(28.27433, circle_area(3))

    def test_circle_area_valid_float(self):
        self.assertAlmostEqual(307.9075, circle_area(9.9))

    def test_circle_area_valid_zero(self):
        self.assertAlmostEqual(0, circle_area(0))

    def test_circle_area_valid_one(self):
        self.assertAlmostEqual(round(pi, 5), circle_area(1))

    def test_circle_area_invalid_non_numeric(self):
        with self.assertRaises(ValueError):
            circle_area("six")
        with self.assertRaises(ValueError):
            circle_area(None)

    def test_circle_area_invalid_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_circle_area_valid_floating_precision(self):
        self.assertEqual(85.81669, circle_area(5.2265))

    def test_circle_area_small_values(self):
        self.assertEqual(3.141592653589793e-08, circle_area(0.0001))

    def test_trapezium_area_valid_integers(self):
        self.assertEqual(560, trapezium_area(5, 23, 40))

    def test_trapezium_area_valid_floats(self):
        self.assertEqual(1478.52, trapezium_area(5.9, 23.7, 99.9))

    def test_trapezium_area_valid_with_one(self):
        self.assertEqual(1, trapezium_area(1, 1, 1))

    def test_trapezium_area_valid_with_equal_bases(self):
        self.assertEqual(100, trapezium_area(5, 5, 20))

    def test_trapezium_area_valid_floating_precision(self):
        self.assertEqual(347.82824, trapezium_area(5.2265, 2.2355, 93.226545))

    def test_trapezium_area_invalid_with_zero_height(self):
        with self.assertRaises(ValueError):
            trapezium_area(5.9, 230, 0)

    def test_trapezium_area_invalid_with_zero_base(self):
        with self.assertRaises(ValueError):
            trapezium_area(5, 0, 20)

    def test_trapezium_area_invalid_with_negative(self):
        with self.assertRaises(ValueError):
            trapezium_area(-5, 10, 20)

    def test_trapezium_area_invalid_non_numeric(self):
        with self.assertRaises(TypeError):
            trapezium_area(6, 90, "100")

    def test_trapezium_area_small_values(self):
        self.assertEqual(1e-08, trapezium_area(0.0001, 0.0001, 0.0001))

    def test_ellipse_area_valid_integers(self):
        self.assertEqual(361.28316, ellipse_area(5, 23))

    def test_ellipse_area_valid_floats(self):
        self.assertEqual(439.2889, ellipse_area(5.9, 23.7))

    def test_ellipse_area_valid_with_one(self):
        self.assertEqual(round(pi, 5), ellipse_area(1, 1))

    def test_ellipse_area_valid_with_equal_sides(self):
        self.assertEqual(78.53982, ellipse_area(5, 5))

    def test_ellipse_area_valid_floating_precision(self):
        self.assertEqual(36.70587, ellipse_area(5.2265, 2.2355))

    def test_ellipse_area_invalid_with_side_zero(self):
        with self.assertRaises(ValueError):
            ellipse_area(5, 0)

    def test_ellipse_area_invalid_with_negative(self):
        with self.assertRaises(ValueError):
            ellipse_area(-5, 10)

    def test_ellipse_area_invalid_non_numeric(self):
        with self.assertRaises(TypeError):
            ellipse_area(6, "100")

    def test_ellipse_area_small_values(self):
        self.assertEqual(3.141592653589793e-08, ellipse_area(0.0001, 0.0001))

    def test_rhombus_area_valid_integers(self):
        self.assertEqual(57.5, rhombus_area(5, 23))

    def test_rhombus_area_valid_floats(self):
        self.assertEqual(69.915, rhombus_area(5.9, 23.7))

    def test_rhombus_area_valid_with_one(self):
        self.assertEqual(0.5, rhombus_area(1, 1))

    def test_rhombus_area_valid_with_equal_sides(self):
        self.assertEqual(12.5, rhombus_area(5, 5))

    def test_rhombus_area_valid_floating_precision(self):
        self.assertEqual(5.84192, rhombus_area(5.2265, 2.2355))

    def test_rhombus_area_invalid_with_side_zero(self):
        with self.assertRaises(ValueError):
            rhombus_area(5, 0)

    def test_rhombus_area_invalid_with_negative(self):
        with self.assertRaises(ValueError):
            rhombus_area(-5, 10)

    def test_rhombus_area_invalid_non_numeric(self):
        with self.assertRaises(TypeError):
            rhombus_area(6, "100")

    def test_rhombus_area_small_values(self):
        self.assertEqual(5e-09, rhombus_area(0.0001, 0.0001))

if __name__ == "__main__":
    unittest.main()