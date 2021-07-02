def solution(triangle):
    answer = 0

    for i in range(len(triangle)):
        for j in range(i + 1):
            left, right = 0, 0

            if i > 0:
                if 0 <= j - 1:
                    left = triangle[i - 1][j - 1]
                if j < i:
                    right = triangle[i - 1][j]

            triangle[i][j] += max(left, right)

    # print(triangle)
    return max(triangle[-1])