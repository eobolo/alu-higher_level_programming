#!/usr/bin/python3
"""
This is a python module

that has the class base

This class will be the “base”

of all other classes in this project

The goal of it is to manage id attribute

in all your future classes and to avoid

duplicating the same code (by extension, same bugs)
"""


class Base:
    """
    This class base has the following;

    private class attribute __nb_objects = 0

    class constructor: def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initialization

        constructor method for each

        instance or object of this class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
