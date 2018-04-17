#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    len_of_arr = len(argv) - 1

    if (not len_of_arr):
        print("{} arguments.".format(len_of_arr))
    elif (len_of_arr == 1):
        print("{} argument:".format(len_of_arr))
    else:
        print("{} arguments:".format(len_of_arr))
    j = 1 if len_of_arr else 0
    for i in argv[1:]:
        if (j >= 1):
            print("{}: {}".format(j, i))
            j += 1
