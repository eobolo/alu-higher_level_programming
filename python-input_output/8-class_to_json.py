#!/usr/bin/python3
# 8-class_to_json.py
"""This is a python file
that has a function taking
an object of a class then
does some serialization
"""


def class_to_json(obj):
    return obj.__dict__
