"""
https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
"""

import re

pattern = r"([a-zA-Z0-9])\1+"
m = re.search(pattern, input())
print(m.group(1)) if m else print("-1")