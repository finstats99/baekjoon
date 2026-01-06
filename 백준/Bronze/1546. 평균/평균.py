N = int(input())

score = list(map(int, input().split()))

mean_score = sum(score)/len(score)
max_score = max(score)

for i in range(len(score)):
    score[i] = (score[i]/max_score) * 100

result = sum(score)/len(score)
print(result)