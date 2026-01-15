def solution(A,B):
    # 각 list에서 최소값 * 최대값 수행. 
    # 이때 최소 최대의 idx를 활용한 pop으로 연산
    n = len(A)
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    
    return sum([A[i]*B[i] for i in range(n)])

