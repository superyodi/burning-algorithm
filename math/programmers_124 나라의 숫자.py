# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899#

def solution(n):
    if n < 4:
        if n == 3:
            n = 4
        return str(n)

    remain = n % 3

    if remain == 0:
        return solution(n // 3 - 1) + '4'
    return solution(n // 3) + str(remain)
