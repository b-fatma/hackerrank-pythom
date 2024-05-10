"""
https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
note: works wih PyPy3 and not python3
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))