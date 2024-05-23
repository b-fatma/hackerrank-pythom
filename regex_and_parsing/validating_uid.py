"""
https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true
"""

import re

def n_uppercase(s):
    return len(re.findall(r'[A-Z]', s))

def n_digits(s):
    return len(re.findall(r'[0-9]', s))
    
def unique_chars(s):
    return len(s) == len(set(s))
    
for _ in range(int(input())):
    s = input()
    pattern = r'^[a-zA-Z0-9]{10}$'
    if n_uppercase(s) >= 2 and n_digits(s) >= 3 and unique_chars(s) and bool(re.match(pattern, s)):
        print('Valid')
    else:
        print('Invalid')