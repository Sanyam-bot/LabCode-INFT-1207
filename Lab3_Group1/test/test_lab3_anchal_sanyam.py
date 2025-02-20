from math import pi
import unittest
from app.lab3_anchal_sanyam import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid_int(self):
        self.assertAlmostEqual(circle_area(3), 28.27433)

    def test_circle_area_valid_float(self):
        self.assertAlmostEqual(circle_area(9.9), 307.9075)

    def test_circle_area_valid_zero(self):
        self.assertAlmostEqual(circle_area(0), 0)

    def test_circle_area_valid_one(self):
        self.assertAlmostEqual(circle_area(1), round(pi, 5))

    def test_circle_area_invalid_non_numeric(self):
        with self.assertRaises(ValueError):
            circle_area("six")
        with self.assertRaises(ValueError):
            circle_area(None)

    def test_circle_area_invalid_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_circle_area_valid_floating_precision(self):
        self.assertEqual(circle_area(5.2265), 85.81669)

    def test_circle_area_small_values(self):
        self.assertEqual(circle_area(0.0001), 3.141592653589793e-08)


    def test_trapezium_area_valid_integers(self):
        self.assertEqual(trapezium_area(5, 23, 40), 560)

    def test_trapezium_area_valid_floats(self):
        self.assertEqual(trapezium_area(5.9, 23.7, 99.9), 1478.52)

    def test_trapezium_area_valid_with_one(self):
        self.assertEqual(trapezium_area(1, 1, 1), 1)

    def test_trapezium_area_valid_with_equal_bases(self):
        self.assertEqual(trapezium_area(5, 5, 20), 100)

    def test_trapezium_area_valid_floating_precision(self):
        self.assertEqual(trapezium_area(5.2265, 2.2355, 93.226545), 347.82824)

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
        self.assertEqual(trapezium_area(0.0001, 0.0001, 0.0001), 1e-08)

    def test_ellipse_area_valid_integers(self):
        self.assertEqual(ellipse_area(5, 23), 361.28316)

    def test_ellipse_area_valid_floats(self):
        self.assertEqual(ellipse_area(5.9, 23.7), 439.2889)

    def test_ellipse_area_valid_with_one(self):
        self.assertEqual(ellipse_area(1, 1), round(pi, 5))

    def test_ellipse_area_valid_with_equal_sides(self):
        self.assertEqual(ellipse_area(5, 5), 78.53982)

    def test_ellipse_area_valid_floating_precision(self):
        self.assertEqual(ellipse_area(5.2265, 2.2355), 36.70587)

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
        self.assertEqual(ellipse_area(0.0001, 0.0001), 3.141592653589793e-08)


    def test_rhombus_area_valid(self):
        pass

    def test_rhombus_area_invalid(self):
        pass

if __name__ == "__main__":
    unittest.main()