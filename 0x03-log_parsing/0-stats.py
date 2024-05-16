#!/usr/bin/python3
import sys
import re
from collections import defaultdict

try:
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    for line in sys.stdin:
        match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', line)
        if match:
            status_code = match.group(2)
            size = int(match.group(3))
            total_size += size
            status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code, count in sorted(status_codes.items()):
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")
