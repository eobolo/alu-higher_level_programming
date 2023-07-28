#!/usr/bin/python3
# 10-student.py
"""This is a python script that
creates a class and does json
serialization and deserialization
"""


class_to_json = __import__('8-class_to_json').class_to_json


class Student():
    """This is our class student
    with the init() method and a
    public method
    """
    def __init__(self, first_name, last_name, age):
        """This is the initialization
        method with public instance atrributes
        first-name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This public method
        serializes and deserializes
        using json
        """
        loads = self.__dict__
        if isinstance(attrs, list):
            new_dict = {}
            for i in attrs:
                if i in loads:
                    new_dict[i] = loads[i]
            return new_dict
        else:
            return loads
