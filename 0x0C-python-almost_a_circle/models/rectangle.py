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

    def display(self):
        ''' display the rectangle'''
        if (self.__y):
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            if (self.__x):
                for i in range(self.__x):
                    print(' ', end='')
            for i in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        string = "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" \
                + str(self.__y) + "- " + str(self.__width) + "/" \
                + str(self.__height) + ""
        return string

    def update(self, *args, **kwargs):
        ''' updates any arguments passed '''
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.__width = j
                if i == 2:
                    self.__height = j
                if i == 3:
                    self.__x = j
                if i == 4:
                    self.__y = j
        else:
            for i in kwargs:
                if i == "height":
                    self.__height = kwargs[i]
                if i == 'width':
                    self.__width = kwargs[i]
                if i == 'x':
                    self.__x = kwargs[i]
                if i == 'y':
                    self.__y = kwargs[i]
                if i == 'id':
                    self.id = kwargs[i]

    def to_dictionary(self):
        ''' return dictionary represenation'''
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
