"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
"""

import itertools

n = int(input())
mylist = input().split()
k = int(input())

comb = list(itertools.combinations(mylist, k))
print(len(list(itertools.filterfalse(lambda x: 'a' not in x, comb))) / len(comb))