"""
https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
"""

from itertools import product

a, b = [set(map(int, input().split())) for _ in range(2)]
print(*product(a, b))