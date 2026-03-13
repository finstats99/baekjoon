def solution(tickets):
    tickets.sort()
    used = [False] * len(tickets)
    path = ['ICN']
    
    def dfs(curr):
        if len(path) == len(tickets) + 1:  # 모든 경로 탐색된 경우
            return True                   # 성공 반환(dfs종료)
        
        for i in range(len(tickets)):
            # 티켓 출발지가 현 curr값이고, 방문되지 않은 경우
            if curr == tickets[i][0] and used[i] == False:
                path.append(tickets[i][1]) # 티켓 도착지를 path에 추가
                used[i] = True
                
                if dfs(tickets[i][1]): # 재귀 호출 -> 다음 경로 탐색
                    return True        # 재귀 호출이 성공했다면 성공 반환, dfs 종료
                
                # 위에서 실패반환이 된 경우 재귀 호출이 되지않고 아래 적용됨(백트래킹)
                path.pop() # 마지막 추가된 tickets[i][1]제거
                used[i] = False # 방문표시 취소
        
        return False  # dfs 실패 반환, dfs 종료
        
    dfs('ICN') # ICN에서 path 탐색 시작
    return path