"""
https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
"""

from itertools import combinations

s, k = input().split()
for i in range(int(k)):
    print(*[''.join(x) for x in list(combinations(sorted(s), i+1))], sep='\n')