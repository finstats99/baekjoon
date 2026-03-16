import sys

input = sys.stdin.readline

n = int(input())

graph = [input().rstrip() for _ in range(n)]
visited = [[False] * n for _ in range(n)]


    # 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1,1,  0, 0]

def dfs(x, y, cnt):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == '1':
            visited[nx][ny] = True
            cnt = dfs(nx, ny, cnt + 1)
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            ans.append(dfs(i, j, 1))

ans.sort()
print(len(ans))
for i in ans:
    print(i)