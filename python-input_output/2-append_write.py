#!/usr/bin/python3
# 2-append_write.py
"""This is a python script
that appends to a file after
opening it for writing in text mode
"""


def append_write(filename="", text=""):
    """This is the function that opens a file
    for writing, If the file doesn’t exist, it should be created
    and appends to the file without overriding
    previous data
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num_char_append = f.write(text)
        return num_char_append
