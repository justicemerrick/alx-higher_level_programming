#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of two numbers.

    Args:
        a (:obj:'int, float'): First number.
        b (:obj:'int, float', optional): Second number.

    Returns:
        int: addition results.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num)
    """Cast the data type of num parameter

    Convert a float number to a integer number

    Args:
        num (:obj:'int, float'): The number to be casted.

    Returns:
        int: The number casted to integer.

    """
    if type(num) is float:
        num = int(num)
        return num

    return num
