N = int(input())
str_N = str(N)

sum_num = 0
N_digit = len(str_N) # 자릿수

start = N - 9 * N_digit

if start < 1:
    start = 1

result = 0
for sec_num in range(start, N):
    sum_sec_num = 0
    temp = sec_num  # sec_num의 사본

    while temp > 0:
        sum_sec_num += temp % 10
        temp //= 10

    if sec_num + sum_sec_num == N:
        result = sec_num
        break

print(result)