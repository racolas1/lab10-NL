"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("a must be non-negative")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("a must be an integer")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Both inputs must be integers")

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
    if a <= 0 or a == 1:
        raise ValueError("base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("must be positive")
    return math.log(a, b)

def exp(a, b):
    return a ** b