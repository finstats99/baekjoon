def solution(n, times):
    min_times = 0
    max_times = max(times) * n
    ans = max_times
    
    while min_times <= max_times:
        mid = (min_times + max_times) // 2
        
        total_people = 0
        for t in times:
            total_people += mid // t # mid시간동안 심사 가능한 총 인원수 합
            if total_people >= n:
                break
            
        if total_people >= n:
            ans = mid
            max_times = mid - 1
            
        else:
            min_times = mid + 1
    return ans
