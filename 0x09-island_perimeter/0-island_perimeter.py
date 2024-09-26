#!/usr/bin/python3
"""This script implements the solution to the island
perimeter problem"""


def island_perimeter(grid):
    """This function returns the perimeter of an island in a grid.
    Args:
        grid(List[int])- a list of integers.
    Returns:
        The perimeter of the island as an integer."""
    visit = set()

    def dfs(i, j):
        """The recursive helper function taking in the
        coordinates of the grid.
        Args:
            i and j: integers representing the grid coordinates"""
        if i >= len(
            grid) or j >= len(
                grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0

        visit.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)
        return perim
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
