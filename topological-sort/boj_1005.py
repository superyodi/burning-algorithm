# 백준 ACM Crft

import sys, collections

T = int(sys.stdin.readline())

tc = 0

def t_sort(goal):
    t_times = times.copy()
    q = collections.deque()
    visited = [False] * N

    if indegrees[goal] == 0:
        return times[goal]


    for n in range(N):
        if indegrees[n] == 0:
            q.append(n)


    while q:
        now = q.popleft()
        if visited[now]: continue
        visited[now] = True

        for node in graph[now]:
            indegrees[node] -= 1
            t_times[node] = max(t_times[node], t_times[now] + times[node])

            if not visited[node] and indegrees[node] == 0:
                q.append(node)


    return t_times[goal]


while tc < T:
    N, K = map(int, sys.stdin.readline().split(' '))
    times = list(map(int, sys.stdin.readline().split(' ')))
    indegrees = [0] * N
    graph = {i : set() for i in range(N)}

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split(' '))

        graph[x-1].add(y-1)
        indegrees[y-1] += 1

    W = int(sys.stdin.readline())

    print(t_sort(W-1))

    tc += 1