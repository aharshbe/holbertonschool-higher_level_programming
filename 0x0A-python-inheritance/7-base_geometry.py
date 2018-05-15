#!/usr/bin/python3
"""geometry module"""


class BaseGeometry:
    """geometry class"""
    def area(self):
        """method that has no content
        Raises:
            Excpetion: that it isn't implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate int value
        Args:
            name: name
            value: integer
        Raises:
            TypeError: for int check
            ValueError: if value < 0
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
