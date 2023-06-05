#!/usr/bin/python3
'''python3 -c 'print(__import__("3-square").__doc__)'
Returns a square
'''


class Square:
    '''python3 -c 'print(__import__("3-square").Square.__doc__)'
    '''
    def __init__(self, size=0):
        '''python3 -c 'print(__import__("3-square").Square.init.__doc__)'
        Args:
            1. size (int): side of a square
        Raises:
            1. TypeError: if size is not an int
            2. ValueError: if size is less than 0
        '''
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''python3 -c 'print(__import("3-square").Square.area.__doc__)'
        Returns:
            1.size * size
        '''
        return self.__size * self.__size
