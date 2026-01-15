def solution(cards1, cards2, goal):
    for i in goal:
        # print(f'for {i}', cards1, cards2)
        
        if cards1 and cards1[0] == i:
            # print(f'pop {cards1[0]}')
            cards1.pop(0)
            
        elif cards2 and cards2[0] == i:
            # print(f'pop {cards2[0]}')
            cards2.pop(0)
            
        else:
            return "No"
            
    return "Yes"