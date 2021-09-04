# 백준 - 숨바꼭질3

# deque + bfs

import sys, collections

N, K = map(int, sys.stdin.readline().split(' '))

def bfs():
    deq = collections.deque()
    deq.append(N)
    time = [ -1 for _ in range(100001)]
    time[N] = 0

    while deq:
        now = deq.popleft()
        # print(now, time[now])
        if now == K: break
        if now > K*2: continue


        if now*2 < 100001 and time[now*2] == -1:
            time[now*2] = time[now]
            deq.appendleft(now*2)

        if now+1 < 100001 and time[now+1] == -1:
            time[now+1] = time [now] + 1
            deq.append(now+1)

        if now-1 >= 0 and time[now-1] == -1:
            time[now - 1] = time[now] + 1
            deq.append(now-1)



    return time[K]

if N >= K:
    print(N-K)
else:
    print(bfs())



