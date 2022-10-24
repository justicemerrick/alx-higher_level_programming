#!/usr/bin/python3
"""Defines an object attribute lookup function."""

def lookup(obj):
    """Returns a list of avaiblable attributes and methods in the object"""
    return (dir(obj))
