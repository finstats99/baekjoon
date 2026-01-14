import sys
input = sys.stdin.readline

n = int(input())
w = int(input())

if n < 3:
    score = n*10
elif n<5:
    score = n*10 + 20
else:
    score = n*10 + 70

if w > 1000:
    score -= 15
if score < 0:
    score = 0

print(score)