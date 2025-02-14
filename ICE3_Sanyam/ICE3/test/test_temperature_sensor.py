import unittest
from ICE3.src.temperature_sensor import process_temperatures, custom_min, custom_max

class TestTemperatureSensor(unittest.TestCase):
    # Boundary Value Analysis(BVA)
    def test_process_temperatures_minimum_boundary(self):
        result = process_temperatures([-50])
        self.assertEqual(result, "Min: -50°C, Max: -50°C, Avg: -50°C")

    def test_process_temperatures_maximum_boundary(self):
        result = process_temperatures([150])
        self.assertEqual(result, "Min: 150°C, Max: 150°C, Avg: 150°C")

    def test_process_temperatures_near_boundary_valid(self):
        result = process_temperatures([-49, 149])
        self.assertEqual(result, "Min: -49°C, Max: 149°C, Avg: 50°C")

    def test_process_temperatures_near_boundary_invalid(self):
        result = process_temperatures([-51, 151])
        self.assertEqual(result, "Error: No valid input provided.")

    # Robustness Testing
    def test_process_temperature_sensor_mixed_valid_invalid(self): # Removes the invalid data from the list, and continues.
        result = process_temperatures([30, 70, -90])
        self.assertEqual(result, "Min: 30°C, Max: 70°C, Avg: 50°C")

    def test_process_temperature_with_string(self):
        result = process_temperatures([90, 100, "twenty"])
        self.assertEqual(result, "Error: Invalid input detected.")

    def test_process_temperature_with_special_characters(self):
        result = process_temperatures([50, 110, "@"])
        self.assertEqual(result, "Error: Invalid input detected.")

    # Special sceanrios
    def test_process_temperature_with_large_inputs(self):
        result = process_temperatures([2**31 - 1, 50, -2**31])
        self.assertEqual(result, "Min: 50°C, Max: 50°C, Avg: 50°C")

    def test_process_temperature_with_overflow_float(self):
        result = process_temperatures([10**310 - 1, 50, -2**31])
        self.assertEqual(result, "Error: The input is too large to convert to float.")

    def test_process_temperature_with_same_inputs(self):
        result = process_temperatures([40, 40, 40])
        self.assertEqual(result, "Min: 40°C, Max: 40°C, Avg: 40°C")

    def test_process_temperature_with_empty_input(self):
        result = process_temperatures([])
        self.assertEqual(result, "Error: No valid input provided.")

    def test_custom_min_TypeError(self):
        with self.assertRaises(TypeError):
            custom_min(45)

    def test_custom_min_ValueError(self):
        with self.assertRaises(ValueError):
            custom_min([])

    def test_custom_min_normal(self):
        result = custom_min([0, 4, 6, 1, -9])
        self.assertEqual(result, -9)

    def test_custom_max_TypeError(self):
        with self.assertRaises(TypeError):
            custom_max(45)

    def test_custom_max_ValueError(self):
        with self.assertRaises(ValueError):
            custom_max([])

    def test_custom_max_normal(self):
        result = custom_max([0, 4, 6, 1])
        self.assertEqual(result, 6)