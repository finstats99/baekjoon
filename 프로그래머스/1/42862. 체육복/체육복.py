def solution(n, lost, reserve):
    r_lost = set(lost) - set(reserve)
    r_reserve = set(reserve) - set(lost)
    lost_num = len(r_lost)
    # print(dir(r_lost))
    for i in r_reserve:
        if i-1 in r_lost:
            r_lost.discard(i-1)
            lost_num -= 1
        elif i+1 in r_lost:
            r_lost.discard(i+1)
            lost_num -= 1
            
    return n - lost_num