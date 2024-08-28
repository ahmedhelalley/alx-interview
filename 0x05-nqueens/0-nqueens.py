#!/usr/bin/python3
"""Defines 0-nqueens module"""

import sys


def nqueens(n):
    """Solve nqueens problem"""
    board = []
    columns = []
    solve_nqueens(n, 0, columns, board)
    return board


def solve_nqueens(n, row, col_placements, board):
    """Find the valid colmun replacements"""
    if (row == n):
        row_in_borad = []
        for idx in range(len(col_placements)):
            row_in_borad.append([idx, col_placements[idx]])

        board.append(row_in_borad)
    else:
        for col in range(n):
            col_placements.append(col)
            if is_valid(col_placements):
                solve_nqueens(n, row + 1, col_placements, board)

            col_placements.pop()


def is_valid(col_placements):
    """Validate column"""
    row_id = len(col_placements) - 1
    for idx in range(row_id):
        diff = abs(col_placements[idx] - col_placements[row_id])
        if diff == 0 or diff == row_id - idx:
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    n = sys.argv[1]

    if (not n.isdigit()):
        print('N must be a number')
        sys.exit(1)

    if (int(n) < 4):
        print('N must be at least 4')
        sys.exit(1)

    result = nqueens(int(n))

    for row in result:
        print(row)
