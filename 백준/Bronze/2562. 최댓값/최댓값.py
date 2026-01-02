import sys
input = sys.stdin.readline

my_list = []

for _ in range(9):
    my_list.append(int(input().rstrip()))

print(max(my_list))
print(my_list.index(max(my_list))+1)