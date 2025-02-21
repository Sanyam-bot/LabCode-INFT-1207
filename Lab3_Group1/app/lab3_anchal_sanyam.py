from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        result = pi * (r ** 2)
        result_rounded = round(result, 5)
        if result_rounded == 0:  # If the result after rounding is zero, return without rounding
            return result
        return result_rounded
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(h, (int, float)):
        if a <= 0 or b <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        if h <= 0:
            raise ValueError("Invalid height. Must be a positive number.")
        result = 0.5 * (a + b) * h
        result_rounded = round(result, 5)
        if result_rounded == 0: # If the result after rounding is zero, return without rounding
            return result
        return result_rounded
    else:
        raise TypeError("The value needs to be numeric.")

def ellipse_area(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a <= 0 or b <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        result = pi * a * b
        result_rounded = round(result, 5)
        if result_rounded == 0: # If the result after rounding is zero, return without rounding
            return result
        return result_rounded
    else:
        raise TypeError("The value needs to be numeric.")


def rhombus_area(d1, d2):
    if isinstance(d1, (int, float)) and isinstance(d2, (int, float)):
        if d1 <= 0 or d2 <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        result = 0.5 * d1 * d2
        result_rounded = round(result, 5)
        if result_rounded == 0: # If the result after rounding is zero, return without rounding
            return result
        return result_rounded
    else:
        raise TypeError("The value needs to be numeric.")
