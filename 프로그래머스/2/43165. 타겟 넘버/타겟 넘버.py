def solution(numbers, target):
    n = len(numbers)
    
    def dfs(idx, summ):
        if idx == n: # 탈출 정의
            return 1 if summ == target else 0
        
        return dfs(idx + 1, summ + numbers[idx]) + \
                dfs(idx + 1, summ - numbers[idx])
    
    return dfs(0, 0)
        






def answer(numbers, target):
    # n은 사용할 수 있는 숫자의 총 개수입니다.
    n = len(numbers)
    
    def dfs(index, current_sum):
        # [탈출 조건] 모든 숫자를 다 사용했을 때
        if index == n:
            # 지금까지의 합이 타겟과 일치하면 1(정답)을, 아니면 0을 반환합니다.
            return 1 if current_sum == target else 0
        
        # [재귀 호출] 현재 숫자를 더하는 경우와 빼는 경우의 모든 정답 수를 합산합니다.
        # 이 과정이 반복되면서 모든 경우의 수를 탐색하게 됩니다.
        return dfs(index + 1, current_sum + numbers[index]) + \
               dfs(index + 1, current_sum - numbers[index])

    # 0번째 인덱스부터, 합계 0으로 탐색을 시작합니다.
    return dfs(0, 0)