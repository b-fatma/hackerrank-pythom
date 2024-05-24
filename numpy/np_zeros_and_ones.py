"""
https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
"""

import numpy

shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, dtype=int), numpy.ones(shape, dtype=int), sep='\n')
