#!/usr/bin/python3
i = 'a'
for i in range(ord('a'), ord('z') + 1):
    if (not (chr(i) == 'e' or chr(i) == 'q')):
        print("{}".format(chr(i)), end='')
