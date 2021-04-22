def sum_nums(depth, n):
    sigma = depth * (depth - 1) // 2

    # k < 0 ---> 그만
    # k == 0 ---> depth개의 연속된 수로 나타낼수있음
    # k > 0 ---> 나타낼수없음
    k = n - sigma

    if k < 0: return -1
    if k != 0 and k % depth == 0: return 1
    return 0


def solution(n):
    answer = 1
    depth = 2

    while True:
        flag = sum_nums(depth, n)
        if flag == -1:
            # print(depth)
            return answer
        elif flag == 1:
            print(depth)
            answer += 1

        depth += 1

    return answer