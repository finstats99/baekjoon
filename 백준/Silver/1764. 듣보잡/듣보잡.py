import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_hear = set([input().strip() for _ in range(n)])
n_see = set([input().strip() for _ in range(m)])


hear_see = n_hear - n_see

answer = n_hear - hear_see

print(len(answer))
for i in sorted(list(answer)):
    print(i)