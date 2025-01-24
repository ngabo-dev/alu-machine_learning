#!/usr/bin/env python3
"""
Module to perform matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.
    Args:
        mat1 (list of list of int/float): The first matrix.
        mat2 (list of list of int/float): The second matrix.
    Returns:
        list of list of int/float: The product of the two matrices.
        None: If the matrices cannot be multiplied.
    """
    # Validate matrix dimensions
    if len(mat1[0]) != len(mat2):
        return None

    # Perform matrix multiplication
    result = [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
        for row in mat1
    ]
    return result
