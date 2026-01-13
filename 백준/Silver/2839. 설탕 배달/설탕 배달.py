import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
while True:
    if n%5 == 0:
        cnt = cnt + (n//5)
        break
    elif n < 0:
        cnt = -1
        break
    else:
        n -= 3
        cnt += 1



print(cnt)
