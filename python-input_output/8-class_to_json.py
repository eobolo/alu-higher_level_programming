#!/usr/bin/python3
# 8-class_to_json.py
"""This is a python file
that has a function taking
an object of a class then
does some serialization
"""


import json


def class_to_json(obj):
    dumps = json.dumps(obj.__dict__)
    loads = json.loads(dumps)
    return loads
