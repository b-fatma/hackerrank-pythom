"""
https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
"""

K = int(input())
r = list(map(int, input().split()))
s1 = set()
s2 = set()
for a in r:
    if a not in s1:
        s1.add(a)
    else:
        s2.add(a)
[print(x) for x in s1.symmetric_difference(s2)]