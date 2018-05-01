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
        """Returns size square"""
        return (size)

    def size(self, value):
        """Sets value of square's size"""
        try:
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.size = value
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """Return area of square"""
        try:
            return (self.size ** 2)
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Print square"""
        if (not self.size):
            for i in range(1):
                for i in range(1):
                    print("", end='')
            print()

        for i in range(self.size):
            for i in range(self.size):
                print("#", end='')
            print()
