def solution(participant, completion):
    part_dict = {}
    for i in participant:
        if i in part_dict:
            part_dict[i] += 1
        else:
            part_dict[i] = 1
        
    for j in completion:
        if j in part_dict:
            part_dict[j] -= 1
        else:
            pass
    
    for key, val in part_dict.items():
        if val >= 1:
            return key
        else:
            pass