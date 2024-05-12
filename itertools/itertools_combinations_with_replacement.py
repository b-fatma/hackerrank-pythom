"""
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
"""

from itertools import combinations_with_replacement

string, k = input().split()
k = int(k)

[print(''.join(x)) for x in list(combinations_with_replacement(sorted(string), k))]
