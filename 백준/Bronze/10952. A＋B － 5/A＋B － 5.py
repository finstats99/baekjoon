A, B = -1, -1
while (A != 0) and (B != 0):
    A, B = map(int, input().split())
    if (A and B) != 0:
        print(A + B)