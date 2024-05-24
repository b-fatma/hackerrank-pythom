"""
https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
"""

import numpy as np

print(np.polyval(np.array(input().split(), float), int(input())))