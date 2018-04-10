#!/usr/bin/python3
for i in range(1, 90, 11):
    for i in range(i, int(i / 10) * 10 + 10):
        if (i < 89):
            print("{:02d}, ".format(i), end='')
        else:
            print(i)
