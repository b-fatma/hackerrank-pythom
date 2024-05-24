"""
https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
"""

import numpy as np
np.set_printoptions(legacy='1.13')

a = np.array(input().split(), dtype='f')
print(np.floor(a), np.ceil(a), np.rint(a), sep='\n')