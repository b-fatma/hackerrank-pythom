"""
https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
"""

a = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    inst, b = input().split()
    B = set(map(int, input().split()))
    eval(f"A.{inst}(B)")
print(sum(A))
