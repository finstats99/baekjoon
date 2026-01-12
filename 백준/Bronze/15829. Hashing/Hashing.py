import sys
input = sys.stdin.readline

N = int(input())
r = 31
M = 1234567891
list_ = list(input().rstrip())

dict_ = {}
for i in range(26):
    dict_[chr(i+97)] = i + 1

def solution(x, i):
    return int(dict_[x]) * r ** i

ans = 0
for j in range(len(list_)):
    ans += solution(list_[j], j)

print(ans%M)