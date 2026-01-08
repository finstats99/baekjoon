import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(x):
    if x == 0:
        return 1
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans


print(int(factorial(n)/(factorial(k)*factorial(n-k))))