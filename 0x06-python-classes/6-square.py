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
            self.__position = position

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

    @property
    def position(self):
        """Getter for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (type(self.__position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(__position) is not 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(self.__position[0]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(self.__position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return area size"""
        return (self.size ** 2)

    def my_print(self):
        """
        prints to the stdout square with # or empty line if 0
        """
        if (not self.size):
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.__position[0], "#" * self.size))
