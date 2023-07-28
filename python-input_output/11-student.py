#!/usr/bin/python3
# 10-student.py
"""This is a python script that
creates a class and does json
serialization and deserialization
"""


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

    def reload_from_json(self, json):
        """A method that replaces
        the attributes of an instance
        by the attributes found in the
        object.__dict__ dictionary
        """
        for key in json.keys():
            if key == "first_name":
                self.first_name = json["first_name"]
            elif key == "last_name":
                self.last_name = json["last_name"]
            elif key == "age":
                self.age = json["age"]
            else:
                continue
