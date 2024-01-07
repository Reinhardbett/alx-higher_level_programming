#!/usr/bin/python3
'''This module contains class Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Build a class Square that inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize the class properties
        Assign size to width and height of superclass
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

    def update(self, *args, **kwargs):
        '''Assign attributes from function calls
        '''
        if args or len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1
        elif kwargs or len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        '''Return dictionary representation
        Must contain id, size, x, y
        '''
        dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
        return dict
