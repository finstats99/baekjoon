from itertools import permutations

def act(k, min_num, use):
    if k >= min_num:
        k -= use
        return int(k)
    return k

def solution(k, dungeons):
    
    count_list = []
    for loop in permutations(dungeons, len(dungeons)):
        
        remain_k = k
        count = 0
        
        for i, j in list(loop):
            past_k = remain_k
            remain_k = act(remain_k, i, j)

            if past_k > remain_k:
                count+=1

        count_list.append(count)
        
    return max(count_list)