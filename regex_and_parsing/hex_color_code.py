"""
https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
"""

import re

pattern = r"(?<=(:| ))(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(;|,|\))"

for _ in range(int(input())):
    m = re.findall(pattern, input())
    [print(x[1]) for x in m]