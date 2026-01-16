import sys
input = sys.stdin.readline

n = int(input())

from collections import deque
queue = deque()

for _ in range(n):
    i = input().rstrip()
    if i[:4] == 'push':
        push_num = int(i[5:])
        queue.append(push_num)
    
    elif i == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif i == 'size':
        print(len(queue))
    
    elif i == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif i == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif i == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    