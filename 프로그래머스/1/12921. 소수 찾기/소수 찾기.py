def solution(n):
    cnt = 0
    
    def is_prime(x):
        for i in range(2, int(x**0.5) + 1):
            if x%i == 0:
                return False
        return True
    
    for i in range(2,n+1):
        if is_prime(i):
            cnt += 1
            
    return cnt
