"""
https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
"""

A = set(map(int, input().split()))
superset = True
for _ in range(int(input())):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        superset = False
        break
print(superset)