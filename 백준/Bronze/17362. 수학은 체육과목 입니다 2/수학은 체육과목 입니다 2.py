n = int(input())

pattern = n%8
if pattern == 0:
    pattern = 8
    
if pattern <= 4:
    print(pattern)
else:
    print(10 - pattern)