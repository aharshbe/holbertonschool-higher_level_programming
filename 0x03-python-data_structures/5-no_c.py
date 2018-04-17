#!/usr/bin/python3
def no_c(my_string):
    s = ''
    for j in my_string:
        if (j != 'C' and j != 'c'):
            s += j
    return s
