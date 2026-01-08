import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

cards = list(map(int, input().split()))


min_gap = sum(cards)

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            new_sum = cards[i] + cards[j] + cards[k]
            gap = m - new_sum
            if 0 <= gap < min_gap:
                min_gap = gap
                ans = new_sum            
print(ans)
