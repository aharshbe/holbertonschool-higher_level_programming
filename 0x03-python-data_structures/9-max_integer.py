#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = 0
        for j in my_list:
            if (not a > j):
                a = j
        return a
    return
