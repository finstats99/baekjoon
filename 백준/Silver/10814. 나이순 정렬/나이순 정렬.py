import sys
input = sys.stdin.readline

n = int(input())

list_ = []
for _ in range(n):
    a, b = input().split()
    list_.append((a,b))

sorted_list = sorted(list_, key = lambda x:int(x[0]))
# print('\n'.join(sorted_list))
for i, j in sorted_list:
    print(i, j)