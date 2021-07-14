# 백준


import sys, collections

N = int(sys.stdin.readline())
graph = {i+1 : set() for i in range(N)}
depths = [0] * (N+1) # 각 노드까지의 깊이
parents = [0 for _ in range(N+1)]




# save depth
def find_depth():
    root, depth = 1, 0
    visited = [False] * (N + 1)
    queue = collections.deque()
    queue.append([root, depth])

    while queue:
        now, depth = queue.popleft()
        if visited[now]: continue

        visited[now] = True
        depths[now] = depth

        for node in graph[now]:
            if not visited[node]:
                parents[node] = now
                queue.append([node, depth+1])


def lca(a,b):
    # 1. a, b의 depth가 동일하도록 조정
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:
            a = parents[a]

        else: b = parents[b]

    # 2. 노드가 같아질때까지 올라감
    while a != b:
        a = parents[a]
        b = parents[b]

    return a



# input graph
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split(" "))

    graph[b].add(a)
    graph[a].add(b)


# input command

find_depth()

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(lca(a, b ))