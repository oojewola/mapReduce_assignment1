import sys
import re

for line in sys.stdin:
    line = line.strip()
    # Extract the IP address and hour from the log line
    match = re.search(r'(\d+\.\d+\.\d+\.\d+).*\[(\d+/\w+/\d+):(\d+):\d+:\d+.*\]', line)
    if match:
        ip = match.group(1)
        hour = match.group(3)
        print(f"{hour}-{str(int(hour)+1)}\t{ip}\t1}")
