#!/usr/bin/python3
"""This script houses the method for validates UTF-8 encoding"""


def validUTF8(data):
    """A method that determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        Data [int]: A list of integers.
    Returns:
        Boolean: True if it is """
    # Holder for number of bytes in the current UTF-8 character
    num_bytes = 0
    # Initialize checkers for the most significant bits
    check1 = 1 << 7
    check2 = 1 << 6

    for num in data:
        check = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8
            while check & num:
                num_bytes += 1
                check >>= 1
            # if 1 byte character (0xxxxxxx) or invalid (10xxxxxx)
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is of form 10xxxxxx
            if not (num & check1 and not (num & check2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
