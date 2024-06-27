# 0x09. Island Perimeter

## Description

This project focuses on calculating the perimeter of an island in a grid. The grid is represented as a 2D array of integers where:
- `0` represents water
- `1` represents land

Each cell in the grid is a square with a side length of 1. The cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is only one island (or none). The island does not have "lakes" (water inside that isn't connected to the water surrounding the island).

## Requirements

- Python 3.4.3 or higher
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7)
- No module imports are allowed
- All modules and functions must be documented
- All files must be executable

## Files

### 0-island_perimeter.py

Contains the function `island_perimeter(grid)` which calculates the perimeter of the island described in the grid.

### 0-main.py

A test file to verify the functionality of the `island_perimeter` function.

## Usage

To test the `island_perimeter` function, you can run the `0-main.py` file:

```sh
./0-main.py

Example

Given the grid:

csharp

[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

The output will be:

12

Function Documentation
island_perimeter(grid)

Returns the perimeter of the island described in grid.

    grid is a list of lists of integers:
        0 represents water
        1 represents land
        Each cell is square with a side length of 1
        Cells are connected horizontally/vertically (not diagonally)
        The grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or none)
    The island does not have "lakes" (water inside that isn't connected to the water surrounding the island)

Example:

python

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

Author

    Delsa Marasha