#!/usr/bin/python3
if  __name__ == '__main__':
    from add_0 import add
    b = a = 1
    b += 1
    print("{} + {} = {}".format(a, b, add(a, b)))
