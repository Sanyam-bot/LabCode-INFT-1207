# Name: Anchalpreet kaur and Sanyam Singh Sachdeva
# Name of the program: Area Calculator
# Date: Feb 20, 2025
# Description: Functions to calculate the area of circle, trapezium, ellipse,and rhombus.

from math import pi

def round_upto_five(result):
    result_rounded = round(result, 5)
    if result_rounded == 0:  # If the result after rounding is zero, return without rounding
        return result
    return result_rounded

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        result = pi * (r ** 2)
        return round_upto_five(result)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(h, (int, float)):
        if a <= 0 or b <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        if h <= 0:
            raise ValueError("Invalid height. Must be a positive number.")
        result = 0.5 * (a + b) * h
        return round_upto_five(result)
    else:
        raise TypeError("The value needs to be numeric.")

def ellipse_area(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a <= 0 or b <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        result = pi * a * b
        return round_upto_five(result)
    else:
        raise TypeError("The value needs to be numeric.")


def rhombus_area(d1, d2):
    if isinstance(d1, (int, float)) and isinstance(d2, (int, float)):
        if d1 <= 0 or d2 <= 0:
            raise ValueError("Invalid side length. Must be a positive number.")
        result = 0.5 * d1 * d2
        return round_upto_five(result)
    else:
        raise TypeError("The value needs to be numeric.")
