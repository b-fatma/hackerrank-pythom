"""
https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    for c in Counter(sorted(s)).most_common(3):
        print(*c) 