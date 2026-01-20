def solution(people, limit):
    people.sort(reverse = True)
    # idx 활용
    left = 0
    cnt = 0
    right = len(people) - 1
    
    while left <= right: 
        ans = people[left] # 무거운 사람 1명 탑승
        
        if ans + people[right] <= limit: # 한명 더 태울 수 있을때 
            ans += people[right]  # 가벼운 사람 1명 탑승
            right -= 1  # 다음순번으로 이동
            left += 1
            cnt += 1
            
        elif ans + people[right] > limit: # 한명 더 못태울때
            left += 1
            cnt += 1
        
            
    return cnt


