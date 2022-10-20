#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of two numbers.

    Float arguments are typecasted to int before adding them.

    Raises:
        TypeError: If either of the two numbers is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinsatance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
