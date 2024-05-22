"""
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
"""

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    arr = []
    for i in range(n):
        if i <= 1:
            arr.append(i)
        else:
            arr.append(arr[i-1]+arr[i-2])
    return arr 

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))