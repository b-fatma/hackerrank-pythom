"""
https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))
A, B = [set(map(int, input().split())) for _ in range(2)]
h = 0
for x in array:
    if x in A:
        h += 1
    if x in B:
        h -= 1
print(h)
