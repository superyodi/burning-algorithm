# 백준 - 절댓값 힙


import sys
import heapq as hq


N = int(sys.stdin.readline())
pos_heap = []
neg_heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num < 0: # 음수일때
        hq.heappush(neg_heap, num * -1)
    elif num > 0:
        hq.heappush(pos_heap, num)
    else:
        if pos_heap and neg_heap:
            pos = hq.heappop(pos_heap)
            neg = hq.heappop(neg_heap)

            if pos < neg:
                print(pos)
                hq.heappush(neg_heap, neg)
            else:
                print(neg * -1)
                hq.heappush(pos_heap, pos)
        elif pos_heap:
            pos = hq.heappop(pos_heap)
            print(pos)
        elif neg_heap:
            neg = hq.heappop(neg_heap)
            print(neg * -1)
        else:
            print(0)





