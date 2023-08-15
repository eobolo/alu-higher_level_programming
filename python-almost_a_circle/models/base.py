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


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation.

        the static method def to_json_string(list_dictionaries)

        that returns the JSON string representation of list_dictionaries

        list_dictionaries is a list of dictionaries

        If list_dictionaries is None or empty, return the string: "[]"

        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
