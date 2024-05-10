import math

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Cannot calculate square root of a negative number!")

def power(a, b):
    return math.pow(a, b)