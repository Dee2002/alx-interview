# 0x02. Minimum Operations

## Introduction
This project aims to implement a Python function to calculate the minimum number of operations needed to achieve a given number of characters using only "Copy All" and "Paste" operations.

## Requirements
- Allowed editors: vi, vim, emacs
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- The code should be documented
- The code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Files
- `0-minoperations.py`: Python script containing the implementation of the `minOperations` function.
- `0-main.py`: Main file for testing the `minOperations` function.

## Usage
To test the `minOperations` function, run the `0-main.py` script:

./0-main.py

## Example
```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

This will output:

Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
