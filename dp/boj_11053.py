# 백준 - 가장 긴 증가하는 부분 수열

import sys

size = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split(' ') ))

dp = [1 for _ in range(size)]
answer = 1

if size > 1:
    for i in range(1, size):
        max_dp = 1
        for j in range(i-1, -1, -1):
            if(arr[j] < arr[i]):
                max_dp = max(dp[j]+1, max_dp)
        dp[i] = max_dp
        answer = max(answer, dp[i])

print(answer)
