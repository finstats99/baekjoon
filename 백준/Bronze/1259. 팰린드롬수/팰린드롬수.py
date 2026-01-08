import sys
input = sys.stdin.readline

while True:
    num = str(input().rstrip())
    # print(num, len(num))
    if num == str(0):
        break

    if len(num)%2 == 0:
        bool_ = 'yes'
        for i in range(int(len(num)/2)):
            # print('len :', len(num), num[len(num) - i - 1], num[i]) 
            if bool_ == 'no':
                break

            if num[i] == num[len(num) - i - 1]:
                bool_ = 'yes'
            else:
                bool_ = 'no'
    else :
        bool_ = 'yes'
        for i in range(int(len(num)//2)):
            if bool_ == 'no':
                # print('len :', len(num), num[len(num) - i - 1], num[i])
                break

            if num[i] == num[len(num) - i - 1]:
                bool_ = 'yes'
            else:
                bool_ = 'no'

    print(bool_)
