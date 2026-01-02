my_list = []
for _ in range(10):
    my_list.append(int(input()))

div_list = []
for i in my_list:
    div_list.append(i % 42)

print(len(set(div_list)))