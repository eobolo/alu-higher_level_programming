#!/usr/bin/python3
# 5-save_to_json_file.py
"""This is a python script that
convert complex data heirarchies
to json object and writes it to a file
with write permission
"""


import json


def save_to_json_file(my_obj, filename):
    """The function that opens a file for writing
    converts a complex data into json format based
    on the mode at which file was open either
    binary or text mode
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
