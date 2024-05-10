"""
https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
"""

n = int(input())
myset = set()
for _ in range(n):
    myset.add(input())
print(len(myset))
