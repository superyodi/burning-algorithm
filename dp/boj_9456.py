# 백준 - 스티커

import sys

T = int(sys.stdin.readline())
tc = 0


while tc < T:
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(2):
        arr.append(
            list(map(int, sys.stdin.readline().split(' ')))
        )
    if n == 1:
        print(max(arr[1][0], arr[0][0]))
        tc += 1
        continue

    dp = [[0 for _ in range(len(arr[0]))] for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[0][1] + dp[1][0]
    dp[1][1] = arr[1][1] + dp[0][0]

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]


    # print(*dp, sep='\n')
    print(max(dp[0][n-1], dp[1][n-1]))



    tc += 1


