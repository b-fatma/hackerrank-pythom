"""
https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
"""

from cmath import phase

x = complex(input())
print(abs(x), phase(x), sep='\n')
