#!/usr/bin/python3
'''
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    '''finds minimum number of operations'''
    if not isinstance(n, int) or n < 2:
        return 0

    best_ops = int(n / 1)  # current best number of operations
    total_ops = 1  # initialized to 1 for copying the very first character
    i = 1  # current position in the string
    best_i = 1  # i value that will give us the least number of operations

    while i < n:
        if n % i == 0 and n / i < best_ops:
            # we've found a new optimal number
            best_ops = int(n / i)
            total_ops += 2  # for the initial copy and paste operation
            best_i = i
        else:
            # just paste our current best
            total_ops += 1
        i += best_i
    return total_ops
