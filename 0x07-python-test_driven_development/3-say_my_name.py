#!/usr/bin/python3
'''The module returns a name with first name and last name
'''


def say_my_name(first_name, last_name=""):
    '''Print a name after checking if both inputs are strings
    Args:
        first_name(str): The first name input
        last_name(str): The last name input
    Raises:
        TypeError: if either inputs are not strings
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
