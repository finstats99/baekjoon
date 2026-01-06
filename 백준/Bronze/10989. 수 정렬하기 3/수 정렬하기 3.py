import sys
N = int(sys.stdin.readline())

result = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    result[num] += 1

# print(result)
for i in range(1, 10001):
    for _ in range(result[i]):
        print(i)