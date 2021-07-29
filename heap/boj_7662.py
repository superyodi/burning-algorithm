# 백준 - 이중 우선순위 큐

import sys
import heapq as hq

T = int(sys.stdin.readline())
tc = 0

while tc < T:
    k = int(sys.stdin.readline())
    min_arr = []
    max_arr = []
    num_dict = dict()
    size = 0
    for _ in range(k):
        line = sys.stdin.readline()
        cmd = line[0]
        num = int(line[2:])

        if cmd == 'D': # 삭제
            if size != 0:
                if num == 1: # 최댓값 삭제
                    n = hq.heappop(max_arr) * -1
                    while num_dict[n] == 0:
                        n = hq.heappop(max_arr) * -1

                else:
                    n = hq.heappop(min_arr)
                    while num_dict[n] == 0:
                        n = hq.heappop(min_arr)

                num_dict[n] -= 1
                size -= 1

        else: # 추가
            hq.heappush(min_arr, num)
            hq.heappush(max_arr, -num)

            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
            size += 1

    if size == 0:
        print("EMPTY")
    else:
        min_n = hq.heappop(min_arr)
        max_n = hq.heappop(max_arr)*-1

        while num_dict[max_n] == 0:
            max_n = hq.heappop(max_arr) * -1

        while num_dict[min_n] == 0:
            min_n = hq.heappop(min_arr)

        print(max_n, min_n)

    tc += 1



'''
2
11
I 0
I 1
I 2
I 3
I 4
D -1
D -1
D -1
D -1
I 2
D 1
11
I 0
I 1
I 2
I 3
I 4
D -1
D -1
D -1
D -1
I 2
D 1


'''