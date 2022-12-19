#!/usr/bin/python3
def safe_print_integer(value):
    """ Print integers
    Args:
        value: what to print
    Returns:
        return true or false
    """
    try:
        print("{:d}".format(value))
    except Exception as error:
        return False
    else:
        return True
