#!/usr/bin/python3
""" A method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file."""


def minOperations(n: int) -> int:
    """ A method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file..
    Args:
        n: the number of times the content of a file
        will be copied and pasted.

    Returns:
        The least amount of times the operations will
        be carried out as an int.
    """
    if n <= 0:
        return 0

    operations = 0

    divisibilator = 2

    while n > 1:
        while n % divisibilator == 0:
            operations += divisibilator
            n //= divisibilator
        divisibilator += 1

    return operations
