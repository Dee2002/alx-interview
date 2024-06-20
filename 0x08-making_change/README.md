# Coin Change Problem

## Description

This project tackles the classic coin change problem using dynamic programming. The objective is to determine the minimum number of coins needed to make up a given total amount from a list of coin denominations. The solution is designed to be both correct and efficient, ensuring it meets the specified runtime constraints.

## Usage

To use the provided solution, ensure you have Python 3 installed on your system. The main function `makeChange(coins, total)` can be used to compute the minimum number of coins required to make the given total.

### Prototype
```python
def makeChange(coins, total):

Parameters

    coins: A list of integers representing the coin denominations.
    total: An integer representing the total amount to make.

Returns

    The fewest number of coins needed to meet the total.
    If the total is 0 or less, returns 0.
    If the total cannot be met by any number of coins, returns -1.

Example

python

#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

Requirements

    Python 3.4.3+
    All files should end with a new line.
    The first line of all files should be exactly #!/usr/bin/python3.
    Follow PEP 8 style guidelines (version 1.7.x).
    All files must be executable.

Repository Structure

css

.
├── 0-making_change.py
├── 0-main.py
└── README.md

How to run

Make sure all files are executable and run the main file to test the solution:

bash

chmod +x 0-main.py
./0-main.py
