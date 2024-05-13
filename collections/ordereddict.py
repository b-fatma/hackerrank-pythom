"""
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
"""

from collections import OrderedDict

od = OrderedDict()
for _ in range(int(input())):
    string = input().split()
    key, value = ' '.join(string[:-1]), int(string[-1])
    if key in od.keys():
        od[key] += value
    else:
        od[key] = value
[print(*x) for x in od.items()]