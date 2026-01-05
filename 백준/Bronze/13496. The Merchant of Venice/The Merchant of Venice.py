K = int(input())


# 선박수(n), 선박속도(s), 계약 만기일수(d)
# 선박과 베니스 거리(di), 선박 적재량(vi)

for i in range(1, K+1):
    n, s, d = map(int, input().split())
    ans = 0
    print(f"Data Set {i}:")

    for _ in range(n):
        di, vi = map(int, input().split())
    
        if di <= d * s:
            ans += vi

    print(ans)
    print()
