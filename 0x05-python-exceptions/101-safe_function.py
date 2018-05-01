#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        val = fct(*args)
        return val
    except Exception as ERROR:
        stderr.write("Exception: {}\n".format(ERROR))
        return None
