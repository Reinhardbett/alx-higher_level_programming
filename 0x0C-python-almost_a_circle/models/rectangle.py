#!/usr/bin/python3
'''Build another class inheriting from base
'''
from models.base import Base


class Rectangle(Base):
    '''Assign properties to a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize new Rectangle
        Args:
            width(int): The width of the new Rectangle.
            height(int): The height of the new Rectangle.
            x(int): The x coordinate of the new Rectangle.
            y(int): The y coordinaate of the new Rectangle.
            id(int): The identity of the new Rectangle.
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''get width of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''get height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''get x coordinate of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''get y coordinate of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
