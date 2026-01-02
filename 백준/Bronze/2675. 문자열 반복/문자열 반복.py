N = int(input())

for _ in range(N):
    num, sentence = input().split()
    num = int(num)

    sen_len = len(sentence)
    answer = ''
    for i in range(sen_len):
        for _ in range(num):
            answer += sentence[i]

    print(answer)