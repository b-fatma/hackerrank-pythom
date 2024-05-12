"""
https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
"""

from itertools import groupby

string = input()

[print((len(list(g)), int(k)),end=' ') for k, g in groupby(string)]
