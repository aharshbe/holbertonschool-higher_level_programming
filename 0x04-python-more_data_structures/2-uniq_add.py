#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    s = set(my_list)
    for i in s:
        j += i
    return j
