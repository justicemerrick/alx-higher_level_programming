#!/usr/bin/python3

"""Defines an inherited list."""


class MyList(list):
    """Prints a sorted list in ascending order"""

    def print_sorted(self):
        print(sorted(self))
