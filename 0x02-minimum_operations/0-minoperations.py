#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to achieve n characters
using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve n characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operation
