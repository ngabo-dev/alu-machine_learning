#!/usr/bin/env python3
"""
Module to calculate and return the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.
    Args:
        matrix (list of lists): The input 2D matrix.
    Returns:
        list of lists: The transposed matrix.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
