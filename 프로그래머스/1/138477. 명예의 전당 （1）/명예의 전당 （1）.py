def solution(k, score):
    answer= [] 
    honer = []
    cnt = 0
    for i in score:
        cnt += 1
        if len(honer) < k:
            honer.append(i)
            honer.sort()
            
        elif i > honer[0]:
            honer[0] = i
            honer.sort()
        
        if cnt < k:
            answer.append(honer[0])
        else:
            answer.append(honer[0])
             
    return answer