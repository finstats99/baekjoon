def solution(n, m, section):
    cnt = 0
    sector = 0
    
    for i in section:
        if m == 1:
            if i > sector:
                cnt += 1
                sector = i
        else:
            if i > sector:
                cnt += 1
                sector = i + m -1  
        
    return cnt
