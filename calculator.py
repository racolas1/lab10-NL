#https://github.com/racolas1/lab10-NL
# Partner 1: Nikolas Lima
# Partner 2: Nikolas Lima

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("a must be non-negative")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("a must be a number")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Both inputs must be numbers")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b <= 0 or b == 1:
        raise ValueError("base must be positive and not equal to 1")
    if a <= 0:
        raise ValueError("argument must be positive")
    return math.log(a,b)

def exp(a, b):
    return a ** b