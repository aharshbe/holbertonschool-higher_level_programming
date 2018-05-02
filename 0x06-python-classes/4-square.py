#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Returns size square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets value of square's size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size ** 2)
