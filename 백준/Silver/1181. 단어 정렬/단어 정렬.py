n = int(input())
str_list = []
for _ in range(n):
    str_list.append(str(input()))

str_list = list(set(str_list))
# print(str_set)
sorted_list = sorted(str_list, key = lambda x:(len(x), x))
for i in sorted_list:
    print(i)