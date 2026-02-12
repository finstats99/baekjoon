n = int(input())

def solution(x):
    f1 = 1
    f2 = 1
    for _ in range(x-2):
        nxt = f1 + f2
        f1, f2 = f2, nxt
    return f2

print(solution(n))