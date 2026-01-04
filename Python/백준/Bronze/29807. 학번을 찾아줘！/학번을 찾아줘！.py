N = int(input())

score = list(map(int, input().split()))

score_list = [0, 0, 0, 0, 0]

for i in range(N):
    score_list[i] = score[i]

kor = score_list[0]
math = score_list[1]
eng = score_list[2]
exp = score_list[3]
fore = score_list[4]

if kor > eng :
    cond1 = abs(kor - eng) * 508
    # print(f"kor > eng ({kor} - {eng}) * 508 = {cond1}")
else :
    cond1 = abs(kor - eng) * 108
    # print(f"kor < eng ({kor} - {eng}) * 108 = {cond1}")

if math > exp :
    cond2 = abs(math - exp) * 212
    # print(f"math > exp ({math} - {exp}) * 212 = {cond2}")    
else :
    cond2 = abs(math - exp) * 305
    # print(f"math < exp ({math} - {exp}) * 305 = {cond2}")

cond3 = fore * 707

result = (cond1 + cond2 + cond3) * 4763

print(result)
