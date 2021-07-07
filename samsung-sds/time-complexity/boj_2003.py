# 백준 - 수들의 합 2


import sys

N, M = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

answer = 0
now_sum = arr[0]

left, right = 0, 0


while left < N and right < N:
    # print(left, right, now_sum)
    if now_sum == M:
        answer += 1
        now_sum -= arr[left]
        left += 1
        right += 1
        if right < N:
            now_sum += arr[right]

    elif now_sum < M:
        right += 1
        if right < N:
            now_sum += arr[right]

    else: # now_sum > M
        now_sum -= arr[left]
        left += 1

print(answer)
