from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n+ + 1)  
    dist[1] = 0
    
    queue = deque([1])
    
    while queue:
        curr = queue.popleft()
        
        for nxt in graph[curr]:
            if dist[nxt] == -1: # 아직 방문되지 않은 노드
                dist[nxt] = dist[curr] + 1 
                # dist[curr] : 현 시점 노드가 1번 노드에서 멀어진 거리
                # dist[nxt] : dist[curr]에서 거리 1 추가
                
                queue.append(nxt)
        
    ans = max(dist) 
    return dist.count(ans)
            










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