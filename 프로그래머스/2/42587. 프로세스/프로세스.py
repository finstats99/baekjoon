from collections import deque

def solution(priorities, location):
    queue = deque(priorities) 
    num_que = deque(range(len(priorities)))
    
    cnt = 0    
    while True:
        curr = queue.popleft()
        curr_num = num_que.popleft()
        if len(queue) == 0:
            cnt += 1
            return cnt
        if curr < max(queue):
            queue.append(curr)
            num_que.append(curr_num)
            
        else:
            cnt += 1
            print(f'else:',curr, curr_num)
            print(queue, num_que, cnt)
            if curr_num == location:
                return cnt
            
            else:
                pass
            