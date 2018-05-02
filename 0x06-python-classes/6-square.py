#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.size = size

        if (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    @property
    def size(self):
        """Returns size square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets value of square's size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def position(self):
        """Offset position of square"""
        return (self.position)

    def position(self, value):
        """Offset position of square"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(value[0]) is not int and type(value[1])) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

    def area(self):
        """Return area of square"""
        return (self.__size ** 2)

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
