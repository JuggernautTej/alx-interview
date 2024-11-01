#!/usr/bin/python3
"""This script determines the winner of each game of
the prime game.

Algorithm:
1. Prime Calculation and Multiples Removal Simulation:
   Use the Sieve of Eratosthenes to identify prime numbers
    up to the largest value of n in the nums list. This allows
    to efficiently identify prime numbers for any round without
    recalculating for each n.
2. Game Simulation:
    - For each game round, initialize a counter for moves, starting with Maria.
    - Simulate the game by iterating through the prime numbers.
        - For each prime, check if it can be selected from the remaining set
        (i.e., it hasn't been removed).
        - If it can be selected, increase the move counter by 1 and mark all
        multiples of that prime as removed.
    - When there are no more primes that can be selected, the game ends.
    - Determine the winner based on who made the last move (odd moves indicate
    Maria won, even moves indicate Ben won).
3. Game Summary:
    - Count the number of rounds each player won.
    - Compare the counts to determine the overall winner across all rounds, or
    return None if the count is tied.
"""


def isWinner(x, nums):
    """The main function to determine the winner of the
    prime game.
    Args:
        x: the number of rounds in the game as an integer.
        nums: an array of n.
    Returns:
        The winner of the game as a string"""
    def sieveOfE(n):
        """The helper function to get the prime numbers
        Args:
            n: the integer as the upper limit of the range of numbers from 1
        Returns:
            A list of booleans where True
        indicates a prime number."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, n + 1, i):
                    primes[multiple] = False
        return primes
    max_n = max(nums)
    prime_flags = sieveOfE(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        move_count = 0
        numbers = [True] * (n + 1)

        for p in range(2, n + 1):
            if prime_flags[p] and numbers[p]:
                move_count += 1
                for multiple in range(p, n + 1, p):
                    numbers[multiple] = False
        # To determine the winner of this round based on who made the last move
        if move_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    # To determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
