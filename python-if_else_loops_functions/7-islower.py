#!/usr/bin/python3
"""
def islower(c):
    if c >= 'a' and c <= 'z':
        return True
    else:
        return False
This could have worked but not all cases will be caught
"""


def islower(c):
    valueInt = ord(c)
    if valueInt >= 97 and valueInt <= 122:
        return True
    else:
        return False
