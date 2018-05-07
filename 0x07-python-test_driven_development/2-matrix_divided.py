#!/usr/bin/python3
"""
    My calculation module


"""


def matrix_divided(matrix, div):
    """
        matrix_divided: divide all elements of a matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError("Each row of the matrix must have the same size")
    if len(matrix[0]) > len(matrix[1]) or len(matrix[0]) < len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = matrix[:]
    for k, j in enumerate(new_matrix):
        new_list = j[:]
        for i, m in enumerate(new_list):
            m = round(m / div, 2)
            new_list[i] = m
        new_matrix[k] = new_list
    return new_matrix
