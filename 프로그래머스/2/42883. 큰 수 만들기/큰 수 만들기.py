def solution(number, k):
    stack = []
    
    for num in number:
        # 1. 스택이 비어있지 않고
        # 2. 제거할 횟수(k)가 남아있고
        # 3. 스택의 마지막 숫자보다 현재 숫자가 더 크다면?
        while stack and k > 0 and stack[-1] < num:
            stack.pop() # 기존 숫자를 버림
            k -= 1      # 제거 횟수 차감
        
        stack.append(num)
        
    # 만약 k가 남아있는 경우 (예: "987", k=1) 뒤를 잘라줌
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)