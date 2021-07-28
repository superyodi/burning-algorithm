# 백준 - 좌표 압축

import sys


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))

sorted_nums = sorted(set(nums))
nums_dict = dict()

for idx, num in enumerate(sorted_nums):
    nums_dict[num] = idx

for num in nums:
    print(nums_dict[num], end=" ")
