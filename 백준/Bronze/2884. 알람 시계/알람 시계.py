a, b = map(int,input().split())


if b<45 :
    answer_m = b+15
    if a == 0:
        answer_h = 23
    else:
        answer_h = a-1
else :
    answer_m = b-45
    answer_h = a

print(answer_h, answer_m)