"""
https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
"""

for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code:", e)