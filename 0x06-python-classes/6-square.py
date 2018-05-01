#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        try:
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.size = size
        except TypeError:
            raise TypeError("size must be an integer")
        try:
            if (position[0] < 0 or position[1] < 0):
                raise TypeError("position must be a tuple of"
                                "2 positive integers")
            else:
                self.position = position
        except TypeError:
            raise TypeError("position must be a tuple of"
                            "2 positive integers")

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

        horozontal = self.position[0]
        verticle = self.position[1]
        for i in range(self.size):
            while (verticle):
                print()
                verticle -= 1
            for i in range(self.size):
                while (horozontal):
                    print(" ", end='')
                    horozontal -= 1
                print("#", end='')
            horozontal = self.position[0]
            print()

    def position(self):
        """Offset position of square"""

    def position(self, value):
        """Offset position of square"""
        try:
            if (value[0] < 0 or value[1] < 0):
                raise TypeError("position must be a"
                                "tuple of 2 positive integers")
            else:
                self.position[0] = value[0]
                self.position[1] = value[1]
        except:
            print("some error")
