num = int(input())

cnt = 1  
sum_ = 1
while sum_ < num:
    sum_ += cnt*6
    cnt += 1

print(cnt)