#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        try:
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
