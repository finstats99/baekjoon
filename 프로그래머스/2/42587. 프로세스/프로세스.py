from collections import deque

def solution(priorities, location):
    queue = deque(priorities) 
    num_que = deque(range(len(priorities)))
    
    cnt = 0    
    while True:
        curr = queue.popleft()
        curr_num = num_que.popleft()
        
        if len(queue) == 0:  # 마지막 원소가 추출 된 경우 
            cnt += 1         # 무조건 추출되니까 cnt + 1
            return cnt       # 원소 더 없어서 끝
        
        if curr < max(queue): # 추출된 프로세스가 queue의 최우선 값보다 작은 경우
            queue.append(curr) # queue에 다시 넣고
            num_que.append(curr_num) # 번호도 같은 진행
            
        else:                 # 추출된 프로세스가 queue의 최우선 값인 경우
            cnt += 1          # 프로세스 실행 cnt + 1
            print(f'else:',curr, curr_num)
            print(queue, num_que, cnt)
            if curr_num == location:   # 만약 location에 해당하는 프로세스가 실행된거면 
                return cnt             # 실행 번호 출력 & 끝
            
            else:
                pass
            
