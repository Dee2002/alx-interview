# 0x03. Log Parsing

This project contains scripts for generating and parsing log files.

## Files

- `0-generator.py`: This script generates log lines and writes them to standard output. Each line has the format `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`.
- `0-stats.py`: This script reads log lines from standard output, parses them, and computes metrics. After every 10 lines and/or a keyboard interruption (CTRL + C), it prints the total file size and the number of lines by status code.

## Usage

Run the generator script and pipe its output to the stats script:

```bash
./0-generator.py | ./0-stats.py
