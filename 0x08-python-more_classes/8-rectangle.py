#!/usr/bin/python3
"""
Create empty class for rectangle
"""


def check_value(value, t):
    """
    Function to check values
    t is the type, height or width
    """
    if not isinstance(value, int):
        if t:
            raise TypeError("width must be an integer")
        else:
            raise TypeError("height must be an integer")
    if value < 0:
        if t:
            raise ValueError("width must be >= 0")
        else:
            raise ValueError("height must be >= 0")
    return value


class Rectangle:
    """
    Class for rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = check_value(value, 1)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = check_value(value, 0)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join([sym * self.width for i in range(self.height)])

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle…")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
