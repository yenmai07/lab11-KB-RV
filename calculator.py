"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try: b / a
    except ZeroDivisionError:
        print("error")

def log(a, b):
    try: math.log(a, b)
    except ValueError:
        print("error")

def exp(a, b):
    return a ** b