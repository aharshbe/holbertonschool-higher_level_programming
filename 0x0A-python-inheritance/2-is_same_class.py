#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Determine object's class/match
    Args:
        obj: object to check
        a_class: type of class to check
    """
    if (type(obj) is a_class):
        return (True)
    else:
        return (False)
