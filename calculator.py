# 12. Write a Python module named calculator.py containing functions for addition, subtraction, multiplication, and division.

def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference when b is subtracted from a.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient when a is divided by b.
    Raises a ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
