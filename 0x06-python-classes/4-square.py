#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        try:
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.size = size
        except TypeError:
            raise TypeError("size must be an integer")

    def size(self):
        return (size)

    def size(self, value):
        try:
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.size = value
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        try:
            return (self.size ** 2)
        except TypeError:
            raise TypeError("size must be an integer")
