"""
https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=false
"""

import email.utils
import re

pattern = r"^<[A-Za-z][A-Za-z0-9\-_\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$"
for _ in range(int(input())):
    s = input()
    if bool(re.match(pattern, s.split()[-1])):
        print(email.utils.formataddr(email.utils.parseaddr(s)))