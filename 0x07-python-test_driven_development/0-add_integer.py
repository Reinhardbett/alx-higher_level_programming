#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").__doc__)'
Args:
    1.a (int): a must be an integer
    2.b (int): b is initialized to 98
'''


def add_integer(a, b=98):
    '''python3 -c 'print(__import__("my_module").my_function.__doc__)'
    The function finds the addition of two integers
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is float:
        b = int(b)
    if type(a) is float:
        a = int(a)
    return (a + b)
