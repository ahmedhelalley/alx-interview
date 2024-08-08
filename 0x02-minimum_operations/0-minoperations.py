#!/usr/bin/python3
"""Defines function minOperations."""


def minOperations(n: int) -> int:
    """
        Calculates the fewest number of operations needed to
        result in exactly n H characters in the file..
    """

    if n <= 1:
        return 0

    operations_num = 0
    copied_chars = 0
    chars_num = 1

    while chars_num < n:
        if n % chars_num == 0:
            operations_num += 1
            copied_chars = chars_num

        operations_num += 1
        chars_num += copied_chars

    return operations_num
