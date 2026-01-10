import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

# print((v-a)/(a-b))
day = (v-a)/(a-b)
if v-a == 0:
    print(1)
else:    
    if day > int(day) :
        ans = int(day) + 1
    else: 
        ans = int(day)
    print(ans + 1)
