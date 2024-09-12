#!/usr/bin/python3
"""This script hosues the rotate_rd_matrix function"""


def rotate_2d_matrix(matrix):
    """This method rotates a n x n 2D matrix by 90 degrees
    clokwise in-place.
    Args:
        matrix(List[List[int]]): The input n x n matrix
    Returns:
    None. The matrix is modified in-place."""
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse the matrix
    for i in range(n):
        matrix[i].reverse()
