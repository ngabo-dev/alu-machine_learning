#!/usr/bin/env python3
import numpy as np

def np_shape(matrix):
    return tuple(len(dim) for dim in matrix.shape)
