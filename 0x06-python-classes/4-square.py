#!/usr/bin/python3
'''python3 -c print'(__import__(4-square).__doc__)'
Access private attributes
'''


class Square:
    '''python3 -c print'(__import__(4-square).Square.__doc__)'
    '''
    def __init__(self, size=0):
        '''python3 -c print'(__import__(4.square).Square.init.__doc__)'
        Args:
            1. size (int): side of a square
        '''
        self.__size = size

    def area(self):
        '''python3 -c print'(__import__(4.square).Square.area.__doc__)'
        Returns:
            1. size * size if successful
        '''
        return self.__size * self.__size

    @property
    def size(self):
        '''python3 -c print'(__import(4.square).Square.size.__doc__)'
        Args:
            1.size (int): side of a square
            2.value (int): public attribute
        Returns:
            1. size if successful
        Raises:
            1.TypeError: if value is not an int
            2.ValueError: if value is less than 0
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
