N = int(input())

my_list = input().split()
int_list = []

for i in range(len(my_list)) :
    int_list.append(int(my_list[i]))

max_val = max(int_list)
min_val = min(int_list)

print(min_val, max_val)