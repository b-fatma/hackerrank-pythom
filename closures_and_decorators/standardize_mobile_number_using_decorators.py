"""
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
"""

def wrapper(f):
    def fun(l):
        # complete the function
        for i in range(len(l)):
            l[i] = l[i][-10:]
            l[i] =  '+91 ' + str(l[i][:-5]) + ' ' + str(l[i][-5:])
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 