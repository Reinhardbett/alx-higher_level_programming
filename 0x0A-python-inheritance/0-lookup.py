#!/usr/bin/python3
'''Find available attributes and methods of an object
'''


def lookup(obj):
    '''Return list of available attributes and methods
    Args:
        1.obj: Any instance or class object
    Returns:
        1.list of obj attributes and method
    '''
    return dir(obj)
