import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    
    num_list = [a, b, c]
    num_list.sort()
    
    tri_1 = num_list[-1]
    tri_2 = num_list[-2]
    tri_3 = num_list[-3]

    if tri_1**2 == tri_2**2 + tri_3**2:
        print('right')
    else:
        print('wrong')