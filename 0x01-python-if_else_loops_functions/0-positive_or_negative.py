#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def check_no(number):
    """Prints  whether number is negative, positive, or zero"""
    if number > 0:
        print("{:.0f} is positive".format(number))
    elif number == 0:
        print("{:.0f} is zero".format(number))
    elif number < 0:
        print("{:.0f} is negative".format(number))


check_no(number)
