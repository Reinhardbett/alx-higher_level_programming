#!/usr/bin/python3
'''Print a square using the character '#'
'''


def print_square(size):
    '''Use the size input as the side of a square
    to print a square
    Args:
        size (int): The side of the square we will print
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is float and less than 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for i in range(size - 1):
            print('#', end="")
        print('#')
