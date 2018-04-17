#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    vals = []
    for i in my_list:
        vals += [True] if (not i % 2) else [False]
    return vals
