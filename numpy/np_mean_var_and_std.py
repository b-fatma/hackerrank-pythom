"""
https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
"""

import numpy as np

n, _ = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)

print(np.mean(a, axis=1), np.var(a, axis=0), round(np.std(a), 11), sep='\n')