#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def Sum():
        summation = 0
        length = len(sys.argv)
        if length == 1:
            print("{0:d}".format(summation))
            return 1
        for i in range(1, length):
            summation += int(sys.argv[i])
        print("{0:d}".format(summation))
        return 0
    Sum()
