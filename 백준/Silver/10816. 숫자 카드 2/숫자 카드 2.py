import sys
input = sys.stdin.readline

n = int(input())


card_list = list(map(int, input().split()))
# print('card_list :', card_list)
card_dict = {}
for i in range(n):
    c = card_list[i]
    if c not in card_dict:
        card_dict[c] = 1
    else:
        card_dict[c] += 1

# print(card_dict)


sg_card = int(input())
sg_card_list = list(map(int, input().split()))

for j in sg_card_list:
    if j in card_dict:
        # print(f'{j}th :',card_dict[j])
        print(card_dict[j], end = ' ')
    else:
        print(0, end = ' ')
# print('sg_card_list :', sg_card_list)