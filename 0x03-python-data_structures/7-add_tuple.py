#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = len(tuple_a)
    d = len(tuple_b)
    if (c < 2):
        tuple_a += (0, 0)
    if (d < 2):
        tuple_b += (0, 0)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new = (a, b)
    return new
