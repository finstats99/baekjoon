import sys
input = sys.stdin.readline
num = int(input())


for _ in range(num):
    a = input().rstrip()
    if 6 <= len(a) <= 9:
        print('yes')
    else:
        print('no')