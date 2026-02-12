import sys

def solve():
    n = int(sys.stdin.readline())
    
    # n이 0이나 1일 경우를 대비해 크기를 n+2 정도로 설정
    dp = [0] * (n + 2)
    
    # 초기값 설정
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    
    # 점화식 진행
    for i in range(2, n + 1):
        # 문제에서 요구한 1,000,000,007로 나눈 나머지 저장
        dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007
        
    print(dp[n])

solve()