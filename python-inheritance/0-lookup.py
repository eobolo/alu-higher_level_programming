#!/usr/bin/python3
# 0-lookup.py
"""This is a python module
that creates a function and returns
an object.
"""


def lookup(obj):
    """This is a function
    that takes in a class
    object as a variable and
    returns a list of it's
    possible attributes, methods
    (magic methods and self defined methods)
    """
    return dir(obj)
