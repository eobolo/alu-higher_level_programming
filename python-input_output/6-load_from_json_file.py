#!/usr/bin/python3
# 6-load_from_json_file.py
"""This is a python script that
deserializes a json serialized file
into the respective object it was serialized
from.
"""


import json


def load_from_json_file(filename):
    """This is a function
    that deserializes the json file
    using json.load after opening a file
    in text mode and setting the mode
    to reading
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
