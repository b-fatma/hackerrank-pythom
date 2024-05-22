"""
https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
"""

import re

s, k = [input() for _ in range(2)]
pattern = f'(?={k})'
m = re.finditer(pattern, s)
[print(f'({x.start()}, {x.start() + len(k) -1})') for x in m]
if k not in s:
    print('(-1, -1)')