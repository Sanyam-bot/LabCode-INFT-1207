# Name: Sanyam Singh Sachdeva
# Student ID: 100963204
# Description: Temperature sensor application, which takes three temperature
#              inputs from the user, then outputs the minimum, maximum and
#              average temperature, it also handles
#              errors in a user-friendly way.


import statistics

TEMPERATURE_LOWER_BOUND = -50
TEMPERATURE_UPPER_BOUND = 150

def custom_min(iterable):
    if not hasattr(iterable, "__iter__"): # Checking if the custom_min() arg is iterable.
        raise TypeError("custom_min() argument must be an iterable.")

    iterator = iter(iterable) # Converting it to iterator, so the next() can be used.

    try:
        minimum = next(iterator)
    except StopIteration:
        raise ValueError("custom_min() arg is an empty sequence")

    for item in iterator:
        if item < minimum:
            minimum = item
    return minimum

def custom_max(iterable):
    if not hasattr(iterable, "__iter__"):  # Checking if the custom_min() arg is iterable.
        raise TypeError("custom_max() argument must be an iterable.")

    iterator = iter(iterable)  # Converting it to iterator, so the next() can be used.

    try:
        maximum = next(iterator)
    except StopIteration:
        raise ValueError("custom_max() arg is an empty sequence")

    for item in iterator:
        if item > maximum:
            maximum = item
    return maximum

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

        min_temp = custom_min(valid_temps)
        max_temp = custom_max(valid_temps)
        avg_temp = round(statistics.mean(valid_temps), 2)

        return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

    except ValueError:
        return "Error: Invalid input detected."
    except OverflowError:
        return "Error: The input is too large to convert to float."