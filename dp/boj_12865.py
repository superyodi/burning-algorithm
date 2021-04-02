# [DP] 평범한 배낭

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(2)]

for i in range(1, N+1):
    dp[0][:] = dp[1][:]
    w, v = map(int, input().split())

    dp[1][1:w] = dp[0][1:w]

    # 가방의 한계
    for limit in range(w, K+1):
        dp[1][limit] = max(dp[0][limit], dp[0][limit - w] + v)



print(dp[1][K])


# 추가) 담은 물품 인덱스 출력


"""
4 7
6 13
4 8
3 6
5 12
"""

'''
4 5
1 4
1 8
3 3
4 8
'''