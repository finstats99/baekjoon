N = int(input())

for _ in range(N):
    test = input()
    len_test = len(test)
    answer = 0
    score = 0
    for i in range(len_test):
        if test[i] == 'O':
            score += 1
            answer += score
            # print('if :', answer)
        else:
            score = 0
            # print('else :',answer)
    print(answer)