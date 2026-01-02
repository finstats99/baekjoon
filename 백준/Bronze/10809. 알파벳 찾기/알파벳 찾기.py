S = input()

my_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for alphabet in my_list:
    if alphabet in S:
        print(S.index(alphabet), end = ' ')
    else:
        print(-1, end = ' ')