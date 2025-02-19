import unittest

def run_tests(choice):
    if choice == 'c':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_circle_area_valid')
    elif choice == 't':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_trapezium_area_valid')
    elif choice == 'e':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_ellipse_area_valid')
    elif choice == 'r':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_rhombus_area_valid')
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)