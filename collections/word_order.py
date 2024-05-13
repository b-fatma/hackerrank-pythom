"""
https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
"""

from collections import Counter

words = list()
for _ in range(int(input())):
    words.append(input())
words_counter = Counter(words)
print(len(words_counter.keys()), ' '.join(str(x) for x in words_counter.values()), sep='\n')