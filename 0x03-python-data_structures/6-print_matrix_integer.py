#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for k, j in enumerate(matrix[i]):
            print("{:d}".format(j), end='')
            if (not k == len(matrix[i]) - 1):
                print(" ", end='')
        print("")
