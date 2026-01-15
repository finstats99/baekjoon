def solution(s):
    len_sum = 0
    cnt = 0
    while s != '1':
        # print(cnt, s)
        cnt += 1
        s_len = len(s)   # 0 제거 전 길이
        s_1 = s.replace('0', '') # 0 제거
        s_1_len = len(s_1)   # 0 제거 후 길이
        # print('s_1_len :', s_1_len)
        len_sum += (s_len - s_1_len) # 제거한 길이

        s = format(s_1_len, 'b') # 0 제거한 길이의 이진수로 업데이트
        # print('binary s_1_len :', s)
            

            
    return [cnt, len_sum]
