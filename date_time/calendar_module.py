"""
https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
"""

from calendar import weekday, day_name

mm, dd, yyyy = list(map(int, input().split()))
print(day_name[weekday(yyyy, mm, dd)].upper())