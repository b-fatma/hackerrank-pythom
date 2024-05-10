"""
https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
"""

import textwrap

def merge_the_tools(string, k):
    substrings = [''.join(set(x)) for x in textwrap.wrap(string, k)]
    print('\n'.join(substrings))


def merge_the_tools_(string, k):
    substrings = []
    for i in range(0, len(string), k):
        substring = ''
        for j in range(k):
            char = string[i+j]
            if char not in substring:
                substring += char
        substrings.append(substring)     
    print('\n'.join(substrings))
        
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)