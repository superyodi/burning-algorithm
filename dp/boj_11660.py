# 백준 - 구간 합 구하기 5

import sys
N, M = map(int, sys.stdin.readline().split(' '))
dp = [[0 for _ in range(N+1)]for _ in range(N+1)]


for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    for j in range(N):
        num = line[j]
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + num


for _ in range(M):
    x1, y1, x2,y2 = map(int, sys.stdin.readline().split(' '))
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)

# print(*dp, sep='\n')
