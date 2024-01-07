#!/usr/bin/python3
'''This module contains class Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Build a class Square that inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize the class properties
        Args:
            1. size (int): square's single side
            2. x (int): x coordinate of the square
            3. y (int): y coordinate of the square
            4. id (int): identifier for every instance
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Get size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''Return [Square] (<id>) <x>/<y> - <size>
        '''
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x, self.y, self.width))
