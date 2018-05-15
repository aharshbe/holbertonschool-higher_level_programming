#!/usr/bin/python3
"""A class that inherits from a list"""


class MyList(list):
    """inherits another list's class
    Args:
        list: the class to be printed
    """
    def print_sorted(self):
        print(sorted(self))