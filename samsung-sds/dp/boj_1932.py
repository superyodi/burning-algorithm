# 백준 - 정수 삼각형

import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split(" "))))


for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][0]
            continue
        if j == i:
            arr[i][j] += arr[i-1][j-1]
            continue

        arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[N-1][:]))
