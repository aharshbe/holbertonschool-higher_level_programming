#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = a += 1
    print("{} + {} = {}".format(a, b, add(a, b)))
