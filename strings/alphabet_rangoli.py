"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
"""

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    s = ''
    res = []
    for i in range(size):
        s = '-'.join(alphabet[i:size])
        res.append((s[::-1]+s[1:]).center(4*n-3, '-'))
    print('\n'.join(res[::-1] + res[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)