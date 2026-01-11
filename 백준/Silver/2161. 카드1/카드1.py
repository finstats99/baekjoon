from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

queue = deque(range(1, N + 1))

discarded = []

while len(queue) > 1:
    discarded.append(queue.popleft()) # 가장 상위 카드 버림
    queue.append(queue.popleft()) # 2순위 카드를 맨 뒤로 

for i in discarded:
    print(i, end = ' ')
print(queue[0])