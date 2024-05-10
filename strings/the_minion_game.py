"""
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
"""

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
                
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)