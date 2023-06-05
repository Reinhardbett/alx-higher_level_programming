#!/usr/bin/python3
'''python3 -c 'print(__import__("2-square").__doc__)'
Add limits to private instance variable
'''


class Square:
    '''python3 -c 'print(__import__("2.square").Square.__doc__)'
    Initialize public instance variable
    '''
    def __init__(self, size=0):
        '''python3 -c 'print(__import__("2-square").Square.init.__doc__)'
        Instantiation with optional size
        Args:
            1.size (int): side of a square
        Returns:
            1.TypeError: if size is not an integer
            2.ValueError: if size is less than 0
        '''
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
