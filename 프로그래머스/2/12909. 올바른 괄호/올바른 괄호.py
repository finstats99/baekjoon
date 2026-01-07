def solution(s):
    len_s = len(s)
    deck = [0, 0]
    for i in range(len_s):
        if s[i] == '(':
            deck[0] += 1
        elif s[i] == ')':
            deck[1] += 1
            
        if deck[0] - deck[1] <0:
            return False
    
    if deck[0] - deck[1] == 0:
        return True
    else:
        return False
    
    