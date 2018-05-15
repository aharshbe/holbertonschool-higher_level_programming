#!/usr/bin/python3


def lookup(obj):
    """return the list of attributes & methods
    Args:
        obj: input object
    """
    return (list(i for i in dir(obj)))
