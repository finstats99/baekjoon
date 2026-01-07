# 시간복잡도 : O(NlogN) 까지 가능

def solution(t, p):
    len_p = len(p)
    
    answer = 0
    for i in range(len(t)-(len_p-1)):
        # print('탐색 대상 :', int(t[i:(i + len_p)]))
        if int(t[i:(i + len_p)]) <= int(p):
            answer += 1
    return answer



def another(t, p):
    m = len(p)
    count = 0
    for i in range(len(t) - m + 1):
        sub = t[i:i+m]
        if sub <= p:
            count += 1
            
    return count