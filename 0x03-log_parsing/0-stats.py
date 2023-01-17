#!/usr/bin/env python3
'''
computes metrics using log formatted input from stdin
'''

import re
import sys
import signal


log_format = (
    r'^([0-9]{1,3}\.){3}([0-9]{1,3}) - \[[0-9]{4}-[0-9]{2}-[0-9]{2} '
    r'[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]+\] "GET /projects/260 HTTP/1.1"'
    r' ([2-5]0[01345]) ([1-9][0-9]?[0-9]?[0-4]?)$'
)

total_file_size = 0
pos = 0
status_code_count = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}


def print_stats(sig=None, frame=None):
    '''prints required log stats'''
    print('File size: {}'.format(total_file_size))
    keys = sorted(status_code_count.keys())
    for i in range(len(keys)):
        if status_code_count[keys[i]] != 0:
            print('{}: {}'.format(keys[i], status_code_count[keys[i]]))


signal.signal(signal.SIGINT, print_stats)

for line in sys.stdin:
    pos += 1
    matches = re.match(log_format, line)
    if matches:
        status_code = matches.group(3)
        file_size = matches.group(4)
        status_code_count[status_code] += 1
        total_file_size += int(file_size)
    if pos != 0 and pos % 10 == 0:
        print_stats()
