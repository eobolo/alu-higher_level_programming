#!/usr/bin/python3
def uppercase(str):
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
