#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
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
