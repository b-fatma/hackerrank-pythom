"""
https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
"""

from collections import namedtuple

n = int(input())
Student = namedtuple('Student', list(input().split()))
marks = 0
for _ in range(n):
    s = input().split()
    student = Student(*s)
    marks += int(student.MARKS)
print(marks/n)
