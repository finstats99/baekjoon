my_list = list(map(int, input().split()))
asc_list = list(range(1, 9))
des_list = list(range(8, 0, -1))

if my_list == asc_list :
    print('ascending')
elif my_list == des_list :
    print('descending')
else:
    print('mixed')