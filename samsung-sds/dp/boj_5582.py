# 백준 - 공통 부분 문자열

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

max_len = 0


for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])


print(max_len)
