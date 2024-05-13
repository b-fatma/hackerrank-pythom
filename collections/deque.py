"""
https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
"""

from collections import deque

n = int(input())
dq = deque()
for _ in range(n):
    exp = input().split()
    if len(exp) == 2:
        eval("dq." + exp[0] + "(" + exp[1] + ")")
    else:
        eval("dq." + exp[0] + "()")
print(*dq)