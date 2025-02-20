from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        if r > 1e308:
            raise ValueError("Radius is too large to calculate the area.")
        return round(pi * (r ** 2), 5)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(h, (int, float)):
        if a <= 0 or b <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        if h <= 0:
            raise ValueError("Invalid height. Must be a positive number.")
        result = 0.5 * (a + b) * h
        if len(str(result).split(".")[-1]) > 5: # If the result is more than five decimals, round it to five decimal places
            return round(result, 5)
        return result
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
    return 0.5 * d1 * d2