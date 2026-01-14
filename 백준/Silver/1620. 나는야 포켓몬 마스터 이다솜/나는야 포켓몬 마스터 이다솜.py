import sys
input = sys.stdin.readline
n, m = map(int, input().split())


all = sys.stdin.read()
list_ = all.split()[:-m]
prob = all.split()[-m:]
dict_ = {}
for i in range(len(list_)):
    dict_[list_[i]] = i+1

for i in prob:
    if i.isdigit():
        print(list_[int(i)-1])
    else:
        print(dict_[i])
