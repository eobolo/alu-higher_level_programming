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
    if isinstance(obj.__class__, a_class) or \
            isinstance(obj.__class__, a_class.__bases__):
        return True
    return False
