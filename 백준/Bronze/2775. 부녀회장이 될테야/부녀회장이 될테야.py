import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    n = int(input())
    k = int(input())
    floor = [i+1 for i in range(k)]
    # 1 2 3
    for _ in range(n):
        next_floor = [sum(floor[:j+1]) for j in range(k)]
        floor = next_floor
    print(next_floor[-1])