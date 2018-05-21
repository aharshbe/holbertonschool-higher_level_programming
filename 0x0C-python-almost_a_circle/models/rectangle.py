#!/usr/bin/python3
from models.base import Base
''' inherits from base class '''


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' inherit id from base '''
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x
        Base.__init__(self, id)

    @property
    def get_x(self):
        return self.__x

    @get_x.setter
    def set_x(self, value=0):
        self.x = value

    @property
    def get_y(self):
        return self.__y

    @get_y.setter
    def set_y(self, value=0):
        self.y = value
