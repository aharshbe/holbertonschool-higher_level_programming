#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Check for object inheritence
    Args:
        obj: obhect to check
        a_class: class type to check
    """
    if (issubclass(type(obj), a_class) and type(obj) is not a_class):
        return (True)
    else:
        return (False)
