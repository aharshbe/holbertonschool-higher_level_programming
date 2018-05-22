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

    def update(self, *args, **kwargs):
        ''' updates any arguments passed '''
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.__size = j
                if i == 2:
                    self.__x = j
                if i == 3:
                    self.__y = j
        else:
            for i in kwargs:
                if i == "size":
                    self.__size = kwargs[i]
                if i == 'x':
                    self.__x = kwargs[i]
                if i == 'y':
                    self.__y = kwargs[i]
                if i == 'id':
                    self.id = kwargs[i]

    def to_dictionary(self):
        ''' return dictionary represenation'''
        return {'id': self.id, 'size': self.__size,
                'x': self.__x, 'y': self.__y}
