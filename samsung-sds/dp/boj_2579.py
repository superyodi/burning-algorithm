# 백준 - 계단 오르기

import sys

N = int(sys.stdin.readline())

stairs = []
dp = [0 for _ in range(N)]

for _ in range(N):
    num = int(sys.stdin.readline())
    stairs.append(num)

if N == 1:
    print(stairs[0])

elif N == 2:
    print(stairs[0] + stairs[1])

else:

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

    print(dp[N-1])

