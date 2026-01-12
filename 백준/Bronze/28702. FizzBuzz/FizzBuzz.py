def solution(x):
    if x % 3 == 0 and x % 5 == 0:
        return print('FizzBuzz')
    elif x % 3 == 0 and x % 5 != 0:
        return print('Fizz')
    elif x % 3 != 0 and x % 5 == 0:
        return print('Buzz')
    else:
        return print(x)

import sys
a, b, c = sys.stdin.read().split()

if a.isdigit():
    solution(int(a) + 3)
elif b.isdigit():
    solution(int(b) + 2)
else:
    solution(int(c) + 1)