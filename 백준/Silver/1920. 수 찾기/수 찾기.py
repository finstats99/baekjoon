import sys
input = sys.stdin.readline

n = int(input())

list_ = list(set(map(int, input().split())))
main_box = {}
for i in list_:
    main_box[i] = 1




m = int(input())
test_box = list(map(int, input().split()))

for i in test_box:
    try :
        if main_box[i] == 1:
            print(1)
    except:
        print(0)