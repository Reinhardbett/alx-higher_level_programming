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
        Raises:
            TypeError: If either inputs is not an int
            ValueError: If either width/height is less or equal to zero
            ValueError: If either x/y is less than zero
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''get width of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''get height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''get x coordinate of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get y coordinate of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Return rectangle area
        '''
        return self.width * self.height

    def display(self):
        '''Print to stdout using character #'''
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        '''Return [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''Assign an argument to each attribute
        Follow the order of id, width, height, x, y
        '''
        if args or len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        elif kwargs or len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v
