#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            num = 32
        else:
            num = 0
        print("{}".format(chr(ord(i) - num)), end="")
    print()
