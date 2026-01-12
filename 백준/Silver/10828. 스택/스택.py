import sys
input = sys.stdin.readline
N = int(input())

stack = []
for _ in range(N):
    input_list = input().rstrip().split()

    if len(input_list) == 2:
        stack.append(int(input_list[1]))

    else:
        # top인 경우
        if input_list[0] == 'top':
            # 길이가 0이면 -1
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        
        # size인 경우
        elif input_list[0] == 'size':
            print(len(stack))

        # empty인 경우
        elif input_list[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else: print(0)

        # pop인 경우
        elif input_list[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:            
                print(stack[-1])
                stack = stack[:-1]