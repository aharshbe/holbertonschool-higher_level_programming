#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """create class
    Args:
        int: inherit int
    """
    def __init__(self, value):
        """initalize object with given value
        Args:
            value: int
        Attributes:
            __integer: private int
        """
        self.__integer = value

    def __eq__(self, num):
        """check if the size is equal
        Args:
            num: int
        Return:
            false if they are equal
        """
        return self.__integer != num

    def __ne__(self, num):
        """check if the size is not equal
        Args:
            num: int
        Return:
            false if they are not equal
        """
        return self.__integer == num

    def __str__(self):
        """return readable string
        Return:
            the string
        """
        return str(self.__integer)
