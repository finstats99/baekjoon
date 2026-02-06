import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# 방문처리 리스트
visited = [False] * (n+1)

cnt = 0
def dfs(v):
    global cnt
    visited[v] = True

    for nxt in graph[v]:
        if visited[nxt] == False:
            cnt += 1
            dfs(nxt)
        
dfs(1)
print(cnt)