#!/usr/bin/python3
"""
Create empty class for rectangle
"""


def check_value(value, t):
    """
    Function to check values
    """
    e1w = "width must be an integer"
    e2w = "width must be >= 0"
    e1h = "height must be an integer"
    e2h = "height must be >= 0"

    if not isinstance(value, int):
        if t:
            raise TypeError(e1w)
        else:
            raise TypeError(e1h)
    if value < 0:
        if t:
            raise ValueError(e2w)
        else:
            raise ValueError(e2h)
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
