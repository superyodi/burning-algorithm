# 백준 - 최소 힙

import sys
import heapq as hq


N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    x= int(sys.stdin.readline())

    if x == 0:
        if not nums:
            print(0)

        else:
            print(hq.heappop(nums))

    else:
        hq.heappush(nums, x)
