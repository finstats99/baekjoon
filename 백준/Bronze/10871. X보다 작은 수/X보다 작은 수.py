N, x = map(int, input().split())

A = list(map(int, input().split()))

answer = []
for i in range(N):
    if A[i] < x:
        answer.append(A[i])

print(*answer)