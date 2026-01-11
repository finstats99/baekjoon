import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = input().split()
    for j in string:
        print(''.join(reversed(j)), end = ' ')
    print()
