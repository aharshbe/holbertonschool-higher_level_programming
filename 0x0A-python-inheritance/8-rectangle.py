#!/usr/bin/python3
"""a rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates a rectable
    Args:
        BaseGeometry: inherits from given class
    """
    def __init__(self, width, height):
        """initalizer method
        Args:
            width: width
            height: height
        Attributes:
            __width: private width
            __height: private height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
