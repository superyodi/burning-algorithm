# 백준 - 숨바꼭질2
# bfs

import sys, collections

N, K = map(int, sys.stdin.readline().split(' '))

def bfs():
    q = collections.deque()
    q.append(N)
    time = [ K-N for _ in range(100001)]
    time[N] = 0
    cnt = 0

    while q:
        now = q.popleft()
        # print(now, time[now])
        if now == K:
            cnt += 1
            continue

        if now > K*2: continue

        if now*2 < 100001 and time[now*2] >= time[now]+1:
            time[now*2] = time[now] + 1
            q.append(now*2)

        if now+1 < 100001 and time[now+1] >= time[now]+1:
            time[now+1] = time [now] + 1
            q.append(now+1)

        if now-1 >= 0 and time[now-1] >= time[now]+1:
            time[now - 1] = time[now] + 1
            q.append(now-1)

    print(time[K])
    print(cnt)


if N >= K:
    print(N-K)
    print(1)

else:
    bfs()



