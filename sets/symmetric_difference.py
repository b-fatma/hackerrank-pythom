"""
https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
"""

M = int(input())
a = set(map(int, input().split(' ')))
N = int(input())
b = set(map(int, input().split(' ')))
symmetric_diff = (a.union(b)).difference(a.intersection(b))
[print(x) for x in sorted(symmetric_diff)]
