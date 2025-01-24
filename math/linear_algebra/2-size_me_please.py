#!/usr/bin/env python3
"""
Module to calculate and print the shape of a matrix.
"""
def matrix_shape(matrix):
    """Calculates and prints the shape of a matrix."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    print(shape)
