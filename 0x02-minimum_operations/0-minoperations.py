#!/usr/bin/python3
"""
documentation of minimum operations
"""


def minOperations(n):
    """minioperations function"""
    if n == 1:
        return 0
    # Initialize min_ops with a large value
    min_ops = float('inf')
    # Iterate from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # Calculate number of operations for this factor
            min_ops = min(min_ops, i + minOperations(n // i))
    # If min_ops is not updated, it means n is a prime number
    # In that case, we can only achieve n by copying once and pasting n-1 times
    return min_ops if min_ops != float('inf') else n
