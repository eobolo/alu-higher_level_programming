#!/usr/bin/python3
# 4-from_json_string.py
"""This is a python file thats
has a function for deserializing
json strings
"""


import json


def from_json_string(my_str):
    """This is a function
    that takes in an already serialized
    string and deserializes it using
    json.load() function
    """
    return json.loads(my_str)
