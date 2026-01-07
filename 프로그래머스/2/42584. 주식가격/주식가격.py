def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        target = prices[i]
        cnt = 0
        try :
            for j in range(i+1, n):
                contrast = prices[j]
                # print(f'try{i}', contrast)
                if contrast >= target:
                    # print(f'plus 1 in {cnt} at {i} - {j}')
                    cnt += 1
                else:
                    cnt += 1
                    break
            answer[i] = cnt
            # print(answer)
        except:
            print('except', i)
    return answer