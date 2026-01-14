import sys
input = sys.stdin.readline

n, k = map(int, input().split())

list_ = []
for _ in range(n):
    list_.append(int(input()))

list_ = sorted(list_, reverse = True)

cnt = 0
for i in list_:
    if i < k:
        cnt += k // i
        k %= i
    elif i == k:
        cnt += 1
        break
    elif i > k:
        pass
print(cnt)

