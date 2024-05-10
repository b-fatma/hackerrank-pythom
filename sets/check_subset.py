"""
https://www.hackerrank.com/challenges/py-check-subset/problem
"""

n = int(input())
for _ in range(n):
    a, b = [set(map(int, input().split())) for _ in range(4)][1::2]
    print(a.issubset(b))