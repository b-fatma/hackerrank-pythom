"""
https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
"""

import numpy

n, _ = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')