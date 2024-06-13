# Rotate 2D Matrix

## Description

This project implements an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. The algorithm leverages matrix transposition followed by row reversal to achieve the desired rotation without using additional memory for another matrix.

## Files

- `0-rotate_2d_matrix.py`: Contains the `rotate_2d_matrix` function that performs the matrix rotation.
- `main_0.py`: A test script to demonstrate the functionality of the `rotate_2d_matrix` function.

## Requirements

- Python 3.8.10
- No external libraries are required.
- Code must conform to the `pycodestyle` style guide (version 2.8.0).

## Function Description

### rotate_2d_matrix

```python
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.
    Args:
        matrix (list of list of int): The n x n matrix to be rotated.
    """

    Parameters:
        matrix: A list of lists of integers representing the n x n matrix.

    Returns: This function does not return anything. The matrix is modified in place.

Algorithm

    Transpose the Matrix:
        Iterate through the matrix and swap elements at positions (i, j) and (j, i) for all i < j.

    Reverse Each Row:
        Reverse the order of elements in each row using the reverse() method.

Example

Given the matrix:

python

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

After applying rotate_2d_matrix(matrix), the matrix becomes:

python

[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
