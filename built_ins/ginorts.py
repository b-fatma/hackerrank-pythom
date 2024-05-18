"""
https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
"""

s = sorted(input())
lower = "".join([x for x in s if x.islower()])
upper = "".join([x for x in s if x.isupper()])
odd = "".join([x for x in s if x.isdigit() and int(x)%2==1])
even = "".join([x for x in s if x.isdigit() and int(x)%2==0])
print(lower, upper, odd, even, sep='')