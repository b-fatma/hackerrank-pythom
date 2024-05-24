"""
https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
"""

import numpy

n, _ = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int) 
print(arr.transpose(), arr.flatten(), sep='\n')