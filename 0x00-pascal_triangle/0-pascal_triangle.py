#!/usr/bin/python3
"""This is to define pascal_triangle function"""


def pascal_triangle(n):
    """Returns list of integer lists representing the Pascal's triangle"""

    if n <= 0:
        return []

    result = [[1]]

    for idx in range(n - 1):
        current_row = result[idx]
        current_row_length = len(current_row)

        new_row = []

        for idx2 in range(current_row_length - 1):
            if (current_row[idx2 + 1]):
                new_row.append(current_row[idx2] + current_row[idx2 + 1])

        new_row = [1] + new_row + [1]
        result.append(new_row)

    return result