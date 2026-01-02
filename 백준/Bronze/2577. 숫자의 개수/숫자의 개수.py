import sys 
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num = a * b * c
ans_step1 = str(num)
for i in range(10):
    print(ans_step1.count(f'{i}'))