#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    j = 1
    for i in argv[1:]:
        if int(i):
            j += int(i)
    j -= 1
    print("{}".format(j))
