#!/usr/bin/python3


'''Create a Rectangle class with height and width
'''


class Rectangle:
    '''Define rectangle using private instance attributes
    height and width.
    Attributes:
        1.width
        2.height
        3.number_of_instances
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize private instance variables
        & increment public class attribute
        '''
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def area(self):
        '''Return area of rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Return perimeter of rectangle unless
        width or height is 0
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        '''Print rectangle with '#' and return string
        representation to end user
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        '''Return a string representation or Rectangle
        object which can be parsed by Python interpreter
        using eval()
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Print a string after using the destructor del
        & decrement number_of_instances
        '''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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
