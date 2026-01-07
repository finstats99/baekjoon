# 시간복잡도 : 자릿수 활용 -> O(logN) = 9

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

def another(n):
    answer = 0
    while n > 0:
        answer += n % 10  # 마지막 자릿수 합
        n //= 10          # 마지막 자릿수 제거
    return answer