"""
https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
"""

from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))
total = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size]:
        total += price
        shoes[size] -= 1
print(total)