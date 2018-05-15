#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Check object again a_class
    Args:
        obj: object to check
        a_class: class type to check against
    """
    if (isinstance(obj, a_class)):
        return (True)
    else:
        return False
