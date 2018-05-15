#!/usr/bin/python3
"""a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates a square
    Args:
        BaseGeometry: inherits from given class
    """
    def __init__(self, size):
        """initializer method
        Args:
            size: size
        Attributes:
            __size: private size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """return readable string for size
        Return:
            returns the string
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
