#!/usr/bin/python3
'''Manage the id attribute in all future classes
'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the JSON string representation of
        list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_object = json.dumps(list_dictionaries)
        return json_object
