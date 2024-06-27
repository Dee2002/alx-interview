#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    :param grid: List of lists of integers representing the grid.
    :return: Integer perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:  # Check top
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # Check bottom
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # Check right
                    perimeter -= 1

    return perimeter
