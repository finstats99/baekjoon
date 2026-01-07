def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i == 0:
            ans.append(arr[i])
        else:
            if arr[i-1] == arr[i]:
                pass
            else:
                ans.append(arr[i])
                
    return ans














def another(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer