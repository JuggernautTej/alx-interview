#!/usr/bin/python3
"""This script implements the solution to the island
perimeter problem"""


def island_perimeter(grid):
    """This function returns the perimeter of an island in a grid.
    Args:
        grid(List[int])- a list of integers.
    Returns:
        The perimeter of the island as an integer."""
    # visit = set()

    # def dfs(i, j):
    #     """The recursive helper function taking in the
    #     coordinates of the grid.
    #     Args:
    #         i and j: integers representing the grid coordinates"""
    #     if i >= len(
    #         grid) or j >= len(
    #             grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
    #         return 1
    #     if (i, j) in visit:
    #         return 0

    #     visit.add((i, j))
    #     perim = dfs(i, j + 1)
    #     perim += dfs(i + 1, j)
    #     perim += dfs(i, j - 1)
    #     perim += dfs(i - 1, j)
    #     return perim
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j]:
    #             return dfs(i, j)
    perimeter = 0
    # Dimensions of grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    # Iterate through each cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Check if cell is land (1)
            if grid[x][y] == 1:
                # Check all four neighbours (up, down, left, right)
                # If the neighbour is water (0) or out of bounds,
                # add to perimeter
                # check up
                if x == 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                # check below
                if x == rows - 1 or grid[x + 1][y] == 0:
                    perimeter += 1
                # CHeck left
                if y == 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                # Check right
                if y == cols - 1 or grid[x][y + 1] == 0:
                    perimeter += 1
    return perimeter
