# 백준 - 숨바꼭질

import sys, collections

n, k = map(int, sys.stdin.readline().split(' '))

queue = collections.deque()
queue.append(n)
visited = [0] * 100001

while queue:
    n = queue.popleft()

    if n == k:
        print(visited[k])
        break

    # 뒤로 이동
    for nxt in (n-1, n+1, n*2):
        if 0<= nxt <= 100000 and not visited[nxt]:
            visited[nxt] = visited[n] + 1
            queue.append(nxt)



