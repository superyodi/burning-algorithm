# 시험 감독

import sys

# input
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

B, C = map(int, sys.stdin.readline().split(' '))

answer = 0


for num in arr:
    # 총 감독관 배치

    num -= B
    answer += 1
    # 부 감독관 배치

    if num > 0:
        answer += num // C

        if num % C:
            answer +=  1

print(answer)