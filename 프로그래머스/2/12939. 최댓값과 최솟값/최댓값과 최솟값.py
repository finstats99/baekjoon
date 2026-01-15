def solution(s):
    list_ = s.split()
    answer = []
    for i in list_:
        answer.append(int(i))
        
    answer.sort()
    
    return str(answer[0]) + ' ' + str(answer[len(answer)-1])