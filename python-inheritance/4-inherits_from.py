#!/usr/bin/python3
# 4-inherits_from.py
"""This is a python module
thats checks if a class is
a sub class of another class
"""


def inherits_from(obj, a_class):
    """The function checking
    for the inheritance on an object
    """
    if issubclass(obj.__class__, a_class):
        return True
    return False
