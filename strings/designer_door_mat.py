"""
https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
"""

n, m = map(int, input().split())
a=".|."
b="-"
for i in range(n//2):
    print(((2*i+1)*a).center(m, b))
print(("WELCOME").center(m, b))
for i in range(n//2):
    print((((2 * (n//2) - (2*i + 1)))*a).center(m, b))