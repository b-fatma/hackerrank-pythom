"""
https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
"""

from itertools import permutations

string, k = input().split()
k = int(k)

[print(''.join(x)) for x in sorted(list(permutations(string, k)))]