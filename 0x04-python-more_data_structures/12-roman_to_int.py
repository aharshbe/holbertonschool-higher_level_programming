#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is str):
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        b = x = 0
        for p in roman_string:
            if (b < r[p]):
                x -= b * 2
            b = r[p]
            x += r[p]
        return x
    return 0
