def solution(sequence, k):
    n = len(sequence)
    left = 0
    current_sum = 0
    min_len = n + 1
    answer = [0, 0]
    
    for right in range(n):
        current_sum += sequence[right]
        
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1
            
        if current_sum == k:
            current_len = right - left
            if current_len < min_len:
                min_len = current_len
                answer = [left, right]
    return answer