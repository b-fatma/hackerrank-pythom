"""
https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
"""

from itertools import product
 
K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = []
for X in product(*N):
    results.append(sum(c**2 for c in X)%M)
print(max(results))