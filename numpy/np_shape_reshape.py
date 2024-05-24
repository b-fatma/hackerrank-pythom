"""
https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
"""

import numpy as np

arr = input().split()
print(np.reshape(np.array(arr, int), (3, 3)))
