def solution(participant, completion):
    part_dict = {}
    for i in participant:
        part_dict[i] = 1 + part_dict.get(i, 0)
        
    for j in completion:
        if j in part_dict:
            part_dict[j] -= 1
    
    for key, val in part_dict.items():
        if val >= 1:
            return key
        else:
            pass
        
        
        
        
def another(participant, completion):
    from collections import Counter
    
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    