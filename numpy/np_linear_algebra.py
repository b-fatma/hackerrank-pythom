"""
https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
"""

import numpy as np

n = int(input())

a = np.array([np.array(input().split(), float) for _ in range(n)])

print(round(np.linalg.det(a), 2))