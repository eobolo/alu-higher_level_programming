#!/usr/bin/python3
# 1-write_file.py
"""This is a python file that
writes to a file, creates the file
if it doesn't exist, creates it, also
overwrites the content of the file if
it exists
"""


def write_file(filename="", text=""):
    """This is the function doing the
    creation of the file and writing into
    it and making sure a new line is
    appended to the end of the string
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        # if text[len(text) - 1] != "\n": text += "\n"
        num_char_written = f.write(text)
        return num_char_written
