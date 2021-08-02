# 백준 - N과 M (9)

import sys

N, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
visited = [False] * N

def permutation(m, nums):
    if len(nums) == m:
        print(" ".join(map(str, nums)))
        return

    dup = 0
    for i in range(N):
        if not visited[i] and dup != arr[i]: # 방금 뺀 값과 넣으려는 값이 같다면 pass, 중복 방지
            visited[i] = True
            dup = arr[i] # 최근에 집어넣은 값 저장, 중복 방지
            nums.append(arr[i])
            permutation(m, nums)
            visited[i] = False
            nums.pop()

arr.sort()
permutation(M, [])