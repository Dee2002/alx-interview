# 0x04. UTF-8 Validation

## Project Overview

This project involves creating a function to validate UTF-8 encoded data. The function will determine if a given list of integers represents a valid UTF-8 encoded sequence. UTF-8 encoding uses one to four bytes to encode characters, and the function must correctly identify and validate these sequences.

## Concepts Needed

### 1. Bitwise Operations in Python
Understanding bitwise operations like AND (`&`), OR (`|`), NOT (`~`), and shifts (`<<`, `>>`) is essential for manipulating bits and validating UTF-8 encoding rules.

### 2. UTF-8 Encoding Scheme
UTF-8 encoding rules specify how characters are encoded using one to four bytes. The encoding patterns are:
- **1-byte character**: 0xxxxxxx
- **2-byte character**: 110xxxxx 10xxxxxx
- **3-byte character**: 1110xxxx 10xxxxxx 10xxxxxx
- **4-byte character**: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

### 3. Data Representation
Handling data at the byte level involves working with the least significant bits of integers.

### 4. List Manipulation in Python
Iterating through lists and accessing elements is crucial for validating the encoding.

### 5. Boolean Logic
Logical operations are used to make decisions about the validity of the encoding.

## Function Requirements

- **Prototype**: `def validUTF8(data):`
- **Input**: A list of integers where each integer represents 1 byte of data.
- **Output**: `True` if the data is a valid UTF-8 encoding, otherwise `False`.

## Steps to Implement the Function

1. Initialize the number of bytes expected to be part of the current character to 0.
2. Iterate through each byte in the data.
3. Check the pattern of the leading byte to determine the number of bytes in the character.
4. Verify that each continuation byte starts with the bits `10xxxxxx`.
5. Return `False` if any invalid sequence is found; otherwise, return `True`.

## Code Implementation

Create a file `0-validate_utf8.py` with the following function:

```python
#!/usr/bin/python3
"""
Function to validate UTF-8 encoding
"""

def validUTF8(data):
    num_bytes = 0

    # Masks to check most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & num:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            # UTF-8 characters are 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the subsequent bytes start with 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
