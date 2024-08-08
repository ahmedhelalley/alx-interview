# Project: 0x02. Minimum Operations.

## Tasks

**[0-minoperations.py](./0-minoperations.py)**


In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0

***Example***:

Consider the case where `n = 9`:

1. Initial State: H
2. Copy All => Paste => HH
3. Paste => HHH
4. Copy All => Paste => HHHHHH
5. Paste => HHHHHHHHH

Number of operations: 6

