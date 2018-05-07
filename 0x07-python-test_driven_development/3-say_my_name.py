#!/usr/bin/python3
"""
    Print a name to stdout


"""


def say_my_name(first_name, last_name=""):
    """
        print a name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if (not last_name):
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
