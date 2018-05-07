#!/usr/bin/python3
"""
Create empty class for rectangle
"""


def check_value(value, t):
    """
    Function to check values
    t is the type, height or width
    """
    if not isinstance(value, int):
        if t:
            raise TypeError("width must be an integer")
        else:
            raise TypeError("height must be an integer")
    if value < 0:
        if t:
            raise ValueError("width must be >= 0")
        else:
            raise ValueError("height must be >= 0")
    return value


class Rectangle:
    """
    Class for rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = check_value(value, 1)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = check_value(value, 0)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for i in range(self.height)])
