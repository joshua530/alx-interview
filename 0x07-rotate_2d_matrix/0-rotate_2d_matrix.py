#!/usr/bin/python3
"""Contains 2d matrix 90 degrees clockwise rotation implementation"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n matrix 90 degrees clockwise"""
    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # rotate
    for i in range(len(matrix)):
        matrix[i].reverse()

    # left, right = 0, len(matrix) - 1

    # while left < right:
    #     for i in range(right - 1):
    #         top, bottom = left, right
    #         topLeft = matrix[top][left+i]
    #         matrix[top][left+i] = matrix[bottom-i][left]
    #         matrix[bottom-i][left] = matrix[bottom][right-i]

    #         matrix[bottom][right-i] = matrix[top+i][right]

    #         matrix[top+i][right] = topLeft
    #     left += 1
    #     right -= 1
