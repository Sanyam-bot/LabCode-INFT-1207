# Name: Anchalpreet kaur and Sanyam Singh Sachdeva
# Name of the program: Menu-Driven test cases
# Date: Feb 20, 2025
# Description: A menu-driven system which lets the user choose which function's test cases to run from test_lab3_anchal_sanyam.
import unittest

def run_tests(choice):
    suite = unittest.TestSuite()
    if choice == 'c':
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_valid_int'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_valid_float'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_valid_zero'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_valid_one'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_invalid_non_numeric'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_invalid_negative'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_valid_floating_precision'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_circle_area_small_values'))
    elif choice == 't':
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_valid_integers'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_valid_floats'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_valid_with_one'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_valid_with_equal_bases'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_valid_floating_precision'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_invalid_with_zero_height'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_invalid_with_zero_base'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_invalid_with_negative'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_invalid_non_numeric'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_trapezium_area_small_values'))
    elif choice == 'e':
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_valid_integers'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_valid_floats'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_valid_with_one'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_valid_with_equal_sides'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_valid_floating_precision'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_invalid_with_side_zero'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_invalid_with_negative'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_invalid_non_numeric'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_ellipse_area_small_values'))
    elif choice == 'r':
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_valid_integers'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_valid_floats'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_valid_with_one'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_valid_with_equal_sides'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_valid_floating_precision'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_invalid_with_side_zero'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_invalid_with_negative'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_invalid_non_numeric'))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test.test_lab3_anchal_sanyam.TestShapes.test_rhombus_area_small_values'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)