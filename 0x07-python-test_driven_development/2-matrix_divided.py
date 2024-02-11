#!/usr/bin/python3
"""defines function to scalar divde matrix"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer, rounded to two decimal places"""
    sum = 0
    value = len(matrix[1])
    for i in matrix:
        if len(i) != value:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            sum += 1
            if type(j) is not float and type(j) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return result_matrix
