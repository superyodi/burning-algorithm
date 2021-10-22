# 백준 신입사원

import sys

T = int(sys.stdin.readline())

tc = 0

while tc < T:
    tc += 1
    N = int(sys.stdin.readline())
    arr = [0] * (N+1)

    for _ in range(N):
        a,b = map(int, sys.stdin.readline().split(' '))
        arr[a] = b


    if N == 1:
        print(1)
        continue

    cnt = 1
    tmp = arr[1]

    for i in range(2, N+1):

        if arr[i] < tmp:
            cnt += 1
        tmp = min(tmp, arr[i])

    print(cnt)


