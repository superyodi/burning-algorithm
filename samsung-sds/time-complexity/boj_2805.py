# 백준 - 나무 자르기

import sys
N, M = map(int, sys.stdin.readline().split(" "))
trees = list(map(int,sys.stdin.readline().split(" ")))

def sum_trees(height):
    now_sum = 0
    for i in range(N):
        if trees[i] > height:
            now_sum += trees[i] - height

        if now_sum > M: break
    return now_sum

left , right = 0, 1000000000
answer = 0

while left <= right:
    mid = (left + right) // 2
    now_sum = sum_trees(mid)

    if now_sum >= M:
        answer = mid
        left = mid+1

    else: # now_sum < M
        right = mid-1
print(answer)