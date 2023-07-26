#!/usr/bin/python3
# 6-base_geometry.py
"""A python module
that creates an empty
class
"""


class BaseGeometry():
    """An empty class
    called BaseGeometry
    """
    __count = 0
    def __init__(self):
        type(self).__count += 1
        self.count = BaseGeometry.__count

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not type(value) == int:
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        else:
            self.value = value
