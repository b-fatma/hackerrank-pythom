"""
https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
"""

_, num = (input(), input().split())
print(all([int(x) > 0 for x in num]) and any([j == j[::-1] for j in num]))