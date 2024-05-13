"""
https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=false
"""

#!/bin/python3

import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_ = "%a %d %b %Y %H:%M:%S %z"
    ts1 = datetime.strptime(t1, format_)
    ts2 = datetime.strptime(t2, format_)

    return str(int(abs(ts1-ts2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
