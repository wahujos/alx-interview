#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regular expression pattern to match the log format
log_pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>.+?)\] '
    r'"GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)')

# Initialize metrics
total_size = 0
status_counts = defaultdict(int)
line_count = 0


def print_metrics(total_size, status_counts):
    """Function to print the metrics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        print(f"{status}: {status_counts[status]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            data = match.groupdict()
            status = int(data['status'])
            size = int(data['size'])

            # Update metrics
            total_size += size
            status_counts[status] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_metrics(total_size, status_counts)

except KeyboardInterrupt:
    pass
finally:
    print_metrics(total_size, status_counts)
