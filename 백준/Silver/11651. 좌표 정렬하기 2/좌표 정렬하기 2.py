import sys
input = sys.stdin.readline

N = int(input())
list_ = []
for _ in range(N):
    a, b = map(int, input().split())
    list_.append((a, b))

# print(list_)
sorted_list = sorted(list_, key = lambda x: (x[1], x[0]))
for j in range(len(sorted_list)):
    print(sorted_list[j][0], sorted_list[j][1])