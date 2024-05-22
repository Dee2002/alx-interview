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
