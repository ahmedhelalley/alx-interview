#!/usr/bin/python3
"""Defines rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix by 90 degrees clockwise"""
    for i, row in enumerate(matrix):
        for j in range(i + 1, len(row)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        row.reverse()
