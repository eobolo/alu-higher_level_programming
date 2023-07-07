#!/usr/bin/python3
i = 122
while i >= 97:
    number = None
    if i % 2 == 0:
        number = ord(chr(i))
    else:
        number = ord(chr(i)) - 32
    print("{0:c}".format(number), end="")
    i -= 1
