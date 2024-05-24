"""
https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
"""

import numpy as np
np.set_printoptions(legacy='1.13')

n, _ = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)

print(np.max(np.min(a, axis=1)), sep='\n')