def solution(s, n):
    answer = []
    for i in s:
        if ord('A') <= ord(i) <= ord('Z'):
            if ord(i) + n > ord('Z'):
                answer.append(chr((ord(i) + n - (ord('Z') - ord('A') + 1))))
            else:
                answer.append(chr(ord(i)+n))
                
        elif ord('a') <= ord(i) <= ord('z'):
            print('else', ord(i) + n, ord('z'))
            if ord(i) + n > ord('z'):
                answer.append(chr(ord(i) + n - (ord('z') - ord('a') + 1)))
            else:
                answer.append(chr(ord(i)+n))
        
        else: 
            answer.append(i)
                              
    return ''.join(answer)
