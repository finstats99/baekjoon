import sys
from collections import deque
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



############## bfs
def bfs(v):
    queue = deque([v])
    visited[v] = True
    cnt = 0

    while queue:
        curr = queue.popleft()

        for nxt in graph[curr]:
            if visited[nxt] == False:
                visited[nxt] = True
                queue.append(nxt)
                cnt += 1

    return cnt


############## dfs
cnt = 0
def dfs(v):
    global cnt
    visited[v] = True

    for nxt in graph[v]:
        if visited[nxt] == False:
            cnt += 1
            dfs(nxt)
        
# dfs(1)
# print(cnt)

print(bfs(1))
