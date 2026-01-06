# 시간복잡도 : n은 1000 이하 자연수 -> O(N^2) 1000^2 = 1,000,000  까지 가능
# 사용할 시간 복잡도 : if return -> O(N)

def solution(x, n):
    return [x*i for i in range(1, n+1)]