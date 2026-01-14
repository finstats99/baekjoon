import sys
input = sys.stdin.readline

n = int(input())
s = set([])
all_s = set([str(i) for i in range(1, 21)])
for i in range(n):
    do = input().split()
    if (do[0] == 'add'):# and (do[1] not in s):
        s.add(do[1])
        # print(f'{i} - add{do[1]}:',s)
        
    elif do[0] == 'remove':# and (do[1] in s):
        s.discard(do[1])
        # print(f'{i} - remove{do[1]}:',s)
    
    elif do[0] == 'check':
        if do[1] in s:
            print(1)
        else:
            print(0)
    
    elif do[0] == 'toggle':
        if do[1] in s:
            s.remove(do[1])
            # print(f'{i} - tog/remove{do[1]}:',s)
        else:
            s.add(do[1])
            # print(f'{i} - tog/add{do[1]}:',s)

    elif do[0] == 'all':
        s = all_s.copy()
        # print(f'{i} - all:',s)
    
    elif do[0] == 'empty':
        s = set()
        # print(f'{i} - empty:',s)

