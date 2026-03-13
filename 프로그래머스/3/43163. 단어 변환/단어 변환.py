from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def diff1(a, b):
        return sum(x != y for x, y in zip(a, b)) == 1
    
    visited = [False] * len(words)
    q = deque([(begin, 0)])
    
    while q:
        cur, cnt = q.popleft()
        for i, word in enumerate(words):
            if not visited[i] and diff1(cur, word):
                if word == target:
                    return cnt + 1
                visited[i] = True
                q.append((word, cnt + 1))
    
    return 0