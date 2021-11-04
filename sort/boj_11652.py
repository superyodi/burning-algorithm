# 백준 - 카드

import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    n = int(sys.stdin.readline())
    nums.append(n)


nums.sort()
tmp = nums[0]
cnt = 1
max_cnt = 1

for i in range(1, N):
    if nums[i] == nums[i-1]:
        cnt += 1
    else:
        cnt = 1

    if cnt > max_cnt:
        tmp = nums[i]
        max_cnt = cnt


print(tmp)