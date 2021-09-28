# 백준 부분수열의 합


import sys
N, S = map(int, sys.stdin.readline().split(' '))

arr = list(map(int, sys.stdin.readline().split(' ')))
cnt = 0
visited = [False] * N


def backtracking(size, now_sum):
    global cnt

    if size == N:
        if now_sum == S: cnt += 1
        return

    backtracking(size+1, now_sum + arr[size])
    backtracking(size + 1, now_sum)



backtracking(0, 0)
if S == 0: cnt -= 1
print(cnt)
