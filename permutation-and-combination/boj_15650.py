# 백준 - N과 M (2)

import sys

N, M = map(int , sys.stdin.readline().split(' '))

visited = [False] * (N+1)


def combination(k, l, nums):
    if len(nums) == k:
        print(" ".join(map(str, nums)))
        return


    for n in range(1, N+1):
        if not visited[n] and n > l:
            n_nums = nums.copy()
            n_nums.append(n)
            visited[n] = True
            combination(k, n, n_nums)
            visited[n] = False


combination(M, 0, [])