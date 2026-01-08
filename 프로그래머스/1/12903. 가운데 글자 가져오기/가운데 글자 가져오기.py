def solution(s):

    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2:len(s)//2+1]
        


#  a b c d e 
# 0 1 2 3 4 5 