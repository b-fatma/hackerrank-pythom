"""
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
"""

from collections import defaultdict

n, m = list(map(int, input().split()))
dic = defaultdict(list)
for i in range(1, n+1):
    x = input()
    dic[x].append(i)
for _ in range(m):
    x = input()
    if x in dic.keys():
        print(*dic[x])
    else:
        print(-1)