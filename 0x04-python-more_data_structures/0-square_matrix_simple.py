#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_mat = []
    for i in matrix:
        new_mat.append([pow(j, 2) for j in i])
    return new_mat
