#!/usr/bin/python3
"""Inherits  from a list"""


class MyList(list):
    """Prints a sorted list in ascending order"""

    def print_sorted(self):
        print(sorted(self))
