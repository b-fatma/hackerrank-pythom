"""
https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
"""

import re

def and_or(match):
    if match.group(0) == '||':
        return 'or'
    else:
        return 'and'

n = int(input())
for _ in range(n):
    s = input()
    print(re.sub(r"(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)", and_or, s))