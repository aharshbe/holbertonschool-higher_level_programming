#!/usr/bin/python3

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
