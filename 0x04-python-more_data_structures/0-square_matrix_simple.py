#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for k, i in enumerate(matrix):
        for l, j in enumerate(i):
            new_matrix[k][l] = j ** 2
    return new_matrix
