#  백준 - RGB 거리

import sys

N = int(sys.stdin.readline())
h = []
dp = [[1000 for _ in range(3)]for _ in range(N)]


for _ in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    h.append(line)

dp[0][0] = h[0][0]
dp[0][1] = h[0][1]
dp[0][2] = h[0][2]

for idx in range(1, N):
    dp[idx][0] = min(dp[idx - 1][1], dp[idx - 1][2]) + h[idx][0]
    dp[idx][1] = min(dp[idx - 1][0], dp[idx - 1][2]) + h[idx][1]
    dp[idx][2] = min(dp[idx - 1][0], dp[idx - 1][1]) + h[idx][2]


print(min(dp[N-1]))



