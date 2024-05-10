"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
"""

if __name__ == '__main__':
    dict_scores = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in dict_scores:
            dict_scores[score] = [name]
        else:
            dict_scores[score].append(name)
    scores = sorted(dict_scores.keys())
    names = dict_scores[scores[1]]
    [print(name, sep='\n') for name in sorted(names)]
    