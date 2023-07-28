#!/usr/bin/python3
# 3-to_json_string.py
"""This is a python script that
serializes complex data heirarchies
using the json module
"""


import json


def to_json_string(my_obj):
    """This is the function that returns
    the serialized complex data in strings
    for better storage in file, data, or sent over
    to a network connection storage
    """
    return json.dumps(my_obj)
