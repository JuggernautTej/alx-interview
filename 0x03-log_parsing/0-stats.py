#!/usr/bin/python3
"""A script that reads stdin line by line and computes
the staus code and file size metrics"""

import sys
import signal
from collections import defaultdict

# Initialize holders
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

# Define status codes
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}


def print_stats():
    """This method prints the statistics collected"""
    print('File size: {}'.format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print('{}: {}'.format(code, status_code_counts[code]))


def signal_handler(sig, frame):
    """This method handles the keyboard interruption (Ctrl + C)
    signal gracefully"""
    print_stats()
    sys.exit(0)


# Set up the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from sys.stdin
for line in sys.stdin:
    line = line.strip()
    parts = line.split()

    # validate the log line format
    if len(parts) < 7 or not parts[-2].isdigit() or not parts[-1].isdigit():
        continue

    # Extract the status code and file size
    status_code = int(parts[-2])
    file_size = int(parts[-1])

    # validate status codes and count occurrences of each code
    if status_code in valid_status_codes:
        status_code_counts[status_code] += 1

    # aggregate file size and count the number of lines
    total_file_size += file_size
    line_count += 1

    # Print statistics for every 10 lines
    if line_count % 10 == 0:
        print_stats()

# run the statistics if Ctrl + C is not encountered
print_stats()
