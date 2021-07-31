# 백준 - LCS


import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

# 원활한 인덱스 접근을 위한 전처리
s1 = 'a' + s1
s2 = 'b' + s2

n, m = len(s1), len(s2)
dp = [[0 for _ in range(m)] for _ in range(n)]
max_len = 0
for i in range(1, n):
    for j in range(1, m):

        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[n-1][m-1])


# print(*dp, sep='\n')