#!/usr/bin/python3
def remove_char_at(str, n):
    if (not n < 0):
        str2 = str[:n]
        n += 1
        str3 = str[n:]
        str2 += str3
        return (str2)
    else:
        return (str)
