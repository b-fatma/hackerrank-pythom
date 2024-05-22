"""
https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=false
"""

import re

pattern = r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"
matches = re.findall(pattern, input())
if matches:
    [print(x) for x in matches]
else:
    print("-1")