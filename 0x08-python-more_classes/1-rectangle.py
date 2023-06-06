#!/usr/bin/python3
'''Create a Rectangle class with height and width
'''


class Rectangle:
    '''Define rectangle using private instance attributes
    height and width.
    Attributes:
        1.width
        2.height
    '''
    def __init__(self, width=0, height=0):
        '''Initialize private instance variables
        '''
        self.width = width
        self.height = height

    @property
    def height(self):
        '''
        Returns:
            1.height if successful
        Raises:
            1.TypeError:if height is not an integer
            2.ValueErrror: if height is less than zero
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        '''
        Returns:
            1.width if successful
        Raises:
            1.TypeError: if width is not an integer
            2.ValueError: if width is less than zero
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
