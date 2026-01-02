import sys 

N = int(sys.stdin.readline())

my_list = list(map(int, sys.stdin.readline().split()))
max_val = max(my_list)
min_val = min(my_list)

print(min_val, max_val)
