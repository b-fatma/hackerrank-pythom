"""
https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
"""

import math
degree_sign = u'\N{DEGREE SIGN}'
ab, bc = [int(input()) for _ in range(2)][::1]
print(round(math.degrees(math.atan2(ab, bc))) ,degree_sign, sep='')