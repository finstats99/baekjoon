import sys
input = sys.stdin.readline

N = int(input())

stack = [*map(int, sys.stdin.read().split())]
minimum, cnt = 0, 0
for i in stack[::-1]:
    if i > minimum:
        minimum = i
        cnt += 1

print(cnt)
