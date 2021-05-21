import heapq
import sys

min_heap = []
max_heap = []

N = int(sys.stdin.readline())
meidan = 0

for i in range(N):
    num = int(sys.stdin.readline())

    if i == 0:
        heapq.heappush(min_heap, (-num, num))
        print(num)
        continue

    if num > min_heap[0][1]:
        heapq.heappush(max_heap, num)

    else:
        heapq.heappush(min_heap, (-num, num))

    # 중간값 구하기
    if len(min_heap) > len(max_heap) + 1:
        tmp = heapq.heappop(min_heap)
        heapq.heappush(max_heap, tmp[1])

    elif len(min_heap) < len(max_heap):
        tmp = heapq.heappop(max_heap)
        heapq.heappush(min_heap, (-tmp, tmp))

    print(min_heap[0][1])








