# 백준 N 과 M 5

import sys

N, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))


visited = [False] * N

def permu(nums):
    # print(nums)
    if len(nums) == M:
        print(" ".join(list(map(str,nums))))
        return

    for i in range(len(arr)):
        num = arr[i]
        if not visited[i]:
            visited[i] = True
            nums.append(num)
            permu(nums)
            visited[i] = False
            nums.pop()


arr.sort()
permu([])