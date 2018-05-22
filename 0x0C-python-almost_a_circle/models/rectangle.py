#!/usr/bin/python3
from models.base import Base
''' inherits from base class '''


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' inherit id from base '''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        Base.__init__(self, id)

    @property
    def x(self):
        ''' x getter'''
        return self.x

    @x.setter
    def x(self, value=0):
        ''' x setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = value

    @property
    def y(self):
        ''' y getter'''
        return self.y

    @y.setter
    def y(self, value=0):
        ''' y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = value

    @property
    def height(self):
        ''' height getter'''
        return self.height

    @height.setter
    def height(self, value=0):
        ''' height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value

    @property
    def width(self):
        ''' width getter'''
        return self.width

    @width.setter
    def width(self, value=0):
        ''' width setting'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def area(self):
        ''' return the area of the rectangle '''
        return self.__height * self.__width
