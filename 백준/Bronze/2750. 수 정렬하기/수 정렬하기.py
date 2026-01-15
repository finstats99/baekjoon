import sys 
n = int(input())
list_ = []
for _ in range(n):
    list_.append(int(input()))

list_.sort()
for i in list_:
    print(i)