#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise ValueError("size must be >= 0")
        elif (size < 0):
            raise TypeError("size must be an integer")
        else:
            self.__size = size
