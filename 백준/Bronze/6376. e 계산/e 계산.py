def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

print('n e')
print('- -----------')

total_sum = 0
for i in range(10):
    total_sum += 1 / factorial(i)
    
    if i == 0:
        print(f"{i} {int(total_sum)}")
    elif i == 1:
        print(f"{i} {int(total_sum)}")
    elif i == 2:
        print(f"{i} {total_sum:.1f}")
    else:
        print("%d %.9f" % (i, total_sum))
