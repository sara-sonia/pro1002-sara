"""
calculator.py module
Provides basic arithmetic functions: add, subtract, multiply, divide.
"""

def add(a, b):
    """return the sum of a and b"""
    return a + b

def subtract(a, b):
    """return the difference of a and b"""
    return a - b

def multiply(a, b)
    """return the product of a and b"""
    return a * b

def divide(a, b)
    """return the division of a by b, raises ZeroDivisionError if b is 0"""
    if b == 0:
        raise ZeroDivisionError("Can not divide by zero")
    return a / b

