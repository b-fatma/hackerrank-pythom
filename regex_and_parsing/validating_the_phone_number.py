"""
https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
"""
import re

regex_pattern = r"^(7|8|9)\d{9}$"

for _ in range(int(input())):
    print('YES') if bool(re.match(regex_pattern, input())) else print('NO')