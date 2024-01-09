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
        '''Return the JSON string representation
        Args:
            list_dictionaries (list): a list of dictionaries
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            json_object = json.dumps(list_dictionaries)
        return json_object

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON representation of list to a file
        Arg:
            1. list_objs (list): list of instances
        '''
        fname = cls.__name__ + ".json"
        with open(fname, 'w') as g:
            if list_objs is None:
                g.write("[]")
            NewList = [o.to_dictionary() for o in list_objs]
            g.write(Base.to_json_string(NewList))

    @staticmethod
    def from_json_string(json_string):
        '''Return list of json_string
        Arg:
            1. json_string (str): string for dictionaries list
        '''
        if json_string is None or json_string == "":
            return "[]"
        list_obj = json.loads(json_string)
        return list_obj

    @classmethod
    def create(cls, **dictionary):
        '''Return an instance with all attributes set
        Args:
            1. dictionary (dict): double pointer to dict
        '''
        if dictionary and dictionary != {}:
            x = cls(1, 1)
            x.update(**dictionary)
        return x
