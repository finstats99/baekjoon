N = int(input())

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

num_list = list(map(int, input().split()))

ans = 0
for i in num_list:
    if is_prime(i):
        ans += 1

print(ans)