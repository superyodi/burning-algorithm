# 백준 - 절댓값 힙


import sys
import heapq as hq


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        if x < 0:
            hq.heappush(arr, (x*-1, x))
        else:
            hq.heappush(arr, (x, x))

    else:
        if arr:
            num = hq.heappop(arr)
            print(num[1])
        else:

            print("0")

