#!/usr/bin/python3
'''Manage the id attribute in all future classes
'''


class Base:
    '''Keep track of all other class instances
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Assign id the new value or the initialized count
        '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
