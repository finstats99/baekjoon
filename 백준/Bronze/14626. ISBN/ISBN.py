import sys

inp = sys.stdin.read().strip()
times_list = [1, 3]

cnt = 0
star_weight = 0

for i in range(len(inp)):
    if inp[i].isdigit():
        cnt += times_list[i % 2] * int(inp[i])
    else: 
        star_weight = times_list[i % 2]

for k in range(10):
    if (cnt + (k * star_weight)) % 10 == 0:
        print(k)
        break