#!/usr/bin/python3
"""
this file contain a function that can add 2 numbers and return the integer sum
it converts the float numbers to int
only using int or float 
"""

def add(a, b):
    """ Addition of two integers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
