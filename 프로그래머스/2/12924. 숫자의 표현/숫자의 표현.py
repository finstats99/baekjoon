def solution(n):
    left = 1
    right = 1
    current_sum = 1
    cnt = 0
    
    while left <= n:
        if current_sum < n:
            right += 1
            current_sum += right
        elif current_sum > n:
            current_sum -= left
            left += 1
        else: # current_sum == n
            cnt += 1
            current_sum -= left
            left += 1
            
    return cnt