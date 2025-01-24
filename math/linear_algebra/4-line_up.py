#!/usr/bin/env python3
"""
Module to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.
    Args:
        arr1 (list of int/float): The first array.
        arr2 (list of int/float): The second array.
    Returns:
        list of int/float: A new array containing the element-wise sums.
        None: If the arrays are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
