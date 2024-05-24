"""
https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
"""

import numpy as np
np.set_printoptions(legacy='1.13')

n, _ = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)

print(np.prod(np.sum(a, axis=0)), sep='\n')