import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    # print('-----start-----')
    text = input().rstrip()
    answer = 0
    for i in range(len(text)):
        # print(f'{i} /',len(text))
        if answer <0:
            break
        if text[i] == '(':
            answer += 1
        else:
            answer -= 1
        # print('current answer :', answer)
    if answer == 0:
        print('YES')
    else : 
        print('NO')
