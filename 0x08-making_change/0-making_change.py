#!/usr/bin/python3
"""This script houses the function makeChange"""


def makeChange(coins, total):
    """This function determines the fewest number of coins needed
    to meet a given amount.
    Args:
        coins(List[int]): A list of the coins as integers
        total(int): The total amount that the coins should meet
    Returns:
        An integer of the fewest number of coins needed to meet
        total, zero (if total is zero or less), or -1 if the total
        cannot be met by the number of coins"""
    # if total <= 0:
    #     return 0
    # Initialize dynamic programming array with a large number
    arr = [total + 1] * (total + 1)
    # Initialize base case that no coins are needed to make amount 0
    arr[0] = 0
    # Iterate through all amounts from 1 to total
    for x in range(1, total + 1):
        # Check every coin in the list
        for coin in coins:
            # Update arr[x] to minimum no of coins needed if coin
            # value is less than or equal to current amount
            if coin <= x:
                arr[x] = min(
                    arr[x], arr[x - coin] + 1
                )
    # If arr[total] is still greater than total, total can't be met
    return arr[total] if arr[total] <= total else -1
