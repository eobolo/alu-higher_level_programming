#!/usr/bin/python3
def remove_char_at(string, n):
    __strcpy__ = ""

    for i in range(0, len(string)):
        if i == n:
            __strcpy__ += ""
        else:
            __strcpy__ += string[i]
    return __strcpy__
