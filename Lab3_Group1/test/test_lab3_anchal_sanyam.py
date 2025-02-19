import unittest
from app.Lab3_firstname1_firstname2 import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

//

def test_trapezium_area_valid(self):
    //

    def test_trapezium_area_invalid(self):

    //

    def test_ellipse_area_valid(self):

    //

    def test_ellipse_area_invalid(self):

    //

    def test_rhombus_area_valid(self):

    //

    def test_rhombus_area_invalid(self):


if __name__ == "__main__":
    unittest.main()