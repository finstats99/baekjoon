
import sys
input = sys.stdin.readline


n = int(input())
peo_list = []
for _ in range(n):
    (a, b) = map(int, input().split())
    peo_list.append((a, b))

grade_list = []
for i in range(len(peo_list)):
    cnt = 1
    for j in range(len(peo_list)):
        if peo_list[i][0] < peo_list[j][0] and peo_list[i][1] < peo_list[j][1]:
            cnt += 1
    
    grade_list.append(cnt)

print(*grade_list)