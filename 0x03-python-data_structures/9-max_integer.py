#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = my_list[0]
        for j in my_list:
            if (a > j):
                continue
            else:
                a = j
        return a
    return
