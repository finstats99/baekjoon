n = int(input())

cum = []
for _ in range(n):
    i = int(input())
    if i == 0:
        a = cum.pop()
        # print('pop', a)
    else:
        cum.append(i)

print(sum(cum))