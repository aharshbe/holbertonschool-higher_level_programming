#!/usr/bin/python3
from models.rectangle import Rectangle
''' inherits rectangle class'''


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        ''' class constructor '''
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__x = x
        self.__y = y
        self.__size = size

    def __str__(self):
        ''' overload str method '''
        string = "[Square] (" + str(self.id) + ") " + str(self.__x) + "/" \
            + str(self.__y) + "- " + str(self.__size) + ""
        return string

    @property
    def size(self):
        ''' size getter'''
        return self.__size

    @size.setter
    def size(self, value=0):
        ''' setter for size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__size = value
