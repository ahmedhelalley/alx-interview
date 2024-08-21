#!/usr/bin/python3
"""Defines validUTF8 function."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding..."""
    idx = 0
    while idx < len(data):
        if data[idx] <= 127:
            idx += 1
            continue

        if data[idx] & 0b11110000 == 0b11110000:
            idx = process_multi_byte(data, idx, 3)
        elif data[idx] & 0b11100000 == 0b11100000:
            idx = process_multi_byte(data, idx, 2)
        elif data[idx] & 0b11000000 == 0b11000000:
            idx = process_multi_byte(data, idx, 1)
        else:
            return False

        if idx == -1:
            return False

    return True


def process_multi_byte(data: List[int], idx: int, remaining_bytes: int) -> int:
    """Helper function to process multi byte characters."""
    while remaining_bytes != 0:
        idx += 1
        remaining_bytes -= 1

        if (idx >= len(data) or
                not bin(data[idx])[2:].zfill(8)[-8:].startswith('10')):
            return -1

    return idx + 1
