def solution(routes):
    sorted_routes = sorted(routes, key = lambda x : x[0])
    
    before = sorted_routes[0]
    cnt = 1
    
    for i in range(1, len(sorted_routes)):
        now = sorted_routes[i]
        
        if before[0] <= now[0] <= before[1]: 
            if now[1] <= before[1]:
                before[1] = now[1]
            else:
                pass
            
        else :
            cnt += 1
            before = sorted_routes[i]
            
    return cnt
