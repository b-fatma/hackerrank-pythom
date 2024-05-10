"""
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
"""

a, b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.intersection(b)))
