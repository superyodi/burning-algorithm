# 백준 - 연결 요소의 개수

import sys, collections

N, M = map(int, sys.stdin.readline().split(' '))
graph = {i+1 : set() for i in range(N)}
visited = [False] * (N+1)
for _ in range(M):
    i, j = map(int,sys.stdin.readline().split(' '))
    graph[i].add(j)
    graph[j].add(i)


def bfs(start):
    queue = collections.deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        if visited[now]: continue
        visited[now] = True

        for node in graph[now]:
            if not visited[node]:
                queue.append(node)

answer = 0
for node in range(1, N+1):
    if not visited[node]:
        answer += 1
    bfs(node)

print(answer)