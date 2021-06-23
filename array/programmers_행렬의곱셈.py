def solution(arr1, arr2):
    answer = [[]]

    # n * m
    N = len(arr1)
    M = len(arr1[0])
    K = len(arr2[0])

    for n in range(N):
        for k in range(K):
            num = 0
            for m in range(M):
                tmp = arr1[n][m] * arr2[m][k]
                num += tmp
            answer[n].append(num)
        answer.append([])
    answer.pop()

    return answer