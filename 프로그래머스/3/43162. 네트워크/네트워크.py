def solution(n, computers):
    
    graph = [[] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
        
    # 방문 처리 리스트
    visited = [False] * n
    
    def dfs(v):  # 연결된 모든 노드에 대해 방문처리 하는 함수 dfs
        visited[v] = True
        for nxt in graph[v]:
            if visited[nxt] == False:
                dfs(nxt)
                
    ans = 0
    
    for i in range(n): # 모든 노드에 대해서
        if visited[i] == False: # 방문하지 않은 노드인 경우
            dfs(i)
            ans += 1
    
    return ans
