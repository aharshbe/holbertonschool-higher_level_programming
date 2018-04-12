#!/usr/bin/python3
if (__name__ == '__main__'):
    from sys import argv
    j = 1
    len_of_arr = len(argv)
    if (len_of_arr == 1):
        print("0 arguments.")
    else:
        len_of_arr -= 1
        if (len_of_arr == 1):
            print("{} argument:".format(len_of_arr))
        else:
            print("{} arguments:".format(len_of_arr))
            for i in argv[1:]:
                print("{}: {}".format(j, i))
                j += 1
