# 백준 - 피보나치 함수

import sys

T = int(sys.stdin.readline())
tc = 0

cnt0 = 0
cnt1 = 0
dp = [0] * 41

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        dp[n] = 1
        return 1

    if dp[n] != 0: return dp[n]
    dp[n] = fib(n-2) + fib(n-1)
    return dp[n]


while tc < T:
    N = int(sys.stdin.readline())

    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        fib(N)
        print("{} {}".format(dp[N-1], dp[N]))

    cnt0, cnt1 = 0, 0
    tc += 1


