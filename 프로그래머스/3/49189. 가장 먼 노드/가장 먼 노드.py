from collections import deque


def solution(n, vertex):
    
    sort_vertex = sorted(vertex, key = lambda x:x[0])
    graph = [[] for _ in range(n+1)]
    visited = [False] * len(range(n+1))
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
                
    queue = deque([1])
    visited[1] = True
    ans = [0] * len(range(n+1))
    
    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                ans[i] = ans[curr] + 1
    
    max_val = max(ans)
    answer = 0
    for num in ans:
        if num == max_val:
            answer += 1
    return answer
    
    






def answer(n, vertex):
    graph = [[] for _ in range(n + 1)]
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)  # 양방향 간선이므로 양쪽에 추가
        
    # 2. 거리 기록용 배열 초기화
    # -1은 아직 방문하지 않았음을 의미함
    distance = [-1] * (n + 1)
    distance[1] = 0  # 출발 노드(1번)의 거리는 0
    
    # 3. BFS 수행
    queue = deque([1])  # 1번 노드에서 시작
    
    while queue:
        current_node = queue.popleft()
        
        for next_node in graph[current_node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current_node] + 1
                queue.append(next_node)

    max_dist = max(distance)
    return distance.count(max_dist)