# 백준 - 줄 세우기

import sys, collections

N, M = map(int, sys.stdin.readline().split(" "))
graph = {i+1 : set() for i in range(N)}
indegree = [0] * (N+1)


for _ in range(M): # a ---> b , a뒤에 b가 와야함
    a,b = map(int, sys.stdin.readline().split(" "))
    graph[a].add(b)
    indegree[b] += 1


# 시작 노드 찾기 (indegree가 0인 노드)
starts = []
orders = []
queue = collections.deque()
for n in range(1,N+1):
    if not indegree[n]:
        queue.append(n)

visited = [False for _ in range(N+1)]

while queue:
    now = queue.popleft()
    if visited[now]: continue

    if indegree[now] > 0:
        queue.append(now)
        continue
    visited[now] = True
    orders.append(now)


    for node in  graph[now]:
        indegree[node] -= 1
        if not visited[node]:
            queue.append(node)

for order in orders:
    print(order, end=' ')
