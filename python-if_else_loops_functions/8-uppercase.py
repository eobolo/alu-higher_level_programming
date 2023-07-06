#!/usr/bin/python3
def uppercase(str):
    separator = "\n"
    if len(str) == 0:
        print("{}".format(separator), end=separator)
        return 1
    output = ""
    for i in range(0, len(str)):
        value = ord(str[i])
        separator = "\n"
        if i < len(str) - 1:
            separator = ""
        else:
            separator = "\n"
        if value < 97 or value > 122:
            output += chr(value)
            #print("{0:c}".format(value), end=separator)
        else:
            value = value - 32
            output += chr(value)
            #print("{0:c}".format(value), end=separator)
    print("{0:s}".format(output), end=separator)
    return 0
