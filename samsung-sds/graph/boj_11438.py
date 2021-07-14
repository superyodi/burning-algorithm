# 백준 - LCA 2


import sys, collections, math

N = int(sys.stdin.readline())
logN = int(math.log2(N)) + 1
graph = {i+1 : set() for i in range(N)}
depths = [0] * (N+1) # 각 노드까지의 깊이
parents = [[0 for _ in range(logN)] for _ in range(N+1)] # 각 노드에 대해 2^i번째 부모 정보를 기록




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
                parents[node][0] = now
                queue.append([node, depth+1])

def set_parents():
    find_depth()



    for i in range(1, logN):
        for j in range(1, N+1):

            parents[j][i] = parents[parents[j][i-1]][i-1]



def lca(a,b):
    # 1. a, b의 depth가 동일하도록 조정
    if depths[a] != depths[b]:
        # b가 더 depth가 깊다고 설정
        if depths[a] > depths[b]:
            a, b = b, a

    for i in range(logN-1, -1, -1):
        if depths[b] - depths[a] >= 2**i:
            b= parents[b][i]

    if a == b: return a

    # 2. 노드가 같아질때까지 올라감
    for i in range(logN-1, -1, -1):
        if parents[a][i] != parents[b][i]:

            a = parents[a][i]
            b = parents[b][i]

    return parents[a][0]



# input graph
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split(" "))

    graph[b].add(a)
    graph[a].add(b)


# input command

set_parents()

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(lca(a, b ))