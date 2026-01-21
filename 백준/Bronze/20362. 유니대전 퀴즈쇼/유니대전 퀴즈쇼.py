import sys
input = sys.stdin.readline

n, ans_peo = input().rstrip().split()
n = int(n)

cnt = 0
dict_ = {}
while True:
    peo, word = input().rstrip().split()
    if peo == ans_peo:
        if word not in dict_:
            print(0)
        else:
            print(dict_[word])

        break
    
    if word not in dict_:
        dict_[word] = 1
    else:
        dict_[word] += 1
