"""
https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true
"""

a, b, m = [int(input()) for _ in range(3)]
# pow(a, b, m) = pow(a, b) mod m
print(pow(a, b), pow(a, b, m), sep='\n')
