"""
https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
pattern = r"(?<=[a-zA-Z])[^A-Za-z]+(?=[a-zA-Z])"
result = ''

pattern = r"(?<=[a-zA-Z])[^A-Za-z]+(?=[a-zA-Z])"
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))
print(re.sub(pattern, ' ', s))
