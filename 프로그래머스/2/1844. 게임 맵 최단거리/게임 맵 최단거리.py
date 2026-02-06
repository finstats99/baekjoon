from collections import deque

def solution(maps):
    # dx, dy 정의 : 상하좌우 (좌측상단이 (1, 1)임을 고려)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    queue = deque([(0, 0)])
    
    # 맵 크기 정의
    n = len(maps)
    m = len(maps[0])
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for j in range(4): # 상하좌우 이동
            nx = curr_x + dx[j]
            ny = curr_y + dy[j]
            # 이동한 nx, ny가 0~4 이내에 위치해야함.
            if 0<=nx<=n-1 and 0<=ny<=m-1 and maps[nx][ny] == 1:
                maps[nx][ny] = maps[curr_x][curr_y] + 1  # maps의 자리에 거리 표시
                queue.append((nx, ny))
        
    # 상대 팀 진영(우측 하단)의 값 확인 -> 도착한 경우 거리의 값으로 대체되어 있음
    answer = maps[n-1][m-1]
    
    # 도달할 수 없는 경우 값이 1 그대로이므로 -1 반환
    return answer if answer > 1 else -1




def ans(maps):
    # 맵의 크기 (n: 행, m: 열)
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 이동을 위한 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 생성 (시작 좌표 x, y)
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 맵 범위 안에 있고
            if 0 <= nx < n and 0 <= ny < m:
                # 2. 벽이 아니며(1) 처음 방문하는 곳이라면
                if maps[nx][ny] == 1:
                    # 현재 거리 + 1을 기록하고 큐에 삽입
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
    
    # 상대 팀 진영(우측 하단)의 값 확인
    answer = maps[n-1][m-1]
    
    # 도달할 수 없는 경우 값이 1 그대로이므로 -1 반환
    return answer if answer > 1 else -1