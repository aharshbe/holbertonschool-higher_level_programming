#!/usr/bin/python3
class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.size = size
        if (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter for position"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) is not 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int and type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return area"""
        return (self.size ** 2)

    def my_print(self):
        """print square"""
        if (not self.size):
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
