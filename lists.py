"""
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
"""

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        exp = input().split()
        if len(exp) == 3:
            eval("l." + exp[0] + "(" + exp[1]+ "," + exp[2] + ")")
        elif len(exp) == 2:
            eval("l." + exp[0] + "(" + exp[1]+ ")")
        elif exp[0] == 'print':
            print(l)
        else:
            eval("l." + exp[0] + "()")