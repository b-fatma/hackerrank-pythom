"""
https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
"""

from collections import deque

dq = deque()
for _ in range(int(input())):
    n = int(input())
    dq = deque(list(map(int, input().split())))
    flag = 'Yes' 
    while(len(dq) > 1):
        if dq[0] <= dq[-1]:
            x = dq.pop() 
        else:
            x = dq.popleft()
        if x < max(dq[0], dq[-1]):
            flag = 'No'
            break
    print(flag)