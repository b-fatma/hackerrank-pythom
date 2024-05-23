"""
https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
"""

import re

pattern = r"^[456][0-9]{3}(-?[0-9]{4}){3}$"

def no_consecutive_four_digits(s):
    s = s.replace('-', '')
    for i in range(12):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            return False
    return True
  
for _ in range(int(input())):  
    s = input()
    if bool(re.match(pattern, s)) and no_consecutive_four_digits(s):
        print('Valid')
    else:
        print('Invalid')