#!/usr/bin/python3
"""This script houses the pascal triangle function"""

"""
Algorithm
1- Declare empty list to store all rows.
2- Using for-loop that iterates through 0 to n+1,
append the sub-lists to the main list.
3- Append 1 to the main list (first element of
the triangle).
4- Intialize the sub-list to store current row.
5- Use a for-loop to construct the current row
in the triangle
6- Append the current value of n
7- The next value of n is calculated using a
binomial coefficient formula
8- Append the constructed row in the sub-list
to the main list.
9- Return the main list of rows representing
the Pascal's Triangle
"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing the Pascal's triangle of n rows.
    Args:
        n: the number of rows of the triangle

    Returns:
        A list of lists of integers.
    """
    main_list = []
    if n <= 0:
        return main_list

    for x in range(1, n + 1):
        n = 1
        sub_list = []
        for y in range(1, x + 1):
            sub_list.append(n)
            n = n * (x - y) // y
        main_list.append(sub_list)
    return main_list
