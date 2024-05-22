"""
https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
"""

regex_pattern = r"^M{0,3}(CM|D?C{0,3}|CD)(XC|L?X{0,3}|XL)(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))