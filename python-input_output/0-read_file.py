#!/usr/bin/python3
# 0-read_file.py
"""This is a python file that
opens a file for reading and
prints to the standard output
"""


def read_file(filename=""):
    """This function reads a filename
    using the key word arguement filename
    and encodes in utf-8 opens in textmode
    and prints data to standard output
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
