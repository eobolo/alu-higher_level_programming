#!/usr/bin/python3
"""
This was my first function that was doing
the worst special case an empty string ""

def uppercase(str):
    if len(str) == 0:
        return "\n"
    for i in range(0, len(str)):
        value = ord(str[i])
        separator = "\n"
        if i < len(str) - 1:
            separator = ""
        else:
            separator = "\n"
        if value < 97 or value > 122:
            print("{0:c}".format(value), end=separator)
        else:
            value = value - 32
            print("{0:c}".format(value), end=separator)
    return 0
"""


def uppercase(str):
    if len(str) == 0:
        print("\n")
        return 1
    output = ""
    for i in str:
        value = ord(i)
        if value < 97 or value > 122:
            output += "{0:c}".format(value)
        else:
            value = value - 32
            output += "{0:c}".format(value)
    print(output)
    return 0
