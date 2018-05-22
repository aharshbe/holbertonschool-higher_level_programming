#!/usr/bin/python3
import json

''' This file creates a base class '''


class Base:
    ''' this is the base of all other files in the project'''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' init class, with argument none '''
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        ''' Convert to JSON string '''
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
