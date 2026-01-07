# n <= 3,000 -> O(N^2)까지 가능 -> for문 시도

def solution(n):
    
    return sum([i for i in range(1, n+1) if n % i == 0])