# Name: Sanyam Singh Sachdeva
# Student ID: 100963204
# Description: Temperature sensor application, which takes three temperature
#              inputs from the user, then outputs the minimum, maximum and
#              average temperature, it also handles
#              errors in a user-friendly way.


import statistics

TEMPERATURE_LOWER_BOUND = -50
TEMPERATURE_UPPER_BOUND = 150

def validate_temperature(value):
    if TEMPERATURE_LOWER_BOUND <= value <= TEMPERATURE_UPPER_BOUND:
        return value
    return None

def process_temperatures(temp_list):
    """Process the list of temperatures and return min, max, and avg."""
    try:
        valid_temps = [float(temp) for temp in temp_list]
        valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]

        if not valid_temps:
            return "Error: No valid input provided."

        min_temp = min(valid_temps)
        max_temp = max(valid_temps)
        avg_temp = round(statistics.mean(valid_temps), 2)

        return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

    except ValueError:
        return "Error: Invalid input detected."

# Test Cases
# Students should analyze and ensure the correctness of the outputs

test_cases = [
    [20], # Normal
    [15, 35], # Normal
    [], # Empty
    [10, -10, 30], # Normal
    [-50, 20, 150, 25], # Normal
    [10, "abc", 30], # Invalid type
    [2**31 - 1, -2**31], # Exceeding the limit of integer.
    [10, 10, 10], # Normal
    [-50],  # Lower boundary
    [150],  # Upper boundary
    [-49, 149],  # Values inside range
    [100, 160]
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)