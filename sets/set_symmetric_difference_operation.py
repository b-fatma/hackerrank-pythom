"""
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
"""

a, b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.symmetric_difference(b)))
