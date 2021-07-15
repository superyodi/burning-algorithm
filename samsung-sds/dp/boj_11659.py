# 백준 - 구간 합 구하기 4

import sys, math

N, M = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

sum_sub = [0] * N

sum_sub[0] = arr[0]
for n in range(1, N):
    sum_sub[n] = sum_sub[n-1] + arr[n]


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split(" "))
    if i == 1:
        print(sum_sub[j-1])
    else:
        print(sum_sub[j-1] - sum_sub[i-1-1])

