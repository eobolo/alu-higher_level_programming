#!/usr/bin/python3
# 7-add_item.py
"""This python script
loads, adds, and save
new elements to a json list
serialized format
"""


import os
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
with open(filename, mode="a", encoding="utf-8"):
    pass
if os.path.getsize(filename) > 0:
    list_data = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        list_data.append(sys.argv[i])
    save_to_json_file(list_data, filename)
else:
    list_data = []
    for i in range(1, len(sys.argv)):
        list_data.append(sys.argv[i])
    save_to_json_file(list_data, filename)
