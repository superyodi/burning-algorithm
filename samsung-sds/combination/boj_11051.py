# 백준 - 이항 계수2


import sys

cache= [[-1 for _ in range(1001)] for _ in range(1001)]
N, K = map(int, sys.stdin.readline().split(" "))


def nCr(n, r):
    global cache
    if r==0: return 1

    if n < r: return 0

    if n < 0 or n > 1000 or r <0 or r > 1000: return 0

    if cache[n][r] != -1: return cache[n][r]

    cache[n][r] = (nCr(n-1, r-1) + nCr(n-1, r)) % 10007
    return cache[n][r]



print(nCr(N, K))


