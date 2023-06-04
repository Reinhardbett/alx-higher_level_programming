#!/usr/bin/python3
'''python3 -c 'print(__import__("1-square").__doc__)'
Define a class Square and include a private instance
attribute: size
'''


class Square:
    '''python3 -c 'print(__import__("1-square").Square.__doc__)'
    Represent a square
    '''
    def __init__(self, size):
        '''python3 -c 'print(__import__("1-square").Square.init.__doc__)'
        Initialize the instance variable size
        Args:
            size (int): The size of one side of our square
        '''
        self.__size = size
