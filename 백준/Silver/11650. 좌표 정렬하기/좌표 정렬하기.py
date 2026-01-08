import sys
input = sys.stdin.readline

n = int(input())
list_ = []
for _ in range(n):
    a, b = map(int, input().split())
    list_.append((a,b))

sorted_list = sorted(list_, key = lambda x:(x[0], x[1]))
for i, j in sorted_list:
    print(i, j)