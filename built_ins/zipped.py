"""
https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
"""

n, x = map(int, input().split())
arr = []
for _ in range(x):
    arr.append(list(map(float, input().split())))
[print(sum(y)/x) for y in zip(*arr)]