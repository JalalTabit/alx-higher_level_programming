import sys
import signal
from collections import defaultdict

# Define the status codes to track
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store the metrics
total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_metrics():
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) >= 7:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_size += file_size
        if status_code in status_codes:
            status_code_counts[status_code] += 1

    # Print metrics every 10 lines
    if line_count % 10 == 0:
        print_metrics()
