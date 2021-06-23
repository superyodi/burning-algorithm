def solution(n):
    answer = []
    arr = [[0 for j in range(i + 1)] for i in range(n)]

    k = 1
    max_k = n * (n + 1) // 2
    i, j = 0, 0

    # 아래, 오른쪽, 위
    dirs = [(1, 0), (0, 1), (-1, -1)]
    d_i = 0

    while k <= max_k:

        arr[i][j] = k
        b_i, b_j = i, j

        i, j = i + dirs[d_i][0], j + dirs[d_i][1]

        # 방향을 바꿔야할때 ---> 범위벗어남
        if 0 <= i < n and 0 <= j < n:
            if arr[i][j] != 0:
                d_i = (d_i + 1) % 3
        else:
            d_i = (d_i + 1) % 3

        # 다음 블록
        i, j = b_i + dirs[d_i][0], b_j + dirs[d_i][1]
        k += 1

    for nums in arr:
        answer.extend(nums)
    # print(answer)

    return answer